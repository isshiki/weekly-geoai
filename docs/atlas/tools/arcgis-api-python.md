---
layout: default
title: ArcGIS API for Python
category: tools
updated: 2026-09-26
---

# ArcGIS API for Python

ArcGIS API for Pythonは、PythonからArcGISの地理情報や組織内コンテンツを操作するライブラリである。地理処理だけでなく、コンテンツの移行・管理を自動化する用途も持つ。

## 2.4.4で確認した管理機能

公式リリースノートでは、オフライン出力に対応するアイテム構造の拡張と非同期処理、依存関係グラフ生成のパラメーター追加、ArcGIS Video Serverの管理モジュール、StoryMapsの内容確認メソッドを案内している。

アイテム間の関係を調べるAPIは、すべての種類・関係を必ず返すとは限らない。移行や削除の影響を確認する際は、依存関係の取得結果と実際のアプリ・地図の参照先を照合する。

共有されたブログ本文は今回取得できなかったため、Rust製のarcgis_geometryや98％のアイテム種別への対応という説明は未確認である。版の日付は公式製品ページでは2026年9月22日とされており、ブログ公開日とは区別する。

## 関連項目

- [外部地図サービスの廃止と依存関係の点検](../methods/map-service-lifecycle.md)

## 出典

- [Esri Developer：What's new in version 2.4.4](https://developers.arcgis.com/python/latest/guide/release-notes-244/)（2026-09-26確認）
- [Esri Developer：Managing your content](https://developers.arcgis.com/python/latest/guide/managing-your-content/)（2026-09-26確認）
- [Esri Developer：ArcGIS API for Python](https://developers.arcgis.com/python/latest/)（2026-09-26確認）
