---
layout: default
title: 位置情報PaaSの選び方と相互運用性
category: methods
updated: 2026-09-25
---

# 位置情報PaaSの選び方と相互運用性

位置情報PaaSは、地図表示、住所検索、経路計算などをAPIやSDKでアプリへ組み込むクラウドサービスである。EsriはArcGIS Location Platformを例に、OSSライブラリとの連携や、機能を追加できる構成を説明している。

## 選定時に分けて見る項目

| 観点 | 確認する内容 |
| --- | --- |
| 必要な機能 | 地図・ジオコーディング・経路・標高・分析が用途を満たすか |
| 接続と形式 | REST API、標準形式、既存の地図ライブラリで扱えるか |
| データの扱い | 保存・共有・移行についてどの条件があるか |
| 運用 | 利用量に対する価格、サポート、終了時の代替を確認できるか |

前半の観点はEsriの選定記事に基づく。終了時の代替も合わせて確認するのは、Atlasでの運用上の整理である。

Esriの記事はLeaflet、OpenLayers、MapLibre GL JS、CesiumJSなどとの連携を紹介する製品提供者の解説である。APIが公開されていること、OSSから呼べること、データを自由に再配布できることは別々に確認する。記事でいう「オープン開発」を、サービス全体がオープンソースであるという意味には使わない。

## 関連項目

- [外部地図サービスの廃止と依存関係の点検](map-service-lifecycle.md)
- [GeoAIの標準化と実務での採用](../concepts/geoai-standards-and-adoption.md)

## 出典

- [Esri Community：ロケーション サービスにオープンな開発をサポートする PaaS を選ぶべき理由](https://community.esri.com/ja/discussion/1720940/)（2026-09-25確認）
- [Esri：For Location Services, Pick a PaaS That Supports Open Development](https://www.esri.com/arcgis-blog/products/platform/developers/for-location-services-pick-a-paas-that-supports-open-development-heres-why)（2026-09-25確認）
