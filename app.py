import streamlit as st
import pandas as pd
from src.grc_toolkit.pipeline import run_pipeline
from src.grc_toolkit.data_loader import load_controls

st.set_page_config(page_title="GRC Toolkit", layout="wide")

st.title("GRC Compliance Automation Toolkit")

uploaded_file = st.file_uploader("Upload Control CSV", type=["csv"])

if uploaded_file:
    df = load_controls(uploaded_file)

    st.subheader("Raw Data")
    st.dataframe(df.head())

    if st.button("Run Analysis"):
        df["hipaa_match"] = df["discussion"].str.contains(r"HIPAA|164\.", case=False, na=False)

        st.subheader("HIPAA Matches")
        st.dataframe(df[df["hipaa_match"]])

        st.subheader("Summary Metrics")
        st.metric("Total Controls", len(df))
        st.metric("HIPAA Matches", df["hipaa_match"].sum())