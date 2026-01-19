"""
transformer.py
---------------
Converts extracted data into a standard schema.
"""

from datetime import datetime


def transform(website_url, sections):
    """
    Convert section data into standardized records.
    """

    final_records = []

    for section, content in sections.items():

        if not content.strip():
            continue

        record = {
            "website": website_url,
            "section": section,
            "content": content,
            "crawl_timestamp": datetime.utcnow().isoformat(),
            "isActive": True
        }

        final_records.append(record)

    return final_records
