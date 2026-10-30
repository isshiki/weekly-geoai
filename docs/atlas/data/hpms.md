---
layout: default
title: HPMS：米国の道路属性データ
category: data
updated: 2026-10-30
---

# HPMS：米国の道路属性データ

HPMSは、米国FHWAが道路の利用・状態・特性を整理する情報基盤である。道路線の位置だけでなく、その区間の属性を使う交通分析に向く。GISまたは対応するデータ分析環境が必要になる。

## 区間が違う属性をまとめる

2026年10月29日のEsri記事は、ArcGIS Living AtlasでHPMSの全国レイヤーを提供すると案内する。交通量の記録が道路の1〜5マイル、舗装状態が2〜4マイルを対象にすると、記録の区間が一致しない。記事では属性が変わる位置で道路を分割し、各区間へ対応する情報をまとめる方法を説明している。

単純に道路名で結合するのではなく、属性の有効範囲に合わせる点が重要である。交通計画や維持管理などへ利用できるが、情報の提供日と観測年を区別し、すべての道路で同じ属性がそろうと仮定しない。

## 観測時点と利用目的

FHWAの2024版カタログは2024年末の状態を示すスナップショットと説明し、リアルタイムのナビゲーション用データではないと注意している。Living AtlasのCurrentレイヤーと固定年の配布版は同一視せず、利用した版と属性を記録する。Atlasではデータ取得・分析の実行試験はしていない。

## 次に読む

- [空間結合と集計の基本](../methods/spatial-join-and-aggregation.md)：位置や範囲による対応付け。

## 出典

- [Esri：HPMSのLiving Atlas提供](https://www.esri.com/arcgis-blog/products/arcgis-living-atlas/transportation/latest-highway-performance-monitoring-system-data-now-available-in-arcgis-living-atlas)（2026-10-30確認）
- [FHWA：HPMS 2024カタログ](https://catalog.data.gov/dataset/highway-performance-monitoring-system-hpms-2024)（2026-10-30確認）
