---
layout: default
title: Portolan
category: data
updated: 2026-09-15
---

# Portolan

Portolanは、地理空間データを人とAIエージェントの双方が発見・理解・直接利用できるようにする、オープンソースのカタログ仕様とツール群である。独自の地理ファイル形式や集中型プラットフォームではなく、既存のクラウドネイティブ形式、STACメタデータ、文書を組み合わせる。

## データ公開の構成

2026年9月2日の公式紹介では、ベクターにGeoParquetとPMTiles、ラスターにCOGを用い、ZarrとCOPCは今後の対応予定としている。対応範囲は採用する仕様バージョンで確認する。データはSTACの `catalog.json` または `collection.json` で記述し、人向けの `README.md` とAIエージェント向けの `AGENTS.md` を添える。

```text
catalog.json     機械が読む構造化メタデータ
README.md        人が読む説明
AGENTS.md        エージェントが読む利用上の手引き
collection/
  collection.json
  README.md
  AGENTS.md
  data.parquet
  data.pmtiles
```

`AGENTS.md` には、推奨するクエリ、座標参照系、既知の制限、ライセンスなど、データを正しく使うための文脈を記述できる。構造化メタデータだけでは表しにくい運用知識を利用者へ渡す役割がある。

## 公開品質としての要件

Portolanはファイルの種類だけでなく、ネットワーク越しに部分読み込みできる状態までを公開品質として扱う。

- GeoParquetは行を空間的に並べ、row groupごとの空間統計を持たせる。1つのrow groupは150,000行以下とする。
- PMTilesを表示用に提供する場合は、独立したMapLibre Style JSONもカタログへ登録する。
- COGは内部overviewと各バンドの最小、最大、平均、標準偏差をファイル内に持たせる。
- 配信サーバーはHTTP Range Requestを受け、`206 Partial Content`、`Accept-Ranges: bytes`、正確な `Content-Length` を返す。
- ブラウザから直接読めるよう、CORSで `GET`、`HEAD`、`Range` などを許可し、`Content-Range` や `ETag` など必要なレスポンスヘッダーを公開する。

仕様への準拠はメタデータ上の宣言だけでは確定せず、構造、メタデータ、データ本体、配信条件をバリデーターで検査して判断する。

## 分散した公開と発見

データは出版者が選んだS3互換ストレージに置き、QGIS、ArcGIS、Pythonなどの利用側ツールが直接読む。Portolan専用APIやサーバーは必要ない。保存場所、クラウド事業者、処理エンジンを分離でき、データ自体は出版者の管理下に残る。

中央のPortolan Registryはデータ本体を集約せず、独立して公開されたカタログを検索可能にする。2026年9月1日の確認記録では20カタログが登録されていた。一部はボランティアが管理する非公式ミラーであり、収録数と公式性は個別に確認する。

## 仕様とツール

- `portolan-spec`: カタログ構造と要件を定める仕様
- `rashid`: 仕様への適合を検証するバリデーター
- `portolan-cli`: カタログの作成・確認・公開を支援するCLI
- `portolan-registry`: 公開カタログの索引
- `portolan-skills`: カタログを作成・利用するエージェント向けスキル

仕様は2026年9月時点で1.0未満であり、要件は変更され得る。カタログは特定のサービスが終了しても標準形式のファイルとして利用できるが、導入時には宣言されたPortolan仕様バージョンとバリデーターの結果を確認する。

## 作成から利用まで

公式紹介では、CLIが取り込み、形式変換、メタデータ管理、公開を担い、rashidが仕様への適合を検査する。エージェント向けスキルはこれらの工程を組み合わせる。

2026年9月14日のQiita記事は、架空の公園を使って変換・検証・Browserでの閲覧を試している。GeoParquetを分析用、PMTilesを表示用に分け、検索には名前・説明・キーワードなどの整備と利用側ツールが必要であると説明する。静的ファイルを置くだけで任意の日本語検索が完成するわけではない。

## 関連項目

- [geoparquet-io](../tools/geoparquet-io.md)
- [知識グラフとLLMエージェントによる地理空間データ探索](../methods/intelligent-geospatial-data-discovery.md)

## 出典

- [Introducing Portolan（CNG公式）](https://cloudnativegeo.org/blog/2026/09/introducing-portolan/)（2026-09-02公開、2026-09-15確認）
- [PortolanでAI-Readyな地理空間情報カタログを作ってみた](https://qiita.com/nokonoko_1203/items/614f699efd768cdaf3a6)（2026-09-14公開、2026-09-15確認）

- [Portolan公式サイト](https://www.portolan-sdi.org/)（2026-09-08確認）
- [Portolan specification](https://github.com/portolan-sdi/portolan-spec)（2026-09-08確認）
- [Portolan Specification — Core](https://github.com/portolan-sdi/portolan-spec/blob/main/specs/portolan/core.md)（2026-09-09確認）
- [Portolan Specification — Formats](https://github.com/portolan-sdi/portolan-spec/blob/main/specs/portolan/formats.md)（2026-09-09確認）
- [Portolan Registry](https://www.portolan-sdi.org/registry)（2026-09-08確認）
- [【GeoAI】第16回：「地図データを配る」時代の終わり—AIが直接読める空間インフラ「Portolan」とは](https://note.com/pacificspatial/n/nf8466fae24dd)（2026-09-08確認）
- [Portolanとは何か ― GeoParquet・PMTiles・COG・STACで考えるサーバーレスな地理空間データ基盤](https://qiita.com/rino_yume/items/9b0ff6dfa6d7ad5f3f83)（2026-09-09確認）
