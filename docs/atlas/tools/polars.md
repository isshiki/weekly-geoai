---
layout: default
title: Polars
category: tools
updated: 2026-10-30
---

# Polars

Polarsは、表データをDataFrameとして読み込み、絞り込みや集計を行うライブラリである。このページではPython版を中心に、地理空間データの分析につながる更新を追う。利用にはPython環境とコードの実行が必要になる。

## 現在確認している機能

2026-10-30に確認したPython Polars 2.1.0では、GeoParquetの読み書きが実験的に追加された。GeoParquetは地理空間データを列指向ファイルで保存する仕組みであり、その入出力と、距離計算・空間結合などの演算全般への対応は区別する。

| 名前 | このページとの関係 |
| --- | --- |
| Python Polars | 本体。表の処理と2.1.0の実験的GeoParquet入出力を扱う |
| Spatial Polars | 別パッケージ。Shapelyなどと組み合わせて空間処理を行う。詳細は専用ページへ |
| GeoPolarsなど他の関連パッケージ | 本体とは公開元・版・提供機能が異なる。名前の近さだけで機能を合算しない |

## 重要な更新履歴 { #release-history }

初回の収録対象はPython版2.1.0である。それ以前の版における地理空間対応の導入時期は未調査であり、「以前は何もできなかった」という意味ではない。今後、重要な変更が確認できた版を追加する。最新推奨版の提示ではなく、実行・移行・性能試験は未実施である。

| バージョン・公式出典 | 公開日（UTC） | 変わったこと・使いどころ | 状態・更新時の注意 |
| --- | --- | --- | --- |
| [Python 2.1.0（py-2.1.0）](https://github.com/pola-rs/polars/releases/tag/py-2.1.0) | 2026-10-25 | GeoParquet入出力を実験追加。暗号化Parquet、SQL・Iceberg連携も拡充 | Python 3.10対応を終了。GeoParquet入出力は安定APIや空間演算全般の保証ではない |

公式リリースノートを2026-10-30に確認した。日次ニュースへの収録は10月26日であり、公開日とは異なる。

## 導入・更新時の注意

- 実験機能は、将来の変更を想定して利用するAPIと版を記録する。
- 読み書き後に形状、CRS、欠損値が意図どおり保持されるかを確認する。ファイルを開けたことと分析の正しさは別である。
- Python版のタグとRust側の版番号を混在させない。周辺パッケージも別に互換性を確認する。

## 次に読む

- [Spatial Polars](spatial-polars.md)：外部の空間処理パッケージの役割と制約。
- [DuckDBとSpatial拡張](duckdb.md)：SQLで地理空間データを扱う場合。
- [座標参照系](../concepts/coordinate-reference-systems.md)：位置データの意味を読み書きの前後で確かめる。

## 出典

- [Python Polars 2.1.0](https://github.com/pola-rs/polars/releases/tag/py-2.1.0)（2026-10-30確認）
