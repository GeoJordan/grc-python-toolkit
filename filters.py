def filter_families(df):
    return {
        "AC": df[df["identifier"].str.startswith("AC")],
        "CP": df[df["identifier"].str.startswith("CP")],
        "MP": df[df["identifier"].str.startswith("MP")]
    }