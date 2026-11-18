---
layout: default
title: GeoServer
category: tools
updated: 2026-11-18
---

# GeoServer

GeoServerは、地理空間データをOGCサービスなどで配信するオープンソースのサーバーである。GeoSolutionsのFOSS4G 2026報告を基に、クラウドネイティブ形式とAI連携の対応状況を整理する。

## 対応状況と開発方針

| 項目 | 2026年9月15日の報告 |
| --- | --- |
| COG・STAC・PMTiles | 一部はコミュニティーモジュールを通じて対応している |
| Zarr | 対応を埋めるべき課題として挙げている |
| MCP Server | 開発中であり、OGCサービスを対象に含める方針である |
| MCPからの管理操作 | 検討対象であり、確定した提供機能ではない |

同社はGeoServer 3のOGC API、ベクタータイル、地球観測データ配信、大規模運用などを発表した。AIの実用化やクラウドネイティブ形式の定着という評価は、同社の会議参加報告における所見である。

## AIによる管理操作と性能評価

GeoSolutionsの2026年10月7日の講演予告は、GeoServer・MapStore向けに開発中のMCPサーバーで、レイヤー公開、キャッシュ調整、問題診断をAIに支援させる構想を紹介する。11月のFOSS4G North Americaでの紹介予定であり、正式リリースや本番運用の検証結果ではない。

同会議では、同じGeoServerでもデータ形式、セキュリティ、ログ、座標系、JVM設定、規模によって性能がどう変わるかを比較する講演も予定されている。製品名だけの速度比較ではなく運用条件をそろえて評価する観点で読む。具体的な測定結果は本記事では確認できない。

## 行政の地図を長く配信する例

MassGISは、米マサチューセッツ州の地理情報を扱う組織で、2005年11月からGeoServerを本番利用している。土地・住所・湿地・画像などをWMS（地図画像の配信）やWFS（地物データの配信）として公開し、閲覧用のMassMapperや別のGISから使える構成にしている。地図を見る画面と、共通データを配るサーバーの役割を分ける例である。

運用支援企業GeoSolutionsの2026年11月17日の報告では、800件超のデータセットを扱う。2026年1～9月の営業日平均でMassMapperの起動は3,800回超、GeoServerへのリクエストは20万回超とされる。どちらも人数ではなく、他の環境で同じ性能を保証する値でもない。GeoServer 3への更新は作業中と説明されている。

## 関連項目

- [Cloud Native Geospatial](../concepts/cloud-native-geospatial.md)
- [CARTO MCP Server](carto-mcp-server.md)

## 出典

- [GeoSolutions：GeoSolutions at FOSS4G 2026 in Hiroshima](https://www.geosolutionsgroup.com/news/geosolutions-at-foss4g-2026/)（2026-09-15公開、2026-09-16確認）

- [GeoSolutions at FOSS4G North America 2026 in Sacramento](https://www.geosolutionsgroup.com/news/geosolutions-at-foss4g-na-2026/)（2026-10-08確認）

- [GeoSolutions：Four decades of MassGIS, twenty years on GeoServer](https://www.geosolutionsgroup.com/news/massgis-40-years-geoserver/)（2026-11-17公開、2026-11-18本文確認。運用支援企業による報告で、性能の独立検証は未実施）
