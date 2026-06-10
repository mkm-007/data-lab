from datalab.config import DATASETS, DATA_DIR
from datalab.ingest import ingest_csv


def test_all_samples_load():
    for name, cfg in DATASETS.items():
        df, meta = ingest_csv(DATA_DIR / cfg["file"], cfg["required_columns"])
        assert len(df) >= 10
        assert meta["row_count"] == len(df)
