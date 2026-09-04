from __future__ import annotations

import argparse
from io import BytesIO
from pathlib import Path

try:
    import cairosvg
    from PIL import Image, ImageDraw, ImageFont
except ImportError as exc:
    raise SystemExit(
        "ロゴ書き出し用依存がありません。`uv sync --group logo`を実行してください。"
    ) from exc


REPO_ROOT = Path(__file__).resolve().parents[1]
EXPORT_SIZES = (1024, 256)
PREVIEW_SIZES = (160, 64, 48, 32)


def render_png(svg_bytes: bytes, size: int) -> bytes:
    if size < 1:
        raise ValueError("sizeは1以上である必要があります")
    return cairosvg.svg2png(
        bytestring=svg_bytes,
        output_width=size,
        output_height=size,
    )


def create_preview(svg_bytes: bytes, output: Path) -> None:
    cell_widths = (200, 120, 100, 80)
    gap = 12
    margin = 20
    baseline = 188
    canvas_width = sum(cell_widths) + gap * (len(cell_widths) - 1) + margin * 2
    canvas = Image.new("RGB", (canvas_width, 232), "#F3F4F6")
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.load_default()

    x = margin
    for size, cell_width in zip(PREVIEW_SIZES, cell_widths, strict=True):
        cell_left = x
        cell_right = x + cell_width
        draw.rounded_rectangle(
            (cell_left, 16, cell_right, 216),
            radius=8,
            fill="#FFFFFF",
            outline="#D1D5DB",
            width=1,
        )
        logo_bytes = render_png(svg_bytes, size)
        with Image.open(BytesIO(logo_bytes)) as logo:
            logo = logo.convert("RGBA")
            logo_x = cell_left + (cell_width - size) // 2
            logo_y = baseline - size
            canvas.paste(logo, (logo_x, logo_y), logo)

        label = f"{size} px"
        label_box = draw.textbbox((0, 0), label, font=font)
        label_width = label_box[2] - label_box[0]
        draw.text(
            (cell_left + (cell_width - label_width) // 2, 198),
            label,
            fill="#1E3A5F",
            font=font,
        )
        x = cell_right + gap

    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output, format="PNG", optimize=True)


def export_logo(svg_path: Path, assets_dir: Path) -> list[Path]:
    if not svg_path.exists():
        raise FileNotFoundError(f"SVGが見つかりません: {svg_path}")
    svg_bytes = svg_path.read_bytes()
    assets_dir.mkdir(parents=True, exist_ok=True)

    outputs: list[Path] = []
    for size in EXPORT_SIZES:
        output = assets_dir / f"logo-{size}.png"
        output.write_bytes(render_png(svg_bytes, size))
        with Image.open(output) as image:
            if image.size != (size, size):
                raise RuntimeError(f"出力サイズが不正です: {output} = {image.size}")
            corner = image.convert("RGBA").getpixel((0, 0))
            if corner != (30, 58, 95, 255):
                raise RuntimeError(f"背景の四隅が不透明な濃紺ではありません: {output} = {corner}")
        outputs.append(output)

    preview = assets_dir / "logo-preview.png"
    create_preview(svg_bytes, preview)
    with Image.open(preview) as image:
        if image.size != (576, 232):
            raise RuntimeError(f"プレビューサイズが不正です: {preview} = {image.size}")
    outputs.append(preview)
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser(
        description="週刊GeoAIのSVGロゴからPNGと縮小プレビューを書き出す"
    )
    parser.add_argument("--svg", type=Path, default=REPO_ROOT / "assets" / "logo.svg")
    parser.add_argument("--assets-dir", type=Path, default=REPO_ROOT / "assets")
    args = parser.parse_args()

    svg_path = args.svg if args.svg.is_absolute() else REPO_ROOT / args.svg
    assets_dir = args.assets_dir if args.assets_dir.is_absolute() else REPO_ROOT / args.assets_dir
    try:
        outputs = export_logo(svg_path, assets_dir)
    except (OSError, RuntimeError, ValueError) as exc:
        parser.error(str(exc))

    for output in outputs:
        try:
            display = output.relative_to(REPO_ROOT)
        except ValueError:
            display = output
        print(f"生成しました: {display}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
