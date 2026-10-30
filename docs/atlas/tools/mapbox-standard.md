---
layout: default
title: Mapbox Standard
category: tools
updated: 2026-10-30
---

# Mapbox Standard

Mapbox Standardは、Mapboxの地図アプリで背景地図として利用するスタイルである。

## 道路の詳細表示

2026年9月18日の更新では、車線境界・右左折矢印・横断歩道・停止線に加え、橋・トンネル・高架道路の立体表現を追加した。車線標示などはズーム16で表示される。

| 対象 | 提供段階・条件（記事公開時点） |
| --- | --- |
| Standardの道路詳細 | 29カ国71都市で提供 |
| 有効化 | Maps SDK 11.30（iOS・Android）またはGL JS 3.30を使い、Lane Detailsまたは`showHdRoads`を有効化 |
| Navigation SDKの3D Lanes | 限定的なPrivate Preview |

道路構造を背景地図で表現する機能であり、Standardの道路表示とナビゲーションSDKの提供段階は分けて確認する。

## 分析結果をWeb地図へ渡す

Matt Forrestの制作紹介では、QGIS・ArcGISでの分析成果をデータ層とし、Mapbox GL JSとStandardを描画に使う。ビルド工程のない単一HTMLから始め、コードの設定値またはStudioの再利用可能なスタイルで外観を調整する。AIコーディング支援にも、望む描画技術を明示する考え方を示している。

2026-10-30に作者の公開投稿で確認した範囲であり、動画本編とアプリの動作は未検証。Standardの新機能発表ではなく、分析と表示の役割分担を学ぶ制作例として読む。

## 出典

- [New road detail in Mapbox Standard](https://www.mapbox.com/blog/new-road-detail-in-mapbox-standard)（2026-09-19確認）

- [Matt Forrest：Web地図制作の紹介](https://www.linkedin.com/posts/mbforr_ask-four-different-coding-agents-to-build-activity-7491128889424048128-zknb)（2026-10-30確認）
