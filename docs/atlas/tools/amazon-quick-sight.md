---
title: Amazon Quick Sightの地図
category: tools
updated: 2026-10-24
---

# Amazon Quick Sightの地図

Amazon Quick Sightは業務データをダッシュボードにするBIサービスである。地図と売上などを結び付ける用途にも使う。レイヤーマップには、利用環境に加えてGeoJSONの形状、指標を持つデータセット、両者を結ぶ共通キーが必要になる。

## 形状と指標を分けて更新する

2026年10月23日の公式記事は、レイヤーマップでPoint（点）とLineString（線）を扱う方法を紹介する。ファイルの上限は100MB。線は渡した座標列を結ぶもので、それ自体が経路計算を行うわけではない。

| 変えるもの | 必要な更新 |
| --- | --- |
| 店舗の売上、色、ツールチップの値 | データセットの更新 |
| 店舗の位置、配送経路の形 | GeoJSONの差し替えとダッシュボードの再公開 |

形状更新はS3とAPIでも自動化できる。既存のPoint mapは位置の更新や点のサイズ変更に対応する一方、レイヤーマップの点は明示的な座標が必要で、サイズは均一である。

表示範囲を固定した点・線・面の重ね合わせは、複数の地図ビジュアルを同じ範囲にそろえて重ねる方式。上側のツールチップだけにアクセスできる点も考慮する。今回は記事確認のみで、実環境での動作は未検証である。

## 次に読む

- [位置情報PaaSの選び方](../methods/location-paas-selection.md)：経路を計算するAPIと表示する道具を分ける。

## 出典

- [AWS：GeoJSONの点・線を表示する](https://aws.amazon.com/blogs/machine-learning/visualize-points-and-routes-with-geojson-in-amazon-quick-sight-layer-maps/)（2026-10-24本文確認）
