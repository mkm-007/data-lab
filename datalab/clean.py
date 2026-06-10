from __future__ import annotations

import pandas as pd


def dedupe_rows(df: pd.DataFrame, key: str) -> tuple[pd.DataFrame, dict]:
    before = len(df)
    cleaned = df.drop_duplicates(subset=[key], keep="first")
    return cleaned, {
        "rows_before": before,
        "rows_after": len(cleaned),
        "rows_removed": before - len(cleaned),
    }
