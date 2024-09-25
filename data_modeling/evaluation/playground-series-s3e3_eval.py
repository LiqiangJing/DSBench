

import os.path

import numpy as np
import pandas as pd
import argparse

from sklearn.metrics import roc_auc_score

parser = argparse.ArgumentParser()

parser.add_argument('--path', type=str, required=True)
parser.add_argument('--name', type=str, required=True)
parser.add_argument('--answer_file', type=str, required=True)
parser.add_argument('--predict_file', type=str, required=True)

parser.add_argument('--value', type=str, default="Attrition")

args = parser.parse_args()


actual = pd.read_csv(args.answer_file)
submission = pd.read_csv(args.predict_file)

actual.sort_values(by=actual.columns[0])
submission.sort_values(by=submission.columns[0])

# 计算平均错误率
performance = roc_auc_score(actual[args.value], submission[args.value])



with open(os.path.join(args.path, args.name, "result.txt"), "w") as f:
    f.write(str(performance))
