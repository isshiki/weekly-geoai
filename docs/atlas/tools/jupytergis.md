---
title: JupyterGIS
category: tools
updated: 2026-11-10
---

# JupyterGIS

JupyterGISは、ブラウザで地図を作成・共同編集するOSSのGISである。Jupyterを基盤とし、NotebookでのPython分析と地図の確認をつなぐ。研究・授業で同じ地図に注釈を付けたり、分析結果をチームで確認したりする場面に向く。BSD 3-Clauseで公開されている。

## 体験版と共同作業の環境を分ける

| 環境 | できること・必要な準備 |
| --- | --- |
| JupyterLite体験版 | インストールなしでブラウザ内実行。共同編集とQGISプロジェクト入出力は非対応 |
| JupyterLab／JupyterHub等への導入 | サーバー側の構成を用意し、共同編集・コメントやQGISプロジェクト入出力を利用する |

Liteは通常版の完全な代替ではない。残したいファイルはダウンロードする。リモートデータのCORS制約、ブラウザのメモリ、Pythonパッケージの制限もあり、STAC検索は体験版では結果を返さないと公式文書が説明している。

## 地図と分析を行き来する

GeoJSON・GeoTIFF/COG・GeoParquet・GeoPackageなどを扱い、ストーリーマップ、陰影図、ヒートマップを作れる。Python APIに加え、Jupyter AI等との連携による自然言語操作も案内されている。AIは操作を補助する入口で、集計や座標系の正しさを保証するものではない。

2026年11月10日のPyPI確認では、コア拡張`jupytergis-core`は0.18.0（11月6日配布）、Python 3.12以上を要求する。コアパッケージと、公式が導入方法を案内する`jupytergis`全体を混同しない。QGISプロジェクトの完全な再現性やAI接続は、このAtlasでは実操作していない。

## 次に読む

- [Felt](felt.md)：Web地図の共有・業務利用の別の選択肢。
- [分析結果の検証](../methods/spatial-analysis-validation.md)：地図や処理が完成した後に確かめること。

## 出典と確認範囲

2026-11-10に以下を確認。新規公開ニュースではなく、既存プロジェクトの紹介として収録した。

- [公式README](https://github.com/geojupyter/jupytergis)
- [公式ドキュメント](https://jupytergis.readthedocs.io/en/latest/)
- [Lite体験版の制約](https://jupytergis.readthedocs.io/en/latest/user_guide/explanation/jupyter-lite-limitations.html)
- [PyPI配布情報](https://pypi.org/project/jupytergis-core/)（公式JSON APIでも版・Python要件・配布日を確認）
