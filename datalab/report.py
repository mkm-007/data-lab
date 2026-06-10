from __future__ import annotations

import json
from pathlib import Path


def write_reports(out_dir: Path, payload: dict) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "qa_report.json").write_text(json.dumps(payload, indent=2))
    lines = [
        f"Dataset: {payload.get('dataset')}",
        f"Rows after clean: {payload['clean']['rows_after']}",
        f"Categories: {payload.get('top_categories', {})}",
    ]
    if payload.get("top_segments"):
        lines.append(f"Segments: {payload['top_segments']}")
    (out_dir / "qa_report.txt").write_text("\n".join(lines) + "\n")
