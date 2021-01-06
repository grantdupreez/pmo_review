import streamlit as st
import pandas as pd
import numpy as np
import ipywidgets as widgets
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

#    fig = px.parallel_categories(df, dimensions=['CR', 'Piority', 'State', 'Impacted Countries', 'Current STAGE']
#                                 , color="size", color_continuous_scale=px.colors.sequential.Inferno)

#    fig

# Build parcats dimensions
    categorical_dimensions = ['CR', 'State', 'Impacted Countries', 'RAG'];

    dimensions = [dict(values=df[label], label=label) for label in categorical_dimensions]

    # Build colorscale
    color = np.zeros(len(df), dtype='uint8')
    colorscale = [[0, 'gray'], [1, 'firebrick']]

    # Build figure as FigureWidget
    fig = go.FigureWidget(
        data=[go.Scatter(x=df['Process'], y=df['Priority'],
        marker={'color': 'gray'}, mode='markers', selected={'marker': {'color': 'firebrick'}},
        unselected={'marker': {'opacity': 0.3}}), go.Parcats(
            domain={'y': [0, 0.4]}, dimensions=dimensions,
            line={'colorscale': colorscale, 'cmin': 0,
                  'cmax': 1, 'color': color, 'shape': 'hspline'})
        ])

    fig.update_layout(
        xaxis={'title': 'Process'}
        , yaxis={'title': 'Priority'}
        , dragmode='lasso', hovermode='closest')

    # Update color callback
    def update_color(trace, points, state):
        # Update scatter selection
        fig.data[0].selectedpoints = points.point_inds

        # Update parcats colors
        new_color = np.zeros(len(df), dtype='uint8')
        new_color[points.point_inds] = 1
        fig.data[1].line.color = new_color

    # Register callback on scatter selection...
    fig.data[0].on_selection(update_color)
    # and parcats click
    fig.data[1].on_click(update_color)

    fig
