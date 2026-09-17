---
layout: default
title: Overtureのデータスキーマ
category: data
updated: 2026-09-17
---

# Overtureのデータスキーマ

Overtureのスキーマは、地物の属性と制約を定義する。v2ではPythonのPydanticモデルを正本とし、データ検証と文書生成を共通の定義から行う。

## v2での構成

| 要素 | 役割 |
| --- | --- |
| `overture-schema` | 6テーマとツールをまとめて導入するパッケージ |
| Pydanticモデル | 型・制約の定義、属性の参照、データ検証 |
| 生成物 | JSON Schema、PySpark検証式、参照文書 |

GeoJSONとGeoParquetを扱うモデルであり、他形式への拡張可能性も説明されている。JSON Schema自体が廃止されるわけではない。

## 移行時の区別

2026年9月16日の記事は、約2週間前に公開したv2.0.0を説明している。記事公開日をリリース日として扱わない。YAML版の削除は2026年12月の予定で、追加フィールドを標準化するschema extensionsは次の目標である。

## 出典

- [The Overture Schema Is a Library Now](https://docs.overturemaps.org/blog/2026/09/16/schema-v2/)（2026-09-17確認）
