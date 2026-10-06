# 週刊GeoAI 運営ガイド

「週刊GeoAI」は、地図・位置情報データ×AIの1週間を毎週金曜にまとめて届ける個人ニュースレターである。

GIS・位置情報の仕事をしていて、AI・機械学習側の動きを短時間で追いたい人のための日本語ニュースレターです。1週間分のニュース・論文・事例を、毎週金曜にまとめて配信します。

ニュースレターはSubstackで配信する。原稿確認後、生成したHTMLをSubstackへ手動で貼り付ける。バックナンバーもSubstackに集約し、知識サイト「GeoAIアトラス」からはアーカイブへ直接リンクする。

## ディレクトリ

- `daily/`: 日次の「今日の気になったもの」。`YYYY-MM-DD.md`で保存する。
- `drafts/`: 金曜発行分の週次原稿。`YYYY-MM-DD.md`で保存する。
- `docs/atlas/`: GeoAIアトラスのテーマ別知識ページ。
- `docs/updates/`: GeoAIアトラスの日付別更新記録。
- `docs/assets/`: MkDocsから配信するロゴなどの静的ファイル。
- `docs/stylesheets/`: GeoAIアトラス固有の表示調整。
- `substack/`: Substack貼り付け用に生成したHTML。
- `editorial/`: 日次・週次テンプレートと文体規則。
- `.agents/skills/`: Codexが日次保存・週次編集に使うリポジトリ固有スキル。
- `scripts/`: Python標準ライブラリだけで動く補助コマンド。

`daily/`と`drafts/`もGit管理対象であり、パブリックリポジトリでは内容が公開される。日次メモには、第三者に読まれても問題のない一言だけを書くこと。

## セットアップ

Python 3.11以上を使用する。ニュースレター用スクリプトは標準ライブラリだけで動作する。サイトのローカル表示とビルドには、`site`依存グループのMaterial for MkDocsを使用する。

ローカル設定を変更するときだけ、`.env.example`を`.env`へコピーする。`.env`はGit管理対象外である。

```powershell
Copy-Item .env.example .env
uv sync --group site
python -m unittest discover -s tests
```

## 日次保存

URLだけを保存する例：

```powershell
python scripts/capture_daily.py "https://example.com/article"
```

公開可能な一言と確認済みの整理情報を添える例：

```powershell
python scripts/capture_daily.py "https://example.com/article" `
  --title "記事タイトル" `
  --kind "記事" `
  --topics "人流データ, OD" `
  --summary "位置点と集計データの違いを整理した記事である。" `
  --note "自治体での実装例として確認したい" `
  --atlas-path "docs/atlas/data/human-flow-data-types.md"
```

保存日はローカル日付になる。過去日を指定するときは`--date YYYY-MM-DD`を使う。同じURLは同じ日付のファイルへ重複登録しない。

Codexには、URLやニュースチェックを貼って「今日の気になったものとして保存」と依頼すれば、`geoai-save-daily`スキルが出典を確認し、日次ログ、Atlasページ、日付別更新記録へ整理する。貼り付けた文章そのものは保存せず、公開可能な確認済み情報へ書き直す。

## 週次原稿

週次原稿は以下の手順で作成する。Atlasの月次整理は[後述の運用](#atlas-monthly)を使う。

発行日を指定して、前週金曜から木曜までのURLを下書きへ集約する。

```powershell
python scripts/build_weekly.py --date 2026-09-11
```

発行日は金曜だけを受け付ける。番号を省略した場合、既存の下書きから次の号数を採番する。金曜に保存したURLは次週号の対象になる。

木曜にはCodexへ「今週号の候補を提案して」と依頼する。`geoai-build-weekly`スキルが候補、順序、まとまり、所感の切り口を提案する。選定とコメントの確認後に同じスキルでMarkdown原稿を作り、短いサブタイトル、通し番号付きのタイトル、1〜2文の紹介文を完成させる。所感が未確定なら2段落の空欄を残す。項目の番号は順位ではなく掲載順を表す。

## 公開とSubstack用HTML

所感を記入して内容を確認した後、明示的に公開処理を実行する。

```powershell
python scripts/publish_issue.py drafts/2026-09-11.md
```

確認済みのMarkdown原稿は`drafts/`に残り、`substack/2026-09-11.html`へSubstack本文用のHTML断片が生成される。コマンドに表示されたサブタイトルをSubstackのサブタイトル欄へ入力し、HTMLは本文欄へ貼り付ける。GitHub Pagesには週刊GeoAI本文を複製しない。

サブタイトル、所感、紹介文、タイトルの確認用プレースホルダが残っている場合、番号が1からの連番でない場合、紹介文が1〜2文でない場合は公開しない。生成済みファイルを意図的に更新するときだけ`--force`を付ける。

## GeoAIアトラスのローカル確認

ルートのSVGロゴをサイト側へ同期してから、MkDocsの開発サーバーを起動する。

```powershell
uv run --group site python scripts/sync_site_assets.py
uv run --group site mkdocs serve
```

ブラウザで`http://127.0.0.1:8000/weekly-geoai/`を開く。静的ファイルだけを検査するときは、次を実行する。

```powershell
uv run --group site mkdocs build --strict
```

## GitHub Pages設定

GitHub Pagesは次の設定で公開する。

- Source: GitHub Actions
- Workflow: `.github/workflows/pages.yml`

`main`へのpushに応じてMkDocsをビルドし、生成された`site/`をGitHub Pagesへ公開する。独自ドメインは使用しない。

サイトのロゴとファビコンには`assets/logo.svg`を使用する。`scripts/sync_site_assets.py`がMkDocs配信用の`docs/assets/logo.svg`へ同期し、GitHub Actionsでもビルド前に必ず実行する。

<a id="atlas-monthly"></a>

## Atlasの月次整理

月次の点検は[確認台帳](editorial/atlas-review-register.md)から5〜10ページを選ぶ。元の調査9本の照合は初回に一度、実データの性能比較は個別企画として扱う。[暫定対応表と初回候補](editorial/atlas-research-crosswalk.md)に未完了事項を残す。予約の実行頻度は変更しない。

日次追加・月次編集の後は `python scripts/build_atlas_review_register.py` で台帳を更新する。`--check` は再生成が必要なら失敗する。外部サイトを取得するツールではなく、既存本文の出典確認日と未確認表記を集める。

GitHub Actionsでも `--check` を実行し、台帳の更新漏れがあれば公開前に止める。

ページ全体を点検した場合だけ `editorial/atlas-review-records.json` に、`atlas/tools/xxx.md` のようなdocs相対パスをキーとして `reviewed_on`（YYYY-MM-DD）、`evidence`（確認した出典・節・判断・残課題）を記録する。次回の具体的な作業は任意の `next_action` に記録できる。全体点検なしで次の作業だけ記録する場合は `reviewed_on` を省略する。再生成はこの手動記録を上書きしない。

初心者案内・POI案内・OpenLayers・空間結合・検証方法の図は、`python scripts/build_atlas_learning_figures.py`でSVGを再生成できる。生成先は`docs/assets/atlas/`。本文と図の説明をそろえ、変更時はスマートフォン幅と明暗テーマでも表示を確認する。

埋め込みの検索・予測を対比する `spatial-embeddings/search-and-prediction.svg` も `scripts/build_atlas_learning_figures.py` で再生成する。模式図であり、実モデルの性能を表さない。

CNGの形式と処理を示す `format-roles.svg` も同スクリプトで再生成する。既存の `layers.svg` は別の図であり、再生成対象に含まない。

空間結合の演習コードは `docs/assets/exercises/spatial_join.py` が公開用の原本である。`uv run --no-project docs/assets/exercises/spatial_join.py` で独立した依存環境から検証し、演習ページの対応表・環境記録と照合する。サイト用の依存関係へShapelyを追加する必要はない。

画像評価の演習は `python docs/assets/exercises/imagery_evaluation.py` で実行する。追加依存は不要。図は `python scripts/build_imagery_evaluation_figure.py` で同じ入力から再生成する。`python -m unittest discover -s tests` で分母ゼロ・入力形状の検査も行う。

毎月第1月曜日の9:00（日本時間）に、このチャットのCodex自動実行「GeoAIアトラスの月次整理」で見直す。初回は2026年10月5日に実施。予約はCodexアプリで管理し、GitHub Actionsの定期ジョブではない。

内容の基準は[Atlas編集ガイド](editorial/atlas-guide.md#月次整理)を参照する。前月の蓄積から5〜10ページ程度を選び、入口・分類・基礎説明・情報の鮮度を改善する。変更がない場合は通知を控え、改善結果、失敗、要対応事項を報告する。

実施日の`docs/updates/YYYY-MM-DD.md`に整理内容と次回候補を残す。同日のニュース追加がある場合は、当日の最初の変更より前のコミットを比較元にして、Atlasだけの確認リンクを再生成する。

```powershell
python scripts/sync_update_history.py --date YYYY-MM-DD --base <当日の最初の変更より前のコミット>
python -m mkdocs build --strict
python scripts/check_site_links.py --history-date YYYY-MM-DD
python scripts/check_public.py --all
```

リンク・表示・差分と公開内容を確認した後、対象変更だけをコミット・プッシュする。公開URLの到達とGitHub Pagesのデプロイ結果を確認して報告する。ニュースレターの原稿や配信設定は月次整理の対象に含めない。

## 公開前チェック

### リンクとハイライトの検査

ビルド後に `python scripts/check_site_links.py` を実行する。既定では生成済み更新履歴の最新日を厳密に検査する。特定の作業日は `--history-date YYYY-MM-DD` で指定でき、指定日のページがなければ失敗する。別のビルド先は `--site-dir PATH` で指定する。

- 全生成HTMLの `href`・`src` に含まれる内部ページ・画像・スクリプト等の存在と、HTMLのアンカーを確認する。同じ公開サイトの絶対URLにも対応する。
- テキストフラグメントは、履歴生成ツールの `text=文章` と `text=始点,終点` を検査する。複数指定とパーセント符号化にも対応する。
- 指定日以降の履歴・通常ページの不一致はエラー（終了コード1）。それより古い履歴の文章不一致は警告のみとし、過去の記録を自動で書き換えない。リンク先やアンカーの欠落は過去履歴でもエラーにする。
- 外部サイトの到達性、CSS内のURL、`srcset`、JavaScriptで生成するリンク、ブラウザーでの実際のハイライト表示は対象外。テキストはscript/styleを除いたHTMLの静的照合であり、CSSによる可視性やブラウザー固有の一致規則を再現しない。

GitHub Actionsはビルド後に同じ検査を実行し、エラーがあれば公開を止める。チェック自体の回帰テストは `python -m unittest discover -s tests` で実行する。秘密情報の検査は引き続き `check_public.py` が担当する。

### 公開対象の確認

このリポジトリは全履歴を含めて公開される。push前に毎回、次を確認する。

1. `daily/`の一言に個人情報、社内情報、未公開情報がない。
2. `drafts/`に公開できないメモや引用がない。
3. `.env`、APIキー、アクセストークン、秘密鍵が追跡されていない。
4. Substack用HTMLを生成するとき、所感と紹介文にプレースホルダが残っていない。
5. 記事タイトル、リンク先、日付、号数が正しい。
6. `git diff --cached`で実際に公開される差分を読む。

全ファイルまたはGit追跡対象を次のコマンドで検査できる。

`--all`は無視対象のローカル`.env`も検出する。その場合は内容を表示せず、`git check-ignore .env`と`git ls-files .env`で無視・未追跡を確認し、新規ファイルを明示的にステージした後、`--all`なしの追跡対象チェックでも検証する。検出された秘密情報を公開対象へ加えてはならない。

```powershell
python scripts/check_public.py --all
git status --short
git diff --cached
```

秘密情報を一度コミットすると、後からファイルを削除してもGit履歴に残る。見つけた場合はpushせず、まず認証情報を失効・再発行する。
