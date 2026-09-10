---
layout: default
title: GISデータセットカタログ
category: methods
updated: 2026-09-10
---

# GISデータセットカタログ

GISデータセットカタログは、AIエージェントやMCP Toolが任意のファイルを直接開く前に、データを検査、登録、版管理し、安定した識別子で参照するための管理層である。物理ファイルパスをLLMへ渡さず、許可されたデータだけを後段の空間処理へ公開できる。

## 管理情報と実データを分ける

カタログにはGeometry本体ではなく、次のような管理情報を保存する。

- `dataset_id`、version、status
- 格納先とSHA-256
- CRS、geometry type、feature count、bbox
- 列名と型、登録日時

実データはGeoPackageやGeoParquetなどのファイルとして管理し、利用側は `dataset_id` とversionを指定する。これにより保存場所を変更しても外部インターフェースを保ちやすく、同じデータセットの過去版も追跡できる。

## 登録フロー

```text
incoming
  ↓ 形式・読込・CRS・Geometry・件数・bboxを検査
workへコピー
  ↓ コピー後に同じ条件を再検査
datasetsへ確定
  ↓
カタログへmetadataとchecksumを登録
```

コピー前後の二重検査は、検査したファイルと登録するファイルが同じ条件を満たすことを確認するために行う。CRSのないデータをそのまま距離・面積・座標変換へ渡さない、複数レイヤーを持つGeoPackageでは対象レイヤーを明示する、といった入口の規則も重要である。

## MCPより先に作る理由

2026年9月の実装記事では、DuckDBを管理カタログに用い、GeoPackage、GeoJSON、GeoParquetの登録基盤を先に構築している。FastMCPのToolやHTTP Serverは次の段階へ分離し、カタログのServiceをCLIとMCPの双方から再利用する設計である。

この分離により、MCP接続の有無とは独立して、データ検査、版管理、migration、rollback、実ファイルを使ったテストを行える。エージェントへ公開する前にデータ面の境界を固定する考え方として再利用できる。

## 運用時の確認点

- 対応形式、最大容量、展開後容量、レイヤー数を制限する。
- dataset ID、version、checksumをログへ残し、処理結果の再現性を確保する。
- カタログのmigrationをtransactionで適用し、適用済みSQLのhashを記録する。
- 登録済みデータを読み取り専用で扱う処理と、更新・削除の権限を分離する。
- CRSが存在するだけで正しいとは限らないため、範囲と単位も検証する。

## 関連項目

- [AIが扱いやすい地理空間開発環境](ai-ready-geospatial-development.md)
- [Portolan](../data/portolan.md)
- [全国メッシュデータのWeb配信](national-grid-web-delivery.md)

## 出典

- [FastMCP 3 + Docker でGIS MCP Serverを作る ― Step 1 Dataset CatalogとVector GIS登録基盤](https://qiita.com/rino_yume/items/24ee23e203af14682e97)（2026-09-10確認）
