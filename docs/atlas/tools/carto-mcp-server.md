---
layout: default
title: CARTO MCP Server
category: tools
updated: 2026-09-09
---

# CARTO MCP Server

CARTO MCP Serverは、Model Context Protocol（MCP）を通じてCARTOの地図、Workflows、空間分析、ジオコーディング、ルーティング、管理機能などをAIエージェントへ公開する接続層である。エージェントが自然言語の依頼からCARTO上の資産を操作し、結果を再利用できるWorkflowや地図として残す用途を想定している。

## Claudeからの利用

ClaudeではCARTO MCP Serverをカスタムコネクタとして登録し、CARTOアカウントで認証する。CARTOの公式記事によると、この接続では別個のOAuthクライアントを作成せずに利用でき、MCP Appsに対応する地図は会話内へ表示される。

会話から次の処理を行える。

- 接続済みデータの探索とクエリ
- CARTO Builderの地図作成とレイヤー、分類、Popupなどの変更
- CARTO Workflowsの作成、実行、保存
- ジオコーディング、到達圏、ルーティングなどの空間処理
- 接続、ユーザー、資格情報など、許可された管理操作

## 実行権限と監査

各ツール呼び出しは認証したCARTOユーザーとして実行される。クエリは接続済みデータウェアハウス内で実行され、既存のIAM、ロール、行レベルセキュリティが適用される。操作はActivity Dataへ記録されるため、エージェントだから権限や監査の外側で動くわけではない。

接続後は、エージェントから見える接続、テーブル、利用可能なツールを先に確認する。書き込みや管理機能を含むため、最小権限のユーザーで開始し、生成されたWorkflowの入力、処理手順、出力をレビューする。

## Workflowとして残す意味

会話中に一度だけSQLを生成するのではなく、分析手順をCARTO Workflowとして保存すれば、処理を開いて確認し、再実行、複製、スケジュールできる。公式例ではDenverのLTE基地局から1km圏を作り、圏外の建物を用途別に抽出し、最寄り基地局までの距離を計算して地図化した。

AIは分析方法の提案と構築を支援するが、保存後のWorkflowは明示的な処理パイプラインとして実行される。継続的な業務では、会話ログだけを成果物にせず、再現可能な処理と地図を残すことが重要である。

## 関連項目

- [知識グラフとLLMエージェントによる地理空間データ探索](../methods/intelligent-geospatial-data-discovery.md)
- [ロケーションインテリジェンス](../concepts/location-intelligence.md)

## 出典

- [Geospatial Analysis in Claude with the CARTO MCP Server](https://carto.com/blog/geospatial-analysis-claude-mcp-server/)（2026-09-09確認）
- [All of CARTO, in every agent](https://carto.com/blog/all-of-carto-in-every-agent/)（2026-09-09確認）
- [CARTO: Connect Claude](https://docs.carto.com/carto-for-agents/connect-your-platform/claude)（2026-09-09確認）
