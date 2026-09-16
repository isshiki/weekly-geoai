---
layout: default
title: GeoServer
category: tools
updated: 2026-09-16
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

## 関連項目

- [Cloud Native Geospatial](../concepts/cloud-native-geospatial.md)
- [CARTO MCP Server](carto-mcp-server.md)

## 出典

- [GeoSolutions：GeoSolutions at FOSS4G 2026 in Hiroshima](https://www.geosolutionsgroup.com/news/geosolutions-at-foss4g-2026/)（2026-09-15公開、2026-09-16確認）
