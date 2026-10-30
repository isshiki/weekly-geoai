---
layout: default
title: MapLibre GL JS
category: tools
updated: 2026-10-30
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

## 重要な更新履歴 { #release-history }

対象はWeb向けのMapLibre GL JSであり、[MapLibre Native](maplibre-native.md)とは版番号を分ける。2026-10-30に下表の公式リリースノートを確認した。収録範囲は5.0・6.0の大きな節目と6.8.0〜6.16.0の主要変更で、中間版や小さな修正は網羅していない。未掲載は変更なしを意味しない。公開日はUTCで、日次ニュースの収録日や日本時間の日付とは異なる場合がある。最新推奨版の一覧ではなく、実行試験は未実施である。

| バージョン・公式出典 | 公開日（UTC） | 変わったこと・使いどころ | 状態・更新時の注意 |
| --- | --- | --- | --- |
| [v6.16.0](https://github.com/maplibre/maplibre-gl-js/releases/tag/v6.16.0) | 2026-10-25 | 表示範囲を緯度・経度の一方だけに制限。初期化時のスタイル変換を追加 | iOSのWorker停止後や背景復帰時の表示・読み込みを修正。対象端末で確認 |
| [v6.15.0](https://github.com/maplibre/maplibre-gl-js/releases/tag/v6.15.0) | 2026-10-18 | 独自の平面CRSとGeoJSON投影に実験対応。縦書きのvert字形にも対応 | 地図に合うタイルグリッドが必要。回転・傾斜設定のaroundCenterは非推奨 |
| [v6.14.0](https://github.com/maplibre/maplibre-gl-js/releases/tag/v6.14.0) | 2026-10-11 | globalStateの初期値を地図作成・スタイル設定時に指定 | 一部iPadOS 16 Safariの空白表示を修正。利用環境による |
| [v6.13.0](https://github.com/maplibre/maplibre-gl-js/releases/tag/v6.13.0) | 2026-10-06 | globeの中心を極まで移動可能に。カスタム描画を地形へ沿わせる実験API | Workerを再び自己完結に変更。shared.mjs系の配布ファイルは非推奨 |
| [v6.12.0](https://github.com/maplibre/maplibre-gl-js/releases/tag/v6.12.0) | 2026-10-03 | 現在地追跡のズームと地図余白を制御。継続更新するGeoJSONの安定性を改善 | setData連続呼出しによるメモリ増大・クラッシュを修正 |
| [v6.11.0](https://github.com/maplibre/maplibre-gl-js/releases/tag/v6.11.0) | 2026-09-22 | タッチ長押しのcontextmenuと、指定地点を画面上の位置に合わせるカメラ計算 | スマホの操作や地図と説明パネルの連動に利用する機能 |
| [v6.10.0](https://github.com/maplibre/maplibre-gl-js/releases/tag/v6.10.0) | 2026-09-15 | globeの空表示、面の描画、地形に隠れるMarkerの判定を改善 | 古いSafariの部分的な空白表示も修正。地図全体の速度向上率とは区別 |
| [v6.9.0](https://github.com/maplibre/maplibre-gl-js/releases/tag/v6.9.0) | 2026-09-09 | 複雑な文字体系を改善。アラビア語・ヘブライ語をRTLプラグインなしで描画 | setRTLTextPluginなどは非推奨。多言語地図の依存を見直す |
| [v6.8.0](https://github.com/maplibre/maplibre-gl-js/releases/tag/v6.8.0) | 2026-09-07 | スタイルURL取得と塗りパターンのSDF描画を追加。地形のちらつきを改善 | 読み込み・描画の最適化は処理別の変更であり、全体性能は未計測 |
| [v6.0.0](https://github.com/maplibre/maplibre-gl-js/releases/tag/v6.0.0) | 2026-07-22 | 配布をESMへ統一。画像欠落時の解決方法やイベントAPIも変更 | UMD版のscript読込やdefault importなど既存コードの移行が必要 |
| [v5.0.0](https://github.com/maplibre/maplibre-gl-js/releases/tag/v5.0.0) | 2024-12-31 | globeで地形を表示。WebGL設定などを拡充 | onの戻り値、WebGL設定の指定場所などに破壊的変更。独自CRSの導入版とは別 |

## 独自の平面座標系を扱う

v6.15.0の実験対応により、地図を描く「方眼紙」にあたる平面座標系を開発者が登録できる。GeoJSONは定義文字列と投影ハンドラーを使い、ワーカーで登録CRSへ投影する。CRSは座標参照系の略である。

日本の地域向け座標系で分析格子や測量図を見せる用途が考えられる。ただし、タイルの中身は自動再投影されず、表示先のCRSと四分木グリッドに合うタイルを用意する必要がある。表示のCRS変更だけで距離・面積の計算が正しくなるわけではない。[座標系の基礎](../concepts/coordinate-reference-systems.md)で計算と表示の役割を分けて考える。

[公式CRSガイド](https://maplibre.org/maplibre-gl-js/docs/guides/custom-crs/)・[addProjection](https://maplibre.org/maplibre-gl-js/docs/API/functions/addProjection/)（2026-10-30確認）。日本の座標系での描画・性能は本Atlasでは未検証である。

## GIS基盤と地図画面をつなぐ

NextGIS Frontendは、NextGIS Webで管理したデータ・スタイル・権限と、JavaScriptで作る地図画面をつなぐライブラリ群である。2026年10月2日発表の4.0は、Leaflet・OpenLayers・MapLibre間で選択、絞り込み、ポップアップ、操作部品などの扱いを共通化し、React連携を改善した。

QuickMapServicesの背景地図検索用パッケージはNextGIS Webから独立して利用できる。AI開発支援向けの`llms.txt`索引も整備したが、資料があること自体はAIの実装結果の正確さを保証しない。既存利用者はフィルター指定、MapLibre GL JS 6対応、共通操作部品の移行を確認する。

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

- [MapLibre GL JS v6.14.0](https://github.com/maplibre/maplibre-gl-js/releases/tag/v6.14.0)（2026-10-12確認）

- [NextGIS Frontend 4.0: Less Integration Code, More Powerful Web Maps](https://nextgis.com/blog/nextgis-frontend-4/)（2026-10-12確認）

- [MapLibre GL JS v6.15.0](https://github.com/maplibre/maplibre-gl-js/releases/tag/v6.15.0)（2026-10-19確認）

- [v6.16.0（MapLibre GL JS）](https://github.com/maplibre/maplibre-gl-js/releases/tag/v6.16.0)（2026-10-26確認）
