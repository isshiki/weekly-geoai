---
layout: default
title: CADからGeoPackageへの変換と検証
category: methods
updated: 2026-09-21
---

# CADからGeoPackageへの変換と検証

CAD図面からGISで使う形状を取り出すときは、形式の変換と、文字・座標・地物が期待どおり残っているかの検証を組み合わせる。rino_yumeのDWG2GeoPackage v0.2.0は、LibreDWGとGDAL/OGRをDocker内で使う実装例である。

## 処理の流れ

DWGをGNU LibreDWG 0.14でR2018 DXFへ変換し、GDAL/OGRでGeoPackageへ出力する。LibreDWGはコミットまで固定し、変換結果の再現条件を残す。

著者は約44MBの実DWGから直接GeoJSONを作ると約1GBとなり、正常に読み切れない例もあったため、DXF経由へ変更したと報告している。これは当該データでの経験であり、すべてのDWGに共通する容量比ではない。

## 段階ごとの検証

| 対象 | 実装で確認・対処すること |
| --- | --- |
| DXF構造 | INSERT・ATTRIBの終端で欠けたSEQENDのみを補正し、その他の読めない構造はpreflightで停止 |
| 日本語 | ヘッダーと実際のバイト列の不一致を確認し、UTF-8を検証して読み込み側へ指定 |
| 単位 | `--scale-to-m`で倍率を明示。mmからmなら0.001とし、ヘッダー情報だけで自動決定しない |
| 座標参照系 | 元座標に対応するEPSGを指定し、出力の範囲と倍率を確認 |
| Geometry型 | Point・Multipoint・Line・Polygonを分け、出力型を明示 |
| 地物の保持 | 変換前後のFeature数、Geometry型、Z/M次元などを確認 |
| ファイルと索引 | SQLiteの整合性と、実際のgeometry列名に対応するRTreeを確認 |

単位倍率の変更と座標参照系の指定は別の確認項目である。記事のサンプルはEPSG:6676として使う座標値で作図しており、任意のCADへ同じEPSGを付ければ正しい位置になるという意味ではない。

GDALのDXFドライバーの文字コード処理には`DXF_ENCODING`による上書きがある。UTF-8の指定は記事で検証した出力に対する対応であり、あらゆるDXFに適用する固定ルールではない。

## 成功判定と限界

著者は`ogr2ogr`の終了コードだけで成功とせず、`-skipfailures`で地物を落として進めることも避けている。約72.9万Featureを持つ実データでの確認を報告するが、Atlasでは変換プログラム自体を実行検証していない。

目的はGIS向けの形状抽出である。図面の見た目の完全再現や、すべてのブロック・HATCH・特殊オブジェクトへの対応を保証するものではない。

## 関連項目

- [座標参照系（CRS）との関係](../concepts/coordinate-reference-systems.md)
- [FME](../tools/fme.md)

## 出典

- [CADとGISをつなぐ ── LibreDWG × GDALでDWGをQGIS/ArcGIS pro 対応GeoPackageへ変換する](https://qiita.com/rino_yume/items/dad684526717a806fec8)（2026-09-20公開、2026-09-21確認）
- [GDAL AutoCAD DXF driver](https://gdal.org/en/stable/drivers/vector/dxf.html)（2026-09-21確認）
