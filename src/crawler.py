"""
crawler.py
-----------
Handles website crawling and raw HTML storage.
"""

import requests
from datetime import datetime
import os
import time


def crawl_website(website_url):
    """
    Fetch raw HTML content from a website.

    Args:
        website_url (str): Target website URL

    Returns:
        html (str): Raw HTML content
        meta (dict): Crawl metadata
    """

    max_retries = 3

    for attempt in range(max_retries):
        try:
            response = requests.get(website_url, timeout=10)

            meta = {
                "url": website_url,
                "status_code": response.status_code,
                "crawl_time": datetime.utcnow().isoformat()
            }

            return response.text, meta

        except Exception as err:
            time.sleep(2)

    return None, None


def save_raw_html(site_name, html_content):
    """
    Save raw HTML to local storage.

    Path:
        data/raw/<site_name>/homepage.html
    """

    folder_path = f"data/raw/{site_name}"
    os.makedirs(folder_path, exist_ok=True)

    file_path = f"{folder_path}/homepage.html"

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(html_content)

    return file_path
