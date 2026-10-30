---
title: 空間SQLエンジンの選び方
category: tools
updated: 2026-10-30
---

# 空間SQLエンジンの選び方

空間SQLエンジンは、区域内の件数、距離、最近傍などをSQLで問い合わせる道具である。ファイルを一度分析するのか、更新を続けるデータベースを運用するのかで選択が変わる。

## 道具の役割を分ける

| 道具 | 主な使い方と準備 |
| --- | --- |
| DuckDB Spatial | 手元やクラウドのファイルをSQLで分析する。DuckDBと空間拡張を用意する |
| PostGIS | PostgreSQLで地理空間データを保存・更新し、索引を使って問い合わせる |
| SedonaDB | Spark不要の単一マシン向け空間分析エンジン。Python・SQLからファイルを分析する |
| GeoPandas | PythonのGeoDataFrameで読込・加工・空間分析を行う。SQLエンジンへの受け渡しにも使える |

Matt Forrestの比較記事ではGeoPandasを読込役に用いており、SQLの速度比較には含めていない。GeoPandas自体が読込しかできないという意味ではない。記事はGeoParquetを介した併用を提案する。

DuckDBの導入版や互換性の変化は、[DuckDBの重要な更新履歴](duckdb.md#release-history)にまとめている。このページはエンジン間の選択と比較条件を中心に読む。

## ファイルの読み込みと運用を選ぶ

DuckDB 2.0は2026年10月21日公開のLTSで、少なくとも2027年10月まで保守される。公式発表はクラウドファイルの非同期読み込み、サーバー動作の改善、AIエージェント向けの簡潔な出力などを紹介する。サーバーのQuackは1.5.3で導入済みであり、2.0で初めて加わった機能ではない。

2.0で新規作成したデータベースファイルは旧版で読めない。一方、既存ファイルを2.0で読み書きする場合は後方互換性を保つ。ファイル形式と移行先を確認して選ぶ。

Pacific Spatial Solutionsの解説は、クラウド上の全国約2,900万農地区画・約4.5GBのファイルから必要列を読み、約40秒で属性を集計した例を示す。全ファイルの手動ダウンロードを省く使い方だが、空間結合の速さや全データの転送速度を測ったものではない。

### POIを速く集計できても、登録地点を確かめる

Plotlyの地図デモはOvertureのPOIをH3の六角形へ集計する。記事は同じ座標に4,322事業者が登録された登記住所の例を示し、同一座標に20件以上ある地点を除外する処理を使う。これは当該デモの仮の基準で、商業施設内の店舗なども除外し得る。一般的な重複判定としてそのまま適用しない。

同記事の速度比較は同じVMで各版を3回、新しいプロセスで実行した中央値である。地図アプリでは取得後のローカルキャッシュも使うため、初回取得と再表示を分けて読む。本Atlasではいずれの集計も再実行していない。

## 比較値の読み方

2026年10月12日の記事は、NYCの約120万件の建物などを使う4処理を比較した。空間結合の表ではSedonaDB 0.24秒、DuckDB 43秒、PostGIS 6秒と報告するが、本文では同種の処理を0.3秒とも記している。

これらは著者の測定であり、本Atlasでは再実行していない。記事だけでは各ソフトの版、全SQL、ハードウェア、反復・キャッシュ条件を十分にそろえて比較できない。速度の優劣を一般化せず、読込・索引作成・座標変換を計測に含めたかも確認する。

## 同時利用が多いサービスの評価

DatabricksのLakehouse//RTは、レイクハウス上のデータを低遅延・高い同時実行性で問い合わせるクラウドのウェアハウスである。2026年10月15日に空間SQL・空間結合のベータ対応を発表した。Databricks SQL Serverlessで使っている空間クエリをコード変更なしで実行できるとしている。利用にはDatabricks環境と対象ウェアハウスの作成が必要になる。

同社のSpatialBench測定では、従来型クラウドDWH比で単一実行時に平均3倍・最大20倍、50ユーザー同時利用時に最大38倍の高速化を報告する。比較対象が処理できたクエリでの最大値であり、すべての処理が38倍になる意味ではない。記事本文は比較製品名や費用をそろえた詳細条件を十分に示しておらず、本Atlasでも再計測していない。

手元で1回分析する速さと、多数の利用者へ応答する速さは分けて選ぶ。実際の選定ではデータ量、同時実行数、応答時間の分布、費用をそろえて確かめる。

## 次に読む

- [空間結合と集計](../methods/spatial-join-and-aggregation.md)：まず同じ問い・判定になっているかを確認する。
- [空間索引の選択と評価条件](../methods/spatial-index-selection.md)：検索時間と準備時間を分ける。

## DuckDBの拡張導入と移行条件

公式2.0文書は、spatialをINSTALLで導入した後にLOAD spatialで明示的に読み込むよう案内する。自動ロードには対応しない。これは導入手順であり、新機能の発表ではない。

10月のQiita解説は、GeoJSON／GeoJSONLの直接入出力と最近傍結合、座標軸設定を移行時の確認点に挙げる。公式のNEAREST結合は距離や類似度で相手側の上位k件を対応付けるSQLで、空間データ専用でもR-tree利用を保証するものでもない。GEOMETRYの本体組み込みとCRS付き型は1.5由来と区別する。座標軸の設定だけでなく、変換後の位置と距離を確認する。記事のSQLと本Atlasの確認はいずれも実行試験ではない。

## 出典

- [Matt Forrest：PostGIS vs GeoPandas vs DuckDB](https://forrest.nyc/postgis-geopandas-duckdb-spatial-engine/)（2026-10-16確認）

- [Databricks：Lakehouse//RTの空間クエリ](https://www.databricks.com/blog/geospatial-queries-are-38x-faster-lakehousert)（2026-10-17確認）

- [DuckDB：2.0.0 LTS公式発表](https://duckdb.org/2026/10/21/announcing-duckdb-200)（2026-10-24本文確認）

- [Pacific Spatial Solutions：DuckDB 2.0と地理空間データ](https://note.com/pacificspatial/n/n1947bdb5e851)（2026-10-24本文確認）

- [Plotly：DuckDB 2.0の検証と地図デモ](https://plotly.com/blog/duckdb-2-0/)（2026-10-24本文確認）

- [Spatial Extension – DuckDB](https://duckdb.org/docs/2.0/core_extensions/spatial/overview)（2026-10-27確認）
- [DuckDB 2.0で変わったSpatial・GIS機能を整理する ── GeoJSON、最近傍検索、座標軸の変更と移行時の注意点](https://qiita.com/rino_yume/items/9e0cc4ab18ccaf12d14a)（2026-10-27確認）
- [DuckDB：Nearest Joins](https://duckdb.org/docs/2.0/sql/query_syntax/from#nearest-joins)（2026-10-27確認）
