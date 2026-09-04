# 週刊GeoAI

地図・位置情報データ×AIの1週間を、毎週金曜にまとめて届ける個人ニュースレターである。

GIS・位置情報の仕事をしていて、AI・機械学習側の動きを短時間で追いたい人のための日本語ニュースレターです。1週間分のニュース・論文・事例を、毎週金曜にまとめて配信します。

配信先はSubstackとGitHub Pagesである。原稿確認後、Substackには生成したHTMLを手動で貼り付け、GitHub Pagesには同じ内容のMarkdownを公開する。

## ディレクトリ

- `daily/`: 日次の「今日の気になったもの」。`YYYY-MM-DD.md`で保存する。
- `drafts/`: 金曜発行分の週次原稿。`YYYY-MM-DD.md`で保存する。
- `docs/issues/`: GitHub Pagesで公開する各号。
- `substack/`: Substack貼り付け用に生成したHTML。
- `editorial/`: 日次・週次テンプレートと文体規則。
- `.agents/skills/`: Codexが日次保存・週次編集に使うリポジトリ固有スキル。
- `scripts/`: Python標準ライブラリだけで動く補助コマンド。

`daily/`と`drafts/`もGit管理対象であり、パブリックリポジトリでは内容が公開される。日次メモには、第三者に読まれても問題のない一言だけを書くこと。

## ロゴ

マスターは`assets/logo.svg`である。背景は透明で、オレンジ色のピンを濃紺の輪郭で囲んでいる。文字はパスへ変換済みなのでフォントには依存しない。ロゴ本体は濃紺`#1E3A5F`とオレンジ`#FF8A3D`のベタ塗り2色だけを使用する。

PNGの再生成に限り、通常の実行環境とは分離した`logo`依存グループを使用する。

```powershell
uv sync --group logo
uv run --group logo python scripts/export_logo.py
```

次のファイルが生成される。

- `assets/logo-1024.png`: Substackのパブリケーションロゴ用
- `assets/logo-256.png`: faviconなどの小サイズ用
- `assets/logo-preview.png`: 160px・64px・48px・32pxの実寸比較

### CairoSVGを導入しない場合

SVGはブラウザで直接開ける。ブラウザの開発者ツールで表示領域を正方形に固定し、1024×1024または256×256でスクリーンショットを保存する方法がある。ただし、余白やデバイススケールの影響を受けやすいため、書き出し寸法を確認する。

Inkscapeがインストール済みなら、Python依存なしで次のように書き出せる。

```powershell
inkscape assets/logo.svg --export-type=png --export-filename=assets/logo-1024.png --export-width=1024 --export-height=1024
inkscape assets/logo.svg --export-type=png --export-filename=assets/logo-256.png --export-width=256 --export-height=256
```

Inkscapeだけでは比較プレビューを自動合成しないため、160px・64px・48px・32pxへそれぞれ書き出して画像編集ソフト上で実寸配置する。

## セットアップ

Python 3.11以上を使用する。外部パッケージへの依存はない。

ローカル設定を変更するときだけ、`.env.example`を`.env`へコピーする。`.env`はGit管理対象外である。

```powershell
Copy-Item .env.example .env
python -m unittest discover -s tests
```

## 日次保存

URLだけを保存する例：

```powershell
python scripts/capture_daily.py "https://example.com/article"
```

公開可能な一言と既知のタイトルを添える例：

```powershell
python scripts/capture_daily.py "https://example.com/article" `
  --title "記事タイトル" `
  --note "自治体での実装例として確認したい"
```

保存日はローカル日付になる。過去日を指定するときは`--date YYYY-MM-DD`を使う。同じURLは同じ日付のファイルへ重複登録しない。

Codexには、URLを貼って「今日の気になったものとして保存」と依頼すれば、`geoai-save-daily`スキルがこの処理を行う。

## 週次原稿

発行日を指定して、月曜から木曜までのURLを下書きへ集約する。

```powershell
python scripts/build_weekly.py --date 2026-09-11
```

発行日は金曜だけを受け付ける。番号を省略した場合、既存の下書きと公開号から次の号数を採番する。金曜に保存したURLは次週号の対象になる。

Codexには「今週号をまとめて」と依頼すれば、`geoai-build-weekly`スキルがリンク先を確認し、タイトルと1〜2文の紹介文を完成させる。所感2段落は書き手用の空欄として残る。

## 公開とSubstack用HTML

所感を記入して内容を確認した後、明示的に公開処理を実行する。

```powershell
python scripts/publish_issue.py drafts/2026-09-11.md
```

次の2ファイルが同時に生成され、`docs/issues/index.md`も更新される。

- `docs/issues/2026-09-11.md`: GitHub Pages用Markdown
- `substack/2026-09-11.html`: Substack本文へ貼り付けるHTML断片

所感、紹介文、タイトルの確認用プレースホルダが残っている場合や、紹介文が1〜2文でない場合は公開しない。生成済みファイルを意図的に更新するときだけ`--force`を付ける。

## GitHub Pagesの初回設定

GitHubでリポジトリを作成して`main`をpushした後、Settings → Pagesで次を選ぶ。

- Source: Deploy from a branch
- Branch: `main`
- Folder: `/docs`

以後は`docs/`へのpushに応じて標準Jekyllが自動公開する。独自ドメインや独自のActionsワークフローは使用しない。

## 公開前チェック

このリポジトリは全履歴を含めて公開される。push前に毎回、次を確認する。

1. `daily/`の一言に個人情報、社内情報、未公開情報がない。
2. `drafts/`に公開できないメモや引用がない。
3. `.env`、APIキー、アクセストークン、秘密鍵が追跡されていない。
4. 所感と紹介文にプレースホルダが残っていない。
5. 記事タイトル、リンク先、日付、号数が正しい。
6. `git diff --cached`で実際に公開される差分を読む。

初回コミット前は全ファイルを、以後はGit追跡対象を検査できる。

```powershell
python scripts/check_public.py --all
git status --short
git diff --cached
```

秘密情報を一度コミットすると、後からファイルを削除してもGit履歴に残る。見つけた場合はpushせず、まず認証情報を失効・再発行する。
