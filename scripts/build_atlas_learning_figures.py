"""Regenerate the three introductory Atlas diagrams (Python standard library)."""

from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "docs/assets/atlas"
NAVY = "#1E3A5F"
ORANGE = "#FF8A3D"


def text(x, y, value, size=24, bold=False, color=NAVY):
    return (f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{size}" '
            f'font-weight="{700 if bold else 400}" fill="{color}">{escape(value)}</text>')


def box(x, y, w, h, title, subtitle, fill="#ffffff"):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" '
            f'fill="{fill}" stroke="{NAVY}" stroke-width="2"/>'
            + text(x + w / 2, y + 29, title, bold=True)
            + text(x + w / 2, y + 57, subtitle, size=22))


def arrow(path, dashed=False):
    dash = ' stroke-dasharray="7 5"' if dashed else ""
    return (f'<path d="{path}" fill="none" stroke="{NAVY}" stroke-width="2.5"'
            f'{dash} marker-end="url(#arrow)"/>')


def save(slug, name, height, title, description, body):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="540" height="{height}" viewBox="0 0 540 {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title>
<desc id="desc">{escape(description)}</desc>
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="{NAVY}"/></marker></defs>
<rect width="540" height="{height}" rx="16" fill="#f7f9fc"/>
<g font-family="'Noto Sans JP', 'Yu Gothic', Meiryo, sans-serif">
{text(270, 42, title, 26, True)}
{body}
</g></svg>
'''
    folder = ROOT / slug
    folder.mkdir(parents=True, exist_ok=True)
    (folder / name).write_text(svg, encoding="utf-8")


def main():
    steps = [
        ("1  問いを決める", "場所・対象・時点"),
        ("2  データを選ぶ", "利用条件・更新日・属性"),
        ("3  条件をそろえる", "座標系・分類・重複"),
        ("4  分析して地図にする", "集計・分布の確認"),
        ("5  結果を確かめる", "原典との照合・偏りの説明"),
    ]
    body = ""
    for i, (title, subtitle) in enumerate(steps):
        y = 80 + 100 * i
        body += box(90, y, 390, 72, title, subtitle,
                    "#fff0e6" if i == 4 else "#ffffff")
        if i < 4:
            body += arrow(f"M 285 {y + 72} V {y + 98}")
    body += arrow("M 90 516 H 36 V 216 H 88", dashed=True)
    body += text(270, 592, "合わなければ、データや条件を見直す", 22)
    body += text(270, 632, "AIを使う段階でも、結果の確認は必要", 22)
    save("getting-started", "analysis-cycle.svg", 660,
         "問いから検証へ", "五つの段階を進め、結果に問題があればデータ選びや条件の整理に戻る。AIの利用はこの流れの一部であり、検証を省略しない。", body)

    body = text(270, 80, "目的に合う入口を選ぶ（複数でもよい）", 22)
    for y, title, subtitle in [
        (108, "Overture Places", "公開ファイルをSQLで分析"),
        (198, "Foursquare Open Source Places", "店舗・施設の分類から抽出"),
        (288, "OpenStreetMap", "店舗に加え、道路や建物も扱う"),
    ]:
        body += box(24, y, 468, 72, title, subtitle)
        body += f'<path d="M 492 {y+36} H 512" fill="none" stroke="{NAVY}" stroke-width="2.5"/>'
    body += arrow("M 512 144 V 392 H 270 V 418")
    body += box(24, 420, 468, 76, "同じ小さな範囲で試す", "利用条件・取得上限・データ版を確認", "#fff0e6")
    body += arrow("M 270 496 V 526")
    body += box(24, 528, 468, 76, "条件をそろえ、適合性を確かめる", "カテゴリ・重複・欠損・営業状態")
    body += text(270, 642, "上から品質順ではない。件数だけで選ばない。", 21)
    save("poi-workflow", "poi-choice-and-check.svg", 670,
         "POIの候補選びと確認", "用途によりOverture、Foursquare、OpenStreetMapを候補とする。どの候補も同じ小範囲で試し、条件と品質を確認する。順位や排他的な選択を示す図ではない。", body)

    body = f'<rect x="24" y="78" width="492" height="504" rx="16" fill="#e8eef5" stroke="{NAVY}" stroke-width="2"/>'
    body += text(270, 115, "Map：地図画面を組み立てる", 24, True)
    body += box(48, 138, 444, 76, "View：どこを、どう見るか", "中心・ズーム・投影法", "#fff0e6")
    body += text(270, 254, "複数のレイヤーを重ねて表示", 22)
    body += box(44, 276, 214, 76, "Layer A", "背景を描く")
    body += box(282, 276, 214, 76, "Layer B", "店舗の点を描く")
    body += arrow("M 60 430 V 354") + arrow("M 478 430 V 354")
    body += text(151, 401, "データを渡す", 20) + text(389, 401, "データを渡す", 20)
    body += box(44, 432, 214, 76, "Source A", "タイルを読む")
    body += box(282, 432, 214, 76, "Source B", "店舗データを読む")
    body += text(270, 552, "各Layerに、対応するSourceを設定", 22)
    body += text(270, 620, "二つのレイヤーを使う構成例", 22)
    save("openlayers", "map-view-layer-source.svg", 646,
         "OpenLayersの部品の関係", "MapはViewとレイヤー群を持つ。Viewは中心、ズーム、投影法を管理し、各レイヤーはSourceからデータを受け取る。背景と店舗の二つのレイヤーを重ねる例。", body)


if __name__ == "__main__":
    main()
