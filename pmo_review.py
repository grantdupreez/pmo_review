import streamlit as st
import pandas as pd
import numpy as np
import ipywidgets as widgets
import plotly.express as px
import plotly.graph_objs as go

def show_par_chart(dataframe):
    # Create dimensions
    proc_dim = go.parcats.Dimension(
        values=df.Process,
        categoryorder='category ascending', label="Process"
    )
    prio_dim = go.parcats.Dimension(values=df.Priority, label="Priority")
    state_dim = go.parcats.Dimension(
        values=df.State, label="State"
    )
    country_dim = go.parcats.Dimension(
        values=df.Impacted_Countries, label="Countries"
    )
    pm_dim = go.parcats.Dimension(
        values=df.PM, label="PM"
    )
    rag_dim = go.parcats.Dimension(
        values=df.RAG, label="RAG"
    )   
    color = df.Priority;
    fig = go.Figure(data = [go.Parcats(dimensions=[country_dim, pm_dim, proc_dim, prio_dim, state_dim, rag_dim],
        line={'color': ["SkyBlue", "SlateGray", "Silver"]},
        hoveron='color'
        )])
    fig

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
    
    processes = df['Process'].drop_duplicates()
    proc_choice = st.sidebar.selectbox('Select the process:', processes)
#    priority = df["Priority"].loc[df["Process"] = proc_choice]
#    prio_choice = st.sidebar.selectbox('', Priority) 
    
#    df.loc[(df['Process']=proc_choice) & (df['Priority']=prio_choice))]
    df.loc[(df['Process']=proc_choice)]
 
    show_par_chart(df)



#    choice = st.sidebar.selectbox('Select business process(es):', df['Process'].drop_duplicates())
#    if choice:
#    if st.sidebar.selectbox('Select business process(es):', df['Process'].drop_duplicates()):
#        choice = st.sidebar.selectbox('Select business process(es):', df['Process'].drop_duplicates())
#        st.write(choice)
#        newdf = df.Process == choice
#        st.write(df)
#        show_par_chart(newdf)
#        show_par_chart(df)

#ACTION
#    df.to_csv(s3_string+dt_string)
