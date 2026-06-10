from __future__ import annotations

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error


def baseline_regressor(df: pd.DataFrame, target: str) -> dict | None:
    numeric = df.select_dtypes(include="number")
    if target not in numeric.columns or len(numeric.columns) < 2:
        return None
    features = [c for c in numeric.columns if c != target]
    if len(df) < 8:
        return None
    x_train, x_test, y_train, y_test = train_test_split(
        df[features], df[target], test_size=0.3, random_state=42
    )
    model = RandomForestRegressor(n_estimators=50, random_state=42)
    model.fit(x_train, y_train)
    preds = model.predict(x_test)
    return {
        "target": target,
        "mae": round(float(mean_absolute_error(y_test, preds)), 3),
        "train_rows": len(x_train),
        "test_rows": len(x_test),
    }
