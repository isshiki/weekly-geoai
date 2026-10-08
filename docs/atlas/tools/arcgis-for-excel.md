---
layout: default
title: ArcGIS for ExcelとPython in Excel
category: tools
updated: 2026-10-08
---

# ArcGIS for ExcelとPython in Excel

ArcGIS for Excelは、Microsoft Excelへ地図とArcGISサービスの機能を加えるアドインである。Python in Excelは、セルからPythonで表を分析するMicrosoftの機能で、両者を組み合わせて場所ごとの属性と分析結果を同じ表・地図で確認できる。

## 役割と利用の前提

| 構成 | 役割・確認点 |
| --- | --- |
| ArcGIS for Excel | 地点を地図化し、地域属性を付加する。使うサービスのアカウント・権限・利用条件を確認する |
| Python in Excel | Microsoftのクラウドで分析する。対応するExcel環境が必要で、コードの記述を伴う |
| 表と地図の連携 | 表の絞り込みに応じて地図上の対象も変わる |

Esriの2026年10月6日の記事では、Python in Excelは固定のライブラリ構成で、追加パッケージを導入できず、ArcGIS API for PythonなどEsriのPythonライブラリには対応していないと説明する。

## 人口を加えて調査の優先度を考える例

記事は架空の調査30地点に、半径10マイル圏の2026年人口を付加する。リスクと人口をK-Meansで3群に分け、優先度ラベルを付けて地図で確認する。

掲載コードでは人口の対数変換と標準化を行い、リスクと人口の標準化値の合計を使って群に順位を付けている。優先度はK-Meansだけから決まるものではなく、人が選んだ指標・前処理・採点ルールにも依存する。実際の危険性や派遣の最適性を実証した結果ではない。今回は記事と掲載コードを読んだもので、Excelでの実行は未検証である。

## 次に読む

- [分析結果の検証と適用範囲](../methods/spatial-analysis-validation.md)：分析結果を意思決定へ使う前の確認を読む。
- [ArcGIS API for Python](arcgis-api-python.md)：別のPython実行環境で使うライブラリとの違いを確認する。

## 出典

- [An Introduction to Python in Excel with ArcGIS for Excel](https://www.esri.com/arcgis-blog/products/arcgis-for-excel/announcements/an-introduction-to-python-in-excel-with-arcgis-for-excel)（2026-10-06公開、2026-10-08確認）
