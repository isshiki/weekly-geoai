---
layout: default
title: MapLibre Native
category: tools
updated: 2026-11-27
---

# MapLibre Native

MapLibre Nativeは、モバイルなどのネイティブアプリへ地図を組み込むための描画ライブラリである。[MapLibre GL JS](maplibre-gl-js.md)がブラウザ向けであるのに対し、iOSではSwiftやObjective-Cのアプリから利用する。SDKの導入とアプリ開発環境、利用する地図データや配信サービスの準備が必要である。

## iOSでの移行と独自レイヤー

2026年10月28日公開のiOS v7.0.0では、最低対応OSがiOS 15.5になった。Objective-Cでは統合ヘッダーの`Mapbox.h`を`MapLibre.h`へ変更する。Swiftの`import MapLibre`は変更不要である。この変更をWeb向けGL JSの移行条件と混同しない。

実験的なCプラグインAPIは独自のスタイルレイヤー型を追加するための仕組みである。通常版とは別のSwiftパッケージ`maplibre-ios-with-plugin-api`に含まれ、そのMapLibre製品を通常版の代わりに使う。単に既存レイヤーの色を変える設定とは異なり、ネイティブコードで描画機能を拡張する用途である。実験段階のAPIとして扱う。

## 描画と確認点

`global-state`や色の補間式`interpolate-lab`・`interpolate-hcl`、描画済み地物の情報取得が追加された。多数の画像を使うスタイルの処理も改善され、線のパターン画像が約1.7倍に描画される問題やオフラインDBの不具合が修正された。

既存アプリでは対象OS、ヘッダー、地図の見た目、オフラインデータの操作を確認する。ここでは公式リリースノートを確認しており、iOSでのビルドや性能測定は行っていない。

## macOS版を更新するとき

MapLibre NativeにはmacOS向けの配布もある。OS別のリリース番号は別々に管理されるため、iOS版やWeb向けGL JSと同じ番号でも変更内容が同じとは限らない。

macOS v7.0.0では、Objective-Cで読み込む統合ヘッダーが`Mapbox.h`から`MapLibre.h`に変わる。Swiftの`import MapLibre`はそのままでよい。また、動的フレームワークから`MLNPluginStyleLayer`と`MLNBackendResource`が公開される。

リリース本文が空欄のため、同じリリースタグに固定したmacOSのCHANGELOGの`main`節を確認した。最新ブランチの未リリース変更とは区別して参照している。macOSでのビルド・描画確認は未実施。

## ポリゴンの見た目と端末内のメモリ

Android v13.8.0とiOS v7.1.0では、`fill-rounded-corner-distance`で塗りつぶしポリゴンの角を丸められる。見た目の調整には便利だが、この処理ではメモリ使用量が最大約2倍になる場合がある。GPUへ転送した頂点・インデックスのCPU側コピーを解放する改善とは、別の条件として読む。

iOSの`MLNSource.isVolatile`は通常のディスクタイルキャッシュへの保存を抑える指定であり、通信先やアプリ全体でデータが一切保存されないという保証ではない。Androidでは位置表示用のクラスが公開され、独自の位置マーカーを扱いやすくなった。

| 系列・公開日 | 主な変更 | 確認範囲 |
|---|---|---|
| Android 13.8.0・2026-11-26 | 角丸ポリゴン、位置表示クラス、CPUバッファ解放 | 公式本文。実機試験なし |
| iOS 7.1.0・2026-11-25 UTC（日本時間26日） | 角丸ポリゴン、揮発性ソース、CPUバッファ解放 | 公式本文。実機試験なし |

この表は確認した重要更新の抜粋で、全リリースの履歴ではない。

## 次に読む

- [MapLibre GL JS](maplibre-gl-js.md)：Web版との用途の違いを確認する。

## 出典

- [MapLibre Native iOS v7.0.0](https://github.com/maplibre/maplibre-native/releases/tag/ios-v7.0.0)（2026-10-29確認）
- [macOS v7.0.0のCHANGELOG](https://github.com/maplibre/maplibre-native/blob/macos-v7.0.0/platform/macos/CHANGELOG.md)／[リリース](https://github.com/maplibre/maplibre-native/releases/tag/macos-v7.0.0)（2026-11-20確認）
- [Android v13.8.0](https://github.com/maplibre/maplibre-native/releases/tag/android-v13.8.0)／[iOS v7.1.0](https://github.com/maplibre/maplibre-native/releases/tag/ios-v7.1.0)（2026-11-27確認）
