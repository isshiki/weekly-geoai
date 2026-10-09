---
layout: default
title: Cesium
category: tools
updated: 2026-10-09
---

# Cesium

Cesiumは、地球規模の3D地理空間データをタイル化、配信、可視化するための製品・OSS群である。

## ベクタータイルの技術プレビュー

Cesiumは2026年9月2日、3D Tiles 2.0へ向けたベクタータイルの技術プレビューを公開した。Cesium ionへGeoJSON、GeoPackage、ジオデータベース、シェープファイルをアップロードし、属性を保持した3D Tilesへ変換できる。

タイルのペイロードにはglTFを使い、`KHR_mesh_primitive_restart` と `EXT_mesh_polygon` を提案している。Cesiumは、一般的な条件でファイルサイズを最大5分の1へ削減できるとしている。

## 表示とスタイリング

- CesiumJSで大規模な3DベクターをLOD付きで表示する。
- Mapbox Vector Tiles（MVT）を2D・3Dの地理空間コンテキストへ重ねる初期対応を含む。
- 線と面を地形や3D Tilesの表面へドレープできる。
- 地物属性を使い、色や線幅などをJSON式で指定できる。
- Cesium for Unrealでもベクターデータを扱える。

技術プレビュー時点では、点のドレープやスタイルなど未対応の機能が残る。ベクタータイルは3D Tiles 1.1と拡張で提供され、3D Tiles 2.0の一部として採用する計画が示されているため、正式仕様やAPIの変更を前提に評価する。

## その他の2026年9月更新

- CesiumJS 1.145では、地形や3D Tiles上への線・面のドレープに加え、広い範囲でのクリッピング品質と、ポリゴン内のホール指定が改善された。
- BIM/CAD Databaseモデルを対象に、サーバー側で形状へスナップする実験的な `IonSnapService` が追加された。
- Cesium ionでは、元ソースとタイル化済みアセットを分離して管理する変更が案内された。
- Cesium ion Self-Hosted 1.11.0では、iTwin Captureを使う再構築ジョブ、ラベル、IFC metadataなどが更新された。

月次リリースには正式機能、実験的API、技術プレビュー、今後提供予定の変更が混在する。導入時は、利用する製品と機能の成熟度を個別に確認する。

## 設計モデルの更新と変更検出

2026年9月16日、設計モデル向け第2弾技術プレビューが発表された。既存アセットに新しいモデルバージョンを追加し、要素の追加・削除・変更をAPIで調べられる。

設計変更のたびに別アセットへ差し替える運用を減らし、モデルを継続して更新できる点が重要である。変更検出APIでは内部や非表示の要素も対象になり、アプリ側で変更箇所へのズームや分離表示を構成できる。2026年9月21日のPSS解説は、この既報の更新運用を補足している。

| 紹介された機能 | 用途 |
| --- | --- |
| GPUによるクリッピング | 穴のあるポリゴンも使い、地形と設計モデルを重ねる |
| 元形状へのスナップ | 簡略化された表示形状ではなく、ソースモデルの辺・頂点・中点を参照する |
| CRS Search API | 座標参照系を検索してモデルの配置に使う |
| 取り込み時のフィルター | メッシュ・線・文字のうち不要な内容を除く |

スナップ精度はCesiumがミリメートル水準と説明している。自動フットプリント生成、対話型の位置合わせ、スナップを使う計測ツールなどは今後の予定であり、今回の提供機能と区別する。

## 基礎機能の独立と大規模データの読み込み

2026年10月2日の更新で、CesiumJS 1.146は数学・幾何・時間などの基礎クラスを`@cesium/core`へ分離した。外部依存のないパッケージとして、描画エンジン全体を導入せず必要な基礎機能を利用できる。

暗黙的タイルセットの読み込みも改善した。公式記事は大規模建物データのベンチマークで読み込み23倍高速、メモリ使用量1/13と報告する。すべてのデータや描画処理で同じ改善率になるという意味ではない。

UnrealではBlueprintsによるスタイリングを拡充し、UnityではGeoJSONのPoint・MultiPoint描画とポリゴン読み込みに対応した。ionのBIM/CADバージョン管理と変更検出は9月発表の技術プレビューを含む月次整理であり、すべてが10月初出の機能ではない。

## 公開データによる検証と報道向けの可視化

CesiumJSを組み込んだKayhan SpaceのSatcatは、衛星の軌道などをブラウザー上で表示・分析するサービスである。Cesiumの2026年10月6日の事例では、CNNの調査でAIによる候補抽出を人が確認し、時刻・天候・軌道・衛星の用途を踏まえてシミュレーションを作成した。

この調査には公開データを用い、記者が別の道具や情報源でも検証を追えるようにした。Satcat全体には独自データの追加や権限付きデータもあり、サービスの全データが公開されているという意味ではない。

分析の軌道と、放送で理解を助ける衛星モデルを区別する。衛星モデルは説明のため大きく描かれ、CNNが収録後に追加した。3Dで観測可能性を示すことと、実際の観測・情報提供を立証することも分けて読む。今回はベンダーの事例記事の確認であり、調査結果の独立検証は行っていない。

## 設計案を現況に重ねて住民へ伝える

JMTの道路改良事例は、Bentley Infrastructure Cloudの設計モデルをCesium for Unrealで扱い、Google Photorealistic 3D Tilesの周辺環境と重ねている。米国US 281の約20マイルの4車線化計画で、現在と計画後を比較できる映像を住民説明に使った。

設計線だけでは読み取りにくい変化を、住民が知っている道路や土地との関係で伝える用途である。モデルの版比較や属性確認を役割別アプリへ広げる案は今後の検討であり、この事例で提供済みとは扱わない。映像の反響と、工事の実現・安全性・合意形成の効果測定は区別する。

## 出典

- [PSS：設計データを3D地図に重ねるCesiumの新機能](https://note.com/pacificspatial/n/n09d882d31390)（2026-09-21公開、2026-09-22確認）

- [More design model workflows with Cesium](https://cesium.com/blog/2026/09/16/more-design-model-workflows-with-cesium/)（2026-09-17確認）

- [Cesium Releases in September 2026](https://cesium.com/blog/2026/09/02/cesium-releases-in-september-2026/)（2026-09-10確認）
- [Vector Tiles: A Technology Preview for Cesium and 3D Tiles](https://cesium.com/blog/2026/09/02/vector-tiles-technology-preview-cesium-and-3d-tiles/)（2026-09-08確認）
- [【Cesium】ベクタータイルの技術プレビューを公開](https://note.com/pacificspatial/n/n20e3f2309503)（2026-09-08確認）

- [Cesium Releases in October 2026](https://cesium.com/blog/2026/10/02/cesium-releases-in-october-2026/)（2026-10-03確認）

- [Kayhan Space Investigates Satellite Intelligence for CNN with CesiumJS](https://cesium.com/blog/2026/10/06/kayhan-space-satellite-intelligence-cnn-cesiumjs/)（2026-10-07確認）

- [JMTの道路計画可視化](https://cesium.com/blog/2026/10/08/jmt-helps-people-see-the-future-with-cesium/)（2026-10-09確認）
