---
layout: default
title: MCP for ArcGIS Location Services
category: tools
updated: 2026-09-17
---

# MCP for ArcGIS Location Services

MCP for ArcGIS Location Servicesは、AIアプリケーションからArcGISの位置情報サービスを呼び出すためのMCPサーバーである。確認した記事ではパブリックベータとして案内されている。

## 提供するツール

住所検索、逆ジオコーディング、経路計算、標高取得、地図画像生成、場所の説明などを扱う。利用にはArcGIS Location Platformのアカウントとベータへのアクセスが必要である。

## 複数サービスを組み合わせる例

記事は、国土交通データプラットフォームから避難所を取得し、ArcGISで徒歩経路と標高を調べる例を示している。筆者の試行では、ArcGISのMCPを使わない場合は直線距離からの概算となり、使用時は道路に沿う解析が可能になった。一方、一部の距離をマイルからメートルへ修正する作業が必要だった。

この試行は個別の利用例であり、一般的な性能評価や避難経路の安全性を保証する検証ではない。公開日は取得できた本文から確認できていない。

## 出典

- [MCP for ArcGIS Location Services からはじめるエージェンティック AI 体験](https://community.esri.com/ja/discussion/1720846/)（2026-09-17確認）
