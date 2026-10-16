---
title: 移動する地物のリアルタイム描画
category: methods
updated: 2026-10-16
---

# 移動する地物のリアルタイム描画

車両や船などの位置を地図上で更新するときは、データの到着頻度と画面の描画負荷を分けて考える。位置情報を受け取れる速さが、そのまま画面に表示できる速さとは限らない。

## 更新ごとの仕事を減らす

EsriのArcGIS Maps SDK for Qtの検証は、次の工夫を示している。

| 工夫 | 減らす仕事 |
| --- | --- |
| 表示オブジェクトとレンダラーを再利用 | 更新のたびの作り直し |
| 固定IDで対象を直接探す | 全件を順に探す処理 |
| 表示側と座標系を合わせる | 更新のたびの座標変換 |
| 必要な位置・属性だけ更新 | 変化しない情報の再処理 |
| データ準備を別スレッドで行い、制御した単位で受け渡す | 画面操作の停止と処理待ちの蓄積 |

## ベンチマークの範囲

2026年10月15日の記事は、1万個の移動シンボルへ毎秒最大約80万回の位置更新を適用したと報告する。方向や描画に影響する属性は固定したピーク値であり、80万フレーム／秒という意味ではない。

環境はWindows 11、Core i7-14700、32GB RAM、NVIDIA T1000 8GB、Qt 6.10.0、ArcGIS Maps SDK for Qt 300.0。属性変更・シンボル・ハードウェアなどで負荷は変わる。他SDKや自分のアプリでの性能保証ではなく、本Atlasでも再計測していない。

Graphics Overlaysの検証であり、過去の観測や軌跡を扱うDynamic Entitiesとは目的に応じて選ぶ。実装にはSDKと対応する開発環境が必要である。

## 次に読む

- [分析結果の検証と適用範囲](spatial-analysis-validation.md)：地図表示の確認と分析の正しさを分ける。

## 出典

- [Esri：Real-Time Graphics Overlays in ArcGIS Maps SDKs for Native Apps](https://www.esri.com/arcgis-blog/products/developers/developers/real-time-graphics-overlays-in-arcgis-maps-sdks-for-native-apps-benchmark-and-tips)（2026-10-16、ブラウザーで本文確認）
