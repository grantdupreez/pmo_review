import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go

st.write("**Upload project plan for a Gantt chart view**")
st.write("Use the template csv file")

uploaded_files = st.sidebar.file_uploader("Choose a file",type=['CSV'], accept_multiple_files=True)
if uploaded_files is not None:
    for file in uploaded_files:
        file.seek(0)
    df = pd.read_csv(file, header=[0], encoding='latin1')
    concat_df = pd.concat(df)
        
#    df['Start'] = df['Start'].astype('datetime64')
#        df['Finish'] = df['Finish'].astype('datetime64')
#        df['CR'] = df['CR'].astype(str)
    
#        orders = list(df['CR'])
    
    st.write(concat_df)
    

#    fig = px.timeline(df
#                      , x_start="Start"
#                      , x_end="Finish"
#                      , y="CR"
#                      , hover_name="CR"
#                      , color='Status'
#                      , opacity=.7
#    )
    
#    fig.update_yaxes(autorange="reversed")     
    
#    fig
