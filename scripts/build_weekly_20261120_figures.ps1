Add-Type -AssemblyName System.Drawing
$assetRoot = Join-Path $PSScriptRoot '../drafts/assets/2026-11-20'
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
Canvas 1000
Txt '01  街路画像から店名などを読む' 55 28 44
Box 55 105 370 245 '#E5EBEE'
Box 100 155 280 160 '#FFFFFF';Box 90 135 300 55 '#147D80';Txt 'カフェ A' 142 143 32 '#FFFFFF'
Box 125 210 80 105 '#BBD8DB';Box 235 210 115 65 '#D6E8E9'
Txt '写真に写る情報を抽出' 485 140 38
Txt '店名・住所・電話番号など' 485 205 36
Txt '撮影位置も手掛かりに' 485 265 36
Down 600 365
Txt '02  既存の店舗データと照合' 55 425 44
Box 55 505 1090 125 '#FFFFFF'
Txt '同じ店？  情報が変わった？' 95 525 40
Txt '必要に応じて地図やWebの証拠を確認' 95 580 32
Down 600 650
Txt '03  追加・更新の要否を判断' 55 710 44
$labels=@('追加','更新','変更不要','保留')
for($i=0;$i -lt 4;$i++){ $x=55+275*$i; $c=if($i -eq 3){'#F5E4D2'}else{'#DCEDEE'};Box $x 790 250 80 $c;Txt $labels[$i] ($x+30) 807 38 }
Txt '不確かな候補は、人が確認する' 270 910 38
Save 'maps-poi.png'
Canvas 1100
Txt '出店候補の違いを、地図で調べる' 55 30 44
Box 55 115 1090 145 '#20364B'
Txt '「候補地AとBの周りに、どんな飲食店が' 85 140 38 '#FFFFFF'
Txt 'あるか地図にして」' 85 200 38 '#FFFFFF'
Down 600 280
Txt '対応するデータと機能につながったAIが作業' 80 345 36
for($i=0;$i -lt 2;$i++){
 $x=55+560*$i; Box $x 420 530 410 '#FFFFFF';Txt ('候補地'+@('A','B')[$i]) ($x+25) 435 40
 for($j=0;$j -lt 3;$j++){Line ($x+30) (545+90*$j) ($x+500) (545+90*$j) '#E1E7EC' 17}
 Line ($x+180) 515 ($x+180) 795 '#E1E7EC' 17
 Line ($x+380) 515 ($x+380) 795 '#E1E7EC' 17
 $pts=if($i -eq 0){@(@(120,570),@(230,680),@(420,570),@(315,730))}else{@(@(105,710),@(245,570),@(420,680),@(300,730))}
 foreach($pt in $pts){Box ($x+$pt[0]) $pt[1] 25 25 $orange}
 $b=Brush $teal;$script:g.FillEllipse($b,($x+170),625,40,40);$b.Dispose();Txt '候補地' ($x+220) 622 30
}
Box 60 865 22 22 $orange;Txt '飲食店' 95 853 30
Txt '位置・店の種類・集まり方を比較' 370 853 34
Down 600 915
Txt '「駅の反対側も含めたい」と条件を変える' 90 985 38
Save 'site-comparison.png'
