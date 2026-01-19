# Data_Engineer_Intern_Evaluation_Task
## Website Data Pipeline

## 📌 Overview

This project implements an end-to-end data engineering pipeline to crawl websites, extract structured content, standardize the data, and compute basic analytics.
The pipeline is orchestrated using **Apache Airflow** and follows real-world data lake design patterns.

The main goal is to demonstrate:

* Data pipeline design
* Clean code structure
* Reliable orchestration
* Scalable architecture

---

## 🏗 Project Architecture

```
Growthpal-Pipeline/
│
├── dags/
│   └── website_pipeline_dag.py
│
├── src/
│   ├── crawler.py
│   ├── extractor.py
│   ├── transformer.py
│   └── aggregator.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── analytics/
│
├── venv/
├── requirements.txt
└── README.md
```

---

## 🔄 Pipeline Flow

### 1️⃣ Crawl Websites

* Fetch raw HTML using `requests`
* Capture metadata like URL and crawl timestamp
* Store raw files in `data/raw/` (S3 simulation)

### 2️⃣ Extract Content

Using BeautifulSoup:

* Navbar content
* Homepage content
* Footer content
* Case study links (heuristic based)

### 3️⃣ Transform

Convert extracted content into standard JSON structure:

```json
{
  "website": "https://example.com",
  "section": "homepage",
  "content": "Extracted text...",
  "crawl_timestamp": "2026-01-10T10:30:00Z",
  "isActive": true
}
```

### 4️⃣ Aggregate

Compute metrics:

* Number of websites with case studies
* Content length statistics per section

### 5️⃣ Orchestration (Airflow)

* Modular tasks
* Retry enabled
* Idempotent execution
* Easy to extend for new websites

---

## ⚙ Installation & Setup

### 1. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Start Airflow (Local)

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

| Area                  | Reason              |
| --------------------- | ------------------- |
| Modular code          | Easy maintenance    |
| Raw/Processed layers  | Data lake pattern   |
| Heuristic scraping    | Focus on pipeline   |
| JSON output           | API ready           |
| Airflow orchestration | Production workflow |

---

## 🛡 Failure Handling

* Network timeout handling
* Airflow retries enabled
* Skip failed websites
* Logs for debugging

---

## 🚀 Scalability

Future improvements:

* Parallel crawling
* S3 storage
* Spark processing
* API ingestion
* Dynamic Airflow tasks

---

## 📊 Sample Outputs

* `data/raw/` → raw HTML files
* `data/processed/structured.json` → clean data
* `data/analytics/metrics.json` → analytics

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

* Real data engineering practices
* Clean architecture
* Scalable design
* Production mindset

---

⭐ Thank you for reviewing!
