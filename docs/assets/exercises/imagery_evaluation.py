"""Evaluate synthetic binary masks; standard library only, no I/O or model."""
import json
import platform

TRUTH = ((1, 1, 1, 0), (1, 1, 1, 0), (0, 0, 0, 0), (0, 0, 0, 0))
PREDICTION = ((1, 1, 0, 0), (1, 0, 1, 0), (0, 0, 0, 1), (0, 0, 0, 0))


def evaluate(truth, prediction):
    """One equally weighted pixel per cell. Undefined ratios become None."""
    if not truth or not truth[0]:
        raise ValueError("Masks must be nonempty")
    width = len(truth[0])
    if len(truth) != len(prediction) or any(
        len(row) != width for mask in (truth, prediction) for row in mask
    ):
        raise ValueError("Masks must be rectangular and have the same shape")
    if any(value not in (0, 1) for mask in (truth, prediction) for row in mask for value in row):
        raise ValueError("Masks must contain only 0 and 1")
    counts = dict.fromkeys(("TP", "FP", "FN", "TN"), 0)
    for actual_row, predicted_row in zip(truth, prediction):
        for actual, predicted in zip(actual_row, predicted_row):
            key = {(1, 1): "TP", (0, 1): "FP", (1, 0): "FN", (0, 0): "TN"}[actual, predicted]
            counts[key] += 1
    tp, fp, fn, tn = (counts[key] for key in ("TP", "FP", "FN", "TN"))
    def ratio(numerator, denominator):
        return numerator / denominator if denominator else None
    return {
        **counts,
        "precision": ratio(tp, tp + fp),
        "recall": ratio(tp, tp + fn),
        "iou": ratio(tp, tp + fp + fn),
        "accuracy": ratio(tp + tn, tp + fp + fn + tn),
    }


def main():
    result = evaluate(TRUTH, PREDICTION)
    expected = dict(TP=4, FP=1, FN=2, TN=9, precision=4/5, recall=4/6, iou=4/7, accuracy=13/16)
    if result != expected:
        raise RuntimeError(f"Unexpected result: {result}")
    print(json.dumps({"python": platform.python_version(), "pixels": 16,
                      "result": result, "check": "PASS"}, indent=2))


if __name__ == "__main__":
    main()
