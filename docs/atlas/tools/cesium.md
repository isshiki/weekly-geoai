---
layout: default
title: Cesium
category: tools
updated: 2026-09-08
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

- CesiumJS 1.145では、地形や3D Tiles上へのベクターデータのドレープとクリッピングポリゴンが改善された。
- Cesium ionでは、元ソースとタイル化済みアセットを分離して管理する変更が案内された。

## 出典

- [Cesium Releases in September 2026](https://cesium.com/blog/2026/09/02/cesium-releases-in-september-2026/)（2026-09-04確認）
- [Vector Tiles: A Technology Preview for Cesium and 3D Tiles](https://cesium.com/blog/2026/09/02/vector-tiles-technology-preview-cesium-and-3d-tiles/)（2026-09-08確認）
- [【Cesium】ベクタータイルの技術プレビューを公開](https://note.com/pacificspatial/n/n20e3f2309503)（2026-09-08確認）
