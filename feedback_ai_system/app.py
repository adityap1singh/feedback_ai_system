import os
import sys
import streamlit as st
import pandas as pd

st.write("Current working directory:", os.getcwd())
st.write("Python path:", sys.path)

from Pipe_pipeline import run_pipeline
uploaded_file = st.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"])

if uploaded_file:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.dataframe(df)

    if st.button("Analyze with AI"):
        prompt = f"Analyze this data:\n{df.head(20).to_string()}"
        result = run_pipeline(prompt)
        st.success("Analysis Complete")
        st.write(result)