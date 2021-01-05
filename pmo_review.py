import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go

st.write("**Upload project plan for a Gantt chart view**")
st.write("Use the template csv file")

list_of_dataframes = []
uploaded_files = st.sidebar.file_uploader("Choose a file",type=['CSV'], accept_multiple_files=True)
if uploaded_files is not None:
    for file in uploaded_files:
        file.seek(0)
        df = pd.read_csv(file, header=[0], encoding='latin1')
        list_of_dataframes.append(df)
    
    if list_of_dataframes:
        merged_df = pd.concat(list_of_dataframes)
    
    st.write(merged_df)

else:
    static_store.clear()  
