# GRC Compliance Automation Toolkit

Python-based toolkit for automating control mapping, compliance scoring, and regulatory detection across:

- NIST SP 800-53  
- HIPAA Security Rule  
- HITRUST CSF (06.c Access Control)

## Features
- Detects HIPAA references (e.g., 164.x)
- Maps controls across frameworks
- Scores controls and assigns risk levels
- Evaluates HITRUST 06.c relevance
- Streamlit dashboard for interactive analysis

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
