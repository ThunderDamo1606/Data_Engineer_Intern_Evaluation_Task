"""
website_pipeline_dag.py
-----------------------
Airflow DAG responsible for running the complete
website data ingestion pipeline.
"""

import sys
import os

# Add project root to Python path
# This is needed so we can import files from src/ folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import json

# Import pipeline modules
from src.crawler import crawl_website, save_raw_html
from src.extractor import extract_sections
from src.transformer import transform
from src.aggregator import compute_metrics


# List of websites that will be crawled
# You can add more URLs here anytime
WEBSITES = [
    "https://openai.com",
    "https://stripe.com",
    "https://shopify.com"
]


def run_pipeline():
    """
    Executes the complete pipeline step-by-step:

    1. Crawl each website
    2. Save raw HTML
    3. Extract important sections
    4. Transform data into standard format
    5. Generate analytics metrics
    """

    # This will store records from all websites
    all_records = []

    # Loop through each website
    for website_url in WEBSITES:

        # Step 1: Crawl website
        html, meta = crawl_website(website_url)

        # If crawl fails, skip this website
        if not html:
            continue

        # Step 2: Save raw HTML
        # Convert URL to folder-friendly name
        site_name = website_url.replace("https://", "").replace(".", "_")
        save_raw_html(site_name, html)

        # Step 3: Extract structured content
        sections = extract_sections(html)

        # Step 4: Transform extracted data
        records = transform(website_url, sections)

        # Add records to main list
        all_records.extend(records)

    # Save processed structured data to file
    os.makedirs("data/processed", exist_ok=True)

    with open("data/processed/structured.json", "w") as f:
        json.dump(all_records, f, indent=2)

    # Step 5: Compute analytics metrics
    metrics = compute_metrics(all_records)

    os.makedirs("data/analytics", exist_ok=True)

    with open("data/analytics/metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)


# DAG Configuration
with DAG(
    dag_id="growthpal_pipeline",          # Unique DAG name
    start_date=datetime(2026, 1, 1),      # DAG start date
    schedule_interval="@daily",           # Runs once every day
    catchup=False,                        # Do not backfill old runs
    default_args={
        "retries": 3,                     # Retry failed task 3 times
        "retry_delay": timedelta(minutes=2)  # Wait 2 min before retry
    }
) as dag:

    # Single task that runs full pipeline
    run_pipeline_task = PythonOperator(
        task_id="run_full_pipeline",
        python_callable=run_pipeline
    )
