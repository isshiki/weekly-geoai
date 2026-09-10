---
layout: default
title: MapLibre GL JS
category: tools
updated: 2026-09-10
---

# MapLibre GL JS

MapLibre GL JSは、ベクタータイルなどからインタラクティブな地図をブラウザ上へ描画するTypeScriptライブラリである。WebGLを利用し、レイヤーの見た目やデータソースをMapLibre Style Specificationに沿ったスタイル文書で制御する。

## 主な役割

- ベクタータイル、GeoJSON、ラスター、terrainなどをWeb地図として表示する。
- レイヤー、カメラ、Marker、Popup、ユーザー操作をAPIから制御する。
- メルカトル表示に加え、globe表示や3D terrainを扱う。
- PMTilesなど、追加プロトコルを介した配信形式と組み合わせられる。

## v6.9.0で確認した変更

2026年9月9日に公開されたv6.9.0では、デーヴァナーガリー、クメール、ビルマ語などの複雑な文字体系と、アラビア語・ヘブライ語の右から左へ書くラベルの描画が改善された。右横書き用プラグインを読み込まずに描画できるようになり、`setRTLTextPlugin` と `getRTLTextPluginStatus` は非推奨となった。

性能面では、Spriteや画像のピクセル読み出しに利用可能な環境で `OffscreenCanvas` を使い、現在のズームで非表示のレイヤーに対するクリッピングマスクや、キャッシュ済みVertex Arrayの不要な再Bindを省いた。terrainでは古いdrapeの再描画を1フレーム最大1件に制限している。

このほか、terrain読み込み中の `setStyle()`、GeoJSONの `updateData`、カメラ操作へ `undefined` を渡した場合、非表示コンテナから表示した直後のサイズ、`iframe` と `srcdoc` のDOM sanitizationなどが修正された。

## v6.8.0で確認した変更

2026年9月に公開されたv6.8.0では、スタイルをURLから読み込んだ場合に元URLを取得する `map.getStyleUrl()` が追加された。表示と性能では、terrainのrender-to-texture出力へのmipmapとtrilinear filtering、シェーダーコンパイル待ちの短縮、テキスト整形用 `Intl.Segmenter` の遅延生成、デフォルトMarkerの複製方式が導入された。

同リリースでは、次のような描画・操作上の不具合も修正された。

- 反子午線をまたぐMarkerに付随するPopupが別のworld copyへ移る問題
- ズーム変更後にterrain drape textureが更新されない問題
- globeからmercatorへ遷移するときに空と地面の間へ隙間が出る問題
- HTTP 204などの空タイル応答をエラーとして扱う問題
- hillshadeのタイル境界、globe上の高所シンボル、同一フレーム内の `setTiles` 更新などの問題

## 更新時に確認する点

- メジャーバージョンを上げるときは移行ガイドを確認する。
- terrain、globe、カスタムレイヤーを使う場合は、通常の平面地図とは別に表示確認を行う。
- 大量のMarkerをDOM要素として配置する前に、シンボルレイヤーやクラスタリングとの使い分けを検討する。
- タイル配信では、空レスポンス、CORS、キャッシュ、Range Requestなど、ライブラリ外の配信条件も確認する。

## 関連項目

- [全国メッシュデータのWeb配信](../methods/national-grid-web-delivery.md)
- [Portolan](../data/portolan.md)
- [Cesium](cesium.md)

## 出典

- [MapLibre GL JS documentation](https://maplibre.org/maplibre-gl-js/docs/)（2026-09-09確認）
- [MapLibre GL JS v6.8.0 release](https://github.com/maplibre/maplibre-gl-js/releases/tag/v6.8.0)（2026-09-09確認）
- [MapLibre GL JS v6.9.0 release](https://github.com/maplibre/maplibre-gl-js/releases/tag/v6.9.0)（2026-09-10確認）
