from data_loader import load_controls
from search import (
    hipaa_matches,
    refined_hipaa,
    proxy_matches,
    record_lifecycle
)
from mapping import (
    infer_basic_hipaa,
    map_family_to_hipaa
)
from export import export_csv
from scoring import score_control, assign_risk


def run_pipeline(input_file: str):
    df = load_controls(input_file)

    # HIPAA direct matches
    hipaa_df = hipaa_matches(df)

    # Refined search
    refined_df = refined_hipaa(df)

    # Proxy search
    proxy_df = proxy_matches(df)

    # Record lifecycle
    records_df = record_lifecycle(df)

    # Add mappings
    df["inferred_hipaa"] = df["identifier"].apply(infer_basic_hipaa)
    records_df["HIPAA_Reference"] = records_df["identifier"].apply(map_family_to_hipaa)

    # Add scoring
    df["score"] = df.apply(score_control, axis=1)
    df["risk_level"] = df["score"].apply(assign_risk)

    # Export artifacts
    export_csv(hipaa_df, "data/processed/hipaa_matches.csv")
    export_csv(refined_df, "data/processed/refined_matches.csv")
    export_csv(proxy_df, "data/processed/proxy_matches.csv")
    export_csv(records_df, "data/processed/06c_records.csv")
    export_csv(df, "data/processed/full_with_mapping.csv")

    print("✅ Pipeline complete. All artifacts generated.")

    return df