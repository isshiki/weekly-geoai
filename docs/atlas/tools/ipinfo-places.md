---
layout: default
title: IPinfo Places
category: tools
updated: 2026-09-23
---

# IPinfo Places

IPinfo Placesは、IPアドレスに空港、ホテル、競技場などの施設情報を付けるデータ製品である。IPinfoが2026年9月21日に発表した。

## 何を対応付けるか

| 項目 | 発表時の説明 |
| --- | --- |
| 対象 | 236カ国、57施設カテゴリの約270万IPアドレス |
| 属性 | 施設名・カテゴリ、SSID、建物レベルの座標など |
| 提供 | APIとデータベースのダウンロード。有料プランに含まれ、詳細度はプラン別 |

約270万は施設数でも人数でもない。公共Wi-Fiでは多くの端末が同じIPアドレスを共有するため、IPを一人や一世帯とみなすと広告の頻度制御や到達人数推計を誤る。発表では施設の文脈を加えてこれらの処理を調整する用途を挙げている。

## 読み方と限界

IPと施設の対応は、個々の利用者の正確な位置や来訪を保証するものではない。建物レベルの座標という属性の粒度と、対応付けの正確さを区別する。実際の網羅率・更新頻度・精度は本ページでは検証していない。

オープンなPOIデータセットの公開ではなく商用データの提供である。既存の通信情報へ場所の文脈を追加する場合も、利用目的や保存期間、利用者への説明を検討する。

## 関連項目

- [位置情報データのプライバシー保護](../methods/location-data-privacy.md)
- [人流データの種類と加工段階](../data/human-flow-data-types.md)

## 出典

- [IPinfoの発表（Business Wire）](https://www.businesswire.com/news/home/20260921958712/en/IPinfo-Launches-Places-Bringing-Venue-Level-Context-to-IP-Address-Data)（2026-09-21公開、2026-09-23確認）
