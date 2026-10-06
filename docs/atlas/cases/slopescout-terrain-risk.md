---
layout: default
title: SlopeScout：住所から地形リスクを確認する
category: cases
updated: 2026-10-06
---

# SlopeScout：住所から地形リスクを確認する

SlopeScoutは、住所を入力すると建物周辺の地形と災害情報をまとめるWebアプリの事例である。WSRBと子会社BuildingMetrixがGCSと開発し、Esriが2026年10月5日に紹介した。

## 解析を業務の帳票につなぐ

ワシントン州の高解像度DEM（数値標高モデル）を用い、傾斜のヒートマップ、標高断面、建物外形を含むダウンロード可能なレポートを生成する。洪水区域、地震、火山泥流、断層、津波浸水、液状化などの情報も重ねる。

ArcGIS Enterprise・Serverが解析サービスを提供し、ArcPyが処理、Maps SDK for JavaScriptが住所検索と地図表示、Print Templatesが帳票化を担う。保険の引受判断や防災のために、GISの操作手順を住所検索と成果物の確認へまとめた例である。

## この事例から読み取れる範囲

公式の導入事例であり、Atlasでサービスを操作したり、危険度や業務効果を独立検証したりした結果ではない。機械学習による災害予測と決めつけず、地形解析と既存災害データを組み合わせた業務自動化として読む。対象地域・利用条件は導入先で確認する必要がある。

## 次に読む

- [地形指標と測定スケール](../methods/terrain-scale.md)：標高データの解像度と傾斜の読み方を学ぶ。
- [防災データの再利用](../data/hazard-data-reuse.md)：別の地域で同様の処理を作る前に利用条件を確認する。

## 出典

- [Esri：SlopeScout](https://www.esri.com/arcgis-blog/products/js-api-arcgis/developers/slopescout-decoding-terrain-risk-with-arcgis-one-address-at-a-time)（2026-10-05公開、2026-10-06確認）
