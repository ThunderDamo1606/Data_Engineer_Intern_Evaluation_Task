"""
run_pipeline.py
---------------
Standalone pipeline runner.
This file runs the complete pipeline
without using Apache Airflow.
"""

from src.logger import setup_logger
from src.crawler import crawl_website, save_raw_html
from src.extractor import extract_sections
from src.transformer import transform
from src.aggregator import compute_metrics

import os
import json

# Initialize logger
logger = setup_logger()

# Websites selected for crawling
WEBSITES = [
    "https://openai.com",
    "https://stripe.com",
    "https://shopify.com"
]


def main():
    """
    Executes the complete pipeline locally:

    1. Crawl websites
    2. Store raw HTML
    3. Extract structured content
    4. Transform into standard format
    5. Generate analytics metrics
    """

    all_records = []

    # Loop through each website
    for website_url in WEBSITES:

        logger.info(f"Starting crawl -> {website_url}")

        # Step 1: Crawl website
        html, meta = crawl_website(website_url)

        # If crawl fails, skip website
        if not html:
            logger.error(f"Crawl failed -> {website_url}")
            continue

        # Step 2: Save raw HTML
        site_name = website_url.replace("https://", "").replace(".", "_")
        save_raw_html(site_name, html)

        # Step 3: Extract sections
        sections = extract_sections(html)

        # Step 4: Transform data
        records = transform(website_url, sections)
        all_records.extend(records)

    # Save processed structured data
    os.makedirs("data/processed", exist_ok=True)

    with open("data/processed/structured.json", "w") as f:
        json.dump(all_records, f, indent=2)

    # Generate analytics metrics
    metrics = compute_metrics(all_records)

    os.makedirs("data/analytics", exist_ok=True)

    with open("data/analytics/metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)

    logger.info("Pipeline completed successfully")


if __name__ == "__main__":
    main()
