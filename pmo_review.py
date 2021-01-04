import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go

st.write("**Upload project plans for review**")
st.write("Use csv files")

uploaded_file = st.sidebar.file_uploader("Choose a file",type=['CSV'], accept_multiple_files=True)
if uploaded_files:
    for file in uploaded_files:
        file.seek(0)
    uploaded_data_read = [pd.read_csv(file) for file in uploaded_files]
    raw_data = pd.concat(uploaded_data_read)
    
    st.write(raw_data)
    
