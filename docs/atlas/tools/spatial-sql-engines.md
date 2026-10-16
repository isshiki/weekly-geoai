---
title: 空間SQLエンジンの選び方
category: tools
updated: 2026-10-16
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

## 次に読む

- [空間結合と集計](../methods/spatial-join-and-aggregation.md)：まず同じ問い・判定になっているかを確認する。
- [空間索引の選択と評価条件](../methods/spatial-index-selection.md)：検索時間と準備時間を分ける。

## 出典

- [Matt Forrest：PostGIS vs GeoPandas vs DuckDB](https://forrest.nyc/postgis-geopandas-duckdb-spatial-engine/)（2026-10-16確認）
