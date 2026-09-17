---
layout: default
title: maplibre-gl-streetview
category: tools
updated: 2026-09-17
---

# maplibre-gl-streetview

maplibre-gl-streetviewは、地図上でStreet Viewの位置を扱うコントロールである。

## v0.8.0のMarker差し替え

2026年9月16日公開のv0.8.0では、`createMarker`で別エンジンのMarkerを生成できる。MapLibreのMarkerが参照する内部構造がMapbox GL JSにはなく、地図クリック時にエラーとなる問題に対応した。

ファクトリーは`element`と`anchor: 'center'`を受け取り、`setLngLat`・`addTo`・`remove`を持つオブジェクトを返す。Mapbox GL JS利用時は同エンジンのMarkerを渡す。省略時は従来どおりMapLibreのMarkerを使う。

これはコントロールの互換性改善であり、両地図エンジンの全APIが互換になったという意味ではない。

## 出典

- [Release v0.8.0 — opengeos/maplibre-gl-streetview](https://github.com/opengeos/maplibre-gl-streetview/releases/tag/v0.8.0)（2026-09-17確認）
