---
layout: default
title: RustGIS
category: tools
updated: 2026-10-16
---

# RustGIS

RustGISは、地図の作成、編集、解析、出力を行うRust製の無料・オープンソースGISアプリである。2026年10月12日に初版v0.1.0を公開した。Windows・macOS・Linuxで動き、WebAssemblyを使うブラウザー版も提供する。

## 使いどころと必要な準備

手元の地理空間データを読み込み、地図の色分けや解析、レイアウト・PDF出力を行う。画面操作に加え、CLI（コマンドライン）から操作をスクリプト化できる。AIアシスタントは選択したモデルで同じアプリのコマンドを実行する。

| 利用方法 | 確認する条件 |
| --- | --- |
| デスクトップ | OSに合うアプリと入力データを用意する |
| ブラウザー | WebGPUまたはWebGL2に対応した環境を使い、形式ごとの対応を確認する |
| AIアシスタント | 選択するプロバイダー・モデルの接続設定と、送信する情報を確認する |
| 拡張・自動化 | CLIのコマンドやWebAssemblyプラグインを利用する |

## 読込・SQL・外部AIの連携

2026年10月13日公開のv0.2.0では、GeoPackage・GeoParquet・FlatGeobufなどを直接開き、大きなファイルは表示範囲に応じて段階的に読む。ZIP形式のShapefileも含め、ブラウザー版の対応形式が拡張された。初版の導入資料にあった制限と、現行版の対応を混同しない。

DuckDB SpatialでのSQL実行・DuckDBファイルの読込と、GDALのogr2ogrを使う形式の読込は、対応する外部ツールの導入が前提になる。MCPサーバーからAIエージェントがRustGISのコマンドを実行し、地図を作れる。GeoPackage・GeoParquetなどへの書き出しも加わった。

## データとAIの関係

開発元は、選択したAIモデルへ送る場合を除き、データは利用者のマシンに保持すると説明する。クラウドのAIモデルへの送信とローカルのGIS処理を分ける。初版・v0.2.0の発表と公式資料を確認したもので、アプリの実行や性能比較は行っていない。

## 次に読む

- [GeoLibre](geolibre.md)：同じ開発元の別GISアプリ。RustGISの別名ではない。
- [分析の検証](../methods/spatial-analysis-validation.md)：処理の成功と結果の正しさを分けて確認する。

## 出典

- [公式概要](https://rustgis.app/)（2026-10-13確認）
- [導入と環境別の条件](https://rustgis.app/installation/)（2026-10-13確認）

- [RustGIS v0.1.0](https://github.com/opengeos/RustGIS/releases/tag/v0.1.0)（2026-10-13確認）

- [v0.2.0リリースノート](https://github.com/opengeos/RustGIS/releases/tag/v0.2.0)（2026-10-16確認）
