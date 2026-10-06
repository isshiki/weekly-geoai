# 調査とAtlasの暫定対応表

2026-10-06作成。元の調査9本は指定されていたDownloads直下・その配下・プロジェクト内で見つからなかった。以下は[整備計画](atlas-roadmap.md)と現行ページを照合した表であり、9本の原文を逐条照合した結果ではない。モデル別の一致率・誤り数・網羅率は算出しない。

## 原資料の受領・確認状態

| 原資料 | 原文の再照合 | 次の処理 |
| --- | --- | --- |
| ChatGPT-1-deep-research-report.md | 未了・ファイル所在未確認 | 再受領後に論点へ分解 |
| ChatGPT-2-deep-research-report.md | 未了・ファイル所在未確認 | 同上 |
| ChatGPT-3-deep-research-report.md | 未了・ファイル所在未確認 | 同上 |
| Claude-1-compass_artifact_wf-8cb9a989-8759-5584-af63-3a9c7083bd31_text_markdown.md | 未了・ファイル所在未確認 | 同上 |
| Claude-2-compass_artifact_wf-751cc3fd-d2cb-5933-a8b2-6de3eb8e3d48_text_markdown.md | 未了・ファイル所在未確認 | 同上 |
| Claude-3-compass_artifact_wf-47a29bfe-564a-5cb6-9f7b-ea4f8157c5b5_text_markdown.md | 未了・ファイル所在未確認 | 同上 |
| Gemini-1-GeoAI知識サイト体系化調査.md | 未了・ファイル所在未確認 | 同上 |
| Gemini-2-GeoAI実務知識体系の調査.md | 未了・ファイル所在未確認 | 同上 |
| Gemini-3-GeoAI初心者向け学習サイト設計.md | 未了・ファイル所在未確認 | 同上 |

## 現行実装との対応

「対応済み」は下記の範囲の解説が存在するという判断であり、研究全体の検証完了ではない。状態は対応済み・不足・採用しない・根拠未確認を使う。原文再受領までは各行の原資料箇所を「未照合」のまま保持する。

| ID | 論点 | Atlasの対応先 | 実装状態 | 原資料箇所 | 残る作業 |
| --- | --- | --- | --- | --- | --- |
| R01 | 全体像・手法選択 | [全体像](../docs/atlas/concepts/geoai-overview.md) | 対応済み | 未照合 | 分析と操作支援の区別を維持 |
| R02 | 座標・測定 | [CRS](../docs/atlas/concepts/coordinate-reference-systems.md) | 対応済み | 未照合 | 単位・投影の前提を巡回確認 |
| R03 | ベクター・ラスター | [表現と解像度](../docs/atlas/concepts/vector-raster-data.md) | 対応済み | 未照合 | 精度と解像度の区別を維持 |
| R04 | 空間集計・検証 | [検証](../docs/atlas/methods/spatial-analysis-validation.md)・[空間結合演習](../docs/atlas/guides/spatial-join-exercise.md) | 対応済み（架空データ） | 未照合 | 実データの一連の処理は不足 |
| R05 | 空間索引 | [索引の選択](../docs/atlas/methods/spatial-index-selection.md) | 対応済み（基礎）／根拠未確認（レビュー全文） | 未照合 | 論文全文と研究別の条件、性能比較 |
| R06 | 予測・説明・因果 | [モデルの目的](../docs/atlas/concepts/geographic-model-reasoning.md) | 対応済み | 未照合 | 性能と因果の説明を混同しない |
| R07 | 解像度・集計単位 | [地形スケール](../docs/atlas/methods/terrain-scale.md) | 対応済み（既存ページ間の接続） | 未照合 | 総合ページ新設は採用しない（現時点で重複が大きい） |
| R08 | データの来歴 | [入力・処理・出力の記録](../docs/atlas/data/geospatial-record-provenance.md) | 対応済み | 未照合 | 実データ演習で記録を具体化 |
| R09 | CNG・形式の役割 | [CNG](../docs/atlas/concepts/cloud-native-geospatial.md) | 対応済み（説明）／不足（測定） | 未照合 | 転送量・要求数・時間の実測は別企画 |
| R10 | 画像解析・評価 | [画像からGIS](../docs/atlas/methods/imagery-to-gis.md)・[16画素演習](../docs/atlas/guides/imagery-evaluation-exercise.md) | 対応済み（基礎・架空データ） | 未照合 | 実モデルの比較は未実施 |
| R11 | 埋め込み | [検索と予測](../docs/atlas/methods/spatial-embeddings.md) | 対応済み（具体例） | 未照合 | 実データの精度改善は未検証 |
| R12 | GISエージェント | [依頼設計](../docs/atlas/concepts/location-ai.md) | 対応済み（ひな形） | 未照合 | 実行・権限・失敗時挙動の試験は未実施 |
| R13 | 初心者の学習導線 | [3ルート](../docs/atlas/guides/getting-started.md) | 対応済み | 未照合 | 月次に行き止まりと前提を確認 |

## 原文が戻った後の照合方法

1. 各資料へ固定IDを付け、見出しと行番号を記録する。原文や私的なメモを無条件に公開リポジトリへコピーしない。
2. 一つの提案・事実主張を一行に分け、上記IDへ対応付ける。新しい論点は追記する。
3. 共通する主張でも一次資料を確認する。Geminiを含め全モデルへ同じ基準を適用し、架空の引用・名称・性能数値・提供条件を優先確認する。
4. 食い違いは対象年、定義、対象地域、評価条件の違いかを調べ、根拠URLと確認範囲を残す。
5. 全論点に状態・対応先または不採用理由・未確認理由が付いたら初回照合を完了する。未確認を「対応済み」へまとめない。

## 初回の月次候補

全体点検は未実施。次の5ページから始め、必要なら10ページまで広げる。

| ページ | 優先する確認 |
| --- | --- |
| [Mapbox Search Box](../docs/atlas/tools/mapbox-search-box.md) | POI取得・保存条件、料金・利用枠と対象地域 |
| [POI比較](../docs/atlas/data/poi-open-data-comparison.md) | 取得上限、カテゴリ、データ版、件数比較の前提 |
| [地域埋め込み](../docs/atlas/methods/spatial-embeddings.md) | PDIの対象地域・提供条件と発表時点の区別 |
| [GeoLibre](../docs/atlas/tools/geolibre.md) | 操作機能の前提、版ごとの記述の統合 |
| [Kodawari](../docs/atlas/tools/kodawari.md) | 評価式・データ出典・更新頻度の公開有無 |

これは作業候補であり、確認結果ではない。既存の月次枠で[確認台帳](atlas-review-register.md)とともに見直す。

## 実データ演習の設計案（実行前）

最初は1データ・小地域で、POIの取得から検証までを通す。候補は既存記事で扱った吉祥寺周辺のOverture Placesである。公開データの利用条件・現在のスキーマ・選択できる版を実装前に公式資料で再確認する。大規模取得や有償API契約は前提にしない。

- 問い：同じデータ版・対象範囲で、bboxによる候補抽出とgeometryによる最終判定の件数を再現できるか。
- 固定する条件：データ版、範囲座標、CRS、分類条件、取得上限、環境とコード版。
- 出力：段階別件数、重複ID・欠損・境界上の点の確認、来歴記録、再実行手順。生データの再配布条件が確認できなければ取得コードと集計だけを公開する。
- 完了条件：途中で取得が打ち切られていないことと、同じ条件で結果を再現できることを確認し、未確認の範囲を明記する。
- 件数は営業中の店舗数や網羅率とは呼ばない。まず正しさと再現性を扱い、性能比較は同じ入力・出力条件、複数回測定、キャッシュ条件を決めた別段階にする。
