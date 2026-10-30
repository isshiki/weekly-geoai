---
layout: default
title: GeoPandas
category: tools
updated: 2026-10-30
---

# GeoPandas

GeoPandasは、pandasの表に図形と座標参照系（CRS）を持たせるPythonライブラリである。POIと行政区域を重ね、地域ごとの件数をAIモデルの入力にする、といった前処理に使う。Python環境とpandasの基本知識があると始めやすい。

## 使いどころと役割

| 道具 | 担当する処理 |
| --- | --- |
| GeoPandas | 属性の表と図形を一緒に扱い、区域との対応付けや集計結果の地図化を行う |
| Shapely | 図形同士の交差、包含、距離などを計算する |
| DuckDB・Polars | 大きな表の抽出・集計を担う。必要な範囲だけGeoPandasへ渡す使い方もある |
| TorchGeo・geoai-py | 学習・推論側の道具。GeoPandas自体が予測モデルを学習するわけではない |

## 重要な更新履歴 { #release-history }

2026-10-30に公式変更履歴を確認。日付は公式Changelogの記載日で、配布ファイルのアップロード日と異なる場合がある。0.14〜1.2の主要な節目の選集であり、全修正版の一覧や推奨インストール版ではない。

| 版・公式出典 | 公開日 | 主な変化 | 移行・利用の確認点 |
| --- | --- | --- | --- |
| [1.2.0](https://geopandas.org/en/stable/docs/changelog.html#version-1-2-0-september-28-2026) | 2026-09-28 | 静的地図の描画を刷新し、凡例や背景地図の扱いを拡充 | 描画結果の内部構造へ依存するコードには影響。背景地図には追加依存が必要 |
| [1.1.0](https://geopandas.org/en/stable/docs/changelog.html#version-1-1-0-june-1-2025) | 2025-06-01 | 面の結合時の精度指定、面集合の境界整合性の検証など | Python 3.10以上。対応するShapely・GEOSの条件も確認 |
| [1.0.0](https://geopandas.org/en/stable/docs/changelog.html#version-1-0-0-june-24-2024) | 2024-06-24 | 形状処理をShapely 2以上へ統一し、標準I/OをPyogrioへ変更 | PyGEOS・古いShapely・rtreeベースの索引への依存を見直す |
| [0.14](https://geopandas.org/en/stable/docs/changelog.html#version-0-14-sep-15-2023) | 2023-09-15 | 条件を満たす環境でShapely 2を既定に採用 | 1.0での旧エンジン終了に先立つ移行段階 |

## 使うときの確認点

例えば区域内POIを数えるなら、座標系、境界上の点の扱い、重複登録を先に決める。ライブラリの更新だけで集計定義の違いは解消しない。計算用CRSは対象地域と目的に合わせる。今回の整理は公式文書に基づき、コード・性能の実行検証はしていない。

## 次に読む

- [Shapely](shapely.md)：図形演算と表処理の役割分担。
- [DuckDB](duckdb.md)・[Polars](polars.md)：データ抽出・集計との組み合わせ。
- [TorchGeo](torchgeo.md)・[geoai-py](geoai-py.md)：機械学習へ進む場合。
- [座標参照系](../concepts/coordinate-reference-systems.md)：指定と変換の違い。

## 出典

- [公式概要](https://geopandas.org/en/stable/about.html)・[公式変更履歴](https://geopandas.org/en/stable/docs/changelog.html)（2026-10-30確認）。stable文書の表示版には開発版表記もあるため、年表は日付付きの公開版の項目だけを使用した。
