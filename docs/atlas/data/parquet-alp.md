---
layout: default
title: ParquetのALP浮動小数点符号化
category: data
updated: 2026-09-24
---

# ParquetのALP浮動小数点符号化

ALP（Adaptive Lossless floating-Point）は、ParquetのFLOAT・DOUBLE列に対する可逆な符号化方式である。parquet-format 2.14.0に追加された仕様であり、各言語の読み書きライブラリの版や対応状況とは区別する。

## 向く値と向かない値

少ない十進桁を持つ数値を整数で表し、差分とビット詰めで保存する。元の浮動小数点値へ戻せない値やNaNなどは例外として元の値を保持するため、単純な丸めによる精度削減ではない。

| 対象 | 考え方 |
| --- | --- |
| 桁数の少ない価格・測定値・経緯度 | ALPの利点が出やすい候補 |
| 有効桁が多い生センサー値や計算結果 | 例外が増えて圧縮効果が弱くなる場合がある |
| WKB形式のGeometry列 | バイナリ列なのでALPの直接の対象ではない |

GPS座標だから一律に不得意なのではなく、値の有効桁や分布が関係する。圧縮のために事前に丸める操作は別の非可逆な変更であり、必要精度を定めずに行わない。

## 速度と互換性

公式比較はALP単体とPLAIN・BYTE_STREAM_SPLITにZSTDを組み合わせた構成を比較し、デコードとランダムアクセスの高速化を報告している。圧縮率だけでなく、列型、値の分布、読み方、CPU負荷で評価する。特定ベンチマークの倍率をGIS処理全体に一般化しない。

仕様への追加と、利用中のwriter・readerが対応することは別である。ALP対応ファイルを配布する前に受け手の実装を確認する。DuckDBなどが独自の保存形式でALPを使うことも、ParquetのALP対応を直接意味しない。

## 出典

- [Apache Parquet公式解説](https://parquet.apache.org/blog/2026/09/22/alp-adaptive-lossless-floating-point-encoding-in-apache-parquet/)（2026-09-22公開、2026-09-24確認）
- [MIERUNEの解説](https://zenn.dev/mierune/articles/21c94dbaefb147)（2026-09-23公開、2026-09-24確認）
