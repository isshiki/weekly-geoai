---
layout: default
title: AIが扱いやすい地理空間開発環境
category: methods
updated: 2026-10-27
---

# AIが扱いやすい地理空間開発環境

AIエージェントが地図ライブラリや位置情報APIを正しく扱うには、コード例を増やすだけでは足りない。最新の機械可読文書、用途別の手順、入力スキーマ、実行結果の読み戻し、認証・コスト・利用規約のガードレールを一体として整える必要がある。

## 起きやすい問題と対策

| 問題 | 対策 |
| --- | --- |
| 学習済み知識が古い | 最新文書を取得し、Agent Skillsや `llms.txt` から正規の実装経路を示す |
| 複数の古い実装パターンが併存する | 環境ごとに推奨経路を一本化し、非推奨APIと代替を明示する |
| 存在しないレイヤーや式が黙って無視される | JSON Schema、変換レポート、厳格な検証を提供する |
| エージェントが地図の状態を確認できない | viewport、レイヤー、件数、選択対象、エラー、必要ならスクリーンショットを返す |
| APIキーや従量課金を誤って扱う | キー制限、最小権限、費用の注意、利用規約の確認を手順へ組み込む |
| AI生成コードが動くように見えて検証されない | 実ブラウザでレンダリングし、コンソール、表示、操作、アクセシビリティを確認する |

## deck.glで確認された課題

CARTOは2026年9月、7つのAIモデルへ地図作成課題を与え、生成物をヘッドレスブラウザでレンダリングして比較した。大半の地図は動作した一方、モデルが認識するdeck.glのバージョンは当時の最新版9.4.0より古く、v8系の公式例に引っ張られたコードも多かった。

同記事は、エージェント向けインターフェースとして `@deck.gl/json` v2を提案している。JSON Schema、変換時の警告ではなく構造化されたレポート、状態の読み戻し、複数ターン編集用の差分更新などを備え、エージェントが「生成した」だけでなく「正しく表示された」ことを確認できる構成である。

この検証はCARTOが設定した課題と評価方法による一例であり、モデルやライブラリ全般の順位付けではない。再利用すべきなのは、生成物を実行し、失敗を観測可能にした評価方法である。

## Agent Skillsの役割

Google Maps Platform Agent Skillsは、タスクに応じたサブスキルと最新資料を取得し、旧APIの回避、APIキー、費用、利用規約、典型的な実装失敗をチェックする手順を定義している。場所名、住所、評価、座標などをモデルの記憶から補わず、実際のAPIまたはGroundingから取得する規則も含む。

Agent SkillsはAPIそのものではない。エージェントが最新資料と制約に沿ってAPIを利用するための手順・ガバナンス層である。リポジトリはApache 2.0で公開されているが、READMEには公式サポート対象のGoogle製品ではないと明記されている。

### Mapboxの実装知識と操作機能の分担

Mapbox公式のAgent Skillsは、Web・iOS・Android・Flutterの実装、地図デザイン、検索・ナビ、店舗検索、移行、性能・トークン管理などを扱う。2026年10月19日の確認時点では20種類を案内している。数は確認時点の情報で、公開日を示すものではない。

| 要素 | 役割 |
| --- | --- |
| Agent Skills | 環境ごとの実装手順や使い方の知識を伝える |
| Mapbox MCP Server | Mapbox APIを呼び出す機能を提供する |
| DevKit MCP Server | スタイル管理の機能を提供する |

Skillsの導入だけでAPIの認証・利用条件が不要になったり、操作が自動的に正しくなるわけではない。公式はClaude Code、Cursor、GitHub Copilot対応のVS Codeなどへの導入を案内する。今回は資料確認のみで、導入やAPI呼び出しは行っていない。

## 実装・評価の順序

実装前に、[Location AIの依頼ひな形](../concepts/location-ai.md#request-template)で対象範囲・距離条件・操作権限・出力を明示する。[結果確認表](../concepts/location-ai.md#result-checks)は、件数や表示状態を返す仕組みの設計に使える。

1. 用途、対象環境、データ量、必要な地図操作を定義する。
2. 最新の公式文書と推奨APIを取得する。
3. 入出力スキーマ、認証、費用、データ利用条件を固定する。
4. 生成物を実際のブラウザまたは対象環境で実行する。
5. エラー、データ件数、地図状態、ユーザー操作を機械的に確認する。
6. 人が地図表現と分析上の妥当性をレビューする。

## QGISとMCPを使う取得・加工・表示の分担

ソフトバンク テックブログの2026年9月30日の記事は、Claude Codeから外部ツールを組み合わせる構成を紹介する。本文は同年6月時点の情報である。

| 段階 | 実装例 |
| --- | --- |
| 統合 | Claude CodeとClaude Sonnet 4.6 |
| 取得 | 第三者製のmlit-geospatial-mcpで国土交通省のAPIを呼び出す。一部の人流データは事前に用意する |
| 加工 | 動的に生成したPythonコードで集計する |
| 表示 | QGISとQGIS MCPでレイヤーを描画する |

港区の2019年・2020年を比べる例では、駅別乗降客数と1kmメッシュの昼夜の滞在人口差を重ねる。後者は人流データの換算人口値から算出し、国勢調査の昼間人口・夜間人口とは異なる。2年で同じ色階調と記号サイズの基準を使うことで、表示設定による差を避けている。

環境構築と一部のデータ準備は手動である。記事は検証時のコミットを示し、接続表示の確認だけで終えず、各MCPツールを一度呼んで応答を確かめる手順も紹介している。

## 再現可能なAI利用記録を成果物に含める

GeoapifyのOpen Geospatial Program第2期は、OpenAPI仕様を参照する開発と、MCP経由でAIエージェントが地理空間ツールを使う開発を対象にしている。2026年10月の募集では、アプリだけでなくスクリプト・実験・再現可能なワークフローも認める。

注目すべき成果物の条件は、公開コードと実行手順に加え、プロンプト、AIの設定、人の修正が必要だった点、既知の制約も記録することである。これは提供企業の募集要件であり、完成済み事例の性能評価ではない。日程は[日次の更新履歴](../../updates/2026-10-11.md)へ分けて記録する。

## 居住候補地を探すアプリの開発事例

NGSのCameron Panagrossoは、都市と近くに欲しい施設・サービスを指定し、候補地域を探すアプリをClaudeと開発した経験を2026年10月16日に公開した。当初の直線距離から、徒歩・自転車・車での到達時間を考慮する設計へ広げたと説明する。

計画を段階に分け、生成コードのレビューに加えて本人が画面操作を確かめた点が参考になる。作者はコードレビューだけでは見つけにくい画面の問題を報告している。AIとの開発過程の事例であり、地域の推薦精度や到達時間の正確さを検証した比較研究ではない。Atlasでのアプリ動作確認も行っていない。

## AIの操作支援と評価・提供段階を分ける

自然言語でGISを操作する仕組みでも、呼び出せる機能、評価の条件、提供段階は異なる。

| 例 | 対象 | 確認する点 |
| --- | --- | --- |
| Geoapify MCP | POI検索、経路・時間行列、交差・バッファー等 | APIを呼ぶ機能と、正しい条件を選ぶ判断を分ける |
| TerraLab AI Agent | QGIS内でデータ取得・空間分析・出典付きレイヤーを作成 | 自社評価の問題数・採点方法・比較した構成 |
| KKC Satellite Analyst | 日本語から衛星データ選定・解析計画・GIS操作・地図出力 | ユースケース提案と正式サービスを分ける |

GeoapifyのPOI・経路・幾何演算は2026年8月の拡張で、10月の新発表ではない。

TerraLabは公開ベンチマークの41問を各3回実行し、Low effortの総合得点43.8/100を報告する。事前に調べたテンプレート由来の9問を除き、比較は同社が試したモデルとQGIS MCP構成に限る。「最も強力」という記事タイトルをGIS全体の順位として受け取らない。10月21日の案内ではQGIS 3.28以降、無料枠はLow effort月5タスク。Atlasではプラグインの動作や点数を再検証していない。

国際航業はGeozén上のKKC Satellite Analystを10月20日に発表し、クマ出没履歴と衛星データを用いたデモを予定している。2027年度中のサービス化を目標とする開発段階であり、予測精度や時間短縮の実測値はこの発表から判断できない。

## 関連項目

- [Location AI](../concepts/location-ai.md)
- [MapLibre GL JS](../tools/maplibre-gl-js.md)
- [CARTO MCP Server](../tools/carto-mcp-server.md)
- [GISデータセットカタログ](gis-dataset-catalog-for-agents.md)

## 空間計算を専用エンジンへ渡すGeoSpark

GeoSpark（PyPI名geospark-ai）は、LLMから距離・包含・交差・座標変換などを呼び出すためのOSSである。Python・CLI・REST API・MCPを提供し、Shapelyやpyprojなどの計算エンジンを使う。地図データや経路などの外部サービスへの接続には、それぞれの利用条件がある。

現行説明は出典・単位・警告と、回答可能・部分回答・回答不能の状態を返す設計を重視する。Apache-2.0で公開されているが、公式ページのMCPツール数に17・追加3・15という不一致があるため、固定件数を導入条件にしない。旧要約の6ツール・距離正答率0％から70％は現行版の結果として再掲しない。開発者の性能報告を独立検証とは扱わず、本Atlasでもツールを実行していない。

## 出典

- [Making deck.gl AI-Ready: What Seven Frontier Models Taught Us About Maps](https://carto.com/blog/making-deckgl-ai-ready/)（2026-09-10確認）
- [Google Maps Platform Agent Skills](https://github.com/googlemaps/agent-skills)（2026-09-10確認）
- [Google Maps Platform Main Skill](https://github.com/googlemaps/agent-skills/blob/main/skills/google-maps-platform/SKILL.md)（2026-09-10確認）
- [ソフトバンク：自然言語による地物情報の取得・可視化](https://zenn.dev/softbank/articles/a83d02f48e0e84)（2026-10-01確認）

- [Open Geospatial Program Batch #2: AI × Geospatial](https://www.geoapify.com/open-geospatial-program/)（2026-10-11確認）

- [Mapbox Agent Skills](https://docs.mapbox.com/location-ai/agent-skills/)（2026-10-19確認）

- [NGS：AI-Powered Development: Jumping in the Deep End](https://newmoyergeospatial.com/2026/10/ai-powered-development-jumping-in-the-deep-end)（2026-10-20本文確認）

- [Geoapify：更新一覧](https://www.geoapify.com/news-and-updates/)（2026-10-21本文確認）
- [TerraLab：QGIS AI Agent評価](https://terra-lab.ai/blog/ai-agent-qgis-plugin-geospatial-benchmark)（2026-10-21本文確認）
- [国際航業：KKC Satellite Analyst](https://prtimes.jp/main/html/rd/p/000000152.000086246.html)（2026-10-21本文確認）

- [GeoSpark（geospark-ai）](https://pypi.org/project/geospark-ai/)（2026-10-27確認）
