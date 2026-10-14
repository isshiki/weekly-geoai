---
layout: default
title: Overture Maps API
category: tools
updated: 2026-10-14
---

# Overture Maps API

Overture Maps APIは、ThatAPICompanyがOvertureのデータをREST APIで検索できるようにした第三者サービスである。Overture Maps Foundationの公式APIではない。大量ファイルのSQL検索に入る前に、周辺施設などをアプリから照会したい場合の選択肢になる。

## 検索できる内容

Placesでは位置と半径、国、カテゴリ、ブランド、名称、営業状態などを指定する。元データに存在する場合は連絡先も取得できる。APIキーが必要で、公開デモキーには利用場所・検索方法の制約がある。

営業状態で絞ると、不明値のレコードは結果から外れる。「営業中として取得できた件数」と「実際に営業中の全店舗数」は一致するとは限らない。

## データとサービスの条件を分ける

| 確認対象 | 確認すること |
| --- | --- |
| 元データ | Overtureの収録版、属性、ライセンスと出典表示 |
| ホスト版 | APIキー、利用上限、継続利用条件。概要は試用・探索向けと説明する |
| 自前運用 | 公開コードとGCP・BigQuery向けの配置手順、実行費用と保守 |

公開データであることは、第三者APIの無制限利用や継続提供を意味しない。2026年10月14日に資料を確認したもので、新規公開日を特定したニュースではない。API実行や課金条件の全件検証は行っていない。

## 次に読む

- [OpenPOI API](openpoi-api.md)：別の提供者によるPOI API。収録データと利用条件を区別する。
- [Overtureのデータスキーマ](../data/overture-schema.md)：元データの属性と版を確認する。

## 出典

- [提供者・ホスト版と自前運用の説明](https://www.overturemapsapi.com/docs/intro)（2026-10-14確認）

- [Overture Places API — Query POIs by Category, Brand, Country & Location](https://www.overturemapsapi.com/docs/api-endpoints/places)（2026-10-14確認）
