---
layout: default
title: MCP for ArcGIS Location Services
category: tools
updated: 2026-11-17
---

# MCP for ArcGIS Location Services

MCP for ArcGIS Location Servicesは、AIアプリケーションからArcGISの位置情報サービスを呼び出すためのMCPサーバーである。確認した記事ではパブリックベータとして案内されている。

## 提供するツール

住所検索、逆ジオコーディング、経路計算、標高取得、地図画像生成、場所の説明などを扱う。利用にはArcGIS Location Platformのアカウントとベータへのアクセスが必要である。

## 開発支援のMCPとの違い

ArcGISには、地図サービスを呼び出す接続と、地図アプリを作るための資料を読む接続がある。「MCP対応」という名前だけで、できる作業を判断しない。

| 仕組み | 主に行うこと | 利用場面 |
| --- | --- | --- |
| MCP for ArcGIS Location Services | 住所・経路などの位置情報サービスを呼ぶ | 指定した地点への道順を調べる |
| ArcGIS agentic developer toolkitのMCP | 公式の開発ガイド、SDK/API資料、コード例を検索・取得する | AIにArcGISアプリの実装方法を調べてもらう |
| 同toolkitのAgent Skills | 認証や実装パターン、エラー処理などの開発手順を案内する | 資料を使って設計・コード作成を進める |

公式用語集は、開発資料向けMCPの接続先を公開していると説明する。接続先が公開されていることと、作ったアプリが使うArcGISサービスの認証・利用条件は別に確認する。資料の取得だけで利用者の地図を操作したことにはならない。

2026年11月16日のESRIジャパンの案内では、Location PlatformとEnterpriseのMCPはベータで、年内の一般提供を予定している。これは発表時点の予定であり、一般提供済みとして扱わない。開発支援toolkitと、これらのサービス側MCPは提供段階も別々に確認する。

## 複数サービスを組み合わせる例

記事は、国土交通データプラットフォームから避難所を取得し、ArcGISで徒歩経路と標高を調べる例を示している。筆者の試行では、ArcGISのMCPを使わない場合は直線距離からの概算となり、使用時は道路に沿う解析が可能になった。一方、一部の距離をマイルからメートルへ修正する作業が必要だった。

この試行は個別の利用例であり、一般的な性能評価や避難経路の安全性を保証する検証ではない。公開日は取得できた本文から確認できていない。

## 出典

- [MCP for ArcGIS Location Services からはじめるエージェンティック AI 体験](https://community.esri.com/ja/discussion/1720846/)（2026-09-17確認）

- [ArcGIS agentic developer toolkit公式用語集](https://developers.arcgis.com/documentation/glossary/arcgis-agentic-developer-toolkit/)（2026-11-17確認。資料取得とSkillsの役割。接続・コード生成は未実行）
- [Geospatial AI 最新情報（2026年11月）](https://blog.esrij.com/archives/73197)（2026-11-17確認。11月16日公開、MCPの提供段階）
