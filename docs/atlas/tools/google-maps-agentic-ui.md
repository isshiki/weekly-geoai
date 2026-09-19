---
layout: default
title: Google Maps Agentic UI Toolkit
category: tools
updated: 2026-09-19
---

# Google Maps Agentic UI Toolkit

Google Maps Agentic UI Toolkitは、会話型AIの回答に場所情報を表示するためのシステム指示とUIコンポーネントを提供するツールキットである。

## 意図と表示の対応

LLMがユーザーの意図を解釈し、ツール定義に沿ったパラメーターを渡す。Web・Android・iOS向けに次の表示を提供する。

| 表示 | 主な用途 |
| --- | --- |
| プレイスカード | 特定の場所の情報確認 |
| インラインマップ | 地点や範囲の位置確認 |
| 地図とルート | 旅程や移動経路のプレビュー |
| 画像を含む地図表示 | 場所の雰囲気や詳細の確認 |

## 利用条件

- Gemini・OpenAI・Anthropicなど、LLMに依存しない設計とされる。公式の開始手順ではGeminiとGoogle Maps PlatformのAPIキーを使う。
- 2026年9月19日の確認時点では試験運用版（pre-GA）である。ツールキット自体は試験運用中無料だが、呼び出すMapsサービスは課金対象になり得る。
- 結果に含まれるGoogleマップの情報源を、生成コンテンツの直後から1回の操作で確認できるように表示する必要がある。

## 出典

- [Google マップ エージェント型 UI ツールキット（試験運用版）](https://developers.google.com/maps/ai/agentic-ui-toolkit?hl=ja)（2026-09-19確認）
