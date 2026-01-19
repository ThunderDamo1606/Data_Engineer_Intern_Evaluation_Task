# Data Engineer Intern – Website Data Pipeline

## 📌 Overview

This project implements a **production-style end-to-end data engineering pipeline** to crawl websites, extract structured content, standardize it into a clean data model, and generate analytical insights.

The pipeline follows a **real-world data lake architecture** and is orchestrated using **Apache Airflow** for scheduling and reliability.

### Key Objectives

* Demonstrate data pipeline design
* Show modular and clean code structure
* Implement reliable orchestration
* Build scalable architecture

---

## 🏗 Project Architecture

```
Growthpal-Pipeline/
│
├── dags/
│   └── website_pipeline_dag.py     # Airflow DAG (orchestration layer)
│
├── src/
│   ├── crawler.py                 # Website crawling logic
│   ├── extractor.py               # HTML parsing & tagging
│   ├── transformer.py             # Standard data model creation
│   └── aggregator.py              # Analytics & metrics
│
├── data/
│   ├── raw/                       # Raw HTML (S3 simulation)
│   ├── processed/                # Clean structured data
│   └── analytics/                # Aggregated metrics
│
├── run_pipeline.py                # Local pipeline runner (without Airflow)
├── venv/
├── requirements.txt
└── README.md
```

---

## 🔄 Pipeline Flow

### 1️⃣ Website Crawling

* Fetch raw HTML using `requests`
* Capture metadata (URL, status code, crawl timestamp)
* Store raw files in `data/raw/`
  *(Simulates S3 raw storage layer)*

### 2️⃣ Content Extraction

Using **BeautifulSoup**, extract:

* Navbar content
* Homepage content
* Footer content
* Case study links (heuristic based)

### 3️⃣ Data Transformation

Convert extracted content into a **standard JSON format**:

```json
{
  "website": "https://example.com",
  "section": "homepage",
  "content": "Extracted text...",
  "crawl_timestamp": "2026-01-10T10:30:00Z",
  "isActive": true
}
```

Each website generates multiple records (one per section).

### 4️⃣ Aggregation & Metrics

Compute:

* Number of websites with case studies
* Content length statistics per section

### 5️⃣ Orchestration (Apache Airflow)

* Modular task design
* Retry enabled for failures
* Idempotent execution
* Easily extendable to new websites

---

## ⚙ Installation & Setup

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Pipeline Locally (Without Airflow)

```bash
python run_pipeline.py
```

This generates:

* Raw HTML → `data/raw/`
* Structured data → `data/processed/structured.json`
* Metrics → `data/analytics/metrics.json`

### 4️⃣ Run with Airflow (Optional)

```bash
airflow db init

airflow users create \
  --username admin \
  --password admin \
  --firstname admin \
  --lastname admin \
  --role Admin \
  --email admin@test.com

airflow webserver -p 8080
airflow scheduler
```

Open:

```
http://localhost:8080
```

Trigger DAG:
**growthpal_pipeline**

---

## 🧠 Design Decisions

| Area                   | Reason                     |
| ---------------------- | -------------------------- |
| Modular code           | Easy maintenance & testing |
| Raw → Processed layers | Follows data lake pattern  |
| Heuristic scraping     | Focus on pipeline design   |
| JSON output            | API & analytics ready      |
| Airflow orchestration  | Production scheduling      |

---

## 🛡 Failure Handling

* Network timeout handling
* Retry enabled in Airflow
* Failed websites skipped safely
* Logs available for debugging

---

## 🚀 Scalability & Future Enhancements

* Parallel crawling using async processing
* S3 integration for storage
* Spark for big data processing
* API-based ingestion
* Dynamic Airflow task generation

---

## 📊 Sample Outputs

* `data/raw/` → raw HTML files
* `data/processed/structured.json` → clean structured data
* `data/analytics/metrics.json` → analytical metrics

---

## 👨‍💻 Author

**Damodar Sadavarte**
Software Engineer | Data Analytics | AI & ML Engineer

📧 Email: [damodarsadavarte2000@gmail.com](mailto:damodarsadavarte2000@gmail.com)
🔗 GitHub: [https://github.com/ThunderDamo1606](https://github.com/ThunderDamo1606)
🔗 LinkedIn: [https://linkedin.com/in/damodar-sadavarte](https://linkedin.com/in/damodar-sadavarte)

---

## 🏁 Conclusion

This project demonstrates:

* Real-world data engineering workflow
* Clean & scalable architecture
* Production-ready design
* Strong understanding of ETL pipelines

---

⭐ Thank you for reviewing!
