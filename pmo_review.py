import streamlit as st
import pandas as pd
import numpy as np
import ipywidgets as widgets
import plotly.express as px
import plotly.graph_objs as go

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

	
st.title("Project deliverable viewer")
st.write("Use the template csv file")
st.sidebar.title("Upload the template")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, header=[0])
    orders = list(df['Process'])
    sel_proc = data_set['Process'].drop_duplicates()
    choice = st.sidebar.selectbox('Select a business process:', sel_proc)
    st.write(choice)
#    if st.button("Process"):
#	data_set.Process == choice
#	st.write(data_set)
#	show_par_chart(data_set)
