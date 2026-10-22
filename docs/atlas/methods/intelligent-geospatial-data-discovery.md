---
layout: default
title: 知識グラフとLLMエージェントによる地理空間データ探索
category: methods
updated: 2026-10-22
---

# 知識グラフとLLMエージェントによる地理空間データ探索

異なる地理空間メタデータを知識グラフへ統合し、LLMエージェントが自然言語の意図解析、候補検索、回答生成を分担するデータ探索手法が研究されている。キーワード一致だけでは扱いにくい主題、場所、期間、形式、ライセンスなどの条件を構造化して検索するアプローチである。

## 確認したポイント

- 2026年の論文では、異種メタデータを統合オントロジーへ写像するIGDDフレームワークが提案された。
- Intent Parsing、Graph Retrieval、Answer Synthesisの各エージェントが処理を分担する。
- 知識グラフによる制約付き検索と、LLMによる候補の再順位付けおよび説明生成を組み合わせる。

## 住所の規則から位置関係をたどる

データセットを探す以外にも、知識グラフで場所同士の関係を検索する研究がある。韓国の道路名住所の番号の奇偶・順序・差を関係として持たせ、向かい側や建物内の階などをグラフでたどる方法である。検索時の座標計算を省くという意味で、座標情報があらゆる工程で不要になるわけではない。

2026年10月21日の論文の公開要旨は、ソウル鍾路区の191,808要素・380,743関係と400問の評価で検索F1を0.381、公式の形状データがない未登録階への質問では0.647と報告する。3種類の小型LLMによる回答生成後は0.316～0.359だった。住所と実体の対応付けの不足が制約になる。

今回確認できたのは早期公開版の要旨までで、PDF全文や評価問題の詳細は未確認である。住所付番規則に依存するため、日本の住所へ同じ規則・精度をそのまま適用できるとはしない。屋内の安全な移動経路を求める仕組みとしても評価していない。

## 関連項目

- [Location AI](../concepts/location-ai.md)
- [GISデータセットカタログ](gis-dataset-catalog-for-agents.md)
- [CARTO MCP Server](../tools/carto-mcp-server.md)
- [Portolan](../data/portolan.md)

## 出典

- [Towards intelligent geospatial data discovery: a knowledge graph-driven multi-agent framework powered by large language models](https://www.tandfonline.com/doi/full/10.1080/13658816.2026.2724505)（2026-09-04確認）

- [Rule-Derived Address Knowledge Graph for Indoor–Outdoor Spatial Question Answering](https://www.mdpi.com/2220-9964/15/10/478)（2026-10-22公開要旨確認。全文未確認）
