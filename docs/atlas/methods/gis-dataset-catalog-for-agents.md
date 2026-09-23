---
layout: default
title: GISデータセットカタログ
category: methods
updated: 2026-09-23
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

## 読み取り専用のMCP公開

2026年9月17日のStep 2記事は、既存の`CatalogService`の外側へFastMCPの層を追加する。CLIとMCPでカタログ処理を二重実装せず、共通サービスを呼び出す構成である。

- Tool：`gis_list_datasets`、`gis_describe_dataset`、`gis_list_versions`、`gis_runtime_status`。
- Resource：`gis://catalog`と`gis://dataset/{dataset_id}`。
- 公開する情報：データの意味、CRS、geometry、件数など。コンテナー内部の保存パスは返さない。
- 検証：メモリ内、プロセス内HTTP、Docker Composeの別コンテナーからの接続を分けて確認する。

記事の実装はFastMCP 3.4.7を固定し、Streamable HTTPを利用する。登録やGIS解析をMCP Toolへ追加する前に、カタログの読み取りを検証する段階である。記事が示す実装内容を整理したもので、Atlasでコードを実行・検証したものではない。

## 出力を追跡するResult Store

2026年9月22日のStep 3では、入力のカタログに加えて出力を`result_id`で管理するResult Storeを追加した。入力データの版、処理条件、成果物、来歴を結び付け、ファイル名だけに依存しない追跡を行う。

| 段階 | 確認すること |
| --- | --- |
| 一時保存 | 成果物を作業領域に書き込む |
| 再検査 | 保存したファイルを開き直して検証する |
| 確定 | 成果物と来歴を登録して利用可能にする |
| 復旧 | DB状態と実ファイルを照合し、未完了処理を再検査する |

DBのトランザクションだけでは、ファイルの移動とDB更新を一括して元に戻せない。記事では処理途中の停止を想定し、検査に失敗した隔離結果は自動で利用可能に戻さない設計を取る。

MCPには結果の一覧・詳細を読み取り専用で公開し、保存パスや全Geometryを応答に載せない。検証用処理は登録済みデータのsnapshotであり、BufferやIntersectionなどの空間演算は次段階である。同じリクエストのfingerprintは追跡用で、自動キャッシュの実装とは区別する。

## 関連項目

- [AIが扱いやすい地理空間開発環境](ai-ready-geospatial-development.md)
- [Portolan](../data/portolan.md)
- [全国メッシュデータのWeb配信](national-grid-web-delivery.md)

## 出典

- [FastMCP 3 + DockerでGIS MCP Serverを作る：Step 3](https://qiita.com/rino_yume/items/d9a0277dc7878d68068a)（2026-09-22公開、2026-09-23確認）

- [FastMCP 3 + Docker でGIS MCP Serverを作る ― Step 2](https://qiita.com/rino_yume/items/71a5872200aa24af24c1)（2026-09-18確認）

- [FastMCP 3 + Docker でGIS MCP Serverを作る ― Step 1 Dataset CatalogとVector GIS登録基盤](https://qiita.com/rino_yume/items/24ee23e203af14682e97)（2026-09-10確認）
