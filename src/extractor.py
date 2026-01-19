"""
extractor.py
-------------
Extract meaningful content from HTML:
- navbar
- homepage
- footer
- case_study
"""

from bs4 import BeautifulSoup


def extract_sections(html):
    """
    Parse HTML and extract sections

    Parameters:
        html (str): raw html content

    Returns:
        dict: extracted sections
    """

    soup = BeautifulSoup(html, "html.parser")

    result = {
        "navbar": "",
        "homepage": "",
        "footer": "",
        "case_study": ""
    }

    # Extract navbar text
    nav = soup.find("nav")
    if nav:
        result["navbar"] = nav.get_text(" ", strip=True)

    # Extract footer text
    footer = soup.find("footer")
    if footer:
        result["footer"] = footer.get_text(" ", strip=True)

    # Extract homepage body text
    body = soup.find("body")
    if body:
        result["homepage"] = body.get_text(" ", strip=True)

    # Heuristic for case studies
    links = soup.find_all("a")
    for link in links:
        text = link.text.lower()

        if "case" in text or "success" in text:
            result["case_study"] += link.text.strip() + " "

    return result
