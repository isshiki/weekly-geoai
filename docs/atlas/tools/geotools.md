---
layout: default
title: GeoTools
category: tools
updated: 2026-10-05
---

# GeoTools

GeoToolsは、Javaアプリケーションで地理空間データの読み書き、座標変換、地図描画などを扱うオープンソースのライブラリ群である。

**種類：Java向け開発ライブラリ。Javaでの開発と依存関係の設定が必要。** 地図を操作する完成済みアプリではなく、自分のアプリへ機能を組み込むための部品である。

## 何を組み合わせるか

| 目的 | 主な部品 |
| --- | --- |
| 地物と属性を扱う | Data APIと、対象形式のプラグイン |
| 座標系を変換する | Referencingと、EPSG定義を供給するプラグイン |
| 地図を描画する | Java2Dを使うレンダラー |
| 画像・ラスタを扱う | Coverageと、GeoTIFFなどの形式別プラグイン |

必要なモジュールを選び、公式導入手順に沿ってMavenで依存関係を管理する。Javaの必要バージョンは採用するGeoToolsの版で確認する。データの[座標参照系](../concepts/coordinate-reference-systems.md)を理解してから、読み込み・変換・表示を試すとよい。

ブラウザー内の地図画面を作る[MapLibre](maplibre-gl-js.md)や[OpenLayers](openlayers.md)とは、実行環境と組み込む場所が異なる。

## GeoPackage表示の実装例

2026年10月2日のQiita記事は、Java 17以上・GeoTools 35.1を使い、GeoPackageを地理院タイルへ重ねる。座標系を確認して表示用にEPSG:3857へ変換し、元ファイルには書き戻さない。移動・拡大縮小・レイヤー切り替え・属性表を備える。背景タイル取得にはネット接続を使う。

| 対象 | このひな形の上限 |
| --- | --- |
| ファイル | 200 MiB |
| 全レイヤーの地物 | 合計100,000件 |
| 頂点 | 合計3,000,000点 |
| 属性表 | 各レイヤーの先頭200件 |

これらはGeoTools自体の上限ではなく、メモリに地物を保持するひな形の制約である。著者は自動テスト25件成功と報告する一方、実機GUIテストはスキップし、Windows／WSLgの画面操作は未確認と明記する。今回も配布コードは実行していない。

## 出典

- [GeoTools公式：Architecture](https://docs.geotools.org/latest/userguide/welcome/architecture.html)（2026-10-05確認）
- [GeoTools公式：How to Use GeoTools](https://docs.geotools.org/latest/userguide/welcome/use.html)（2026-10-05確認）

- [JavaとGeoToolsで、GeoPackageを表示する地図アプリのひな形を作ってみた](https://qiita.com/rino_yume/items/bbbbd4f2b23fc23bd44f)（2026-10-03確認）
