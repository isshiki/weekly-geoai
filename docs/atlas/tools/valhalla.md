---
layout: default
title: Valhalla
category: tools
updated: 2026-09-20
---

# Valhalla

Valhallaは経路探索のオープンソースエンジンである。3.9.0（2026年9月19日）は歩行者エリア内の経路生成や経路コスト処理を更新した。

## 歩行者エリア内の経路生成

広場などのポリゴンから中央を通る骨格を生成し、周囲の歩行者ネットワークへつなぐ。外周を回るだけでなくエリア内を横断する経路を扱える。地図に内側の穴として記録された障害物は避ける。

| 設定・条件 | 内容 |
| --- | --- |
| `mjolnir.pedestrian_areas` | 既定は`false`。有効化するとエリア内の通行経路を生成する |
| `mjolnir.include_pedestrian` | 歩行者ネットワークを含める設定。既定は`true`で、本機能にも必要 |
| 反映方法 | 設定変更後にタイルを再構築する |
| 対象 | `highway=pedestrian`と`area=yes`を持つ閉じたwayや対応するmultipolygon |

3.9.0の文書では、生成する辺がエリア固有のタグを継承せず一般的な歩行者属性を使うなどの制限を明記している。この経路生成だけを根拠に、車いすでの通行可能性を判断することはできない。

## その他の3.9.0更新

- CostMatrixの距離再計算などを修正し、詳細な行列出力へ`cost`を追加した。
- `/sources_to_targets`と`/optimized_route`で`linear_cost_factors`をサポートした。
- 翻訳をlocale JSONから`.po`ファイル中心のワークフローへ移した。

## 出典

- [Valhalla 3.9.0](https://github.com/valhalla/valhalla/releases/tag/3.9.0)（2026-09-20確認）
- [Pedestrian areas（3.9.0の文書）](https://github.com/valhalla/valhalla/blob/3.9.0/docs/docs/concepts/pedestrian-areas.md)（2026-09-20確認）
