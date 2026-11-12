"""Create a probability-weighted ensemble from stored individual submissions.

This is a post-project, reproducible helper. It does not retrain the 2024 models.
The original saved 6:2:2 submission does not exactly match the current saved
individual probability files; see docs/EXPERIMENT_NOTES.md.
"""

from __future__ import annotations
import argparse
from pathlib import Path
import numpy as np
import pandas as pd


def weighted_ensemble(xgb: pd.DataFrame, lgb: pd.DataFrame,
                      cat: pd.DataFrame, weights: list[float]) -> pd.DataFrame:
    """Combine XGBoost, LightGBM and CatBoost probabilities in that order."""
    total = sum(weights)
    if len(weights) != 3 or total <= 0 or any(x < 0 for x in weights):
        raise ValueError('Provide three nonnegative weights with positive sum')
    for model, df in [('XGB', xgb), ('LGB', lgb), ('CatBoost', cat)]:
        if list(df.columns) != ['index', 'health_status']:
            raise ValueError(f'{model}: expected index, health_status columns')
        if df['index'].duplicated().any() or df['health_status'].isna().any():
            raise ValueError(f'{model}: duplicate indices or missing predictions')
        if not df['health_status'].between(0, 1).all():
            raise ValueError(f'{model}: predictions are not probabilities in [0,1]')
    for model, df in [('LGB', lgb), ('CatBoost', cat)]:
        if not xgb['index'].reset_index(drop=True).equals(df['index'].reset_index(drop=True)):
            raise ValueError(f'Index order differs for {model}')
    w = np.asarray(weights, dtype=float) / total
    pred = w[0] * xgb['health_status'].to_numpy() + w[1] * lgb['health_status'].to_numpy() + w[2] * cat['health_status'].to_numpy()
    return pd.DataFrame({'index': xgb['index'].to_numpy(), 'health_status': pred})


def main() -> None:
    project = Path(__file__).resolve().parents[1]
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--weights', default='8,1,1', help='XGBoost,LightGBM,CatBoost weights')
    p.add_argument('--output', type=Path, default=project / 'results/submissions/reproduced_8_1_1.csv')
    args = p.parse_args()
    weights = [float(w) for w in args.weights.split(',')]
    subs = project / 'results' / 'submissions'
    frames = [pd.read_csv(subs / fn) for fn in ['xgb_prediction.csv', 'lightgbm_prediction.csv', 'catboost_prediction.csv']]
    out = weighted_ensemble(*frames, weights)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.output, index=False)
    print(f'Saved {len(out):,} rows to {args.output}')

if __name__ == '__main__':
    main()
