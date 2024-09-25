

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

parser.add_argument('--value', type=str, default="claim")

args = parser.parse_args()

# Compute MAE
def mean_absolute_error(y_true, y_pred):
    return np.mean(np.abs(y_pred - y_true))


answers = pd.read_csv(args.answer_file)
predictions = pd.read_csv(args.predict_file)
answers.sort_values(by=["id"])
predictions.sort_values(by=['id'])
y_true = answers[args.value].values
y_pred = predictions[args.value].values




performance = roc_auc_score(y_true, y_pred)


with open(os.path.join(args.path, args.name, "result.txt"), "w") as f:
    f.write(str(performance))



