---
title: 4店舗で試す空間結合と件数の検証
category: guides
updated: 2026-10-06
---

# 4店舗で試す空間結合と件数の検証

店舗を区域ごとに数える小さな演習である。**合計件数が元の件数と一致しても、正しい集計とは限らない**ことを確かめる。入力はすべて架空で、APIキーや実在店舗のデータは不要である。

前提は[空間結合と集計の基本](../methods/spatial-join-and-aggregation.md)。コードを実行しなくても、次の表から所属を手で求められる。Python経験者は同じ例をShapelyで実行できる。

## 1. 位置を確認する

区域Aは `0 ≤ x ≤ 10, 0 ≤ y ≤ 10`、区域Bは `10 ≤ x ≤ 20, 0 ≤ y ≤ 10` の長方形である。`x = 10` の辺を共有する。座標は説明用の平面上の数値であり、経緯度でも実在する地域のCRSでもない。距離・面積の測定は行わない。

| 店舗ID | x | y | 位置 |
| --- | --- | --- | --- |
| P1 | 5 | 5 | Aの内部 |
| P2 | 15 | 5 | Bの内部 |
| P3 | 10 | 5 | AとBの共有境界 |
| P4 | 25 | 5 | A・Bの外側 |

[基礎ページの模式図](../methods/spatial-join-and-aggregation.md#boundary-example)の3点に、区域外のP4を足した構成である。

## 2. 境界の扱いを変えて数える

点を第1引数、区域を第2引数として判定する。`within`はこの点・面の例で内部のみ、`covered_by`は境界も含む。これは点と面についての説明であり、線や面同士へそのまま一般化しない。

| 確認するもの | within | covered_by |
| --- | --- | --- |
| P1の所属 | A | A |
| P2の所属 | B | B |
| P3の所属 | なし | A・B |
| P4の所属 | なし | なし |
| Aの件数 / Bの件数 | 1 / 1 | 2 / 2 |
| 対応した行数（matched_rows） | 2 | 4 |
| 対応した一意な店舗数（matched_unique_points） | 2 | 3 |
| 未所属（unmatched） | P3・P4 | P4 |
| 複数所属（multiple） | なし | P3 |

ここでいう「対応行」は一致した組だけを数える。左外部結合で未所属の行も残した表全体の行数とは異なる。

`covered_by`の区域別合計は4件で、元の4店舗と一致する。しかし、P3を二重に数え、P4を数えていない。合計だけの照合では、この相殺を見落とす。店舗IDごとの所属数も調べる必要がある。

## 3. Pythonで確かめる { #run }

[実行用コード spatial_join.py](../../assets/exercises/spatial_join.py)を保存する。リンクがコード表示になった場合は、ブラウザーの保存機能で拡張子 `.py` のファイルとして保存する。保存したフォルダーで以下を実行する。

Pythonとpipが使える場合、専用の仮想環境を作る。Windows PowerShellの例：

```powershell
python -m venv .venv-exercise
.venv-exercise/Scripts/python.exe -m pip install shapely==2.1.2
.venv-exercise/Scripts/python.exe spatial_join.py
```

macOS・Linuxでは、上の `Scripts/python.exe` を `bin/python` に置き換える。これらの環境では今回未実行である。

すでにuvを利用している場合は、コード先頭の依存関係指定を使える。

```sh
uv run --no-project spatial_join.py
```

依存パッケージの初回取得にはインターネット接続が必要である。演習実行時は外部データを取得せず、ファイルも書き換えない。

出力はJSON形式で、Python・Shapely・GEOSの版、上表に対応する集計値、最後に `"check": "PASS"` を表示する。組み込んだ正解表との一致と、所属済み一意件数＋未所属件数＝入力件数を検査する。PASSはこの架空例の確認結果であり、実データ全体の品質保証ではない。

## 4. 結果をどう扱うか

「P3をどちらか一方に所属させる」なら、住所や公式区域IDなど別の根拠を用意する。境界を含む判定へ変えるだけでは、一意の所属は決まらない。P4を分析対象外とする場合も、除外した件数と範囲を記録する。

このコードは各点と全区域を順に比較する小規模な学習例である。大量データの高速化、測位誤差、無効な形状、複雑な区域の修復は扱わない。実データでは[CRSの確認](../concepts/coordinate-reference-systems.md)と[結果の検証](../methods/spatial-analysis-validation.md)へ進む。

## 次に試す

[データ分析ルート](getting-started.md#route-analysis)で到達点を確認し、以下から次の課題を選ぶ。

- [16画素の画像評価演習](imagery-evaluation-exercise.md)：データの対応確認から、AIの予測結果の評価へ進む。

- [POIデータを選び、分析する](poi-workflow.md)：実際の店舗データの取得範囲・カテゴリ・重複を確認する。
- [人流データの計測誤差と推計誤差](../data/human-flow-data-quality.md)：点の件数と人数の推計が違うことを学ぶ。人流では観測点をそのまま人数と数えない。

## 出典と検証範囲

- [Shapely within](https://shapely.readthedocs.io/en/stable/reference/shapely.within.html)、[covered_by](https://shapely.readthedocs.io/en/stable/reference/shapely.covered_by.html)（2026-10-05確認）。境界の扱いを参照した。
- 架空データとコードはGeoAIアトラス作成。2026-10-05にWindows、Python 3.14.0、Shapely 2.1.2、GEOS 3.13.1でuv経由の実行を確認した。上表の結果と一致し、組み込み検査はPASS。pip経由のセットアップは今回未実行である。
