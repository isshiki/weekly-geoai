---
layout: default
title: Google Maps Platformの3D地図・場所UI・スタイル
category: tools
updated: 2026-10-30
---

# Google Maps Platformの3D地図・場所UI・スタイル

Google Maps PlatformのSDKやUI部品を使うと、自分のWeb・モバイルアプリへ3D地図、場所の詳細、状況に応じた地図表現を組み込める。完成したGoogleマップアプリの機能とは分けて読む。対象SDKを組み込む開発環境を用意し、サービスごとの利用条件・料金を確認する。

## 何を組み込めるか

2026年10月27日の公式発表を2026-10-30に確認した。

| 機能 | 用途・提供段階 |
| --- | --- |
| Maps 3D SDK（Android・iOS） | ネイティブアプリの3D地図。一般提供、Kotlin・SwiftUI対応 |
| Places UI Kit Pro（iOS） | 場所の情報や独自の操作ボタン。一般提供 |
| 人気の時間帯・現在の混雑 | iOSのPlaces UI Kitで提供。Essentialsでも利用可能 |
| Contextual Styling | 再読み込みせずテーマや地物の強調を変更。一般提供 |
| AI StudioのImmersive area tours | 会話を使う3Dツアー試作のアプレット |

## AIで作る機能とAIへ見せる部品

AI Studioでアプリを試作すること、アプリへ場所のUIを組み込むこと、GIS分析をAIに任せることは別の機能である。[Agentic UI Toolkit](google-maps-agentic-ui.md)の提供段階も、このSDKやUI Kitの一般提供から推定しない。

現地の混雑情報には提供される場所や項目の違いがある。今回、SDKの実装やアプレットの動作は検証していない。

## 出典

- [Google：3D SDK・Places UI Kit・スタイルの更新](https://mapsplatform.google.com/resources/blog/drive-confident-place-decisions-with-immersive-maps-live-crowd-signals-and-responsive-map-styling/)（2026-10-30確認）
