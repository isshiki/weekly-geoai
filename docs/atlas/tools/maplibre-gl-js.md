---
layout: default
title: MapLibre GL JS
category: tools
updated: 2026-10-07
---

# MapLibre GL JS

MapLibre GL JSは、ベクタータイルなどからインタラクティブな地図をブラウザ上へ描画するTypeScriptライブラリである。WebGLを利用し、レイヤーの見た目やデータソースをMapLibre Style Specificationに沿ったスタイル文書で制御する。

## 主な役割

- ベクタータイル、GeoJSON、ラスター、terrainなどをWeb地図として表示する。
- レイヤー、カメラ、Marker、Popup、ユーザー操作をAPIから制御する。
- メルカトル表示に加え、globe表示や3D terrainを扱う。
- PMTilesなど、追加プロトコルを介した配信形式と組み合わせられる。

## 使い始める前に

**種類：Web地図用ライブラリ。JavaScriptまたはTypeScriptでの開発が必要。** 例えば店舗の点を地図へ重ね、クリック時に名称を表示するようなWeb画面を作る。

| 用意するもの | 役割 |
| --- | --- |
| 表示するデータ | 店舗のGeoJSON、背景のタイル、地形データなど |
| スタイル | データをどの色・線・ラベルで描くかを指定する |
| Webページとコード | 地図を配置し、読み込みやクリック操作を組み立てる |

ライブラリ、背景地図、フォント、表示データはそれぞれ利用条件を確認する。描画ライブラリの導入だけで、必要な店舗データや配信基盤がそろうわけではない。

[公式Quickstart](https://maplibre.org/maplibre-gl-js/docs/)で地図表示を確認し、次に自分の小さなGeoJSONを重ねると役割を理解しやすい。画面操作中心の共有を試したい場合は[Felt](felt.md)、他のWeb地図実装を比較する場合は[OpenLayers](openlayers.md)も参照する。

## 更新時に確認する点

- メジャーバージョンを上げるときは移行ガイドを確認する。
- terrain、globe、カスタムレイヤーを使う場合は、通常の平面地図とは別に表示確認を行う。
- 大量のMarkerをDOM要素として配置する前に、シンボルレイヤーやクラスタリングとの使い分けを検討する。
- タイル配信では、空レスポンス、CORS、キャッシュ、Range Requestなど、ライブラリ外の配信条件も確認する。

## 重要な更新例：継続的なデータ更新と描画

v6.12.0は2026年10月4日日本時間に公開された。現在地追跡のズーム調整を制御する`zoomToUserAccuracy`と、既存余白へ加算せず適用する`absolutePadding`を追加した。表示タイル変更時のラベル更新も必要部分に絞った。

GeoJSONでは、ワーカー処理より速い`setData`呼び出しによるメモリ増大・クラッシュ、古い処理結果による上書き、クラスタ更新の不整合を修正した。継続的にデータを差し替える地図で確認する変更である。

地形下のカメラから描画タイル外の標高を読む際に0となる問題も修正し、その読み取り処理を約40倍効率化したと説明する。地図全体の描画速度が40倍になったという意味ではない。今回はリリースノートの確認であり、実機性能は測定していない。

## 地球・地形の表示と配信時の互換性

v6.13.0ではglobe表示の中心を極まで移動できるようになり、従来の緯度85.05度の制限が解消された。カスタムレイヤーを地形へ沿わせ、GPUで地形上に配置するAPIも加わったが、実験的APIとして扱う。

更新後の地図が古いWorkerのキャッシュでクラッシュする問題への対応として、Workerは再び自己完結する構成になった。`maplibre-gl-shared.mjs`と`maplibre-gl-shared-dev.mjs`は既存のコピー処理との互換性のため空ファイルで残るが、非推奨で次のメジャー版に削除予定である。独自に配布ファイルをコピーする場合は、移行時の依存を確認する。リリースノートを確認したもので、表示や性能の実測は行っていない。

## 関連項目

- [全国メッシュデータのWeb配信](../methods/national-grid-web-delivery.md)
- [Portolan](../data/portolan.md)
- [Cesium](cesium.md)

## 出典

- [公式導入ガイド](https://maplibre.org/maplibre-gl-js/docs/)（2026-10-05確認）

- [今回確認した出典](https://github.com/maplibre/maplibre-gl-js/releases/tag/v6.11.0)（2026-09-24確認）

- [MapLibre GL JS v6.10.0 release](https://github.com/maplibre/maplibre-gl-js/releases/tag/v6.10.0)（2026-09-15公開、2026-09-16確認）

- [MapLibre GL JS documentation](https://maplibre.org/maplibre-gl-js/docs/)（2026-09-09確認）
- [MapLibre GL JS v6.8.0 release](https://github.com/maplibre/maplibre-gl-js/releases/tag/v6.8.0)（2026-09-09確認）
- [MapLibre GL JS v6.9.0 release](https://github.com/maplibre/maplibre-gl-js/releases/tag/v6.9.0)（2026-09-10確認）

- [MapLibre GL JS v6.12.0](https://github.com/maplibre/maplibre-gl-js/releases/tag/v6.12.0)（2026-10-05確認）

- [MapLibre GL JS v6.13.0](https://github.com/maplibre/maplibre-gl-js/releases/tag/v6.13.0)（2026-10-07確認）
