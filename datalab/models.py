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


def gtm_deal_size_model(df: pd.DataFrame) -> dict | None:
    """Lead-value baseline for demand-gen / GTM pipelines."""
    if len(df) < 8 or "amount_usd" not in df.columns:
        return None
    feature_cols = [c for c in ("segment", "region", "stage") if c in df.columns]
    if not feature_cols:
        return None
    features = pd.get_dummies(df[feature_cols], drop_first=True)
    target = df["amount_usd"]
    x_train, x_test, y_train, y_test = train_test_split(
        features, target, test_size=0.3, random_state=42
    )
    model = RandomForestRegressor(n_estimators=50, random_state=42)
    model.fit(x_train, y_train)
    preds = model.predict(x_test)
    return {
        "target": "amount_usd",
        "mae": round(float(mean_absolute_error(y_test, preds)), 3),
        "train_rows": len(x_train),
        "test_rows": len(x_test),
        "features": list(features.columns),
    }
