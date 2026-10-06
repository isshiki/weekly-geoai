"""Regenerate the educational SVG from the exercise's exact input masks."""
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("exercise", ROOT / "docs/assets/exercises/imagery_evaluation.py")
exercise = importlib.util.module_from_spec(spec)
spec.loader.exec_module(exercise)


def main():
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 850" role="img" aria-labelledby="title desc">',
             '<title id="title">16画素の正解・予測・照合</title>',
             '<desc id="desc">正解は建物6画素。予測との照合はTP4、FP1、FN2、TN9。</desc>',
             '<rect width="420" height="850" fill="#ffffff"/>',
             '<g font-family="sans-serif" text-anchor="middle" fill="#1E3A5F">']
    labels = {(1, 1): 'TP', (0, 1): 'FP', (1, 0): 'FN', (0, 0): 'TN'}
    colors = {'1': '#1E3A5F', '0': '#edf2f7', 'TP': '#1E3A5F',
              'FP': '#FF8A3D', 'FN': '#ffddc7', 'TN': '#edf2f7'}
    for panel, heading in enumerate(('正解：建物 6画素', '予測：建物 5画素', '照合：TP 4 / FP 1 / FN 2 / TN 9')):
        top = 48 + panel * 270
        parts.append(f'<text x="210" y="{top-18}" font-size="20">{heading}</text>')
        for row in range(4):
            for col in range(4):
                actual, predicted = exercise.TRUTH[row][col], exercise.PREDICTION[row][col]
                label = str((actual, predicted)[panel]) if panel < 2 else labels[actual, predicted]
                x, y = 106 + col * 52, top + row * 52
                parts.append(f'<rect x="{x}" y="{y}" width="52" height="52" fill="{colors[label]}" stroke="#778899"/>')
                ink = '#ffffff' if label in ('1', 'TP') else '#1E3A5F'
                parts.append(f'<text x="{x+26}" y="{y+33}" font-size="20" fill="{ink}">{label}</text>')
    parts.append('<text x="210" y="840" font-size="17">1 = 建物 / 0 = 背景（架空データ）</text></g></svg>')
    target = ROOT / 'docs/assets/atlas/imagery-evaluation-exercise/pixel-comparison.svg'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text('\n'.join(parts) + '\n', encoding='utf-8')
    print(target.relative_to(ROOT))


if __name__ == '__main__':
    main()
