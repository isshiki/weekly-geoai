---
title: anymap-ts
category: tools
updated: 2026-11-01
---

# anymap-ts

anymap-tsは、anywidgetを通じてPythonとJavaScriptを連携し、Jupyterなどで対話型の地図を扱うパッケージである。TypeScriptを使った表示側とPython側をつなぎ、MapLibre・Mapboxなどの描画エンジンを利用する。Python環境が必要で、独立したデスクトップGISではない。

## 描画エンジンと配布方法を分ける

2026年10月31日UTC公開のv0.17.3は、Mapbox GL JSを同梱せず、MapboxのCDNから必要時に読み込む方式へ変更した。配布するmapbox.jsは約2MB小さくなるが、Mapbox利用時はローカルスタイルでもapi.mapbox.comへの接続が必要になる。他の描画エンジンはこのMapboxコードを読み込まない。

MapLibreとMapboxの内部プロパティの競合による白紙地図を修正し、ビルド互換性のためmaplibre-glの依存範囲を^5.14.0に制限した。これはanymap-tsの対応条件であり、MapLibre v6全体が利用不能という意味ではない。

## 利用時の確認

公式リリースはMapbox GL JS v2以降が独自ライセンスであることを説明する。包むパッケージと各エンジンの利用条件・ネットワーク要件を別々に確認する。小さな版番号でも配布と起動の条件が変わる例として保存した。実行・オフライン利用の試験は行っていない。

## 次に読む

- [MapLibre GL JS](maplibre-gl-js.md)：描画エンジン側の更新。
- [GeoJSON](../data/geojson.md)：地図へ渡す形と属性。

## 出典

- [anymap-ts README](https://github.com/opengeos/anymap-ts)（2026-11-01確認）
- [v0.17.3](https://github.com/opengeos/anymap-ts/releases/tag/v0.17.3)（2026-11-01 GitHub公式APIで本文・公開日時確認）
