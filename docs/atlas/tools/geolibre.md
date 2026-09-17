---
layout: default
title: GeoLibre
category: tools
updated: 2026-09-17
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

## UIなしで使う @geolibre/map

`@geolibre/map`は、データ読み込み、レイヤー同期、スタイル処理を取り出したパッケージである。公式READMEは、公開するheadless機能にはReact、Zustandストア、Cesium、地図コントロールを含まないと説明している。

`createLayerSync(map)`で同期処理を作り、`sync.sync(layers)`へレイヤー一覧を渡す。COG DEM・PMTilesのプロトコル登録や、Mapbox Style・SLD・QMLの入出力も案内されている。ESM専用でTypeScriptの型定義を提供する。

2026年9月17日に公式READMEとnpmレジストリを確認し、v3.0.0、MITライセンス、同バージョンの公開日時が9月14日（UTC）であることを確認した。npmの紹介画面は取得できなかった。アプリ全体の対応レンダラーと、このパッケージのheadless機能の範囲は区別する。

## 出典

- [@geolibre/map README](https://github.com/opengeos/GeoLibre/blob/main/packages/map/README.md)（2026-09-17確認）
- [npmレジストリのパッケージ情報](https://registry.npmjs.org/@geolibre/map)（2026-09-17確認）
- [@geolibre/map](https://www.npmjs.com/package/@geolibre/map)（共有URL。2026-09-17時点で紹介画面の取得は未了）

- [GeoLibre v3.0.0](https://github.com/opengeos/GeoLibre/releases/tag/v3.0.0)（2026-09-14公開、2026-09-15確認）

- [GeoLibre v2.9.0](https://github.com/opengeos/GeoLibre/releases/tag/v2.9.0)（2026-09-04確認）
