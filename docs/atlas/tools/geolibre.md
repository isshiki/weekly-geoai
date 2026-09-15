---
layout: default
title: GeoLibre
category: tools
updated: 2026-09-15
---

# GeoLibre

GeoLibreは、地理空間データの可視化、取得、編集、分析を扱うオープンソースのアプリケーションである。

## 確認したポイント

- v2.9.0では、Plotly Dash向けのDashMap、VantorおよびPlanetのオープンデータ連携が追加された。
- アノテーション編集、GeoParquetメタデータ解析、DEM取得、3D Globeが強化された。
- デスクトップ、Web、Android、Pythonにまたがる不具合修正も含まれる。

## v3.0.0での拡張

2026年9月14日のv3.0.0では、Cesiumを主要3D描画エンジンとして選択できるようになった。MapEngineの共通インターフェースを通し、エンジンが対応する機能に応じてUIとプラグインを切り替える。

- GeoJSON、COG、I3S、点群などのCesium表示を拡張した。
- CSWカタログ検索を追加した。
- 外部プラグインがJSON SchemaでAIアシスタントのツールを登録できるようになった。

上記はリリースノートで確認した変更であり、Atlas側での動作検証結果ではない。

## 出典

- [GeoLibre v3.0.0](https://github.com/opengeos/GeoLibre/releases/tag/v3.0.0)（2026-09-14公開、2026-09-15確認）

- [GeoLibre v2.9.0](https://github.com/opengeos/GeoLibre/releases/tag/v2.9.0)（2026-09-04確認）
