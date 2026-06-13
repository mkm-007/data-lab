from __future__ import annotations

import pandas as pd

from datalab.clean import dedupe_rows
from datalab.config import DATA_DIR, DATASETS, OUTPUT_DIR
from datalab.features import numeric_summary, top_categories
from datalab.ingest import ingest_csv
from datalab.models import baseline_regressor, gtm_deal_size_model, sports_performance_model
from datalab.report import write_reports


def run(dataset: str) -> dict:
    cfg = DATASETS[dataset]
    path = DATA_DIR / cfg["file"]
    df, ingest_meta = ingest_csv(path, cfg["required_columns"])
    cleaned, clean_meta = dedupe_rows(df, cfg["dedupe_key"])

    payload = {
        "dataset": dataset,
        "ingest": ingest_meta,
        "clean": clean_meta,
        "numeric_summary": numeric_summary(cleaned),
        "top_categories": top_categories(cleaned, cfg["category_col"]),
    }
    if cfg.get("segment_col"):
        payload["top_segments"] = top_categories(cleaned, cfg["segment_col"])
    if cfg.get("stat_col"):
        payload["top_stat_types"] = top_categories(cleaned, cfg["stat_col"])
    if dataset == "gtm":
        payload["baseline_model"] = gtm_deal_size_model(cleaned)
    elif dataset == "sports":
        payload["baseline_model"] = sports_performance_model(cleaned)
    elif cfg.get("model_target"):
        payload["baseline_model"] = baseline_regressor(cleaned, cfg["model_target"])
    else:
        payload["baseline_model"] = None

    out_dir = OUTPUT_DIR / dataset
    write_reports(out_dir, payload)
    cleaned.to_csv(out_dir / "cleaned.csv", index=False)
    return payload
