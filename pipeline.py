from grc_toolkit.data_loader import load_controls
from grc_toolkit.search import (
    hipaa_matches,
    refined_hipaa,
    proxy_matches,
    record_lifecycle
)
from grc_toolkit.mapping import (
    infer_basic_hipaa,
    map_family_to_hipaa
)
from grc_toolkit.export import export_csv


def run_pipeline(input_file: str):
    df = load_controls(input_file)

    # --- HIPAA direct matches ---
    hipaa_df = hipaa_matches(df)

    # --- Refined search ---
    refined_df = refined_hipaa(df)

    # --- Proxy search ---
    proxy_df = proxy_matches(df)

    # --- Record lifecycle (your 06.c focus) ---
    records_df = record_lifecycle(df)

    # --- Add mappings ---
    df["inferred_hipaa"] = df["identifier"].apply(infer_basic_hipaa)
    records_df["HIPAA_Reference"] = records_df["identifier"].apply(map_family_to_hipaa)

    # --- Export artifacts ---
    export_csv(hipaa_df, "data/processed/hipaa_matches.csv")
    export_csv(refined_df, "data/processed/refined_matches.csv")
    export_csv(proxy_df, "data/processed/proxy_matches.csv")
    export_csv(records_df, "data/processed/06c_records.csv")
    export_csv(df, "data/processed/full_with_mapping.csv")

    print("✅ Pipeline complete. All artifacts generated.")