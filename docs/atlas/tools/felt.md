---
layout: default
title: Felt
category: tools
updated: 2026-09-14
---

# Felt

Feltは、地理空間データの表示、分析、ダッシュボード、共有をブラウザ上で扱うWeb GISである。ローカルファイルのアップロードに加え、データウェアハウス、Postgres、クラウドストレージ、STACなどへ接続し、元データを既存環境に残したまま地図を利用者へ届ける構成を取れる。

## GIS構成での役割

Feltを計算、保管、公開のすべてを担う単独システムとして使う必要はない。既存環境と組み合わせる場合は、次のように役割を分けられる。

| 層 | 主な役割 |
| --- | --- |
| QGISや分析コード | データ作成、専門的な解析、品質確認 |
| PostGIS・データウェアハウス | 正式データの保管、SQLによる抽出・集計 |
| オブジェクトストレージ | COGなど大規模ファイルの保管と部分配信 |
| Felt | Web表示、スタイル、ダッシュボード、共同編集、共有 |
| AIエージェントとMCP | 指示をSQL、空間処理、地図作成へ接続 |

大量データでは、全件をブラウザへ送るのではなく、データベース側で対象を絞るか、COGのように必要部分を読める形式で配信する。

## 対応データとCloud Native GIS

FeltはShapefile、GeoJSON、GeoPackage、GeoParquetなどのベクターデータと、GeoTIFFなどのラスターデータを読み込める。大規模ラスタでは、S3、Google Cloud Storage、Azure Blob StorageなどにCOGを置き、Range Requestで必要部分を読む構成を案内している。静的STACとSTAC APIもデータソースとして登録できる。

これらのクラウド接続やストリーミングにはプラン条件がある。導入時には、アップロードによる複製か元データへの直接接続か、保存リージョン、アクセス権限、通信量、更新方法を確認する。

## Felt AIとMCP Server

Feltは自然言語から地図や空間分析を作るFelt AIを提供する。2026年4月に発表されたFelt MCP Serverは、1つのエンドポイントから約30のツールを公開し、次の処理をAIエージェントから扱う。

- 地図とプロジェクトの作成・更新
- ArcGISサービス、WMS、GeoJSON、Shapefile、クラウドデータの取り込み
- Snowflake、BigQuery、Databricks、Postgres、RedshiftへのSQL
- レイヤーの検索、結合、絞り込み、新規レイヤー生成
- カテゴリー、数値、ヒートマップ、H3のスタイル設定
- ピン、経路、ポリゴン、注記による共同作業

MCP経由の操作にはFeltユーザーの権限が引き継がれ、結果は閲覧・編集可能な地図として残る。公式発表時点ではMCP ServerはEnterprise workspace向けであるため、利用可否と契約条件は最新情報を確認する。

## 導入時の確認点

- 正式な原本とFelt上の派生データを区別する。
- AIが生成したSQL、集計条件、結合結果を地図と件数の双方で確認する。
- SaaSへ送信または接続するデータの機密区分と契約条件を確認する。
- 高度な数値計算や再現可能なバッチ処理は、適切な分析環境へ残す。
- プラン、API、MCPツール、料金の変更を前提に依存範囲を決める。

## 関連項目

- [Cloud Native Geospatial](../concepts/cloud-native-geospatial.md)
- [Location AI](../concepts/location-ai.md)
- [CARTO MCP Server](carto-mcp-server.md)
- [AIが扱いやすい地理空間開発環境](../methods/ai-ready-geospatial-development.md)

## 出典

- [Every AI agent now has a full GIS: Introducing Felt’s MCP server](https://felt.com/blog/introducing-felt-mcp-server)（2026-09-14確認）
- [Felt Help Center: Files](https://help.felt.com/upload-anything/files)（2026-09-14確認）
- [Felt Help Center: Organizing your raster data](https://help.felt.com/upload-anything/raster-infrastructure/organizing-your-raster-data)（2026-09-14確認）
- [Feltを調べてみた ― Cloud Native GISはどこまで身近になったのか](https://qiita.com/rino_yume/items/b76443c5010bf0de2ceb)（2026-09-14確認）
