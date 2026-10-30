---
layout: default
title: Shapely
category: tools
updated: 2026-10-30
---

# Shapely

Shapelyは、点・線・面の形状を計算するPythonライブラリである。内部ではGEOSを利用する。例えば店舗の点が区域に入るか、2つの区域がどこで重なるかを判定し、GeoAIの特徴量作成やデータ点検を支える。Python環境が必要で、単独のGISアプリやAIモデルではない。

## GeoPandasとの違い

[GeoPandas](geopandas.md)が「店舗名や売上などの表＋図形」を管理するのに対し、Shapelyは図形の計算を担当する。図形配列にまとめて演算したい場合にも使える。ファイルの読み書きやCRS管理まで一式で扱いたい場合は、GeoPandasなどと組み合わせる。

## 重要な更新履歴 { #release-history }

公式変更履歴を2026-10-30に確認。日付は同文書の記載日。2.0〜2.2の主要な節目を選んでおり、全修正版や1.x以前の履歴は網羅しない。最新推奨版を示すものではない。

| 版・公式出典 | 公開日 | 主な変化 | 移行・利用の確認点 |
| --- | --- | --- | --- |
| [2.2.0](https://shapely.readthedocs.io/en/stable/release/2.x.html#version-2-2-0-2026-10-07) | 2026-10-07 | 単一図形の呼び出し性能を改善。面集合を整えるcoverage_cleanを追加 | coverage_cleanにはGEOS 3.14以上が必要。処理全体の速度は未測定 |
| [2.1.0](https://shapely.readthedocs.io/en/stable/release/2.x.html#version-2-1-0-2025-04-03) | 2025-04-03 | M値の初期対応、面集合の整合性検証・簡略化 | これらにはGEOS 3.12以上が必要。隣接境界をそろえた面集合が対象 |
| [2.0.0](https://shapely.readthedocs.io/en/stable/release/2.x.html#version-2-0-0-2022-12-12) | 2022-12-12 | 図形配列をまとめて計算する演算を導入し内部構造を刷新 | 図形は変更不能に。複合図形の直接反復やSTRtreeの戻り値などに互換性変更 |

## 使うときの確認点

Shapelyの基本演算は平面上の計算である。緯度経度を渡しただけで距離がメートルになるわけではなく、CRSの変換は適切な外部処理と組み合わせる。入力の無効な形状、空の図形、欠損の扱いも確認する。

面を簡略化するとき、1枚ずつ処理する方法と、隣接する境界を保ちながら集合を処理する方法は違う。行政区域などをGeoAIの集計単位に使う場合は、重複・隙間が生じていないかを確かめる。今回、形状演算や性能の実行検証はしていない。

## 次に読む

- [GeoPandas](geopandas.md)：図形に属性・CRSを組み合わせる。
- [座標参照系](../concepts/coordinate-reference-systems.md)：計算に合う座標を選ぶ。

## 出典

- [公式マニュアル](https://shapely.readthedocs.io/en/stable/manual.html)・[公式2.x変更履歴](https://shapely.readthedocs.io/en/stable/release/2.x.html)（2026-10-30確認）。
