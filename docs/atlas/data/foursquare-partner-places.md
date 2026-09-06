---
layout: default
title: Foursquare Placesへのパートナーデータ取り込み
category: data
updated: 2026-09-06
---

# Foursquare Placesへのパートナーデータ取り込み

FoursquareのPartner Places Ingestionは、パートナーが保有する施設データをFoursquare Placesへ一括投入し、既存POIとの照合と統合を行う仕組みである。ベータ版のFSQ Places API for Partnersでは、データの取り込みに加え、自社IDとFSQ Place IDの対応確認や編集の追跡を扱う。

## 入力データ

- ファイル形式はParquetで、同一配送日のファイル間ではスキーマを統一する。
- `foreign_id`はパートナー側で一意かつ安定したIDとし、配送をまたいで維持する。重複があるとジョブ全体が失敗する。
- 必須項目は住所、国、`foreign_id`、緯度、経度、地域名、名称である。
- カテゴリー、営業時間、電話番号、Webサイト、閉店情報などを任意項目として追加できる。
- `closed=true`は恒久的な閉店や施設の消滅にだけ使い、一時休業や管理対象外になったことを表す用途には使わない。

## 更新と照合

更新は差分ではなくデータセット全体のスナップショットとして送る。Foursquareの仕様では少なくとも90日に1回の更新が必要である。投入後は既存Placeとの照合が行われ、対応するPlaceはResolve Endpointへ `foreign_id`を渡して確認できる。

ベータ版APIの発表では、対応するPOIが存在しない場合の新規Place追加、パートナーIDとFSQ Place IDの恒久的な対応表、人気度や評価などの属性参照、提案・適用された編集の追跡も示されている。

## 品質管理で見る指標

ジョブは `metrics.json` を出力し、受信、受理、拒否、変更なし、更新、新規、既存一致、新規一致、不一致などの件数を記録する。網羅性を高めるには新規追加数だけでなく、拒否率、不一致率、既存POIへの誤った照合、更新頻度を継続して確認する必要がある。

外部のPlaceデータを統合する仕組みはカバレッジ拡大に役立つ一方、入力元ごとの鮮度、IDの持続性、重複、閉店判定が最終データの品質を左右する。

## 出典

- [Foursquare Docs: Partner Places Ingestion](https://docs.foursquare.com/fsq-developers-places/reference/partner-places-ingestion)（2026-09-06確認）
- [Foursquare「FSQ Places API for Partners」発表](https://x.com/Foursquare/status/2095195279376908620)（2026-09-06確認）
