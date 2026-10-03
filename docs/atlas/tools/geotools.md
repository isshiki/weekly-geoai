---
layout: default
title: GeoTools
category: tools
updated: 2026-10-03
---

# GeoTools

GeoToolsを使うJavaデスクトップ地図の実装例として、GeoPackageを読み取り専用で表示するSwingアプリのひな形が公開されている。

## GeoPackage表示の実装例

2026年10月2日のQiita記事は、Java 17以上・GeoTools 35.1を使い、GeoPackageを地理院タイルへ重ねる。座標系を確認して表示用にEPSG:3857へ変換し、元ファイルには書き戻さない。移動・拡大縮小・レイヤー切り替え・属性表を備える。背景タイル取得にはネット接続を使う。

| 対象 | このひな形の上限 |
| --- | --- |
| ファイル | 200 MiB |
| 全レイヤーの地物 | 合計100,000件 |
| 頂点 | 合計3,000,000点 |
| 属性表 | 各レイヤーの先頭200件 |

これらはGeoTools自体の上限ではなく、メモリに地物を保持するひな形の制約である。著者は自動テスト25件成功と報告する一方、実機GUIテストはスキップし、Windows／WSLgの画面操作は未確認と明記する。今回も配布コードは実行していない。

## 出典

- [JavaとGeoToolsで、GeoPackageを表示する地図アプリのひな形を作ってみた](https://qiita.com/rino_yume/items/bbbbd4f2b23fc23bd44f)（2026-10-03確認）
