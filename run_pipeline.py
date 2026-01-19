"""
run_pipeline.py
---------------
Direct pipeline runner
(no Airflow dependency)
"""

from src.crawler import crawl_website, save_raw_html
from src.extractor import extract_sections
from src.transformer import transform
from src.aggregator import compute_metrics

import os
import json

WEBSITES = [
    "https://openai.com",
    "https://stripe.com",
    "https://shopify.com"
]


def main():

    all_records = []

    for site in WEBSITES:

        print(f"Crawling -> {site}")

        html, meta = crawl_website(site)

        if not html:
            continue

        # Save raw html
        site_name = site.replace("https://", "").replace(".", "_")
        save_raw_html(site_name, html)

        # Extract
        sections = extract_sections(html)

        # Transform
        records = transform(site, sections)
        all_records.extend(records)

    # Save processed
    os.makedirs("data/processed", exist_ok=True)

    with open("data/processed/structured.json", "w") as f:
        json.dump(all_records, f, indent=2)

    # Aggregate
    metrics = compute_metrics(all_records)

    os.makedirs("data/analytics", exist_ok=True)

    with open("data/analytics/metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)

    print("Pipeline completed successfully")


if __name__ == "__main__":
    main()
