import streamlit as st
import pandas as pd

from data_loader import load_controls
from pipeline import run_pipeline

st.set_page_config(page_title="GRC Toolkit", layout="wide")

st.title("GRC Compliance Automation Toolkit")

uploaded_file = st.file_uploader("Upload Control CSV", type=["csv"])

if uploaded_file:
    df = load_controls(uploaded_file)

    st.subheader("Raw Data")
    st.dataframe(df.head())

    if st.button("Run Analysis"):
        results = run_pipeline(uploaded_file)

        hipaa_matches = results[results["discussion"].str.contains(
            r"HIPAA|164\.",
            case=False,
            na=False
        )]

        st.subheader("Summary Metrics")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Total Controls", len(results))

        with col2:
            st.metric("HIPAA Matches", len(hipaa_matches))

        tab1, tab2, tab3 = st.tabs(["Results", "Risk Summary", "HIPAA Matches"])

        with tab1:
            st.subheader("Analysis Results")
            st.dataframe(results)

        with tab2:
            st.subheader("Risk Summary")
            st.dataframe(results[["identifier", "score", "risk_level"]])

        with tab3:
            st.subheader("HIPAA Matches")
            st.dataframe(hipaa_matches)
