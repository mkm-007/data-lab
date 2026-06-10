#!/usr/bin/env python3
import argparse
import json

from datalab.pipeline import run

CHOICES = ["telemetry", "map", "catastrophe", "gtm"]


def main() -> None:
    parser = argparse.ArgumentParser(description="Run data-lab ETL and QA pipeline")
    parser.add_argument("--dataset", choices=CHOICES, required=True)
    args = parser.parse_args()
    print(json.dumps(run(args.dataset), indent=2))


if __name__ == "__main__":
    main()
