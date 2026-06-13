from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "samples"
OUTPUT_DIR = ROOT / "outputs"

DATASETS = {
    "telemetry": {
        "file": "telemetry_events.csv",
        "required_columns": ["event_id", "vehicle_id", "timestamp", "event_type", "latency_ms"],
        "dedupe_key": "event_id",
        "category_col": "event_type",
    },
    "map": {
        "file": "map_features.csv",
        "required_columns": ["feature_id", "lane_id", "lat", "lon", "feature_type", "confidence"],
        "dedupe_key": "feature_id",
        "category_col": "feature_type",
        "model_target": "confidence",
    },
    "catastrophe": {
        "file": "catastrophe_events.csv",
        "required_columns": ["event_id", "region", "hazard_type", "severity", "event_date"],
        "dedupe_key": "event_id",
        "category_col": "hazard_type",
    },
    "gtm": {
        "file": "gtm_pipeline.csv",
        "required_columns": ["opportunity_id", "segment", "stage", "region", "amount_usd", "close_month"],
        "dedupe_key": "opportunity_id",
        "category_col": "stage",
        "segment_col": "segment",
    },
    "sports": {
        "file": "sports_projections.csv",
        "required_columns": [
            "projection_id",
            "sport",
            "player",
            "stat_type",
            "line",
            "projected",
            "actual",
            "game_date",
        ],
        "dedupe_key": "projection_id",
        "category_col": "sport",
        "stat_col": "stat_type",
    },
}
