Add-Type -AssemblyName System.Drawing
$assetRoot = Join-Path $PSScriptRoot '../drafts/assets/2026-11-27'
$navy = '#20364B'; $teal = '#147D80'; $orange = '#D88236'
function Brush($c) { return [System.Drawing.SolidBrush]::new([System.Drawing.ColorTranslator]::FromHtml($c)) }
function Txt($s,$x,$y,$size=38,$color=$navy) {
 $f=[System.Drawing.Font]::new('Yu Gothic',$size,[System.Drawing.FontStyle]::Bold,[System.Drawing.GraphicsUnit]::Pixel)
 $b=Brush $color; $script:g.DrawString($s,$f,$b,[single]$x,[single]$y);$f.Dispose();$b.Dispose()
}
function Box($x,$y,$w,$h,$color) { $b=Brush $color;$script:g.FillRectangle($b,$x,$y,$w,$h);$b.Dispose() }
function Line($x1,$y1,$x2,$y2,$color=$teal,$width=6) { $p=[System.Drawing.Pen]::new([System.Drawing.ColorTranslator]::FromHtml($color),$width);$script:g.DrawLine($p,$x1,$y1,$x2,$y2);$p.Dispose() }
function Down($x,$y) {Line $x $y $x ($y+40);Line ($x-13) ($y+26) $x ($y+40);Line ($x+13) ($y+26) $x ($y+40)}
function Canvas($h) { $script:im=[System.Drawing.Bitmap]::new(1200,$h);$script:g=[System.Drawing.Graphics]::FromImage($script:im);$script:g.SmoothingMode='AntiAlias';$script:g.TextRenderingHint='AntiAliasGridFit';$script:g.Clear([System.Drawing.ColorTranslator]::FromHtml('#F5F7FA')) }
function Save($name) {$script:im.Save((Join-Path $assetRoot $name),[System.Drawing.Imaging.ImageFormat]::Png);$script:g.Dispose();$script:im.Dispose()}
New-Item -ItemType Directory -Force $assetRoot | Out-Null
function Dot($x,$y,$c,$r=22) { $b=Brush $c;$script:g.FillEllipse($b,($x-$r),($y-$r),($r*2),($r*2));$b.Dispose() }
Canvas 1060
Box 55 40 1090 130 '#20364B'
Txt '「家賃10万円以下の物件だけ見せて」' 90 80 43 '#FFFFFF'
Down 600 190
Box 180 255 840 100 '#DCEDEE'
Txt 'AIが、地図の絞り込み機能を呼び出す' 210 280 37
Down 600 375
for($i=0;$i -lt 2;$i++){
 $x=55+560*$i;Box $x 445 530 400 '#FFFFFF'
 Txt @('条件を絞る前','条件に合う物件を表示')[$i] ($x+25) 460 35
 for($j=0;$j -lt 3;$j++){Line ($x+30) (560+100*$j) ($x+500) (560+100*$j) '#E1E7EC' 18}
 Line ($x+150) 530 ($x+150) 820 '#E1E7EC' 18
 Line ($x+375) 530 ($x+375) 820 '#E1E7EC' 18
 Dot ($x+150) 560 $teal;Txt '8万円' ($x+175) 570 32
 Dot ($x+375) 760 $teal;Txt '9万円' ($x+400) 770 32
 if($i -eq 0){Dot ($x+150) 760 '#87939F';Txt '12万円' ($x+175) 770 32;Dot ($x+375) 560 '#87939F';Txt '15万円' ($x+390) 570 30}
}
Txt '画面で結果を確認し、条件を変えて頼める' 120 885 40
Txt 'サイトへの組み込みと、対応するブラウザ・AI環境が必要' 65 965 31
Save 'mapbox-map-control.png'
Canvas 1040
Txt '学校と市が、同じ地図を見ながら相談' 70 35 43
Box 55 115 1090 575 '#FFFFFF'
Line 105 290 1090 290 '#DCE3E9' 26
Line 105 510 1090 510 '#DCE3E9' 26
Line 360 170 360 650 '#DCE3E9' 26
Line 810 170 810 650 '#DCE3E9' 26
Box 110 355 155 100 '#20364B';Txt '学校' 145 375 40 '#FFFFFF'
Line 270 410 360 410 $teal 8;Line 360 410 360 290 $teal 8;Line 360 290 810 290 $teal 8;Line 810 290 810 510 $teal 8
Dot 360 290 $navy 27;Txt 'A' 346 266 33 '#FFFFFF'
Box 120 155 405 80 '#E9EEF3';Txt 'A：前回、現地を点検' 140 175 33
Dot 810 510 $orange 29;Txt 'B' 796 486 33 '#FFFFFF'
Box 610 580 480 75 '#FAEBDD';Txt 'B：次に確認したい交差点' 625 600 30
Box 650 365 450 65 '#FFFFFF'
Txt '見通しや交通量が気になる' 665 375 30
Line 810 425 810 470 $orange 4
Box 70 730 24 24 $navy;Txt '過去の点検記録' 110 716 32
Box 480 730 24 24 $orange;Txt '気になる場所' 520 716 32
Line 860 742 915 742 $teal 7;Txt '通学路' 930 716 32
Down 600 790
Box 55 860 1090 105 '#20364B'
Txt '「次はBを、通学時間帯に確かめよう」' 125 890 42 '#FFFFFF'
Txt '架空の例。点検済みという記録は、安全の保証ではありません。' 75 985 29
Save 'school-route-review.png'
