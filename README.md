# GeoAIアトラス

地図・位置情報データ×AIの知見を、体系的に整理するためのナレッジサイトである。

- [GeoAIアトラス](https://isshiki.github.io/weekly-geoai/)
- [知識マップ](https://isshiki.github.io/weekly-geoai/atlas/)
- [初めてのGeoAI](https://isshiki.github.io/weekly-geoai/atlas/guides/getting-started/)
- [POIデータを選び、分析する](https://isshiki.github.io/weekly-geoai/atlas/guides/poi-workflow/)
- [週刊GeoAI バックナンバー](https://weeklygeoai.substack.com/archive)

## このリポジトリについて

このリポジトリでは、GeoAIに関する技術、データ、ツール、活用事例などを、長く参照できる形で整理していく。あわせて、ニュースレター「週刊GeoAI」の制作に使用する。

GeoAIアトラスはMaterial for MkDocsで構築し、階層ナビゲーションと全文検索を備えたWiki形式で公開する。

目的別の読む順序と、概念・手法・データ・ツール・事例の索引から内容を探せる。日次の情報追加に加え、毎月第1月曜日に分類・説明・情報の鮮度を見直す。運用は[月次整理](OPERATIONS.md#atlas-monthly)を参照する。

## 学習の入口

読む順序と到達点は[初心者向け3ルート](https://isshiki.github.io/weekly-geoai/atlas/guides/getting-started/#learning-routes)にまとめている。

| ルート | 学ぶこと |
| --- | --- |
| [基礎理解](https://isshiki.github.io/weekly-geoai/atlas/guides/getting-started/#route-foundations) | GeoAIの全体像、データ表現、座標、手法選択 |
| [データ分析](https://isshiki.github.io/weekly-geoai/atlas/guides/getting-started/#route-analysis) | 4店舗・16画素の演習で集計と評価を確認 |
| [AI操作](https://isshiki.github.io/weekly-geoai/atlas/guides/getting-started/#route-agent) | 条件・権限・成果物・検証を依頼文へ整理 |

## 週刊GeoAI

「週刊GeoAI」は、GIS・位置情報の仕事をしていて、AI・機械学習側の動きを短時間で追いたい人のための日本語ニュースレターである。1週間分のニュース・論文・事例を、毎週金曜にSubstackで配信する。

週刊GeoAIのバックナンバーはSubstackで公開する。

## 運営者向け情報

基礎解説の整備状況と次の優先課題は[Atlasの点検・整備計画](editorial/atlas-roadmap.md)にまとめる。

継続保守には[全ページの確認台帳](editorial/atlas-review-register.md)と[調査との対応表](editorial/atlas-research-crosswalk.md)を使う。原調査9本の再照合と実データ比較は、毎月の必須作業とは分けて管理する。

公開前には `scripts/check_site_links.py` で生成HTMLの内部リンク・アンカー・画像参照と更新履歴のハイライトを検査する。GitHub Actionsでも実行する。範囲と実行方法は[運用手順](OPERATIONS.md#リンクとハイライトの検査)を参照。過去のハイライトを修正する際は、元の更新記録を保ち、現行の対応箇所への案内であることを明記する。

日次メモ、週次原稿、Substack用HTML、GitHub Pagesへの公開手順は[OPERATIONS.md](./OPERATIONS.md)にまとめている。

調査9本の原文はGit対象外の `local-research/2026-10-06/` に保管。[受領台帳](editorial/atlas-research-manifest.json)と[共通点・食い違い](editorial/atlas-research-findings.md)はリポジトリで管理する。ローカル原文はpushに含まれない。

Atlasは概念・選択基準・注意点を中心に保守する。新しいプログラミング演習は追加せず、具体的な実装は既存の実践記事や公式資料へ案内する。
