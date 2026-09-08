---
layout: default
title: geoparquet-io
category: tools
updated: 2026-09-08
---

# geoparquet-io

geoparquet-io（`gpio`）は、GeoParquetを中心とした地理空間データの変換、検査、抽出、空間ソート、インデックス付与、分割、公開を扱うCLIとPythonライブラリである。

## 低ズーム向けの集約パイプライン

v1.4.0では、大規模な地物を低ズームでも表示できるようにする3段階の処理が追加された。

1. `gpio process aggregate` で地物をA5、H3、行政区画の単位へ集約する。
2. `gpio process overview` で集約結果からさらに粗いレベルを作る。
3. `gpio pmtiles pyramid` でズーム帯ごとのデータを1つのPMTilesアーカイブへまとめる。

単純な地物数のほか、数値指標の集約やカテゴリー別の内訳を作れる。詳細な地物をすべて低ズームへ送るのではなく、縮尺に合った集計表現へ置き換える処理である。

## 変換・抽出の更新

- `gpio sort str` により、Hilbert順に加えてSort-Tile-Recursive（STR）順の空間ソートを選べる。
- `gpio convert --geoparquet-version 1.1-geoarrow` で、任意の対応入力からネイティブGeoArrowエンコーディングを作れる。
- WFSの大規模レイヤーは自動的にタイル分割して取得し、サーバーの件数上限による黙った切り捨てを避ける。

## v1.4.0の互換性と注意点

v1.4.0はCLIとPython APIで異なっていたデフォルト値を統一し、DuckDBの最低バージョンを1.5.2へ引き上げた。既存処理では出力や既定動作が変わり得るため、更新前にコマンドとAPI双方の引数を確認する。

対象DuckDB向けに `geography` コミュニティ拡張が公開されていないため、この版では `gpio add s2` と `gpio partition s2` を利用できない。代替候補として `gpio add a5` が案内されている。

このリリースでは、CLIとPython APIの比較、書き込み契約、空間インデックスのゴールデン値、E2E処理、ドキュメント例の自動実行など、正確性を確認するテストも増強された。

## 関連項目

- [H3](h3.md)
- [Portolan](../data/portolan.md)

## 出典

- [geoparquet-io Changelog](https://geoparquet.io/CHANGELOG/)（2026-09-08確認）
