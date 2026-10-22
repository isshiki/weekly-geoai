"""Original library overview for the October 23 issue (Pillow, Windows fonts)."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
im = Image.new('RGB', (1200, 990), '#F4F6FA')
d = ImageDraw.Draw(im)

def text(x, y, value, size=40, color='#203047', bold=False):
    name = 'BIZ-UDGothicB.ttc' if bold else 'BIZ-UDGothicR.ttc'
    font = ImageFont.truetype(str(Path('C:/Windows/Fonts') / name), size)
    for line in value.splitlines():
        assert x + d.textlength(line, font=font) < 1170, line
    d.text((x, y), value, font=font, fill=color, spacing=14)

text(56, 42, '何を描く？ Web地図ライブラリ', 52, bold=True)
text(56, 120, '代表的な用途から見る、4つの選択肢', 36, '#526175')
rows = [
    (200, '#285DA8', '店舗・施設を地図に重ねる', 'MapLibre GL JS / MachGL'),
    (350, '#26735D', '多様な地理データを重ねる', 'OpenLayers'),
    (500, '#7855A0', '地球儀・地形・建物を3Dで', 'CesiumJS'),
]
for y, color, heading, names in rows:
    d.rounded_rectangle((48,y,1152,y+130), radius=20, fill='white')
    d.rounded_rectangle((48,y,61,y+130), radius=6, fill=color)
    text(88,y+20,heading,37,color,True)
    text(88,y+75,names,36)

text(56, 677, '今週の動き', 40, bold=True)
text(56, 740, 'MachGL', 37, '#285DA8', True)
text(310, 740, '11月9日公開予定・PLATEAU対応', 35)
text(56, 800, 'MapLibre', 37, '#285DA8', True)
text(310, 800, '独自の平面座標系に実験対応', 35)
text(56, 891, '用途は重なります。性能の順位や機能の網羅表ではありません。', 29, '#526175')
text(56, 939, '概念図｜2026年10月22日時点の公式情報から整理', 27, '#526175')
im.save(ROOT / 'web-map-library-overview.png')
