---
title: 初めてのGeoAI
category: guides
updated: 2026-10-06
---

# 初めてのGeoAI

地図・位置情報とAIを学ぶ入口である。最初から製品名を覚えるより、「どの場所について、何を知りたいか」を一つ決めると、必要なデータと道具を選びやすい。

## まず押さえる言葉

| 言葉 | このサイトで扱う意味 | 身近な例 |
| --- | --- | --- |
| GIS | 位置に結び付いた情報を管理・分析・表示する仕組み | 避難所と浸水区域を重ねて見る |
| POI | 店舗・施設など、関心の対象になる場所の情報 | カフェの名前、位置、カテゴリ |
| 地物と属性 | 地図上の対象と、それに付く説明 | 店舗の点と、名称・業種 |
| レイヤー | 同じ種類の地物をまとめた表示の単位 | 店舗、道路、浸水区域を別々に重ねる |
| 座標参照系（CRS） | 数値の座標が地球上のどこを指すかを決める仕組み | 緯度・経度と平面上のメートル座標 |
| GeoAI | 地理空間データとAI・機械学習を組み合わせる取り組み | 衛星画像の分類や、場所の情報を使う予測 |

## 一つの目的を、五つの段階に分ける

例えば「駅の周辺にどのような店が多いか」を調べる場合は、次の順で進める。

1. **問いを決める**：駅からの範囲、対象業種、調べる時点を決める。
2. **データを選ぶ**：POIの利用条件、更新日、属性を確認する。
3. **条件をそろえる**：座標系、カテゴリ、重複、取得漏れを確認する。
4. **分析して地図にする**：件数や密度を集計し、分布を見る。
5. **結果を確かめる**：元データと照合し、欠損や収録の偏りを説明する。

<figure markdown="span" id="analysis-cycle">
  ![問い、データ選択、条件整理、分析、検証の順に進み、結果に問題があればデータや条件の見直しに戻る](../../assets/atlas/getting-started/analysis-cycle.svg)
  <figcaption>検証で見つかった不足を、データ選びや条件の整理へ戻して改善する。本文の手順を基にGeoAIアトラス作成。</figcaption>
</figure>

単純な集計や地図表示にも価値がある。AIを組み合わせる場合も、この流れのどの段階を任せるかを決め、出力を確かめる。店舗数だけから人気や売上を結論付けることはできない。

## 基礎を五つのテーマで学ぶ { #foundations }

点・線・面と画像の違いから確認したい場合は、[ベクターとラスター](../concepts/vector-raster-data.md)を先に読む。5テーマの後は、[空間索引](../methods/spatial-index-selection.md)で検索の効率化、[データの来歴](../data/geospatial-record-provenance.md)で再現に必要な記録へ進める。

| 順序 | 読むページ | 読み終えたら確かめること |
| --- | --- | --- |
| 1 | [GeoAIの全体像](../concepts/geoai-overview.md) | AIでデータを分析することと、GISを操作させることを分けられる |
| 2 | [座標参照系と距離・面積](../concepts/coordinate-reference-systems.md#measurement) | CRSの設定と変換、平面と曲面の計算を区別できる |
| 3 | [空間結合と集計の基本](../methods/spatial-join-and-aggregation.md) | 境界上の点や複数所属が件数に与える影響を説明できる |
| 4 | [予測・説明・因果の違い](../concepts/geographic-model-reasoning.md#prediction-explanation-causality) | 同じ回帰モデルでも問いと検証が変わることを説明できる |
| 5 | [分析結果の検証と適用範囲](../methods/spatial-analysis-validation.md) | 利用する地域・時点に合わせ、何を照合すべきか挙げられる |

### 経験に合わせて入口を選ぶ

- **GIS経験がある人**：1 → 4 → 5。機械学習の目的と評価を押さえ、必要に応じて画像解析や埋め込みへ進む。
- **Python・データ分析経験がある人**：2 → 3 → 5。座標・境界・集計の違いを押さえ、4で結果の解釈を確認する。
- **コードを書かずに使いたい人**：1 → 2 → 3。境界上の点の模式例を紙の上で数え、5の入力・単位・件数の確認へ進む。モデル開発の詳細は後から読める。

これは編集上の学習案内である。すべてのページを順番に読了することを、地図を試すための条件にはしない。

## 目的別の読む順序

AIの出力を評価したい場合は、[16画素で試す画像分類の評価](imagery-evaluation-exercise.md)で、誤検出・見逃しを数え、適合率・再現率・IoUを比べられる。

手を動かして確かめたい場合は、[4店舗で試す空間結合と件数の検証](spatial-join-exercise.md)へ進む。手計算でもPythonでも、境界の扱いと未所属・重複を確認できる。

| やりたいこと | 最初に読む | 次に読む |
| --- | --- | --- |
| 店舗・施設を分析したい | [POIデータを選び、分析する](poi-workflow.md) | [POI比較と地域特徴量](../data/poi-open-data-comparison.md) |
| 人の動きを知りたい | [人流データの種類](../data/human-flow-data-types.md) | [誤差と品質](../data/human-flow-data-quality.md) → [プライバシー](../methods/location-data-privacy.md) |
| 地図がずれる理由を知りたい | [座標参照系](../concepts/coordinate-reference-systems.md) | [投影法の選び方](../concepts/map-projections.md) |
| データをWeb地図にしたい | [Felt](../tools/felt.md)で共有の流れを知る | コードで作るなら[MapLibre](../tools/maplibre-gl-js.md)・[OpenLayers](../tools/openlayers.md) |
| AIにGIS操作を任せたい | [依頼を実行条件へ分ける例](../concepts/location-ai.md#request-example) | [依頼ひな形](../concepts/location-ai.md#request-template) → [AI向け開発環境](../methods/ai-ready-geospatial-development.md) |
| GeoAIの手法を選びたい | [入力・出力で選ぶ比較表](../concepts/geoai-overview.md#choose-method) | [出力ごとの検証](../methods/spatial-analysis-validation.md#ai-results) |
| 防災データを使いたい | [ハザードデータの再利用条件](../data/hazard-data-reuse.md) | [ポリゴンのメッシュ集計](../methods/polygon-mesh-aggregation.md) |

## 道具を選ぶ前に

「ライブラリ」はプログラムへ組み込む部品、「Webサービス」はブラウザーやAPIを通して利用するサービスである。名前が並んでいても、準備や操作方法は同じではない。各ページでコードの必要性、入力データ、出力、利用条件を確かめる。

データがオープンであること、サービスに無料枠があること、自由に再配布できることは別の条件である。また、論文の実験結果、製品の発表、実際に動作確認した結果も分けて読む。

## この案内の参照先

このページはAtlasの既存解説をつなぐ編集上の案内である。技術の詳細と出典・確認日は、上記の各ページに記載している。全項目は[知識マップ](../index.md)から探せる。
