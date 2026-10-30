---
layout: default
title: ArcGIS API for Python
category: tools
updated: 2026-10-30
---

# ArcGIS API for Python

ArcGIS API for Pythonは、PythonからArcGISの地理情報や組織内コンテンツを操作するライブラリである。地理処理だけでなく、コンテンツの移行・管理を自動化する用途も持つ。

## 2.4.4で確認した管理機能

公式リリースノートでは、オフライン出力に対応するアイテム構造の拡張と非同期処理、依存関係グラフ生成のパラメーター追加、ArcGIS Video Serverの管理モジュール、StoryMapsの内容確認メソッドを案内している。

アイテム間の関係を調べるAPIは、すべての種類・関係を必ず返すとは限らない。移行や削除の影響を確認する際は、依存関係の取得結果と実際のアプリ・地図の参照先を照合する。

2026-10-30にESRIジャパンの10月29日記事を確認し、以前保留していたRust製arcgis_geometryと約98%のアイテムタイプへのオフライン複製対応を補足した。98%は処理成功率ではなく、対応するアイテムタイプの割合として読む。版の公開日は9月22日（日本時間23日）で、今回の記事公開日とは異なる。

## 関連項目

- [外部地図サービスの廃止と依存関係の点検](../methods/map-service-lifecycle.md)

## AI機能と実行環境

文書分析、画像内の文字抽出、音声文字起こし・音声生成はArcGIS Onlineでベータ提供と説明されている。Enterprise 12.2での対応予定と区別する。Rust基盤による性能向上は開発元の説明であり、本Atlasでは処理時間や移行互換性の試験はしていない。

## 出典

- [Esri Developer：What's new in version 2.4.4](https://developers.arcgis.com/python/latest/guide/release-notes-244/)（2026-09-26確認）
- [Esri Developer：Managing your content](https://developers.arcgis.com/python/latest/guide/managing-your-content/)（2026-09-26確認）
- [Esri Developer：ArcGIS API for Python](https://developers.arcgis.com/python/latest/)（2026-09-26確認）

- [ESRIジャパン：2.4.4日本語解説](https://blog.esrij.com/archives/72699)（2026-10-30確認）
