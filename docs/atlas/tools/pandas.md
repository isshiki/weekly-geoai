---
layout: default
title: pandas
category: tools
updated: 2026-09-19
---

# pandas

pandasはPythonで表形式データを扱うライブラリである。地理空間分析の周辺では、属性・日時・CSVなどの前処理に関係する。

## 3.0.6で確認された修正

2026年9月17日のリリースはPython 3.15への一般的な互換性を加え、次の問題を修正した。

| 処理 | 修正内容 |
| --- | --- |
| CSV読み込み | `sep=None`の区切り文字判別や`usecols`の警告・例外 |
| PyArrow型の線形補間 | 連続・末尾の欠損が残る問題と、整数型の補間値が切り捨てられる問題 |
| Copy-on-Write | 全スライス代入後の共有メモリやRangeIndexの参照追跡に起因する意図しない変更 |
| CSVのデコード失敗 | C engineのメモリリーク |

補間やコピーを含む処理では、ライブラリの版とデータ型を結果の再現条件として記録する。これは上記修正を踏まえた実務上の確認観点である。

## 出典

- [What’s new in 3.0.6 (September 17, 2026)](https://pandas.pydata.org/docs/whatsnew/v3.0.6.html)（2026-09-19確認）
