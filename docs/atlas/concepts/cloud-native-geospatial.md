---
layout: default
title: Cloud Native Geospatial
category: concepts
updated: 2026-09-11
---

# Cloud Native Geospatial

Cloud Native Geospatial（CNG）は、地理空間データをクラウド上で扱いやすくするための、形式、配信方法、ツール、運用上の実践をまとめた考え方である。単一の規格や製品名ではない。利用者がデータ全体をダウンロードせず、必要な範囲、列、解像度、時間だけをネットワーク越しに読めるようにすることが中心にある。

<figure markdown="span">
  ![STACのカタログ層、COG・GeoParquet・Zarrのデータ層、直接読み取る処理層をオブジェクトストレージとHTTPSが支える構成](../../assets/atlas/cloud-native-geospatial/layers.svg)
  <figcaption>CNGを、発見・保存・処理の役割分担として整理した図。厳密な標準階層ではなく、GeoAIアトラスでの整理である。</figcaption>
</figure>

## 3つの役割で捉える

| 役割 | 主な技術 | 何を解決するか |
| --- | --- | --- |
| カタログ | STAC | いつ、どこに、どのようなデータがあるかを記述し、発見できるようにする |
| データ | COG、GeoParquet、Zarrなど | 必要な部分だけを読み出せるよう、ラスタ、ベクター、多次元配列を配置する |
| 処理 | ブラウザ、GIS、クエリエンジン、分析ライブラリ | 専用サーバーを必須にせず、保存先のデータへ直接問い合わせる |

この3層は固定された製品構成ではない。データの種類や用途に応じて形式と処理系を組み合わせるための整理である。STACは実データのファイル形式ではなく、データ資産を記述して探すためのカタログ仕様である。

## 必要な部分だけを読む

CNGでは、オブジェクトストレージとHTTPSを使い、ファイルの一部や特定のチャンクを取得する。代表的な仕組みは次のとおりである。

- COGは内部タイルとoverviewを持ち、HTTP Range Requestで必要な解像度と範囲を読む。
- GeoParquetは列指向のParquetを基盤とし、必要な列やrow groupに絞った分析を行う。
- Zarrは多次元配列をチャンクへ分け、必要な領域や時間の配列だけを読む。
- STACはデータの空間・時間範囲や取得先を記述し、対象資産を絞り込む。

ファイル形式だけを変えても、配信サーバーがRange RequestやCORSに対応していなければ、ブラウザや分析ツールからの部分読み込みは機能しない。データ配置、メタデータ、HTTP配信、利用側ツールを一体で設計する必要がある。

## コミュニティと標準化

Cloud-Native Geospatial ForumはRadiant Earthのイニシアチブであり、ベンダー中立なイベント、文書、教育、コミュニティ運営を行う。CNG自体は標準化団体ではなく、STAC、COG、GeoParquet、Zarrの規格やコードを直接管理する組織でもない。実務コミュニティで有効性が確かめられた実践の一部が、OGCなどの標準化へつながる関係にある。

## 関連項目

- [Portolan](../data/portolan.md)
- [geoparquet-io](../tools/geoparquet-io.md)
- [全国メッシュデータのWeb配信](../methods/national-grid-web-delivery.md)
- [GISデータセットカタログ](../methods/gis-dataset-catalog-for-agents.md)

## 出典

- [About CNG](https://cloudnativegeo.org/about/)（2026-09-11確認）
- [Introducing CNG](https://cloudnativegeo.org/blog/2024/09/introducing-cng/)（2026-09-11確認）
- [Cloud-Optimized Geospatial Formats Guide](https://guide.cloudnativegeo.org/overview.html)（2026-09-11確認）
- [【CNG】Cloud Native Geospatialって結局何なのか](https://note.com/pacificspatial/n/nbaab8d8f3cab)（2026-09-11確認）

