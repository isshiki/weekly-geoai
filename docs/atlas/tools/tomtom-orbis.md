---
layout: default
title: TomTom Orbis APIs
category: tools
updated: 2026-09-19
---

# TomTom Orbis APIs

TomTom Orbis APIsは、共通の地図基盤と呼び出し規則で場所検索・経路・交通などを扱うAPI群である。

## APIの構成

2026年7月8日の発表で、Map Display、Traffic、Routing、Places Search、Geocoding、Reverse Geocodingの6 APIが一般提供された。

- 認証とバージョン指定は共通ヘッダーを使い、座標は経度・緯度順のGeoJSONに揃える。
- 各APIにOpenAPI仕様を用意する。Places Searchは候補提示・検索・詳細取得の3操作で構成する。
- 発表時点のGA範囲は自動車ルーティングなどであり、トラック・バッチルーティングなどは対象外である。

## AIから使う方法の区別

| 方法 | 記事で示す用途 |
| --- | --- |
| MCP Server | 会話中に複数のAPIを選択して呼び出す |
| OpenAPI仕様 | コーディングエージェントなどで単一APIを自分のコードへ組み込む |

JavaScript SDKは同記事の時点でPublic Previewであり、APIのGAと区別する。SDKは無料で利用できるが、基盤APIの利用には料金が発生する。

## 出典

- [TomTom Orbis APIs are now in general availability](https://www.tomtom.com/newsroom/product-focus/tomtom-orbis-apis-are-now-in-general-availability/)（2026-09-19確認）
