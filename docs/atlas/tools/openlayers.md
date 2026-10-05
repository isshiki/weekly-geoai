---
layout: default
title: OpenLayers
category: tools
updated: 2026-10-05
---

# OpenLayers

OpenLayersは、地図タイル、ベクターデータ、マーカーなどをWebページに表示するオープンソースのJavaScriptライブラリである。

**種類：Web地図用ライブラリ。JavaScriptでの開発が必要。** データの読み込み元とレイヤーを組み合わせ、自分のWeb画面へ地図を組み込む。

## 最初に理解する四つの部品

| 部品 | 意味 |
| --- | --- |
| Map | 地図を置くWebページ上の領域を管理する |
| View | 表示の中心・ズーム・投影法などを管理する |
| Layer | 背景地図や店舗の点など、重ねる表示の単位 |
| Source | 各レイヤーが読むデータの取得元 |

[公式Quick Start](https://openlayers.org/doc/quickstart.html)で背景地図を表示し、その後に手元の地物を重ねると流れをつかみやすい。座標が緯度・経度なのか、表示用の投影座標なのかを確認する。背景タイルの利用条件と出典表示も別途必要になる。

比較する際は、対応形式だけでなく、自分のデータを読み込めるか、必要な操作を実装できるかを小さな例で確かめる。[MapLibre GL JS](maplibre-gl-js.md)もWeb地図の開発部品であり、[Felt](felt.md)は地図の作成・共有をブラウザーで扱うサービスである。

## 更新例：v10.11.0（2026年10月5日日本時間公開）

以下はこの版の変更点であり、すべての版に共通する導入条件ではない。

### データ対応と読み込み

GeoZarrは汎用の多次元データを表示し、`storeOptions`でヘッダーや認証情報を指定できる。`ol/source/Raster`もデータタイルへ基本対応した。不要になったタイルを待機列から除き、WebGL文字用ワーカーは必要時に読み込む。

### 更新時に確認する表示とデータの扱い

| 変更 | 確認点 |
| --- | --- |
| 色補間をsRGBへ統一 | Canvasの従来の色合いを保つにはinterpolate-hcl。現時点ではCanvasのみ対応 |
| 空座標のGeoJSON | GeometryCollectionを除きnull形状として扱う |
| WMTSの表示範囲 | タイル行列から範囲を導く方式を変更し、低ズームでの切れを修正 |
| WMTSのwrapX自動判定 | 横方向の繰り返しを避ける場合はfalseを明示 |

同じデータでも更新で色や表示範囲が変わり得るため、既存の主題図と凡例を照合する。今回は公式ノートの確認で、アプリへの更新適用は行っていない。

## 出典

- [OpenLayers公式概要](https://openlayers.org/)（2026-10-05確認）
- [OpenLayers公式Quick Start](https://openlayers.org/doc/quickstart.html)（2026-10-05確認）

- [OpenLayers v10.11.0](https://github.com/openlayers/openlayers/releases/tag/v10.11.0)（2026-10-05確認）
