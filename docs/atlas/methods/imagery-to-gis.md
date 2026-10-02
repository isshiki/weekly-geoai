---
layout: default
title: 画像からGIS情報を作る解析と検証
category: methods
updated: 2026-10-02
---

# 画像からGIS情報を作る解析と検証

画像解析では、画素を観察・加工する段階と、抽出結果をGISレイヤーとして使う段階を分ける。Esriの解説は、ラスター処理、深層学習、結果の検証、自動化までを一連の作業として整理する。

## ArcGISでの実行環境

| 環境 | 解説で示す役割 |
| --- | --- |
| ArcGIS Pro | 手元のデータ確認と解析方法の調整 |
| EnterpriseとImage Server | 大規模・反復的な処理 |
| ArcGIS Online | インフラ管理を利用者が担わない画像公開・解析 |

150以上のラスター関数を用意し、補正・植生指数・地形・変化検出などを組み合わせてテンプレートにできると説明する。深層学習で建物・道路・樹木などを抽出した後は、サンプル確認と精度評価を経て利用する。ArcPy・ArcGIS API for Python・REST APIによる自動化と、結果の品質検証は別に設計する。

## 出典

- [From Imagery to Information: Image Analysis Across ArcGIS](https://www.esri.com/arcgis-blog/products/arcgis/imagery/from-imagery-to-information-image-analysis-across-arcgis)（2026-10-02確認）
