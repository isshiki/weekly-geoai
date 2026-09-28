---
layout: default
title: 地図探索エージェントの記憶と空間推論
category: methods
updated: 2026-09-28
---

# 地図探索エージェントの記憶と空間推論

地図探索エージェントでは、局所的な観察を蓄積し、後から位置関係を答えるための記憶表現が評価対象となる。「Thinking on Maps」は、OpenStreetMap由来の15都市の地図を20×20マスに変換し、見える範囲を限って探索させた研究である。

## 記憶表現を変えた比較

論文のTable 4では、探索方針を近いPOIから訪れる方式に固定し、GPT-5.2の全体正答率を次のように報告している。

| 記憶 | 全体正答率 |
| --- | ---: |
| 会話履歴（SDM） | 43.89% |
| 訪問地点と経路を順に記録（NSM） | 77.78% |

方向、距離、近さ、POI密度、経路などを評価しており、この実験では探索順の変更より記憶表現による差が大きかった。実務への示唆としては、会話の蓄積量だけでなく、後の質問に必要な位置関係を残す形式を設計する観点がある。

## 適用範囲

平面上の記号化された地図での結果であり、現実のナビゲーションや一般的なGIS業務の精度を示すものではない。arXiv初版は2025年12月30日、確認したv2は2026年1月1日である。2026年9月の新着論文とは区別する。今回は本文の確認であり、実験の追試は行っていない。

## 関連項目

- [地理空間モデルの予測と地理的理解](../concepts/geographic-model-reasoning.md)
- [空間特徴とLLMエージェントによる次の訪問地点予測](spatial-agent-mobility-prediction.md)

## 出典

- [Thinking on Maps: How Foundation Model Agents Explore, Remember, and Reason Map Environments](https://arxiv.org/abs/2512.24504)（2026-09-28確認）
- [論文v2本文：Section 4.2、Table 4](https://arxiv.org/pdf/2512.24504v2)（2026-09-28確認）
