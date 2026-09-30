---
layout: default
title: geoparquet-io
category: tools
updated: 2026-09-30
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

## 大規模処理と出力の一貫性

v1.6.0（2026年9月23日UTC公開）は、PMTiles生成の分割処理、一時領域の指定、明示的なズーム帯を追加した。変換ではforce-2dによるZ・Mの除去、encodingによる文字コード指定に対応する。

複数の書き込み経路を共通化し、CRSやgeometry型、bbox coveringの保持を改善した。check --fixが入力を上書き・削除する不具合も修正している。主要な書き込み処理の行グループ既定値は49,152行となり、指定値は2,048行単位へ丸める。以前の設定に依存する処理は出力条件を確認する。

bboxメタデータ追加は、データ部分を再圧縮せずフッターのメタデータだけを書き換える方式になった。リリース記載のベンチマークでは490msから12msへ短縮したが、すべてのファイルに同じ比率を保証するものではない。Overture行政区画の取得も復旧し、最新リリースの参照にSTACカタログを利用する。

## 変換・空間ソート・検証を試す

KEI_YAMAの9月29日の入門記事は、全国行政区域のShapefile変換、bbox追加、ヒルベルトソート、H3・A5付与、gpio check allによる検証を紹介する。Apple M2環境で125,130行・173.45MBの出力を8.0秒で生成したという実行例である。

地理的に近い地物をまとめると、bbox統計を利用する読み込み側が検索範囲外の行グループを読み飛ばしやすくなる。並べ替えだけで必ず高速になるとは限らず、読み込み側の対応と検索条件も確認する。記事の計測・コードは今回再実行していない。

## 関連項目

- [H3](h3.md)
- [Portolan](../data/portolan.md)

## 出典

- [geoparquet-io Changelog](https://geoparquet.io/CHANGELOG/)（2026-09-08確認）

- [v1.6.0公式リリース](https://github.com/geoparquet/geoparquet-io/releases/tag/v1.6.0)（2026-09-30確認）
- [geoparquet-ioを使ったGeoParquet入門](https://qiita.com/KEI_YAMA/items/ed85af780a61829e19e8)（2026-09-30確認）
