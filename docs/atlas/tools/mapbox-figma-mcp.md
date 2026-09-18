---
layout: default
title: Mapbox Figma MCP Server
category: tools
updated: 2026-09-18
---

# Mapbox Figma MCP Server

Mapbox Figma MCP Serverは、Figmaから実際の地図、地点、ルート、到達圏や地図デザインの支援機能を呼び出す接続サービスである。2026年9月18日に確認した文書の版はv0.1.0である。

## 利用環境と権限

Figmaの有料プラン、対象ファイルへの編集権限、Mapboxアカウントが必要である。Full seatでは任意のファイル、View・Dev・Collab seatではDrafts内で利用する。

| ツール区分 | 範囲 |
| --- | --- |
| Read：18個 | 地図生成、場所検索、経路計算、デザイン助言など。Mapboxアカウントの内容を変更しない |
| Write：1個 | `manage_style_tool`で地図スタイルを作成・変更・削除する。既定では無効 |

Design、Make、FigJam、Slidesから利用できる。地図や経路の生成と、アカウント上のスタイル変更は権限を分けて扱う。公開日の記載は確認できていない。

## 出典

- [Mapbox Figma MCP Server](https://docs.mapbox.com/location-ai/mcp-servers/figma-mcp-server/)（2026-09-18確認、公開日不明）
