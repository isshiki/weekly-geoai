---
layout: default
title: GeoLibre
category: tools
updated: 2026-10-06
---

# GeoLibre

GeoLibreは、地理空間データの可視化、取得、編集、分析を扱うオープンソースのアプリケーションである。

## 目的に応じて使い方を選ぶ

| 目的 | 読む箇所・確認する前提 |
| --- | --- |
| 地図アプリで表示・編集する | 描画エンジン、点群、外部データへの接続。エンジンごとの対応差を確認 |
| 自分のWebアプリへ組み込む | `@geolibre/map`。アプリ全体とは提供範囲が異なる |
| AIやPythonから操作する | デスクトップ地図の操作。対象アプリ・接続設定・保存権限を確認 |

以下の版番号は機能を確認したリリースの目印であり、最新のインストール推奨版を示すものではない。アプリの実行・接続試験は行っていない。

## データ表示と拡張機能

GeoParquetのメタデータ、DEM、3D表示に加え、v3.0.0ではCesiumを主要3Dエンジンとして選べるようになった。エンジンが対応する機能に応じてUIとプラグインを切り替える。CSWカタログ検索や、外部プラグインからAIアシスタントのツールを登録する機能もリリースノートで案内された。

## UIなしで使う @geolibre/map

`@geolibre/map`は、データ読み込み、レイヤー同期、スタイル処理を取り出したパッケージである。公式READMEは、公開するheadless機能にはReact、Zustandストア、Cesium、地図コントロールを含まないと説明している。

`createLayerSync(map)`で同期処理を作り、`sync.sync(layers)`へレイヤー一覧を渡す。COG DEM・PMTilesのプロトコル登録や、Mapbox Style・SLD・QMLの入出力も案内されている。ESM専用でTypeScriptの型定義を提供する。

2026年9月17日に公式READMEとnpmレジストリを確認し、v3.0.0、MITライセンス、同バージョンの公開日時が9月14日（UTC）であることを確認した。npmの紹介画面は取得できなかった。アプリ全体の対応レンダラーと、このパッケージのheadless機能の範囲は区別する。

## 描画エンジンと操作・共有の拡張

v3.1.0（2026年9月26日日本時間公開）は、MapboxとArcGIS Maps SDK for JavaScriptを選択可能な描画エンジンとして追加した。Mapboxでの3D Tiles・LiDAR・Zarr、ArcGISでの3Dシーン・COG・PMTiles・Zarrなど、エンジンごとの表示対応も広げている。すべてのエンジンが同じ機能を持つという意味ではない。

「God's Eye View」には地震、衛星、航空機、交通カメラ、火災などのデータ源が加わった。AIアシスタントには音声コマンド、プロジェクト共有には閲覧・コメント・編集の権限、リンク期限、パスワード、共有取り消しが追加された。

Windows、macOS、Linux、Android、iOS向けの配布ファイルが掲載されている。ファイルの掲載と各OSでの動作確認は区別し、今回インストールや外部サービス接続は実施していない。

## 点群の注釈と外部データへの接続

v3.2.0は2026年10月2日日本時間に公開された。点群へのラベル、3D枠、線・面・キーポイント、事前ラベル付け、LAZ・NumPy出力を拡充し、PythonとMCPから扱う機能も追加した。

Tessera v1.1の衛星画像埋め込みを表示でき、非公開S3には認証情報・SSO・IAMロールで接続する。デスクトップ版ではWMSの座標系選択・再投影やOSキーチェーンへの認証情報保存、WFSではGeoJSONを出さないサーバーのGML読み込みに対応した。リリースノートの確認であり、点群分類の精度や各接続環境を検証した結果ではない。

## デスクトップ地図を操作・検証する

v3.3.0のリリースノートでは、Python・MCPから開いているデスクトップ地図を操作し、フィルター、ラベル、ストーリーマップの作成や処理実行を扱う機能が追加された。ファイルを生成して終える使い方に加え、アプリ上の地図を操作する接点として読める。

2地点間の見通し分析、3DレイヤーのglTF・OBJ・STL出力、プロジェクト履歴の比較と単一レイヤー復元も加わった。機能追加をリリースノートで確認したものであり、見通し計算の精度やMCP操作の成功を検証した結果ではない。

操作を依頼する前に、[GIS操作の依頼設計](../concepts/location-ai.md)で対象データ・条件・保存権限・結果確認を定める。アプリや外部データの接続設定は別途必要である。

## 出典

- [@geolibre/map README](https://github.com/opengeos/GeoLibre/blob/main/packages/map/README.md)（2026-09-17確認）
- [npmレジストリのパッケージ情報](https://registry.npmjs.org/@geolibre/map)（2026-09-17確認）
- [@geolibre/map](https://www.npmjs.com/package/@geolibre/map)（共有URL。2026-09-17時点で紹介画面の取得は未了）

- [GeoLibre v3.0.0](https://github.com/opengeos/GeoLibre/releases/tag/v3.0.0)（2026-09-14公開、2026-09-15確認）

- [GeoLibre v2.9.0](https://github.com/opengeos/GeoLibre/releases/tag/v2.9.0)（2026-09-04確認）

- [GeoLibre v3.1.0](https://github.com/opengeos/GeoLibre/releases/tag/v3.1.0)（2026-09-27確認）
- [GeoLibre v3.2.0](https://github.com/opengeos/GeoLibre/releases/tag/v3.2.0)（2026-10-02確認）

- [GeoLibre v3.3.0](https://github.com/opengeos/GeoLibre/releases/tag/v3.3.0)（2026-10-06確認）
