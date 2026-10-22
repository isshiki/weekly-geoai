"""Create an original conceptual illustration; no real map or user data."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
im = Image.new('RGB', (1080, 1280), '#F4F6FA')
d = ImageDraw.Draw(im)
FONT = Path('C:/Windows/Fonts')

def text(x, y, value, size=44, color='#203047', bold=False):
    font = ImageFont.truetype(str(FONT / ('BIZ-UDGothicB.ttc' if bold else 'BIZ-UDGothicR.ttc')), size)
    d.text((x, y), value, font=font, fill=color, spacing=16)

text(64, 58, '会話で地図を使う、2つの用途', 54, bold=True)
text(64, 145, '同じチャットでも、任せる仕事が違う', 38, '#526175')

def card(y, accent, title, prompt, result, example, analysis=False):
    d.rounded_rectangle((48, y, 1032, y+450), radius=28, fill='white')
    d.rounded_rectangle((48, y, 62, y+450), radius=7, fill=accent)
    text(90, y+35, title, 52, accent, True)
    text(90, y+122, prompt, 43, bold=True)
    text(90, y+243, result, 40)
    text(90, y+370, example, 35, '#526175')
    # Schematic maps: lines and pins versus colored aggregation cells.
    x, top = 778, y+126
    d.rounded_rectangle((x, top, x+204, top+204), radius=14, fill='#EDF2F6')
    if analysis:
        colors = ['#D7EDE7','#A9D4C5','#6CB29B','#BCE0D3','#2C8068','#80BCA8','#8FC7B5','#4C987F','#CBE6DD']
        for row in range(3):
            for col in range(3):
                a, b = x+12+col*61, top+12+row*61
                d.rectangle((a,b,a+56,b+56), fill=colors[row*3+col])
    else:
        for offset in (50, 100, 150):
            d.line((x+offset,top+8,x+offset,top+196), fill='white', width=10)
            d.line((x+8,top+offset,x+196,top+offset), fill='white', width=10)
        for a,b in ((48,62),(139,94),(90,158)):
            d.polygon(((x+a-13,top+b),(x+a+13,top+b),(x+a,top+b+24)), fill=accent)
            d.ellipse((x+a-16,top+b-23,x+a+16,top+b+9), fill=accent)
            d.ellipse((x+a-5,top+b-12,x+a+5,top+b-2), fill='white')

card(230, '#285DA8', '場所を探す・比べる',
     '「条件に合うお店を\n　探して」', '候補・写真を比べる\n所在地を地図で確認',
     '例：ChatGPTの地図、Googleマップ')
card(720, '#26735D', '地理データを分析する',
     '「店舗と人口データを\n　重ねて集計して」', 'データを加工・集計\n分析結果を地図に表示',
     '例：CARTO、QGIS＋Mapsuke', True)
text(64, 1204, '概念図｜代表的な用途の比較。機能は重なり得ます。', 31, '#526175')
im.save(ROOT / 'conversational-map-comparison.png')
