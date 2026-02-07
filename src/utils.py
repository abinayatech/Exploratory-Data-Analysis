
import pandas as pd
import streamlit as st
import base64

def get_csv_download_link(df, filename="processed_churn_data.csv"):
    """Generates a link allowing the data to be downloaded."""
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}" style="text-decoration: none; color: #4CC9F0; font-weight: 600;">📥 Download Processed Report (CSV)</a>'
    return href

def apply_custom_filters(df, contract_list, internet_list, tenure_range):
    """Utility to filter dataframe based on multiple parameters."""
    return df[
        (df['Contract'].isin(contract_list)) &
        (df['InternetService'].isin(internet_list)) &
        (df['Tenure'].between(tenure_range[0], tenure_range[1]))
    ]
