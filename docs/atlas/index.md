---
layout: default
title: 知識マップ
---

# GeoAIアトラス 知識マップ

日々確認した情報を、長く参照できるテーマ単位で整理する。大分類から用途・テーマを選び、個別の項目へ進む。

- **概念**：用語や技術の関係を理解する。
- **手法**：分析・探索・集計の進め方を調べる。
- **データ**：データの種類・品質・仕様を確認する。
- **ツール**：目的に合う製品・OSS・サービスを探す。
- **事例**：業務や社会での活用を知る。

## 概念

### 位置情報の活用とAI

- [ロケーションインテリジェンス](concepts/location-intelligence.md)
- [Location AI](concepts/location-ai.md)

### 座標参照系と地図投影法

- [選び方と分類](concepts/map-projections.md)
- [座標参照系（CRS）との関係](concepts/coordinate-reference-systems.md)
- [メルカトル図法](concepts/mercator-projection.md)
- [イコールアース図法](concepts/equal-earth-projection.md)

### データ基盤と3D空間

- [Cloud Native Geospatial](concepts/cloud-native-geospatial.md)
- [リアリティーマッピングとデジタルツイン](concepts/reality-mapping-and-digital-twins.md)

## 手法

### AIによる分析と位置推定

- [空間特徴とLLMエージェントによる次の訪問地点予測](methods/spatial-agent-mobility-prediction.md)
- [空間分析への埋め込みの組み込み](methods/spatial-embeddings.md)
- [店舗画像によるPOIローカライゼーション](methods/storefront-poi-localization.md)

### AI向けのデータ探索と開発

- [知識グラフとLLMエージェントによる地理空間データ探索](methods/intelligent-geospatial-data-discovery.md)
- [GISデータセットカタログ](methods/gis-dataset-catalog-for-agents.md)
- [AIが扱いやすい地理空間開発環境](methods/ai-ready-geospatial-development.md)

### 人流の集計とプライバシー

- [人流データの時間処理と集計定義](methods/human-flow-time-processing.md)
- [位置情報データのプライバシー保護](methods/location-data-privacy.md)

### 主題図・モニタリング・配信

- [CADからGeoPackageへの変換と検証](methods/cad-to-geopackage.md)
- [街歩きによるバリア情報マッピング](methods/barrier-information-mapping.md)
- [手描き地図の座標校正と表示](methods/illustrated-map-coordinates.md)
- [地域別最多カテゴリ地図の読み方](methods/regional-winner-maps.md)
- [農業統計・圃場・衛星データを統合する米作モニタリング](methods/california-rice-monitoring.md)
- [全国メッシュデータのWeb配信](methods/national-grid-web-delivery.md)

## データ

### 人流データ

- [種類と加工段階](data/human-flow-data-types.md)
- [計測誤差と推計誤差](data/human-flow-data-quality.md)
- [日本で使えるデータ](data/human-flow-data-sources-japan.md)

### 地理空間データとPOI

- [ハザードデータの再利用条件](data/hazard-data-reuse.md)
- [国土数値情報](data/national-land-numerical-information.md)
- [Foursquare Placesへのパートナーデータ取り込み](data/foursquare-partner-places.md)

### スキーマとカタログ

- [地理空間データの来歴とレコード単位のメタデータ](data/geospatial-record-provenance.md)
- [Overtureのデータスキーマ](data/overture-schema.md)
- [Portolan](data/portolan.md)

## ツール

### 地図表示とWeb GIS

- [OH3 今昔マップビューア](tools/oh3-konjaku.md)
- [Mapbox Standard](tools/mapbox-standard.md)
- [MapLibre GL JS](tools/maplibre-gl-js.md)
- [maplibre-gl-streetview](tools/maplibre-gl-streetview.md)
- [GeoLibre](tools/geolibre.md)
- [Cesium](tools/cesium.md)
- [Felt](tools/felt.md)
- [ArcGIS StoryMaps](tools/arcgis-storymaps.md)

### 空間分析・データ処理・配信

- [pandas](tools/pandas.md)
- [FME](tools/fme.md)
- [Spatial Polars](tools/spatial-polars.md)
- [MovingPandas](tools/movingpandas.md)
- [H3](tools/h3.md)
- [geoparquet-io](tools/geoparquet-io.md)
- [GeoServer](tools/geoserver.md)

### 場所検索・交通・ナビゲーション

- [Valhalla](tools/valhalla.md)
- [TomTom Orbis APIs](tools/tomtom-orbis.md)
- [Mapbox Search Box API](tools/mapbox-search-box.md)
- [Galuchat](tools/galuchat.md)
- [Mapbox Traffic](tools/mapbox-traffic.md)
- [高徳地図（AMAP）](tools/amap.md)
- [ゼンリン地図ナビ](tools/zenrin-map-navigation.md)

### AI・MCP連携

- [Google Maps Agentic UI Toolkit](tools/google-maps-agentic-ui.md)
- [Mapbox Figma MCP Server](tools/mapbox-figma-mcp.md)
- [MCP for ArcGIS Location Services](tools/arcgis-location-services-mcp.md)
- [CARTO MCP Server](tools/carto-mcp-server.md)

### 人流・商圏・不動産分析

- [STLOCAL](tools/stlocal.md)
- [日本のロケーションインテリジェンス製品・サービス](tools/location-intelligence-products-japan.md)
- [コンプレノ](tools/kompreno.md)
- [PASSER-MARKETING](tools/passer-marketing.md)
- [Google Places Insights](tools/google-places-insights.md)
- [DOCOYAフード&ビバレッジ](tools/docoya-food-beverage.md)
- [LightBox](tools/lightbox.md)

## 事例

### 小売・出店・価格比較

- [小売出店候補地のロケーションインテリジェンス](cases/retail-site-selection.md)
- [ブラックフライデーの小売来訪分析](cases/black-friday-retail-visitation.md)
- [pricemap](cases/pricemap.md)

### 位置情報を使う広告

- [来店検知を使う位置連動リテールメディア](cases/location-triggered-retail-media.md)
- [来訪傾向を使う音声広告セグメント](cases/behavior-affinity-audio-ads.md)

### 観光・働き方・物流

- [旅客船のAIS位置情報の可視化](cases/ais-passenger-vessels.md)
- [富士山閉山期の人流分析](cases/mount-fuji-offseason-human-flow.md)
- [人流データによるオフィス訪問指数](cases/office-visitation-index.md)
- [配送経路の最適化と現場フィードバック](cases/here-fleet-route-intelligence.md)

## 更新履歴

[日付別の更新履歴](../updates/index.md)
