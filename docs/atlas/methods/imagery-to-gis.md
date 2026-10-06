---
layout: default
title: 画像からGIS情報を作る解析と検証
category: methods
updated: 2026-10-06
---

# 画像からGIS情報を作る解析と検証

画像解析では、画素を観察・加工する段階と、抽出結果をGISレイヤーとして使う段階を分ける。画像の補正や指数計算は通常の画像処理でも行える。AIを使う場合は、何を分類・抽出したいかを先に決める。

## 入力から検証まで { #workflow }

| 段階 | 確認すること |
| --- | --- |
| 入力 | 観測日、センサー、バンド、解像度、CRS、雲や欠損。正解データの作り方と時点も確認する |
| 処理 | 画像の分類、物体の検出、画素ごとの領域分割のどれが目的に合うか |
| 出力 | クラス名、検出位置、分類ラスター、抽出ポリゴンなど。スコアの意味も残す |
| 検証 | 誤検出・見逃し、地域や時期による差、GISレイヤー化した後の位置・形状 |

## 「見つけた数」だけで評価しない

建物抽出なら、実在しない建物を抽出した誤検出と、ある建物を抽出しなかった見逃しを分ける。適合率（precision）は予測した陽性のうち正しかった割合、再現率（recall）は実際の陽性のうち見つけた割合である。画素を数えるか、建物を一件ずつ数えるかで評価単位が変わるため、先に決める。

領域の重なりにはIoU（共通部分の面積 ÷ 和集合の面積）などを使える。建物単位の評価では、予測と正解を同じ建物とみなす対応規則も必要である。全体の一つのスコアだけで、境界のずれや小さい対象の見逃しを説明できるとは限らない。

これらは検証設計の案内であり、特定モデルの実測結果ではない。[地域・時点を分ける検証](spatial-analysis-validation.md)と[来歴の記録](../data/geospatial-record-provenance.md)も併せて行う。

## ArcGISでの実行環境

以下はEsri公式解説の製品例であり、上記の考え方を特定製品だけに限定するものではない。今回ソフトの実行は行っていない。

| 環境 | 解説で示す役割 |
| --- | --- |
| ArcGIS Pro | 手元のデータ確認と解析方法の調整 |
| EnterpriseとImage Server | 大規模・反復的な処理 |
| ArcGIS Online | インフラ管理を利用者が担わない画像公開・解析 |

150以上のラスター関数を用意し、補正・植生指数・地形・変化検出などを組み合わせてテンプレートにできると説明する。深層学習で建物・道路・樹木などを抽出した後は、サンプル確認と精度評価を経て利用する。ArcPy・ArcGIS API for Python・REST APIによる自動化と、結果の品質検証は別に設計する。

## データ取得の前提を読む

- [ベクターとラスター](../concepts/vector-raster-data.md)：画像のセル・バンドと抽出する地物の違いを確認する。
- [CNGの構成例](../concepts/cloud-native-geospatial.md#workflow)：STACによる発見とCOGからの読み取りを区別する。
- [検証と適用範囲](spatial-analysis-validation.md)：取得できたことと解析結果が妥当なことを分ける。

## 出典

- [From Imagery to Information: Image Analysis Across ArcGIS](https://www.esri.com/arcgis-blog/products/arcgis/imagery/from-imagery-to-information-image-analysis-across-arcgis)（2026-10-06再確認）
- [scikit-learn: Metrics and scoring](https://scikit-learn.org/stable/modules/model_evaluation.html)（適合率・再現率・Jaccardの定義を2026-10-06確認）
