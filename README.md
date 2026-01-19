# Website Data Pipeline – Data Engineer Intern Project Task

## Overview

This project demonstrates an **end-to-end data engineering pipeline** designed to crawl multiple websites, extract meaningful content, transform it into a structured format, and generate analytical insights.

The solution reflects **real-world data engineering practices**, including modular code design, data layering, logging, and workflow orchestration.
The pipeline supports both **local execution** and **production-style orchestration using Apache Airflow**.

---

## Project Architecture

```
Growthpal-Pipeline/
│
├── dags/
│   └── website_pipeline_dag.py      # Airflow DAG definition
│
├── src/
│   ├── crawler.py                   # Website crawling logic
│   ├── extractor.py                 # HTML parsing & content extraction
│   ├── transformer.py               # Standardized data transformation
│   ├── aggregator.py                # Metrics & analytics computation
│   └── logger.py                    # Centralized logging configuration
│
├── data/
│   ├── raw/                         # Raw HTML (data lake – raw layer)
│   ├── processed/                  # Cleaned & structured data
│   └── analytics/                  # Aggregated metrics & insights
│
├── tests/
│   └── test_extractor.py            # Basic unit test
│
├── logs/
│   └── pipeline.log                 # Pipeline execution logs
│
├── run_pipeline.py                  # Local pipeline runner
├── websites.txt                    # Input websites list
├── requirements.txt                # Project dependencies
└── README.md
```

---

## Pipeline Workflow

### 1. Website Crawling

* Fetches website HTML using `requests`
* Captures metadata such as URL, status code, and crawl timestamp
* Persists raw HTML to simulate a **raw data layer**

```
data/raw/<website_name>/homepage.html
```

---

### 2. Content Extraction

HTML content is parsed using **BeautifulSoup**, and the following sections are extracted:

* Navigation bar
* Main homepage content
* Footer
* Case study links (heuristic based)

---

### 3. Data Transformation

Extracted content is normalized into a **standard JSON schema**:

```json
{
  "website": "https://example.com",
  "section": "homepage",
  "content": "Extracted text...",
  "crawl_timestamp": "2026-01-10T10:30:00Z",
  "isActive": true
}
```

Each website generates multiple records, one per extracted section.

---

### 4. Aggregation & Analytics

The pipeline computes high-level metrics, including:

* Number of websites containing case studies
* Content length statistics (minimum, maximum, average) by section

Metrics output location:

```
data/analytics/metrics.json
```

---

## Installation & Setup

### Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Pipeline

### Local Execution

Run the complete pipeline without orchestration:

```bash
python run_pipeline.py
```

Generated outputs:

* Raw HTML → `data/raw/`
* Structured data → `data/processed/structured.json`
* Metrics → `data/analytics/metrics.json`
* Logs → `logs/pipeline.log`

---

### Apache Airflow Orchestration

The project also includes an Airflow DAG for scheduled execution and monitoring.

**Steps:**

1. Initialize Airflow database
2. Create an admin user
3. Start Airflow services
4. Trigger DAG: `growthpal_pipeline`

---

## Configuration

### websites.txt

Defines the list of target websites:

```
https://openai.com
https://shopify.com
https://stripe.com
```

The pipeline dynamically processes all websites listed here.

---

## Key Design Decisions

| Component            | Rationale                            |
| -------------------- | ------------------------------------ |
| Modular architecture | Easier testing & maintainability     |
| Raw → processed flow | Industry-standard data lake pattern  |
| JSON format          | Analytics-ready & API-friendly       |
| Central logging      | Simplified debugging & observability |
| Airflow DAG          | Production-grade orchestration       |

---

## Error Handling & Reliability

* Network timeout handling during crawling
* Graceful skipping of failed websites
* Centralized logging for traceability
* Retry logic enabled at orchestration level

---

## Scalability & Future Enhancements

* Asynchronous crawling
* Cloud storage (S3 / GCS) integration
* Distributed processing (Spark)
* Dynamic Airflow DAG generation
* Monitoring & alerting

---

## Author

**Damodar Sadavarte**

- Software Engineer  
- Data Analyst  
- AI & ML Engineer  

📧 **Email:** damodarsadavarte2000@gmail.com  
🔗 **GitHub:** https://github.com/ThunderDamo1606  
🔗 **LinkedIn:** https://linkedin.com/in/damodar-sadavarte

---

## Summary

This project highlights:

* Practical data engineering skills
* Clean, production-oriented architecture
* End-to-end ETL pipeline implementation
* Workflow orchestration using Airflow

⭐ Thank you for reviewing!
