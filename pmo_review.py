import streamlit as st
import pandas as pd
import io

st.write("**Upload project plans for review**")
st.write("Use csv files")

uploaded_files = st.sidebar.file_uploader("Choose CSV files", accept_multiple_files=True)
if uploaded_files:
    for file in uploaded_files:
        file.seek(0)
    uploaded_data_read = [pd.read_csv(file) for file in uploaded_files]
    raw_data = pd.concat(uploaded_data_read)
    
    st.write(raw_data)
    
