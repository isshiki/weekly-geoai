---
layout: default
title: MapLibre GL JS
category: tools
updated: 2026-09-24
---

# MapLibre GL JS

MapLibre GL JSは、ベクタータイルなどからインタラクティブな地図をブラウザ上へ描画するTypeScriptライブラリである。WebGLを利用し、レイヤーの見た目やデータソースをMapLibre Style Specificationに沿ったスタイル文書で制御する。

## 主な役割

- ベクタータイル、GeoJSON、ラスター、terrainなどをWeb地図として表示する。
- レイヤー、カメラ、Marker、Popup、ユーザー操作をAPIから制御する。
- メルカトル表示に加え、globe表示や3D terrainを扱う。
- PMTilesなど、追加プロトコルを介した配信形式と組み合わせられる。

## v6.10.0で確認した変更

2026年9月15日（GitHub表示日）のv6.10.0では、globe表示の空を高度に応じてフェードさせるよう変更し、fill・fill-extrusionの三角形分割で頂点インデックスの重複参照を減らした。

terrainに隠れたMarkerの判定は、GPUの深度バッファー読み戻しから、DEM上をたどるCPU処理へ変更された。地形付き地図の移動中にMarkerごとに発生するGPU待ちをなくす変更として説明されている。

古いSafariでの部分的な空白表示、style diff中のterrain変更、高ズーム時のモバイルGPUのhillshade表示を修正した。地形へ重ねる描画用テクスチャも、地図の静止時やterrain削除時に解放するようになった。これらはリリースノートの記録であり、端末別の性能をAtlas側で検証したものではない。

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

## v6.11.0で確認した変更

2026年9月22日UTC（日本時間9月23日）公開のv6.11.0では、タッチ端末の長押しによる`contextmenu`イベントと、地理座標を指定した画面位置に置くカメラ設定を計算する`Map#calculateAnchoredCameraOptions`を追加した。後者は計算だけを行い、呼び出し自体では地図を動かさない。

`promoteId`付きソースのタイル間シンボル照合を高速化したほか、macOSのFirefoxで6.8.0以降に発生した移動・ズームの遅さ、投影変更や地形の遅延読み込みによるMarker・Popupの位置ずれを修正している。端末別性能は本ページでは実測していない。

## 関連項目

- [全国メッシュデータのWeb配信](../methods/national-grid-web-delivery.md)
- [Portolan](../data/portolan.md)
- [Cesium](cesium.md)

## 出典

- [今回確認した出典](https://github.com/maplibre/maplibre-gl-js/releases/tag/v6.11.0)（2026-09-24確認）

- [MapLibre GL JS v6.10.0 release](https://github.com/maplibre/maplibre-gl-js/releases/tag/v6.10.0)（2026-09-15公開、2026-09-16確認）

- [MapLibre GL JS documentation](https://maplibre.org/maplibre-gl-js/docs/)（2026-09-09確認）
- [MapLibre GL JS v6.8.0 release](https://github.com/maplibre/maplibre-gl-js/releases/tag/v6.8.0)（2026-09-09確認）
- [MapLibre GL JS v6.9.0 release](https://github.com/maplibre/maplibre-gl-js/releases/tag/v6.9.0)（2026-09-10確認）
