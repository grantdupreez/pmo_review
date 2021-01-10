import streamlit as st
import pandas as pd
import numpy as np
import ipywidgets as widgets
import plotly.express as px
import plotly.graph_objs as go

def log_loc():
    #set the plan logging
    from datetime import datetime
    now = datetime.now()
    dt_string = now.strftime("%Y%m%d%H%M%S")+".csv"
    s3_string = ""
    #S3 storage for the plan logging
    return s3_string+dt_string

def load_file(nrows):
    df = pd.read_csv(uploaded_file, header=[0], nrows=nrows)
    orders = list(df['Process'])
    return df

def show_par_chart(dataframe):
    # Create dimensions
    proc_dim = go.parcats.Dimension(
        values=ds.Process,
        categoryorder='category ascending', label="Process"
    )

    prio_dim = go.parcats.Dimension(values=ds.Priority, label="Priority")

    state_dim = go.parcats.Dimension(
        values=ds.State, label="State"
    )

    country_dim = go.parcats.Dimension(
        values=ds.Impacted_Countries, label="Countries"
    )

    pm_dim = go.parcats.Dimension(
        values=ds.PM, label="PM"
    )
    
    rag_dim = go.parcats.Dimension(
        values=ds.RAG, label="RAG"
    )
        
    color = ds.Priority;

    fig = go.Figure(data = [go.Parcats(dimensions=[country_dim, pm_dim, proc_dim, prio_dim, state_dim, rag_dim],
        line={'color': ["SkyBlue", "SlateGray", "Silver"]},
        hoveron='color'
        )])
    
    fig


    
def main():
    st.title("Project deliverable viewer")
    st.write("Use the template csv file")
    st.sidebar.title("Upload the template")
    if uploaded_file is not None:
        data_set = load_file(100):
            sel_proc = data_set['Process'].drop_duplicates()
            make_choice = st.sidebar.selectbox('Select a business process:', sel_proc)
            if make_choice:
                data_set.Process == make_choice
                st.write(data_set)
                show_par_chart(data_set)
 
