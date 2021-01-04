import streamlit as st
import pandas as pd
import io

st.write("**Upload project plans for review**")
st.write("Use csv files")

uploaded_files = st.sidebar.file_uploader("Choose CSV files", type='csv', accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)







#if uploaded_files:
#    for file in uploaded_files:
#        file.seek(0)
#    uploaded_data_read = [pd.read_csv(file) for file in uploaded_files]
#    raw_data = pd.concat(uploaded_data_read)
#    
#    st.write(raw_data)
#
