# data-lab

Personal data pipeline lab for ETL, validation, feature summaries, lightweight ML baselines, and QA reporting.

| Dataset | Command | JD fit |
|---------|---------|--------|
| `telemetry_events.csv` | `--dataset telemetry` | Data infra, event logs, observability |
| `map_features.csv` | `--dataset map` | HD maps, geospatial QA |
| `catastrophe_events.csv` | `--dataset catastrophe` | Risk/regional analytics |
| `gtm_pipeline.csv` | `--dataset gtm` | GTM funnel, demand gen, pipeline ML baselines |

**Interview:** same repo — run the dataset that matches the role you applied for. Datasets are modules, not separate repos.

## Quick start

```bash
cd labs/data-lab
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python run_pipeline.py --dataset gtm
python run_pipeline.py --dataset telemetry
pytest -q
```

## Push to GitHub

```bash
cd labs/data-lab
git init
git add .
git commit -m "feat: initial data-lab ETL and QA pipeline"
git branch -M main
git remote add origin git@github.com:mkm-007/data-lab.git
git push -u origin main
```
