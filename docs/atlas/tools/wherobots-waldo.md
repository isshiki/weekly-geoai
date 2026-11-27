---
layout: default
title: Wherobots Waldo
category: tools
updated: 2026-11-27
---

# Wherobots Waldo

Waldoは、商用クラウドWherobots上で、自然言語から空間データの探索・加工・地図表示などを進めるAIエージェントである。2026年11月18日の公式発表時点ではパブリックプレビュー。利用アカウント、対象データへの接続権限、クラウドの利用条件の確認が必要になる。

## 使いどころ

複数のデータから調査対象地域を抽出し、地図で結果を確認して、同じ処理を定期実行する用途を想定する。公式発表はHavasu Catalogによるデータ探索、WherobotsDBの空間処理、RasterFlowによる画像処理、地図表示、外部基盤への出力を組み合わせる構成を紹介している。

単に場所を検索する対話地図よりも、分析用データの処理と継続的な運用に軸足がある。Apache SedonaなどのOSSを手元で使うことと、Waldoというクラウドサービスの利用は区別する。

## 導入前に確認すること

- 公開・非公開データの接続権限と、AIへ渡す情報の範囲。
- エージェントの利用枠と、実際のクラウド処理・保存などの費用。
- 生成された処理、結果の件数・位置、定期実行の条件。

公式発表の顧客コメントや速度改善は、独立した比較試験ではない。ここでは発表を確認し、接続・処理精度・料金の実測は行っていない。

## 次に読む

- [GIS Data Agent](gis-data-agent.md)：組織データを扱う別のエージェント構成。
- [空間分析の検証](../methods/spatial-analysis-validation.md)：処理成功と結果の妥当性を区別する。

## 出典

- [Wherobots公式発表](https://wherobots.com/press/wherobots-announces-waldo/)（2026-11-27本文確認）
- [SiliconANGLEの紹介](https://siliconangle.com/2026/11/18/exclusive-wherobots-ai-agents-automate-complex-spatial-data-engineering/)（2026-11-27本文確認）
