"""
extractor.py
-------------
Extracts meaningful sections from HTML.
"""

from bs4 import BeautifulSoup


def extract_sections(html):
    """
    Parse HTML and extract required sections.

    Args:
        html (str): Raw HTML content

    Returns:
        dict: Extracted sections
    """

    soup = BeautifulSoup(html, "html.parser")

    sections = {
        "navbar": "",
        "homepage": "",
        "footer": "",
        "case_study": ""
    }

    nav = soup.find("nav")
    if nav:
        sections["navbar"] = nav.get_text(" ", strip=True)

    footer = soup.find("footer")
    if footer:
        sections["footer"] = footer.get_text(" ", strip=True)

    body = soup.find("body")
    if body:
        sections["homepage"] = body.get_text(" ", strip=True)

    links = soup.find_all("a")
    for link in links:
        text = link.text.lower()
        if "case" in text or "success" in text:
            sections["case_study"] += link.text.strip() + " "

    return sections
