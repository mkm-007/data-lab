from __future__ import annotations

import pandas as pd


def ingest_csv(path, required_columns: list[str]) -> tuple[pd.DataFrame, dict]:
    df = pd.read_csv(path)
    missing = [c for c in required_columns if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    meta = {
        "row_count": len(df),
        "columns": list(df.columns),
        "null_counts": df.isna().sum().to_dict(),
    }
    return df, meta
