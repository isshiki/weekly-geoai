---
layout: default
title: Mapbox CLI
category: tools
updated: 2026-10-10
---

# Mapbox CLI

Mapbox CLIは、端末からMapboxの地図・検索などのAPIを操作するコマンドラインツールである。人だけでなくAIエージェントが操作しやすい入出力を備える。実際のAPI利用には、Mapboxのアカウントや適切な権限のアクセストークンなどが必要になる。

## AIが操作を組み立てるための仕組み

| 仕組み | 役割 |
| --- | --- |
| JSON出力 | 結果をプログラムが読み取れる形式で返す |
| `--schema` | 引数の型・必須項目などを、インストール済みコマンドの定義から取得する。この取得自体に認証やAPI通信は不要 |
| `--dry-run` | 変更操作の入力を検証し、トークンを伏せた送信予定内容を表示する。APIには送信しない |
| 構造化エラー | エラーコードと修正案、次に取れる操作を返す |

例えば、AIが地図スタイルを変更するときに、入力仕様の確認、送信前の点検、失敗時の修正を別々の段階として扱える。ただし、事前検証だけで地図の内容や業務判断の正しさまで保証されるわけではない。

## 利用条件と確認範囲

CLIのMITライセンスと、接続先APIや取得データの利用条件は別である。CLIの公開を、POIデータのオープン化やAPIの無制限な無料提供とは解釈しない。本ページは公式説明の確認であり、インストールやAPI操作は試していない。

## 次に読む

- [Mapbox Figma MCP Server](mapbox-figma-mcp.md)：デザイン作業から地図を扱う別の連携方法を見る。
- [分析結果の検証と適用範囲](../methods/spatial-analysis-validation.md)：操作が成功した後に、結果の妥当性を確かめる。

## 出典

- [New Mapbox CLI for coding agents](https://www.mapbox.com/blog/new-mapbox-cli-for-coding-agents)（2026-10-10確認）
