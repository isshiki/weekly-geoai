---
layout: default
title: Spatial Polars
category: tools
updated: 2026-09-15
---

# Spatial Polars

Spatial Polarsは、Polarsに地理空間データの入出力と空間演算を加えるPythonパッケージである。Polars、Shapely、Pyogrio、GeoArrow Python、PyProjを組み合わせ、地図表示にはLonboardを使う。

## 確認したポイント

- `scan_spatial`はGeoParquetやPyogrio対応のデータを読み、PolarsのLazyFrameを返す。
- `read_spatial`はその結果を`.collect()`してDataFrameを返す。
- ジオメトリはWKBのバイナリとCRSのWKTを組にしたStructで保持する。
- 空間式は`.spatial`または`SpatialExpr`から利用でき、Shapelyへ変換して演算する構成である。
- 同じ列のジオメトリは同一CRSを想定するが、READMEではその制約を強制・検証していないと明記している。

LazyFrameを返すことと、すべての空間演算の高速性を保証することは別である。今回確認したREADMEには性能比較の結果は示されていない。

## 出典

- [ATL2001 / GitHub：Spatial Polars](https://github.com/ATL2001/spatial_polars)（公開日：記載なし（README確認）、2026-09-15確認）
