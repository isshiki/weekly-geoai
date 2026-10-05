---
layout: default
title: 知識マップ
updated: 2026-10-05
---

# GeoAIアトラス 知識マップ

やりたいことから読む順序を選ぶか、分類から個別の項目を探せる。初めて読む場合は[初めてのGeoAI](guides/getting-started.md)から始める。

## 目的から探す { #by-purpose }

| 目的 | 読む順序 |
| --- | --- |
| 店舗・施設のデータを分析する | [POIの案内](guides/poi-workflow.md) → [データ比較](data/poi-open-data-comparison.md) → [取得の網羅性](methods/poi-retrieval-coverage.md) |
| 人の動きを分析する | [種類](data/human-flow-data-types.md) → [品質](data/human-flow-data-quality.md) → [集計](methods/human-flow-time-processing.md) → [プライバシー](methods/location-data-privacy.md) |
| 地図を作り、公開する | [座標系](concepts/coordinate-reference-systems.md) → [Felt](tools/felt.md)／[MapLibre](tools/maplibre-gl-js.md)／[OpenLayers](tools/openlayers.md) → [Web配信](methods/national-grid-web-delivery.md) |
| AIにGIS操作を任せる | [仕組み](concepts/location-ai.md) → [開発環境](methods/ai-ready-geospatial-development.md) → [CARTO MCP](tools/carto-mcp-server.md) |
| 防災・地形データを使う | [再利用条件](data/hazard-data-reuse.md) → [メッシュ集計](methods/polygon-mesh-aggregation.md) → [地形のスケール](methods/terrain-scale.md) |

## 分類から探す { #by-category }

[概念](#concepts) / [手法](#methods) / [データ](#data) / [ツール](#tools) / [事例](#cases)

ツールには、画面で操作するサービスと、コードに組み込むライブラリがある。小分類は主な使い道で整理している。個別ページで必要な準備と利用条件を確認する。

## 概念 { #concepts }

### 位置情報の活用とAI

- [ロケーションインテリジェンス](concepts/location-intelligence.md)
- [Location AI](concepts/location-ai.md)
- [地理空間モデルの予測と地理的理解](concepts/geographic-model-reasoning.md)

### 座標参照系と地図投影法

- [選び方と分類](concepts/map-projections.md)
- [座標参照系（CRS）との関係](concepts/coordinate-reference-systems.md)
- [メルカトル図法](concepts/mercator-projection.md)
- [イコールアース図法](concepts/equal-earth-projection.md)

### データ基盤と3D空間

- [GeoAIの標準化と実務での採用](concepts/geoai-standards-and-adoption.md)
- [Cloud Native Geospatial](concepts/cloud-native-geospatial.md)
- [リアリティーマッピングとデジタルツイン](concepts/reality-mapping-and-digital-twins.md)

## 手法 { #methods }

### AIによる分析と位置推定

- [地図探索エージェントの記憶と空間推論](methods/map-agent-memory.md)
- [空間特徴とLLMエージェントによる次の訪問地点予測](methods/spatial-agent-mobility-prediction.md)
- [空間分析への埋め込みの組み込み](methods/spatial-embeddings.md)
- [店舗画像によるPOIローカライゼーション](methods/storefront-poi-localization.md)

### データの検索・取得とサービス選定

- [空間索引の選択と評価条件](methods/spatial-index-selection.md)
- [POI検索の取得効率と網羅性](methods/poi-retrieval-coverage.md)
- [位置情報PaaSの選び方と相互運用性](methods/location-paas-selection.md)

### AI向けのデータ探索と開発

- [知識グラフとLLMエージェントによる地理空間データ探索](methods/intelligent-geospatial-data-discovery.md)
- [GISデータセットカタログ](methods/gis-dataset-catalog-for-agents.md)
- [AIが扱いやすい地理空間開発環境](methods/ai-ready-geospatial-development.md)

### 人流の集計とプライバシー

- [人流データの時間処理と集計定義](methods/human-flow-time-processing.md)
- [位置情報データのプライバシー保護](methods/location-data-privacy.md)

### 空間集計・地形と主題図

- [ポリゴンのメッシュ集計と被覆率](methods/polygon-mesh-aggregation.md)
- [標高タイルによる地形指標と測定スケール](methods/terrain-scale.md)
- [地域別最多カテゴリ地図の読み方](methods/regional-winner-maps.md)

### データ作成・変換と現地調査

- [画像からGIS情報を作る解析と検証](methods/imagery-to-gis.md)
- [CADからGeoPackageへの変換と検証](methods/cad-to-geopackage.md)
- [街歩きによるバリア情報マッピング](methods/barrier-information-mapping.md)
- [手描き地図の座標校正と表示](methods/illustrated-map-coordinates.md)

### モニタリングと継続運用

- [農業統計・圃場・衛星データを統合する米作モニタリング](methods/california-rice-monitoring.md)
- [全国メッシュデータのWeb配信](methods/national-grid-web-delivery.md)
- [外部地図サービスの廃止と依存関係の点検](methods/map-service-lifecycle.md)

## データ { #data }

### 人流データ

- [種類と加工段階](data/human-flow-data-types.md)
- [計測誤差と推計誤差](data/human-flow-data-quality.md)
- [日本で使えるデータ](data/human-flow-data-sources-japan.md)

### 地理空間データとPOI

- [地図の提供日と現況の時点](data/map-update-dates.md)
- [オープンな基盤地図データと共同整備](data/open-foundational-map-data.md)
- [POIオープンデータの比較と地域特徴量](data/poi-open-data-comparison.md)
- [ハザードデータの再利用条件](data/hazard-data-reuse.md)
- [国土数値情報](data/national-land-numerical-information.md)
- [Foursquare Placesへのパートナーデータ取り込み](data/foursquare-partner-places.md)

### 形式・スキーマ・カタログ

- [地理空間データの来歴とレコード単位のメタデータ](data/geospatial-record-provenance.md)
- [Overtureのデータスキーマ](data/overture-schema.md)
- [Portolan](data/portolan.md)
- [Cloud Optimized GeoParquet（COGP）](data/cloud-optimized-geoparquet.md)
- [ParquetのALP浮動小数点符号化](data/parquet-alp.md)

## ツール { #tools }

### ブラウザーで地図を探索する

- [Kumoy](tools/kumoy.md)
- [Geospect](tools/geospect.md)
- [OH3（Open Hinata 3）](tools/open-hinata3.md)
- [ShadeMapと建物データの更新](tools/shademap.md)
- [OH3 今昔マップビューア](tools/oh3-konjaku.md)

### 地図を作成・共有する

- [GeoLibre](tools/geolibre.md)
- [Felt](tools/felt.md)
- [ArcGIS StoryMaps](tools/arcgis-storymaps.md)

### Web地図をコードで作る

- [MapLibre GL JS](tools/maplibre-gl-js.md)
- [OpenLayers](tools/openlayers.md)
- [Cesium](tools/cesium.md)
- [Mapbox Standard](tools/mapbox-standard.md)
- [maplibre-gl-streetview](tools/maplibre-gl-streetview.md)

### 分析・変換をコードで行う

- [GeoTools](tools/geotools.md)
- [pandas](tools/pandas.md)
- [Spatial Polars](tools/spatial-polars.md)
- [MovingPandas](tools/movingpandas.md)
- [H3](tools/h3.md)
- [geoparquet-io](tools/geoparquet-io.md)
- [ArcGIS API for Python](tools/arcgis-api-python.md)

### 画像解析・機械学習

- [TorchGeo](tools/torchgeo.md)
- [SateAIs](tools/sateais.md)
- [GeoAI（geoai-py）](tools/geoai-py.md)

### データ連携・配信と業務GIS

- [FME](tools/fme.md)
- [GeoServer](tools/geoserver.md)
- [ArcFM](tools/arcfm.md)
- [ArcGIS Solutions](tools/arcgis-solutions.md)

### 場所検索・交通・ナビゲーション

- [ArcGIS Geocoding Service](tools/arcgis-geocoding.md)
- [OpenPOI API](tools/openpoi-api.md)
- [Google MapsのAsk MapsとImmersive Navigation](tools/google-maps-gemini.md)
- [Valhalla](tools/valhalla.md)
- [TomTom Orbis APIs](tools/tomtom-orbis.md)
- [Mapbox Search Box API](tools/mapbox-search-box.md)
- [Galuchat](tools/galuchat.md)
- [Mapbox Traffic](tools/mapbox-traffic.md)
- [高徳地図（AMAP）](tools/amap.md)
- [ゼンリン地図ナビ](tools/zenrin-map-navigation.md)

### AI・MCP連携

- [GIS Data Agent](tools/gis-data-agent.md)
- [Google Maps Agentic UI Toolkit](tools/google-maps-agentic-ui.md)
- [Mapbox Figma MCP Server](tools/mapbox-figma-mcp.md)
- [MCP for ArcGIS Location Services](tools/arcgis-location-services-mcp.md)
- [CARTO MCP Server](tools/carto-mcp-server.md)
- [BigGeo AI](tools/biggeo-ai.md)

### 人流・商圏・不動産分析

- [ゼンリン まっちず](tools/zenrin-matchz.md)
- [GEOSPACE 地番地図とちばんAPIワイド](tools/geospace-chiban.md)
- [LAPと人流アナリティクス](tools/location-ai-platform.md)
- [IPinfo Places](tools/ipinfo-places.md)
- [エリアブースト](tools/area-boost.md)
- [STLOCAL](tools/stlocal.md)
- [日本のロケーションインテリジェンス製品・サービス](tools/location-intelligence-products-japan.md)
- [コンプレノ](tools/kompreno.md)
- [PASSER-MARKETING](tools/passer-marketing.md)
- [Google Places Insights](tools/google-places-insights.md)
- [DOCOYAフード&ビバレッジ](tools/docoya-food-beverage.md)
- [LightBox](tools/lightbox.md)

### 学習・キャリア

- [GIS Career Hub](tools/gis-career-hub.md)

## 事例 { #cases }

### 小売・出店・価格比較

- [小売出店候補地のロケーションインテリジェンス](cases/retail-site-selection.md)
- [ブラックフライデーの小売来訪分析](cases/black-friday-retail-visitation.md)
- [pricemap](cases/pricemap.md)

### 位置情報を使う広告

- [来店検知を使う位置連動リテールメディア](cases/location-triggered-retail-media.md)
- [来訪傾向を使う音声広告セグメント](cases/behavior-affinity-audio-ads.md)

### 都市・観光と働き方

- [渋谷の街区別年代構成と人流の読み方](cases/shibuya-age-distribution.md)
- [富士山閉山期の人流分析](cases/mount-fuji-offseason-human-flow.md)
- [人流データによるオフィス訪問指数](cases/office-visitation-index.md)

### 交通・物流

- [運転支援と地図の継続更新](cases/streaming-maps-driver-assistance.md)
- [旅客船のAIS位置情報の可視化](cases/ais-passenger-vessels.md)
- [配送経路の最適化と現場フィードバック](cases/here-fleet-route-intelligence.md)

### 気候・季節の変化

- [紅葉時期の変化と空間補間](cases/maple-phenology.md)
