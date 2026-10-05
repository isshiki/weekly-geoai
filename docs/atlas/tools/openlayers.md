---
layout: default
title: OpenLayers
category: tools
updated: 2026-10-05
---

# OpenLayers

OpenLayersはWeb地図の描画ライブラリである。2026年10月5日日本時間公開のv10.11.0は、スタイル・多次元ラスタ・OGCサービスへの対応を更新した。

## データ対応と読み込み

GeoZarrは汎用の多次元データを表示し、`storeOptions`でヘッダーや認証情報を指定できる。`ol/source/Raster`もデータタイルへ基本対応した。不要になったタイルを待機列から除き、WebGL文字用ワーカーは必要時に読み込む。

## 更新時に確認する表示とデータの扱い

| 変更 | 確認点 |
| --- | --- |
| 色補間をsRGBへ統一 | Canvasの従来の色合いを保つにはinterpolate-hcl。現時点ではCanvasのみ対応 |
| 空座標のGeoJSON | GeometryCollectionを除きnull形状として扱う |
| WMTSの表示範囲 | タイル行列から範囲を導く方式を変更し、低ズームでの切れを修正 |
| WMTSのwrapX自動判定 | 横方向の繰り返しを避ける場合はfalseを明示 |

同じデータでも更新で色や表示範囲が変わり得るため、既存の主題図と凡例を照合する。今回は公式ノートの確認で、アプリへの更新適用は行っていない。

## 出典

- [OpenLayers v10.11.0](https://github.com/openlayers/openlayers/releases/tag/v10.11.0)（2026-10-05確認）
