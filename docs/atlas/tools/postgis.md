---
title: PostGIS
category: tools
updated: 2026-11-01
---

# PostGIS

PostGISは、PostgreSQLデータベースで位置や図形を保存し、距離・範囲・重なりをSQLで調べるための拡張である。例えば、店舗から一定距離内の施設を検索するなど、更新を続ける地理データの管理と分析に使う。PostgreSQL環境とSQLの知識が必要になる。

## 形状の関係を調べる

3.7.0では最小全域木を計算するST_MinimumSpanningTreeと、ポリゴンの被覆内で共有される辺を抽出するST_CoverageEdgesを追加した。最小全域木は対象をつなぐ木を求める処理であり、そのまま道路上の最短経路や配送計画を求める機能ではない。

ST_DWithinは指定距離内かを調べる関数で、準備済み形状の距離処理とキャッシュによる高速化が案内されている。ST_AsGeoJSONには属性キーの重複を警告する機能が加わった。本Atlasでは動作・速度を測定していない。

## 重要な更新履歴 {#release-history}

3.7.0の公式発表を起点とする。過去版の導入履歴は未整理で、全更新を網羅しない。公開日は公式記事の表記、確認日は2026-11-01である。

| 版・公式出典 | 公開日 | 主な変化 | 移行時の確認 |
| --- | --- | --- | --- |
| [3.7.0](https://postgis.net/2026/10/PostGIS-3.7.0/) | 2026-10-30 | 最小全域木・共有辺の抽出、距離内判定の高速化、GeoJSON属性キーの重複警告 | PostgreSQL 14〜19、GEOS 3.10以上、PROJ 6.1以上、libgmpが必要。postgis拡張の全機能にはGEOS 3.15以上。address_standardizerとtiger_geocoderは別プロジェクトへ分離 |

PostgreSQL 12・13の対応終了に加え、topologyの許容値0は実際の0を意味し、精度設定を使う既定値は-1へ変わる。SFCGAL拡張の全機能にはSFCGAL 2.3以上が必要で、本体と別拡張の要件を混同しない。

## 次に読む

- [空間SQLエンジンの選び方](spatial-sql-engines.md)：ファイルの分析とデータベース運用を比べる。
- [空間索引の選択と評価条件](../methods/spatial-index-selection.md)：検索速度をどの条件で測るかを確認する。

## 出典

- [PostGIS 3.7.0公式リリース](https://postgis.net/2026/10/PostGIS-3.7.0/)（2026-11-01確認）
