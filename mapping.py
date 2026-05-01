def infer_basic_hipaa(identifier: str) -> str:
    if identifier.startswith("MP"):
        return "164.310 - Physical Safeguards"
    elif identifier.startswith("AC"):
        return "164.312 - Technical Access"
    return "General Security"


def map_family_to_hipaa(identifier: str) -> str:
    if identifier.startswith("AC"):
        return "164.312(a)(1) - Access Control"
    if identifier.startswith("AU"):
        return "164.312(b) - Audit Controls"
    if identifier.startswith("MP"):
        return "164.310(d)(1) - Device & Media Controls"
    if identifier.startswith("SC"):
        return "164.312(e)(1) - Transmission Security"
    return "Supporting Control"