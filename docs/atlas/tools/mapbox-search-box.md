---
layout: default
title: Mapbox Search Box API
category: tools
updated: 2026-09-23
---

# Mapbox Search Box API

Mapbox Search Box APIは、場所やPOIを検索するAPIである。2026年9月15日に自然言語の複数条件検索がPublic Previewとして発表された。

## 自然言語検索の適用範囲

| エンドポイント | 今回の機能 |
| --- | --- |
| `/forward` | 場所名、カテゴリ、地域、対応する設備・営業時間などをまとめて解釈する |
| `/suggest`・`/retrieve` | 入力途中の候補提示と取得向けで、今回の複数条件解釈は適用されない |

`/forward`には自動適用され、別の機能スイッチやリクエスト・レスポンス形式の変更は不要と案内されている。例えばWi-Fi、営業中、近接性を含む場所検索を1リクエストで扱う。

AIアシスタントの背後で、会話から得た場所検索を構造化されたPOI結果へ変換する役割を持つ。ただし、主観的な条件、未対応の属性、場所検索を超える推論は、引き続きアプリ側やAIモデルの処理が必要になり得る。記事の例だけで日本語・全地域・全属性の対応を確認したものではない。

## 2025年のカバレッジ拡張との関係

2025年10月16日の公式記事は、カテゴリ検索や多言語対応、住所・POIのカバレッジ拡張を扱う。Geocoding APIの住所検索と、Search Box APIのPOI・カテゴリ・ブランド検索を使い分ける説明である。

同記事のオフライン検索はモバイル向けSearch SDKの機能として紹介されており、Web APIが通信なしで応答するという意味ではない。また、検索APIへのアクセスはPOIデータセット全体の取得・再配布とは区別する。

この記事で将来計画とされた複合クエリと、本ページで別に扱う2026年9月の自然言語検索Public Previewは時点が異なる。2025年の件数や改善率を現在値として引用しない。

## 関連項目

- [Location AI](../concepts/location-ai.md)

## 出典

- [Mapbox：POIカバレッジの拡大とよりスマートな検索](https://www.mapbox.com/ja/blog/mapbox-search-box-api-expanded-poi-coverage-smarter-search)（2025-10-16公開、2026-09-23確認）

- [Mapbox：Introducing Natural Language Queries in the Mapbox Search Box API](https://www.mapbox.com/blog/introducing-natural-language-queries-in-the-mapbox-search-box-api)（2026-09-15公開、2026-09-16確認）
