"""
crawler.py
-----------
Purpose:
- Crawl websites
- Fetch raw HTML
- Store it in raw folder (S3 simulation)
"""

import requests
from datetime import datetime
import os


def crawl_website(url):
    """
    Fetch HTML from a website

    Parameters:
        url (str): website URL

    Returns:
        html (str): raw page content
        meta (dict): crawl metadata
    """

    try:
        response = requests.get(url, timeout=10)

        meta = {
            "url": url,
            "status_code": response.status_code,
            "crawl_time": datetime.utcnow().isoformat()
        }

        return response.text, meta

    except Exception as e:
        print(f"Error while crawling {url} -> {e}")
        return None, None


def save_raw_html(site_name, html):
    """
    Store raw HTML locally

    Folder:
    data/raw/<site_name>/homepage.html
    """

    folder_path = f"data/raw/{site_name}"
    os.makedirs(folder_path, exist_ok=True)

    file_path = f"{folder_path}/homepage.html"

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(html)

    return file_path
