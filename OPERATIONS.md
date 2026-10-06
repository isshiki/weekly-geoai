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

初心者案内・POI案内・OpenLayers・空間結合・検証方法の図は、`python scripts/build_atlas_learning_figures.py`でSVGを再生成できる。生成先は`docs/assets/atlas/`。本文と図の説明をそろえ、変更時はスマートフォン幅と明暗テーマでも表示を確認する。

CNGの形式と処理を示す `format-roles.svg` も同スクリプトで再生成する。既存の `layers.svg` は別の図であり、再生成対象に含まない。

空間結合の演習コードは `docs/assets/exercises/spatial_join.py` が公開用の原本である。`uv run --no-project docs/assets/exercises/spatial_join.py` で独立した依存環境から検証し、演習ページの対応表・環境記録と照合する。サイト用の依存関係へShapelyを追加する必要はない。

毎月第1月曜日の9:00（日本時間）に、このチャットのCodex自動実行「GeoAIアトラスの月次整理」で見直す。初回は2026年10月5日に実施。予約はCodexアプリで管理し、GitHub Actionsの定期ジョブではない。

内容の基準は[Atlas編集ガイド](editorial/atlas-guide.md#月次整理)を参照する。前月の蓄積から5〜10ページ程度を選び、入口・分類・基礎説明・情報の鮮度を改善する。変更がない場合は通知を控え、改善結果、失敗、要対応事項を報告する。

実施日の`docs/updates/YYYY-MM-DD.md`に整理内容と次回候補を残す。同日のニュース追加がある場合は、当日の最初の変更より前のコミットを比較元にして、Atlasだけの確認リンクを再生成する。

```powershell
python scripts/sync_update_history.py --date YYYY-MM-DD --base <当日の最初の変更より前のコミット>
python -m mkdocs build --strict
python scripts/check_public.py --all
```

リンク・表示・差分と公開内容を確認した後、対象変更だけをコミット・プッシュする。公開URLの到達とGitHub Pagesのデプロイ結果を確認して報告する。ニュースレターの原稿や配信設定は月次整理の対象に含めない。

## 公開前チェック

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
