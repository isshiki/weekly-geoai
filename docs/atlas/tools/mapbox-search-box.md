---
layout: default
title: Mapbox Search Box API
category: tools
updated: 2026-10-06
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

## 保存・料金・地域を先に確認する

Search BoxはオープンなPOI一括配布とは異なる。公式API資料は返却データを一時利用に限定し、位置データを保存する用途は営業窓口への相談を案内している。無料枠があっても、自由な蓄積・再配布が認められるという意味ではない。

`/suggest`・`/retrieve`は検索セッション単位、`/category`・`/reverse`はリクエスト単位で課金される。料金表にはプレビュー料金と標準料金が併記されているため、利用するエンドポイントと適用プランを揃えて見積もる。無料枠の数だけで継続費用を決めない。

対象地域にも注意が必要である。2026-10-06に確認したSearch Box API資料の地域欄は米国・カナダ・欧州を挙げる一方、日本向けSearch APIの別ガイドは日本語検索のPublic Betaと住所データを説明している。日本語対応の表記だけで、日本のPOIや自然言語検索の全機能が使えると判断しない。導入時には製品・エンドポイント・地域を指定して確認する。本ページではAPI呼び出しによる検証は未実施。

## 関連項目

- [Location AI](../concepts/location-ai.md)

## 出典

- [Mapbox：POIカバレッジの拡大とよりスマートな検索](https://www.mapbox.com/ja/blog/mapbox-search-box-api-expanded-poi-coverage-smarter-search)（2025-10-16公開、2026-09-23確認）

- [Mapbox：Introducing Natural Language Queries in the Mapbox Search Box API](https://www.mapbox.com/blog/introducing-natural-language-queries-in-the-mapbox-search-box-api)（2026-09-15公開、2026-09-16確認）

- [Search Box API：制限・課金・地域](https://docs.mapbox.com/api/search/search-box/)（2026-10-06確認）
- [Mapbox料金表](https://www.mapbox.com/pricing)（2026-10-06確認）
- [日本向けSearch APIの注意点](https://docs.mapbox.com/help/troubleshooting/japan-specific-considerations-search-api/)（2026-10-06確認。Search Boxの全機能の日本対応を確認したものではない）
