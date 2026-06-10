from __future__ import annotations

import pandas as pd


def numeric_summary(df: pd.DataFrame) -> dict:
    numeric_cols = df.select_dtypes(include="number").columns
    summary = {}
    for col in numeric_cols:
        desc = df[col].describe()
        summary[col] = {k: round(float(v), 3) for k, v in desc.items()}
    return summary


def top_categories(df: pd.DataFrame, column: str, limit: int = 5) -> dict:
    if column not in df.columns:
        return {}
    return df[column].value_counts().head(limit).to_dict()
