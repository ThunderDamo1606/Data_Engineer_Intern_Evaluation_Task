"""
aggregator.py
--------------
Calculate analytics metrics
"""

def compute_metrics(records):
    """
    Compute:
    - websites with case study
    - content length stats

    Parameters:
        records (list)

    Returns:
        dict
    """

    # Count websites with case studies
    case_study_count = len([
        r for r in records
        if r["section"] == "case_study" and len(r["content"]) > 0
    ])

    section_lengths = {}

    for r in records:
        section = r["section"]
        length = len(r["content"])

        if section not in section_lengths:
            section_lengths[section] = []

        section_lengths[section].append(length)

    stats = {}

    for sec, values in section_lengths.items():
        stats[sec] = {
            "min": min(values),
            "max": max(values),
            "avg": sum(values) / len(values)
        }

    return {
        "websites_with_case_study": case_study_count,
        "section_length_stats": stats
    }
