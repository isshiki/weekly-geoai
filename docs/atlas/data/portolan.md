---
layout: default
title: Portolan
category: data
updated: 2026-09-08
---

# Portolan

Portolanは、地理空間データを人とAIエージェントの双方が発見・理解・直接利用できるようにする、オープンソースのカタログ仕様とツール群である。独自の地理ファイル形式や集中型プラットフォームではなく、既存のクラウドネイティブ形式、STACメタデータ、文書を組み合わせる。

## データ公開の構成

Portolanカタログでは、ベクターをGeoParquetとPMTiles、ラスターをCOG、点群をCOPCなどの形式で配置する。これらをSTACの `catalog.json` または `collection.json` で記述し、同じ階層に人向けの `README.md` とAIエージェント向けの `AGENTS.md` を置く。

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

## 関連項目

- [geoparquet-io](../tools/geoparquet-io.md)
- [知識グラフとLLMエージェントによる地理空間データ探索](../methods/intelligent-geospatial-data-discovery.md)

## 出典

- [Portolan公式サイト](https://www.portolan-sdi.org/)（2026-09-08確認）
- [Portolan specification](https://github.com/portolan-sdi/portolan-spec)（2026-09-08確認）
- [Portolan Registry](https://www.portolan-sdi.org/registry)（2026-09-08確認）
- [【GeoAI】第16回：「地図データを配る」時代の終わり—AIが直接読める空間インフラ「Portolan」とは](https://note.com/pacificspatial/n/nf8466fae24dd)（2026-09-08確認）
