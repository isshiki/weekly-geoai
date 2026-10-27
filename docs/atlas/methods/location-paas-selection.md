---
layout: default
title: 位置情報PaaSの選び方と相互運用性
category: methods
updated: 2026-10-27
---

# 位置情報PaaSの選び方と相互運用性

位置情報PaaSは、地図表示、住所検索、経路計算などをAPIやSDKでアプリへ組み込むクラウドサービスである。EsriはArcGIS Location Platformを例に、OSSライブラリとの連携や、機能を追加できる構成を説明している。

## 選定時に分けて見る項目

| 観点 | 確認する内容 |
| --- | --- |
| 必要な機能 | 地図・ジオコーディング・経路・標高・分析が用途を満たすか |
| 接続と形式 | REST API、標準形式、既存の地図ライブラリで扱えるか |
| データの扱い | 保存・共有・移行についてどの条件があるか |
| 運用 | 利用量に対する価格、サポート、終了時の代替を確認できるか |

前半の観点はEsriの選定記事に基づく。終了時の代替も合わせて確認するのは、Atlasでの運用上の整理である。

Esriの記事はLeaflet、OpenLayers、MapLibre GL JS、CesiumJSなどとの連携を紹介する製品提供者の解説である。APIが公開されていること、OSSから呼べること、データを自由に再配布できることは別々に確認する。記事でいう「オープン開発」を、サービス全体がオープンソースであるという意味には使わない。

## ArcGISで組み合わせられるサービス

公式開発文書は、背景地図・静的地図、住所検索、POI検索、経路計算、人口統計などのデータ付加、標高取得を提供機能として整理している。経路には車両群のルート計画や到達圏計算も含まれる。ArcGIS Location PlatformまたはArcGIS Onlineのアカウントを使い、必要なサービスを選ぶ。

2026年10月2日の紹介記事は公式一覧で掲載を確認したが、本文を取得できなかったため、ここでは別の公式開発文書で確認できた機能だけを記載する。言語数や対象国数など、記事固有の数値は未検証である。

## APIを画面上で試して選ぶ

Amazon Location Serviceは2026年10月13日、Places・Routes・Mapsの14 APIをコードなしで試すAPI Playgroundを発表した。AWSコンソールから実際のAPIを呼び、地図上の結果を見てパラメータを変え、リクエスト例をコピーできる。

住所・施設検索、到達圏や訪問順、地図表示などを試して機能を比較する入口になる。東京を含む15リージョンに対応すると発表している。実APIの試用をデータの自由な再配布や無制限の無料利用と混同せず、利用するアカウント・条件を確認する。今回は発表の確認で、API実行はしていない。

### 試した要求を実装へ持ち帰る

公式Playground資料では、要求・応答とパラメーターを確認し、CLI、cURL、Python、JavaScript、Rubyのコード例を取得できる。到達圏は時間・距離と移動手段などの条件を持ち、単純な円とは異なる。訪問順の最適化やGPS座標の道路への補正も、目的に応じて試すAPIとして案内されている。資料を確認したもので、コードの実行や利用料金の試算は行っていない。

## 時間で到達範囲を作る

Google Maps PlatformのIsochrones APIは、出発地点から指定時間内に到達できる範囲を計算する。APIキーを用意して呼び出し、GeoJSONの区域を受け取る。公式の対応地域一覧には日本も掲載されている。2026年10月24日に既存資料を確認したもので、新規リリースの発表とは扱わない。

直線距離の円、道路に沿った距離、移動時間の到達圏は異なる条件である。「駅から何分」を比べるなら、移動手段と出発点をそろえる。公式手順は、施設のPlace IDが中心点へ解決され、道路から遠いとエラーになり得ることも説明する。大きな施設では入口の座標を指定する方法を検討する。実際のAPI実行や料金試算はしていない。

[MAUPと範囲の感度](../concepts/maup.md)も参照し、区域の作り方と比較したい問いを対応させる。

## 配送アプリへ地図と経路案内を組み込む

MapboxのDoorDash事例では、配達員が別アプリへ移動せずに案内を受けられるよう、Maps・Navigation SDKとDirections・Matrix APIを組み合わせている。利用者側では近くの店舗表示や配送追跡に使う。

選定時には地図の見た目だけでなく、経路・到着予想・配送業務を同じ画面で扱えるかを見る。このページは提供元の導入事例で、公開日と定量的な時間短縮効果は未確認である。

### 計画経路をナビへ引き継ぐ

Googleの2026年10月23日のRoutes API変更では、Navigation SDKへ渡すルートトークン内の経路設定がアプリ側の設定より優先される。計画時と案内時の条件をそろえるための変更である。交通状況や経路逸脱などによる再計算はあり、常に同じ道を走る保証ではない。

## 過去の費用比較を現在の見積もりに使わない

RSTの比較記事には2022年4月時点のGoogle Maps無料枠が残る。Google利用時の推計月額42万ドルと、OSM基盤の月額1,500ドルは、同社の特定案件についての説明である。開発・移行・保守の費用まで同じ条件で比較した数字とは扱わない。現在の料金表、利用回数、必要なAPI、運用担当者を置いて見積もる。

OSMのデータ利用と公共タイルサーバーの利用は別である。OSMFのタイル利用方針は容量制限と無保証を明記する。自前配信や契約する配信サービスも含めて選ぶ。HEREの2020年の紹介記事も、当時の取り組みを知る資料として扱い、無料条件や対象都市数を現在の仕様として転載しない。

## 関連項目

- [外部地図サービスの廃止と依存関係の点検](map-service-lifecycle.md)
- [GeoAIの標準化と実務での採用](../concepts/geoai-standards-and-adoption.md)

## 課金単位と保存条件を分ける

Mapboxの公式料金を2026年10月27日に確認すると、通常のGL JSの月間ロードは5万回まで無料で、次の5万回は1,000回当たり5ドルである。ロードは地図の初期化を数え、含まれるタイル取得と別の検索API呼び出しを混同しない。Seats方式など別の課金方式もある。

SuperDuprの比較記事は、一時的な住所検索と結果を保存するPermanent Geocoding、検索セッションとリクエストを分けて試算している。料金比較には無料枠だけでなく段階料金・保存条件・契約をそろえる必要がある。記事のGoogleとの総額比較は著者の想定利用量による試算であり、本Atlasで全条件を再計算した正式見積もりではない。

## 出典

- [Esri Community：ロケーション サービスにオープンな開発をサポートする PaaS を選ぶべき理由](https://community.esri.com/ja/discussion/1720940/)（2026-09-25確認）
- [Esri：For Location Services, Pick a PaaS That Supports Open Development](https://www.esri.com/arcgis-blog/products/platform/developers/for-location-services-pick-a-paas-that-supports-open-development-heres-why)（2026-09-25確認）

- [Esri Developer：Mapping and location services](https://developers.arcgis.com/documentation/mapping-and-location-services/)（2026-10-03確認）
- [Esri：位置情報サービスの紹介](https://www.esri.com/arcgis-blog/products/platform/developers/location-services-available-through-arcgis-location-platform)（2026-10-03確認）

- [AWS：API Playground発表](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-location-service-api-playground/)（2026-10-16確認）

- [AWS：API Playgroundドキュメント](https://docs.aws.amazon.com/location/latest/developerguide/api-playground.html)（2026-10-20確認）

- [Mapbox：DoorDash導入事例](https://www.mapbox.com/showcase/doordash)（2026-10-21本文確認）

- [Google Maps vs. Mapbox vs. OpenStreetMap: which map API should you choose and why?](https://www.rst.software/blog/google-maps-vs-mapbox-vs-openstreetmap-which-map-api-should-you-choose-and-why)（2026-10-22本文確認）

- [Mapping company “democratising” GIS](https://highways-news.com/mapping-company-democratising-gis/)（2026-10-22本文確認）

- [OSMF：Tile Usage Policy](https://operations.osmfoundation.org/policies/tiles/)（2026-10-22確認）

- [Google：Isochrones API](https://developers.google.com/maps/documentation/isochrones?hl=ja)（2026-10-24本文確認）

- [Google：等時線の作成](https://developers.google.com/maps/documentation/isochrones/create-isochrone?hl=ja)（2026-10-24本文確認）

- [Google：対応地域](https://developers.google.com/maps/documentation/isochrones/coverage?hl=ja)（2026-10-24本文確認）

- [Google：Routes API変更履歴](https://developers.google.com/maps/documentation/routes/release-notes#October_23_2026)（2026-10-24本文確認）

- [Google：ルートのカスタマイズ](https://developers.google.com/maps/documentation/navigation/android-sdk/customize-route)（2026-10-24本文確認）

- [Mapbox Pricing 2026: Free Tier, Map Loads, Geocoding, and Mapbox vs Google Maps on Real Bills](https://superdupr.com/blog/mapbox-pricing)（2026-10-27確認）
- [Mapbox公式料金](https://www.mapbox.com/pricing)（2026-10-27確認）
