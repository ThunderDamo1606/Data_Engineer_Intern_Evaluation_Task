"""
website_pipeline_dag.py
-----------------------
Airflow DAG to orchestrate pipeline
"""
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import json
import os

from src.crawler import crawl_website, save_raw_html
from src.extractor import extract_sections
from src.transformer import transform
from src.aggregator import compute_metrics


WEBSITES = [
    "https://openai.com",
    "https://stripe.com",
    "https://shopify.com"
]


def run_pipeline():
    """
    Main pipeline flow:
    1. Crawl websites
    2. Store raw HTML
    3. Extract sections
    4. Transform data
    5. Aggregate metrics
    """

    all_records = []

    for site in WEBSITES:

        html, meta = crawl_website(site)

        if not html:
            continue

        # Store raw html
        site_name = site.replace("https://", "").replace(".", "_")
        save_raw_html(site_name, html)

        # Extract
        sections = extract_sections(html)

        # Transform
        records = transform(site, sections)
        all_records.extend(records)

    # Save processed data
    os.makedirs("data/processed", exist_ok=True)

    with open("data/processed/structured.json", "w") as f:
        json.dump(all_records, f, indent=2)

    # Aggregate metrics
    metrics = compute_metrics(all_records)

    os.makedirs("data/analytics", exist_ok=True)

    with open("data/analytics/metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)

with DAG(
    dag_id="growthpal_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    default_args={"retries": 2}
) as dag:

    run_task = PythonOperator(
        task_id="run_full_pipeline",
        python_callable=run_pipeline
    )
