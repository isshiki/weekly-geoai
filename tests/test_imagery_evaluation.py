import importlib.util
from pathlib import Path
import unittest

PATH = Path(__file__).resolve().parents[1] / "docs/assets/exercises/imagery_evaluation.py"
spec = importlib.util.spec_from_file_location("imagery_evaluation", PATH)
exercise = importlib.util.module_from_spec(spec)
spec.loader.exec_module(exercise)


class ImageryEvaluationTests(unittest.TestCase):
    def test_example_counts_and_metrics(self):
        self.assertEqual(exercise.evaluate(exercise.TRUTH, exercise.PREDICTION),
                         dict(TP=4, FP=1, FN=2, TN=9, precision=.8, recall=2/3, iou=4/7, accuracy=13/16))

    def test_no_positive_prediction(self):
        result = exercise.evaluate(((1, 0),), ((0, 0),))
        self.assertIsNone(result["precision"])
        self.assertEqual(result["recall"], 0)
        self.assertEqual(result["iou"], 0)

    def test_all_background(self):
        result = exercise.evaluate(((0, 0),), ((0, 0),))
        self.assertEqual(result["accuracy"], 1)
        for name in ("precision", "recall", "iou"):
            self.assertIsNone(result[name])

    def test_reject_invalid_masks(self):
        for truth, prediction in (((), ()), (((1,),), ()),
                                  (((1, 0), (1,)), ((1, 0), (1, 0))),
                                  (((2,),), ((1,),))):
            with self.subTest(truth=truth, prediction=prediction):
                with self.assertRaises(ValueError):
                    exercise.evaluate(truth, prediction)
