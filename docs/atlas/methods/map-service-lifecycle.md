---
layout: default
title: 外部地図サービスの廃止と依存関係の点検
category: methods
updated: 2026-09-25
---

# 外部地図サービスの廃止と依存関係の点検

Web地図をコピーしても、参照している外部レイヤーのデータまで複製されるとは限らない。アプリやダッシュボードを維持するには、参照先サービスの更新・廃止を管理する必要がある。

## 人口統計レイヤーの廃止例

Esriは2026年9月22日、一部の旧人口統計地図レイヤーを12月1日から廃止し、対応サービスを12月末までに停止すると告知した。対象は2025年11月に成熟サポートへ移行した旧プレミアム人口統計コンテンツであり、人口統計データすべての終了ではない。

サービス停止後はWeb地図だけでなく、アプリ、ダッシュボード、ArcGIS Enterpriseポータルからの参照にも影響する。

## 点検の順序

| 段階 | 確認すること |
| --- | --- |
| 参照先を把握 | サービスURL・アイテムIDと、それを使う地図・アプリを列挙する |
| 終了条件を確認 | 対象一覧、説明欄の廃止告知、停止日を確認する |
| 代替を比較 | 項目定義、対象地域、基準年、利用条件、料金を照合する |
| 移行を検証 | 表示だけでなく検索・集計・ダッシュボードの結果も確認する |

EsriはBusiness Analyst Web App、GeoEnrichment、データファイルなどの現行提供を案内している。これは必ず同じスキーマで置換できるという保証ではない。保存や複製を検討する場合も元データの利用条件を確認する。

## アプリの終了と再構築

2026年9月24日のCARTOの記事は、移行前に利用状況を棚卸しし、再構築すべきアプリを選ぶよう提案する。CARTOへの移行を勧める提供者側の論考であるため、終了条件は元製品の公式情報と分けて確認する。

Esriの延長告知とサポート資料では、ArcGIS OnlineのWeb AppBuilderは2026年第1四半期に新規作成停止、第4四半期に既存アプリの更新停止、2027年第2四半期に動作終了となる。Experience Builderへの移行にはアプリの再構成が必要である。Enterprise版とDeveloper Editionは別の日程を持つため、同じ終了日を当てはめない。

元のデータレイヤーが残ることと、アプリの画面や処理が動き続けることは別である。利用者、外部リンク、ウィジェット、権限、集計条件を確認し、移行先で操作と結果を照合する。

## 出典

- [Esri：Demographic Map Layers Retiring December 2026](https://www.esri.com/arcgis-blog/products/arcgis-online/announcements/demographic-map-layers-retiring-december-2026)（2026-09-24確認）

- [CARTO：Some of your Esri software is retiring. What now?](https://carto.com/blog/esri-arcgis-apps-retiring/)（2026-09-25確認）
- [Esri：ArcGIS Web AppBuilder in ArcGIS Online Retirement Extended](https://www.esri.com/arcgis-blog/products/web-appbuilder/announcements/arcgis-web-appbuilder-in-arcgis-online-retirement-extended)（2026-09-25確認）
- [Esri Support：ArcGIS Web AppBuilder](https://support.esri.com/en-us/knowledge-base/deprecation-arcgis-web-appbuilder-000036340)（2026-09-25確認）
