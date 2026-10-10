"""Render the October 10 comparison sample. Requires Pillow and repo venv Markdown."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import base64
import math
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ASSETS = HERE / 'assets/2026-10-10-news-pilot'
ASSETS.mkdir(parents=True, exist_ok=True)
NAVY, ORANGE, GRAY = '#1e3a5f', '#e27c32', '#576b7e'
FONT = 'C:/Windows/Fonts/meiryo.ttc'

def font(size):
    return ImageFont.truetype(FONT, size)

def canvas(kicker, title):
    im = Image.new('RGB', (1200, 500), '#f0f5f8')
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, 12, 500), fill=ORANGE)
    d.text((48, 28), kicker, font=font(21), fill=GRAY)
    d.text((48, 69), title, font=font(37), fill=NAVY)
    return im, d

def arrow(d, x, y):
    d.line((x, y, x+52, y), fill=ORANGE, width=5)
    d.polygon([(x+52,y),(x+38,y-10),(x+38,y+10)], fill=ORANGE)

im, d = canvas('MAPBOX CLI  /  CONCEPT', 'AIから地図サービスへ、操作の入口を整える')
for x, title, lines in [(48,'AIアシスタント',['自然言語の指示を','操作につなぐ']), (448,'Mapbox CLI',['仕様を取得','送信前に変更を検証']), (848,'Mapbox APIs',['場所を検索','地図の見た目を変更'])]:
    d.rounded_rectangle((x,180,x+300,370), radius=18, fill='white', outline='#cfdae4', width=2)
    d.text((x+22,207), title, font=font(29), fill=NAVY)
    for i,line in enumerate(lines):
        d.text((x+22,270+i*37), line, font=font(25), fill=GRAY)
for x in [367,767]:
    arrow(d,x,275)
d.text((48,429),'週刊GeoAI 作成  ｜  公式説明に基づく概念図・製品画面ではありません',font=font(21),fill=GRAY)
im.save(ASSETS/'mapbox-cli.png')

im,d = canvas('LEON  /  RESEARCH', '施設の分布から、地域の特徴を数値にする')
for cx,cy in [(130,231),(228,231),(179,316)]:
    points=[(cx+56*math.cos(math.radians(30+60*i)),cy+56*math.sin(math.radians(30+60*i))) for i in range(6)]
    d.polygon(points,fill='#e0ebf2',outline=NAVY,width=2)
    for j,(dx,dy) in enumerate([(-16,-12),(15,8),(-9,21)]):
        d.ellipse((cx+dx-5,cy+dy-5,cx+dx+5,cy+dy+5),fill=[ORANGE,NAVY,'#439688'][j])
d.text((48,379),'施設の種類・数と隣接関係',font=font(24),fill=NAVY)
arrow(d,360,275)
d.rounded_rectangle((445,193,739,354),radius=18,fill='white',outline='#cfdae4',width=2)
d.text((481,215),'地域の特徴を学習',font=font(26),fill=NAVY)
for i,h in enumerate([25,60,37,75,49,32]):
    d.rectangle((482+i*37,323-h,504+i*37,323),fill=ORANGE if i%2 else NAVY)
d.text((470,379),'埋め込み（数値列）',font=font(24),fill=NAVY)
arrow(d,771,275)
d.rounded_rectangle((856,193,1152,354),radius=18,fill='white',outline='#cfdae4',width=2)
d.text((886,226),'住宅価格の予測など',font=font(25),fill=NAVY)
d.text((886,274),'分析への応用を評価',font=font(25),fill=GRAY)
d.text((48,441),'週刊GeoAI 作成  ｜  区画・点・数値列は説明用。実データ・実験結果ではありません',font=font(20),fill=GRAY)
im.save(ASSETS/'leon.png')

source = HERE/'2026-10-10-news-pilot.md'
body = source.read_text(encoding='utf-8').split('---',2)[2].strip()
result = subprocess.run([str(ROOT/'.venv/Scripts/python.exe'), '-X','utf8','-c',
    'import markdown,sys; print(markdown.markdown(sys.stdin.read()))'], input=body,
    encoding='utf-8',capture_output=True,check=True)
html = result.stdout
for p in ASSETS.glob('*.png'):
    html = html.replace('assets/2026-10-10-news-pilot/'+p.name,'data:image/png;base64,'+base64.b64encode(p.read_bytes()).decode())
css = '''body{margin:0;background:#edf1f4;color:#263746;font-family:Meiryo,"Yu Gothic",sans-serif;font-size:16px;line-height:1.9}main{max-width:680px;margin:36px auto;padding:40px 44px;background:white;border-top:7px solid #1e3a5f}h1{font-size:16px;letter-spacing:.08em;color:#576b7e;margin:0 0 20px}h1+p{font-size:29px;line-height:1.5;color:#1e3a5f;margin:0 0 16px}h1+p+p{font-size:13px;color:#647687}h2{font-size:20px;border-top:2px solid #1e3a5f;margin-top:40px;padding-top:20px;color:#1e3a5f}h3{font-size:22px;line-height:1.6;margin:30px 0 14px;color:#1e3a5f}p{margin:14px 0}img{display:block;width:100%;height:auto;border-radius:8px}p:has(>em){font-size:12px;color:#647687;line-height:1.65}em{font-style:normal}a{color:#14657c;text-decoration:none;border-bottom:1px solid #b7ced7}hr{border:0;border-top:1px solid #d9e1e7;margin-top:36px}strong{font-weight:700}@media(max-width:600px){main{margin:0;padding:26px 20px}h1+p{font-size:25px}h3{font-size:20px}}'''
(HERE/'2026-10-10-news-pilot.html').write_text('<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>週刊GeoAI ニュース版サンプル</title><style>'+css+'</style></head><body><main>'+html+'</main></body></html>',encoding='utf-8')
print('Rendered sample HTML and two original PNG illustrations.')
