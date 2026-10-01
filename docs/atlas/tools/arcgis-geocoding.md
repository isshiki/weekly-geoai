---
layout: default
title: ArcGIS Geocoding Service
category: tools
updated: 2026-10-01
---

# ArcGIS Geocoding Service

ArcGIS Geocoding Serviceは住所の照合と位置の特定に使うサービスである。更新を確認する際は、住所データの増強、対象国、APIの入出力仕様を分けて捉える。

## 2026年9月の更新

Esriが9月30日に公開した記事では、7カ国のポイント住所データを増強し、Match Narrativeの対応を日本を含む13カ国へ追加した。対応国は計53カ国となる。住所データの増加率は対象国ごとの数値であり、日本の住所件数が増えたという発表ではない。

| API・出力の変更 | 利用時に確認する点 |
| --- | --- |
| `matchIDFormat` | `findAddressCandidates`と`geocodeAddresses`で短い`matchID`を要求できる |
| サービス情報の`parameters` | 対応するREST API引数を確認できる |

短いIDはファイル容量の削減を目的とした変更であり、住所照合の精度向上とは区別する。今回の確認は更新記事に基づき、日本の住所を用いた実行検証は行っていない。

## 出典

- [公式発表](https://www.esri.com/arcgis-blog/products/platform/announcements/whats-new-with-the-arcgis-geocoding-service-explore-september-2026-updates)（2026-10-01確認）
