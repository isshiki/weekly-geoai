---
layout: default
title: POIオープンデータの比較と地域特徴量
category: data
updated: 2026-09-26
---

# POIオープンデータの比較と地域特徴量

POI（店舗・施設などの地点情報）を地域分析に使う際は、総件数だけでなく、対象地域、カテゴリの定義、更新状況、重複や閉店の扱いを揃えて比較する。Foursquare・Overture・OpenStreetMapは、データの作り方と構造が異なる。

## 3種類のデータの違い

| データ | 構造と取得方法 | 比較時の確認点 |
| --- | --- | --- |
| Foursquare Open Source Places | 整理されたPOIデータ。Places Portalのカタログを通じてIceberg形式で取得する | 商用APIやPro・Premiumの仕様と混同せず、オープン版に含まれる属性を確認する |
| Overture Places | 複数の提供元を共通スキーマにまとめたデータ。GeoParquetや範囲指定による取得を扱う | 提供元と統合条件を確認する。Foursquareの全件コピーとして扱わない |
| OpenStreetMap | node・way・relationと自由なタグからなる地理データベース。PBFやOverpassなどで取得する | POIとして抽出するタグ条件を利用側で決める。地点だけでなく建物・敷地の形状もある |

取得方法やスキーマは2026年9月24日に確認した比較記事に基づく。継続利用時は、各データの公式仕様・利用条件・更新日を確認する。

## 比較条件を揃える

- 同じ範囲を切り出し、取得時点とデータの更新時点を記録する。
- 各データのカフェに相当するカテゴリやタグを、分析用の共通カテゴリへ対応付ける。
- 名称・位置・属性の欠損、同一施設の重複、閉店情報を確認する。収録件数の多さだけで品質を決めない。
- データの出所を保持し、統合後も提供元と利用条件をたどれるようにする。

## 地域の特徴として使う

メッシュや駅周辺などの単位でカテゴリ別の件数、密度、構成比、多様性を計算すると、地域を比較する特徴量になる。カテゴリを揃えてからクラスタリングや埋め込みへ進めると、データごとの分類体系の違いが地域差として表れることを抑えられる。

POIは施設の分布という供給側の情報であり、需要や出店適性そのものではない。人口、人流、交通、賃料などと組み合わせて解釈する。9月24日の比較記事は設計を示すもの。続く実践記事は取得・抽出の動作確認であり、データ間の網羅性を比較した結果ではない。

## DuckDBでの取得とカテゴリ抽出

一色政彦の実践記事は、共通の吉祥寺周辺bbox（経度139.574〜139.586、緯度35.699〜35.708）で次の処理を確認している。件数は記事に報告された実行結果であり、本ページで再実行した値ではない。

| 条件 | Foursquare | Overture |
| --- | --- | --- |
| 接続 | Places PortalのトークンでIcebergカタログへ接続 | 2026-09-23.0版の公開GeoParquetを匿名で読む |
| DuckDB拡張 | httpfs・iceberg | httpfs・spatial |
| 範囲・件数 | 国コードJPとbboxで最大500件を取得。上限到達 | bbox候補3,668件をgeometryで再判定し3,666件。LIMITなし |
| 分類 | OS CategoriesのCafé・Coffee Shopと子カテゴリのID | basic_categoryのcafe・coffee_shop。詳細はtaxonomy |
| 抽出結果 | 500件のサンプルから37件 | 202件。Internet Cafeを含む |

2種類の件数をそのまま比較しない。取得上限とカテゴリの定義が異なり、どちらも営業中のカフェ店舗数を示す結果ではない。Overtureのカフェ相当202件はoperating_statusがすべてNULLであり、営業中とも閉店とも判定できない。

Overtureの実践記事は、schema v2.0.0で旧categoriesを使わず、basic_categoryとtaxonomyを確認している。また、sourcesにFoursquare由来の情報があるため、両データに同じ施設があっても独立した2ソースによる確認とは限らない。

## 次の比較に向けた確認点

取得上限、対象版、空間範囲、共通カテゴリ、重複施設、営業状態の扱いを揃え、同一施設の照合と属性の欠損を調べる。bboxとgeometryの判定に差が出た理由は記事でも特定されておらず、丸め誤差などと断定しない。

## 関連項目

- [地理空間データの来歴とレコード単位のメタデータ](geospatial-record-provenance.md)
- [Overtureのデータスキーマ](overture-schema.md)
- [小売出店候補地のロケーションインテリジェンス](../cases/retail-site-selection.md)

## 出典

- [POIオープンデータを比較する：Foursquare・Overture・OpenStreetMap — 一色政彦の技術ノート](https://blog.masahiko.info/entry/2026/09/24/144544)（2026-09-24確認）

- [Foursquare Open Source Placesを使ってみる：DuckDBで日本のPOIを取得する](https://blog.masahiko.info/entry/2026/09/25/145139)（2026-09-26確認）
- [Overture Maps Placesを使ってみる：DuckDBで日本のPOIを取得する](https://blog.masahiko.info/entry/2026/09/26/124845)（2026-09-26確認）
