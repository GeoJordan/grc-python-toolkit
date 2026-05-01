import re

HIPAA_REGEX = r"HIPAA|164\."

PROXY_TERMS = r"Retention|Disposal|Sanitization|Confidentiality|Integrity|Availability|Encryption|Privacy"

RECORD_KEYWORDS = r"Retention|Disposal|Destruction|Archive|Storage|Media"

def contains_pattern(series, pattern, case=False):
    return series.str.contains(pattern, case=case, na=False)

def hipaa_matches(df):
    return df[contains_pattern(df["discussion"], HIPAA_REGEX)]

def refined_hipaa(df):
    return df[
        contains_pattern(df["discussion"], HIPAA_REGEX) &
        contains_pattern(df["discussion"], r"Retention|Archive|Record")
    ]

def proxy_matches(df):
    return df[contains_pattern(df["discussion"], PROXY_TERMS)]

def record_lifecycle(df):
    return df[contains_pattern(df["discussion"], RECORD_KEYWORDS)]