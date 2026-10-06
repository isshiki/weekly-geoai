---
layout: default
title: Cloud Optimized GeoParquet（COGP）
category: data
updated: 2026-10-06
---

# Cloud Optimized GeoParquet（COGP）

COGPは、GeoParquetの行グループを粗い詳細度から細かい詳細度へ並べ、段階的な地図表示と部分読み込みを支援するプロファイルである。対応リーダーはgeo.lodメタデータから必要な行グループの範囲を選ぶ。非対応リーダーでも通常のGeoParquetとして全行を読めるが、詳細度の選択はできない。

## 分析用の形状と描画用の形状

2026年9月26日公開のv2.0.0では、線・ポリゴンに簡略化・量子化した描画用overviewを追加した。元のジオメトリと属性を保持し、描画用の形状は別列に置く。固定版READMEでは、入力がすべて線、またはすべてポリゴンの場合にwriterがoverviewを追加すると説明している。

| 用途 | 読み方 |
| --- | --- |
| 全体像を素早く表示 | 対応リーダーで粗いLoDと描画用overviewを選ぶ |
| 元の形状を使った分析 | 元のジオメトリ・属性を読み、必要な全行を対象にする |
| 範囲内の厳密な抽出 | 統計による候補選択後、必要な空間条件を再判定する |

## bbox検索で返る候補行

変更説明#37では、coveringメタデータがある場合のreadRows({ bbox })は、行グループやページのbbox統計で取得範囲を絞り、候補行を返す仕様へ変わった。covering列を暗黙に読み込んで各行を厳密に絞る処理は行わない。必要な判定は呼び出し側で実施する。

取得上限も候補行を数えるため、有限の上限を指定すると後続の一致地物を取り逃す場合がある。全件集計では候補抽出と最終判定を分けて設計する。統計がない部分は候補として残し、covering情報がないファイルは従来のgeometry-envelopeによる絞り込みを維持する。

## 取得量と最も粗いLoD

HTTP Rangeの結合は重複または隣接した範囲に限定した。root LoDの最低地物数は既定で2048となったが、これは表示中の画面内ではなくデータセット全体で数える。全入力が2048件未満なら、要求した最も細かい解像度で全行を書き出す。

段階表示のための並び順が、すべての全解像度検索で最速になるとは限らない。性能はデータの分布、行グループの配置、リーダーの対応に依存する。今回コードや性能測定の再実行は行っていない。

## 前提と関連する形式

[CNGの形式比較](../concepts/cloud-native-geospatial.md#choose-format)では、GeoParquetの基本的な役割と、COG・PMTiles・STACとの違いを整理する。COGPのLoD選択は対応リーダーの機能であり、上記の確認済み版の説明をすべてのGeoParquetに一般化しない。

## 出典

- [v2.0.0リリース](https://github.com/Kanahiro/cloud-optimized-geoparquet/releases/tag/v2.0.0)（2026-09-27確認）
- [v2.0.0 README](https://github.com/Kanahiro/cloud-optimized-geoparquet/blob/v2.0.0/README.md)（2026-09-27確認）
- [bbox統計と候補行の仕様変更](https://github.com/Kanahiro/cloud-optimized-geoparquet/pull/37)（2026-09-27確認）
- [root LoDの最低地物数](https://github.com/Kanahiro/cloud-optimized-geoparquet/pull/39)（2026-09-27確認）
