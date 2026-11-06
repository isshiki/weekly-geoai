---
layout: default
title: Google Maps Platformの3D地図・場所UI・スタイル
category: tools
updated: 2026-11-06
---

# Google Maps Platformの3D地図・場所UI・スタイル

Google Maps PlatformのSDKやUI部品を使うと、自分のWeb・モバイルアプリへ3D地図、場所の詳細、状況に応じた地図表現を組み込める。完成したGoogleマップアプリの機能とは分けて読む。対象SDKを組み込む開発環境を用意し、サービスごとの利用条件・料金を確認する。

## ナビ中の通信断に備える

Navigation SDK for Android 8.1.0は、ナビ中に経路沿いの地図を自動先読みする。配送などの移動中に通信が途切れても、取得済みの経路沿いで地図表示と再探索を続けられる。先読みする範囲とタイミングがあるため、任意の地域をいつでもオフライン検索できると解釈しない。

Routes APIで決めた経路は、ルートトークンだけを渡して目的地を設定できる。経由地や移動手段を二重に指定する手間が減り、実際に採用された経路設定も確認できる。従来のCustomRoutesOptionsを使う指定方法は非推奨となった。[公式リリースノート](https://developers.google.com/maps/documentation/navigation/android-sdk/release-notes#November_04_2026)（11月4日公開、2026年11月7日確認。SDK動作は未検証）


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

11月4日の更新で、施設詳細に普段の時間帯別の混み具合を表示できるようになった。現在の混雑も情報がある場合に表示する。普段の傾向と今の観測を読み分けたい。 [Maps JavaScript API 3.66.13d：施設詳細に混雑状況を表示](https://developers.google.com/maps/documentation/javascript/releases?hl=ja#2026-11-04)（2026年11月5日確認）

## 出典

- [Google：3D SDK・Places UI Kit・スタイルの更新](https://mapsplatform.google.com/resources/blog/drive-confident-place-decisions-with-immersive-maps-live-crowd-signals-and-responsive-map-styling/)（2026-10-30確認）
