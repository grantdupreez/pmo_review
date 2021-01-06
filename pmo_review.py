import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go

#set the plan logging
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%Y%m%d%H%M%S")+".csv"

s3_string = ""
#S3 storage for the plan logging

#ACTION activate this when the log location is known - st.write('S3 path and log filename: '+s3_string+dt_string)


st.title("Project deliverable viewer")
st.write("Use the template csv file")

st.sidebar.title("Upload the template")

uploaded_file = st.sidebar.file_uploader("Choose a file",type=['CSV'])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, header=[0])
    
    orders = list(df['Process'])
    
    st.write(df)
    
#ACTION
#    df.to_csv(s3_string+dt_string)

    fig = px.parallel_categories(df, dimensions=['CR', 'Piority', 'State', 'Impacted Countries', 'Current STAGE']
                                 , color="size", color_continuous_scale=px.colors.sequential.Inferno)

    fig
