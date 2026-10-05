---
layout: default
title: Location AI
category: concepts
updated: 2026-10-05
---

# Location AI

Location AIは、地理空間データと位置情報機能をAIエージェントから利用し、場所に関する探索、分析、判断、操作を行うための仕組みを指す呼び方である。標準化された厳密な用語ではなく、各社が示す範囲は異なる。単に地図を会話画面へ表示する機能ではなく、データ、検索・分析ツール、エージェント向けの接続、実行時の検証までを含めて捉える必要がある。

## 例えば何を任せるのか

「駅から歩いて行けるカフェを調べ、地図にする」という依頼なら、場所を検索し、必要に応じて経路を計算し、条件に合う結果を表示する。これは処理の考え方を示す例であり、特定製品で動作確認した手順ではない。

AIへ依頼する文章、実際に検索・計算するツール、根拠になるデータは別の役割を持つ。言葉で指示できることに加え、どのデータと計算を使ったかを確かめられることが重要である。

<figure markdown="span">
  ![地理空間データから業務結果までをつなぐLocation AIの5層](../../assets/atlas/location-ai/location-ai-layers.svg)
  <figcaption>Location AIを構成するデータ、接続、指示、実行、結果の関係。GeoAIアトラス作成。</figcaption>
</figure>

## 構成要素

| 層 | 役割 | 例 |
| --- | --- | --- |
| 地理空間データ | 場所と現実世界の状態を表す | POI、道路、交通、人流、土地、画像 |
| API・ツール接続 | データの検索や空間処理を実行する | REST API、SQL、SDK、MCP Server |
| 指示・ガバナンス | AIへ最新の利用方法と制約を伝える | Agent Skills、機械可読な文書、認証・コスト規則 |
| エージェント実行 | 依頼を複数の処理へ分解し、ツールを組み合わせる | 検索、到達圏、集計、ルート計算、地図作成 |
| 結果とフィードバック | 人が結果を確認し、再実行や修正につなげる | 地図、レポート、Workflow、エラー、状態の読み戻し |

MCPは主にエージェントとデータ・ツールを接続する。Agent Skillsは、どのツールをどう選び、安全性やコストをどう確認するかという手順を補う。同じ「AI対応」であっても役割は異なるため、接続できることと、正しく再現可能に実行できることを分けて評価する。

## 評価するときの確認点

- データの対象地域、更新頻度、空間・時間解像度、ライセンスを確認する。
- LLMの学習済み知識ではなく、実際のAPIやデータセットから場所情報を取得しているかを確認する。
- 読み取り、書き込み、管理操作の権限を分け、操作履歴を監査できるようにする。
- 地図や集計が空でも成功扱いにならないよう、スキーマ検証、エラー、件数、表示状態をエージェントへ返す。
- 個人に関係する位置情報では、同意、利用目的、集計方法、再識別リスク、保存期間を確認する。

## 仕組みを具体例で見る

次は2026年9〜10月に確認した資料の整理であり、製品の順位や現在の提供保証ではない。詳細な機能・契約条件は各ページと公式資料で確認する。

| 役割 | 確認した例 | 読む際の注意 |
| --- | --- | --- |
| 場所の情報を取得する | Mapbox、xMapなどのPOI・位置情報基盤 | データの収録数は地域別の網羅率や営業情報の正確さとは異なる |
| 検索や計算を呼び出す | [TomTom Orbis APIs](../tools/tomtom-orbis.md)、[Mapbox Search Box](../tools/mapbox-search-box.md) | APIを使えることと、依頼全体を正しく遂行できることは別である |
| GIS操作を実行して残す | [CARTO MCP Server](../tools/carto-mcp-server.md) | 権限、処理履歴、再実行可能性を確認する |
| 自社データへ位置の文脈を加える | TomTomとMicrosoft Fabricの連携発表 | プレビューと一般提供を区別する。オープン標準の採用は製品全体の無償利用を意味しない |

### 発表の提供段階を区別する

Mapboxの2026年9月17日発表では、Places APIと自然言語によるSearch Box検索は公開プレビュー、Static Images APIのAI Modeは事前発表として案内された。後日の転載や公式掲載確認を、新たな提供開始として数えない。個別機能は[MapboxのMCP](../tools/mapbox-figma-mcp.md)、[検索](../tools/mapbox-search-box.md)、[Traffic](../tools/mapbox-traffic.md)を参照する。

Amapが9月24日に発表したQianyuは、自然言語から時空間の範囲を決め、情報収集と複数ソースの照合を行う構成を説明している。「open platform」という表現だけでデータのオープンライセンスや他社との互換性を判断しない。分析精度、日本で使えるデータ、契約条件は未検証である。

### データの規模と品質を区別する

xMapの「Global advanced POI data」は、9月28日の確認時点で233カ国・3億件超、各地点に最大36項目と説明していた。これらはベンダー公表値である。属性の仕様があっても、各レコードに値が入るとは限らない。対象地域のサンプルで、営業状態、確認日、欠損を調べる。

## 店舗情報の鮮度とエージェントの誤推薦

PinMeToの2026年10月1日の論考は、Yahoo Financeの試用報告を引用し、Meta Museが閉業済み店舗を推薦し、電話番号を生成した例を紹介する。記事はMuseの参照データ源が未公表であると明記しており、Overtureを原因とした不具合とは確認していない。

著者は店名・住所・電話・営業時間・座標を複数の掲載先で揃え、移転・閉業を反映するよう提案する。これは店舗データ整備を提供する企業の論考であり、AI全般の誤推薦率を測定した研究ではない。

## 関連項目

- [ロケーションインテリジェンス](location-intelligence.md)
- [AIが扱いやすい地理空間開発環境](../methods/ai-ready-geospatial-development.md)
- [CARTO MCP Server](../tools/carto-mcp-server.md)
- [知識グラフとLLMエージェントによる地理空間データ探索](../methods/intelligent-geospatial-data-discovery.md)

## 出典

- [Top announcements from BUILD with Mapbox 2026](https://www.mapbox.com/blog/top-announcements-from-build-with-mapbox-2026)（2026-09-18確認）
- [Mapbox Announces Location Infrastructure for AI](https://www.prnewswire.com/news-releases/mapbox-announces-location-infrastructure-for-ai-mapbox-announces-location-infrastructure-for-ai-302882326.html)（2026-09-18確認）

- [Location AI at Mapbox](https://docs.mapbox.com/help/getting-started/location-ai/)（2026-09-10確認）
- [xMap](https://www.xmap.ai/ja)（2026-09-10確認）
- [TomTom: location intelligence an important growth market](https://www.marketscreener.com/news/tomtom-location-intelligence-an-important-growth-market-ce785bd8db81f32d)（2026-09-10確認、第三者記事）
- [Geospatial Analysis in Claude with the CARTO MCP Server](https://carto.com/blog/geospatial-analysis-claude-mcp-server/)（2026-09-10確認）
- [TomTom Orbis APIs are now in general availability](https://www.tomtom.com/newsroom/product-focus/tomtom-orbis-apis-are-now-in-general-availability/)（2026-09-19確認）

- [Amap：Spatial Intelligence Open Platform for No-Code AI Agents](https://www.prnewswire.com/news-releases/amap-launches-spatial-intelligence-open-platform-for-no-code-ai-agents-in-location-services-302888910.html)（2026-09-25確認）

- [xMap：Global advanced POI data](https://www.xmap.ai/global-advanced-rich-poi-data)（2026-09-28確認）

- [Mapbox Announces Location Infrastructure for AI（発表掲載）](https://www.geoweeknews.com/articles/mapbox-announces-location-infrastructure-for-ai/)（2026-09-29確認）
- [PSS：Google・Esri・CARTO・Mapboxはそれぞれ何を狙っているのか](https://note.com/pacificspatial/n/n6e6a847d4b87)（2026-09-29確認）

- [Mapbox公式：Location Infrastructure for AI](https://www.mapbox.com/press-releases/mapbox-announces-location-infrastructure-for-ai)（2026-09-30確認）
- [TomTom公式発表](https://www.tomtom.com/newsroom/press-releases/general/224935140570399/tomtom-brings-location-intelligence-to-microsoft-fabric/)（2026-10-02確認）
- [TomTom brings location intelligence to Microsoft Fabric](https://finance.yahoo.com/technology/ai/articles/tomtom-brings-location-intelligence-microsoft-053000575.html)（2026-10-02確認）
- [What Meta’s Muse AI Agent Means for Your Location Data](https://www.pinmeto.com/blog/meta-muse-ai-agent-local-data/)（2026-10-02確認）
