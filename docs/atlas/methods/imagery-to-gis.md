---
layout: default
title: 画像からGIS情報を作る解析と検証
category: methods
updated: 2026-10-18
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

## モデル入力と元の地物の対応を残す

SpatialArrowの紹介記事は、元の地物ID・形状・CRSと、モデルに渡す画像・ラベルの変換を対応付ける設計を示す。切り出しや拡大縮小を画像とラベルに同じ条件で適用し、元の座標へ戻すための情報も残す。GeoParquetやGeoArrowを採用するだけで、この対応が自動的に保証されるわけではない。

屋根上の太陽光パネル検出では、RF-DETR MediumのmAP@.50:.95が56.97％から59.35％へ改善したと報告する。ただし文脈範囲やサンプル頻度なども変わる比較であり、一要因の効果とは断定しない。画像上での評価件数は地図上の重複を除いた施設数ではなく、復元後の位置精度・地物の同一性・重複除去は別途確かめる。本Atlasでの再実行は行っていない。

## 手を動かして確かめる

[16画素の画像評価演習](../guides/imagery-evaluation-exercise.md)では、正解と予測を図で照合し、誤検出・見逃しと評価指標を手計算・Pythonで確認できる。

## 画像の変化を行政の確認候補へつなぐ

韓国・始興市のグリーンベルトを扱う研究は、衛星・航空・ドローン画像の変化検出、YOLOv8による構造物抽出、SegFormerによる土地被覆分類を、地籍・行政記録へ結び付ける。画像から分かる物理的な変化と、許可の有無などの法的な状態を分けて扱う設計である。

研究では2,486筆を確認候補とし、手動判読の1,836件より35.4%多かった。ただし、候補が多いことは違反確定件数や再現率が35.4%改善したことを意味しない。現地確認と行政側の判断が必要になる。研究内の評価を別地域での性能保証として扱わず、本Atlasではモデルの再実行も行っていない。

## 出典

- [From Imagery to Information: Image Analysis Across ArcGIS](https://www.esri.com/arcgis-blog/products/arcgis/imagery/from-imagery-to-information-image-analysis-across-arcgis)（2026-10-06再確認）
- [scikit-learn: Metrics and scoring](https://scikit-learn.org/stable/modules/model_evaluation.html)（適合率・再現率・Jaccardの定義を2026-10-06確認）

- [Integrating GeoAI and Multisource Remote Sensing with Cadastral Data for Greenbelt Compliance Screening](https://www.mdpi.com/2220-9964/15/10/461)（2026-10-12確認）
- [GeoAIの精度を地理空間情報の信頼性につなぐ（データとAIの接続をSpatialArrowで整合する）](https://qiita.com/lehukuku0120/items/cd2c29d48b88c18be449)（2026-10-18本文確認）
