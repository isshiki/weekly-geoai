# GeoAIアトラス

地図・位置情報データ×AIの知見を、体系的に整理するためのナレッジサイトである。

- [GeoAIアトラス](https://isshiki.github.io/weekly-geoai/)
- [知識マップ](https://isshiki.github.io/weekly-geoai/atlas/)
- [初めてのGeoAI](https://isshiki.github.io/weekly-geoai/atlas/guides/getting-started/)
- [POIデータを選び、分析する](https://isshiki.github.io/weekly-geoai/atlas/guides/poi-workflow/)
- [週刊GeoAI バックナンバー](https://weeklygeoai.substack.com/archive)

## 最優先：誰に届けるか

**AIをきっかけに、仕事や暮らしで地図・地域データを使い始めたい人へ。** プログラミングやGISの経験は必須にしない。次回以降の選定・執筆・Atlas整備では、[読者と編集方針の正本](editorial/audience-and-positioning.md)を最初に参照する。

[2026-10-31の決定・保留事項](editorial/decisions/2026-10-31-audience.md)に、議論の採用・修正・検討案を記録している。

## このリポジトリについて

このリポジトリでは、GeoAIに関する技術、データ、ツール、活用事例などを、長く参照できる形で整理していく。あわせて、ニュースレター「週刊GeoAI」の制作に使用する。

GeoAIアトラスはMaterial for MkDocsで構築し、階層ナビゲーションと全文検索を備えたWiki形式で公開する。

目的別の読む順序と、概念・手法・データ・ツール・事例の索引から内容を探せる。日次の情報追加に加え、毎月第1月曜日に分類・説明・情報の鮮度を見直す。運用は[月次整理](OPERATIONS.md#atlas-monthly)を参照する。

DuckDB・Polars・MapLibre GL JS・GeoLibre・GeoPandas・Shapelyの[重要な更新履歴](https://isshiki.github.io/weekly-geoai/atlas/#library-history)では、現在の機能と導入バージョン、実験対応・互換性の注意を分けて追える。日次取り込み時に重要な変更を更新し、月次に整理する。全修正版の網羅は行わない。編集方法は[ライブラリ更新履歴の保守](editorial/library-release-history.md)を参照する。

## 学習の入口

読む順序と到達点は[初心者向け3ルート](https://isshiki.github.io/weekly-geoai/atlas/guides/getting-started/#learning-routes)にまとめている。

| ルート | 学ぶこと |
| --- | --- |
| [基礎理解](https://isshiki.github.io/weekly-geoai/atlas/guides/getting-started/#route-foundations) | GeoAIの全体像、データ表現、座標、手法選択 |
| [データ分析](https://isshiki.github.io/weekly-geoai/atlas/guides/getting-started/#route-analysis) | 4店舗・16画素の演習で集計と評価を確認 |
| [AI操作](https://isshiki.github.io/weekly-geoai/atlas/guides/getting-started/#route-agent) | 条件・権限・成果物・検証を依頼文へ整理 |

## 週刊GeoAI

**週刊GeoAI — AIで地図・地域データを使ってみたい人へ**

街・店舗・人口・移動などのデータ活用につながるニュースを、毎週金曜に厳選。新しい道具と事例、その理解を助ける小さな知識を届けます。

[編集ガイド](editorial/writing-guide.md)に沿ってニュースを選び、末尾に身近な仕事・暮らしの活用を紹介する短い初心者コラムを置く。技術解説はAtlasや原典へ分ける。クイズは検討段階で必須ではない。

日次提供時の[追加検索](editorial/developer-news-discovery.md)に加え、水曜9時に[初心者向け活用事例](editorial/beginner-usecase-discovery.md)、木曜9時に参考媒体を確認する（日本時間）。有用な新情報がない場合は通知しない。

週刊GeoAIのバックナンバーはSubstackで公開する。

2026年10月16日号から、ニュース中心の「注目3件＋短報3〜5件＋任意の地図」、図版0〜2枚を基本にする。地図・地域データを使い始める人が新しい動きを把握できる構成とし、手順解説に偏らせない。[Substack掲載手順](editorial/substack-handoff.md)に沿って本文の貼り付けと画像のアップロードを行う。

編集構成の比較用に、[ニュース中心・画像入りの試作（10月4〜10日）](drafts/trials/2026-10-10-news-pilot.md)と[ブラウザー用プレビュー](drafts/trials/2026-10-10-news-pilot.html)を用意している。[従来の開発記事中心の試作](drafts/trials/2026-10-10-developer-pilot.md)と比較できる。正式な配信原稿ではない。

## 運営者向け情報

基礎解説の整備状況と次の優先課題は[Atlasの点検・整備計画](editorial/atlas-roadmap.md)にまとめる。

継続保守には[全ページの確認台帳](editorial/atlas-review-register.md)と[調査との対応表](editorial/atlas-research-crosswalk.md)を使う。原調査9本の再照合と実データ比較は、毎月の必須作業とは分けて管理する。

公開前には `scripts/check_site_links.py` で生成HTMLの内部リンク・アンカー・画像参照と更新履歴のハイライトを検査する。GitHub Actionsでも実行する。範囲と実行方法は[運用手順](OPERATIONS.md#リンクとハイライトの検査)を参照。過去のハイライトを修正する際は、元の更新記録を保ち、現行の対応箇所への案内であることを明記する。

日次メモ、週次原稿、Substack用HTML、GitHub Pagesへの公開手順は[OPERATIONS.md](./OPERATIONS.md)にまとめている。

調査9本の原文はGit対象外の `local-research/2026-10-06/` に保管。[受領台帳](editorial/atlas-research-manifest.json)と[共通点・食い違い](editorial/atlas-research-findings.md)はリポジトリで管理する。ローカル原文はpushに含まれない。

Atlasは概念・選択基準・注意点を中心に保守する。新しいプログラミング演習は追加せず、具体的な実装は既存の実践記事や公式資料へ案内する。

## 依存関係のセキュリティ更新（2026-10-27）

サイト生成環境の `uv.lock` にある certifi を 2026.10.19 に対象更新しました。他のパッケージ版と対応Python範囲は維持しています。これはPython/MkDocsの生成環境の更新で、公開済みの静的HTMLへcertifiを配布する変更ではありません。更新済みvenvでの厳格なローカルサイトビルド（mkdocs build --strict）と依存整合性確認が成功しました。外部リンクのHTTP確認と公開反映は未実施です。

## 残るDependabot警告への対応（2026-10-27）

サイト生成環境のrequests経由のurllib3を2.8.0へ対象更新しました。既存venvで、メモリ内のgzip圧縮HTTP応答のストリーム読取、MkDocsの厳格ビルド、依存・lock整合の確認が成功しました。実際の外部HTTP通信やデータ再取得は行っていません。公開HTMLにurllib3を直接配布する変更ではありません。
