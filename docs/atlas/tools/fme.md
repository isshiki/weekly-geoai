---
layout: default
title: FME
category: tools
updated: 2026-09-29
---

# FME

FMEは、異なる形式・システム間でデータを変換・統合するプラットフォームである。地理空間データの分析・配信向けに、変換と検証を反復可能なワークフローとして組み立てられる。

## 業務データと分析用データの役割

Safe Softwareの2026年1月27日の解説は、GeoParquetを既存の編集・トランザクション処理に追加する分析用の形式として位置付ける。

| 役割 | 構成 |
| --- | --- |
| 業務側 | GeoPackage・PostGISなどで既存の編集・更新を続ける |
| 変換・検証 | 座標参照系・スキーマを揃え、形状や属性を確認する |
| 分析・共有側 | GeoParquetを生成し、必要に応じて分割してオブジェクトストレージへ配置する |

元データの変更に合わせ、オンデマンド・定期・イベント起点で処理を実行する。FME FlowはFMEで作ったワークフローの自動実行を担う。

## CNG Forumの開催前解説

2026年9月18日のPSS記事は、既存GISとクラウド環境をつなぐ視点からFMEを取り上げる。10月開催予定のイベントの予習であり、登壇後の実績報告ではない。

[Cloud Native Geospatial](../concepts/cloud-native-geospatial.md)も参照。

## 道路LOD1に向けた前処理

G空間情報センターのニュースレター第57号（2026年9月）は、アサミ情報システムによる道路LOD1の作成手順を掲載する。DMの道路縁から面を作り、交差部・橋梁部・トンネル部などで区切って属性を付ける。対象は2Dの道路面整備までで、CityGML出力は別工程である。

穴のあるポリゴンを使う道路候補の抽出は、標準で必須の方法ではなく記事の前処理例である。候補外の面も保存し、立体交差などで道路を取りこぼしていないか目視確認する。自動抽出の結果と、確認・修正を経た成果物を分ける点が参考になる。

## 出典

- [【CNG】FMEは「クラウドネイティブ地理空間」の橋渡し役になれるか - CNG Forum 2026予習](https://note.com/pacificspatial/n/n6bb98de03001)（2026-09-19確認）
- [How to migrate to GeoParquet (without disrupting existing GIS workflows)](https://fme.safe.com/blog/2026/01/how-to-migrate-to-geoparquet-without-disrupting-existing-gis-workflows/)（2026-09-19確認）
- [8 ways to automate your data with FME Flow](https://fme.safe.com/blog/2025/06/8-ways-to-automate-your-data-with-fme-flow/)（2026-09-19確認）

- [G空間情報センター ニュースレター第57号（7〜14ページ）](https://front.geospatial.jp/wp-content/uploads/2026/09/NL57.pdf)（2026-09-29確認）
