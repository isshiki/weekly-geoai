---
layout: default
title: Google Places Insights
category: tools
updated: 2026-09-07
---

# Google Places Insights

Google Places Insightsは、Google Maps Platformの場所データを集計し、地域内の施設数や構成を分析するためのデータセットと関数群である。個別店舗の検索だけでなく、地域やH3セルを単位としたPOIの集計に使う。

## 2026年9月の更新

2026年9月2日のリリースでは、月次の履歴スナップショットが一般提供になった。2024年1月まで遡って分析でき、履歴テーブルには評価と評価件数も加わった。

`PLACES_COUNT_CHANGE` は、2つの月次スナップショットを1回のクエリで比較し、条件に合う施設数の変化を返す。開店・閉店を直接表す個別イベントではなく、指定した条件に一致する集計件数の差として読む必要がある。

既存の集計関数にも、次のようなフィルターが追加された。

- スナップショットの日付
- 通常営業時間
- EV充電器の台数、充電速度、コネクター種別

対象は `PLACES_COUNT_PER_H3`、`PLACES_COUNT_V2`、`PLACES_COUNT_PER_TYPE_V2` である。H3集計を使うと、行政区域に依存しない一定の空間単位で地域差や時系列変化を比較できる。

## 利用時の注意

施設数の変化には、実世界の開店・閉店だけでなく、データの追加、修正、カテゴリー変更、検索条件の違いが含まれ得る。月ごとの増減を事業活動の変化と解釈する前に、対象カテゴリー、境界、フィルター、スナップショット日を固定する。

## 関連項目

- [H3](h3.md)
- [Foursquare Placesへのパートナーデータ取り込み](../data/foursquare-partner-places.md)

## 出典

- [Places Insights release notes](https://developers.google.com/maps/documentation/placesinsights/release-notes)（2026-09-07確認）
