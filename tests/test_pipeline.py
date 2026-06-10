from datalab.pipeline import run


def test_telemetry_pipeline():
    result = run("telemetry")
    assert result["clean"]["rows_after"] == 10


def test_map_pipeline():
    result = run("map")
    assert result["clean"]["rows_after"] == 10
    assert result["baseline_model"] is not None


def test_catastrophe_pipeline():
    result = run("catastrophe")
    assert result["clean"]["rows_after"] == 10


def test_gtm_pipeline():
    result = run("gtm")
    assert result["clean"]["rows_after"] == 10
    assert "discovery" in result["top_categories"]
