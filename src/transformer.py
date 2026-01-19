"""
transformer.py
---------------
Convert extracted content
into standard data model
"""

from datetime import datetime


def transform(website, sections):
    """
    Convert section data into
    standardized records

    Parameters:
        website (str)
        sections (dict)

    Returns:
        list of dicts
    """

    records = []

    for section, content in sections.items():

        record = {
            "website": website,
            "section": section,
            "content": content,
            "crawl_timestamp": datetime.utcnow().isoformat(),
            "isActive": True
        }

        records.append(record)

    return records
