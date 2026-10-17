---
title: 空間SQLエンジンの選び方
category: tools
updated: 2026-10-17
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

## 出典

- [Matt Forrest：PostGIS vs GeoPandas vs DuckDB](https://forrest.nyc/postgis-geopandas-duckdb-spatial-engine/)（2026-10-16確認）

- [Databricks：Lakehouse//RTの空間クエリ](https://www.databricks.com/blog/geospatial-queries-are-38x-faster-lakehousert)（2026-10-17確認）
