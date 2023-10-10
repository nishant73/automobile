import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
def app():
    p = []
    plot1 = px.scatter()
    plot2 = px.scatter()
    plot3 = px.scatter()
    plot4 = px.scatter()
    plot5 = px.scatter()
    plot6 = px.scatter()
    plot7 = px.scatter()
    plot8 = px.scatter()
    uploaded_file = st.file_uploader(label="Upload your CSV or Excel file. (200MB max)",type=['csv', 'xlsx'])
    global df
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
        except Exception as e:
            print(e)
            df = pd.read_excel(uploaded_file)
    global numeric_columns
    global non_numeric_columns
    global all_columns
    try:
        numeric_columns = list(df.select_dtypes(['float', 'int']).columns)
        non_numeric_columns = list(df.select_dtypes(['object']).columns)
        all_columns = list(df.select_dtypes(['float', 'int', 'object']).columns)
        length_of_options = len(all_columns)
        length_of_options -= 1
        non_numeric_columns.append(None)
        print(non_numeric_columns)
    except Exception as e:
        print(e)
        st.write("Please upload file to the application.")
    try:
        st.sidebar.title("**Visualization Settings**")
        x = st.sidebar.selectbox('X axis', options=all_columns)
        y = st.sidebar.selectbox('Y axis', options=all_columns)
        color_value = st.sidebar.selectbox("Color", options=all_columns)
        radio1 = st.sidebar.radio("Visualization 1",('Scatter Plot', 'Line Plot', 'Violin Chart', 'Pie Chart'))
        if radio1 == 'Scatter Plot':
            plot1 = px.scatter(data_frame=df, x=x, y=y, color=color_value, title = 'Scatter Plot')
        if radio1 == 'Line Plot':
            plot1 = px.line(data_frame=df, x=x, y=y, color=color_value, title = 'Line Plot')
        if radio1 == 'Violin Chart':
            plot1 = px.violin(data_frame=df, y=y, x=x, color=color_value, title = 'Violin Plot')
        if radio1 == 'Pie Chart':
            plot1 = px.pie(data_frame=df, names=x, values=y, color=color_value, title = 'Pie Chart')
        radio2 = st.sidebar.radio("Visualization 2",('Histogram', 'Box Plot', 'Density Contour', 'Density Heatmap'))
        if radio2 == 'Histogram':
            plot2 = px.histogram(data_frame=df, x=x, y=y, color=color_value, histfunc='sum', title = 'Histogram')
        if radio2 == 'Box Plot':
            plot2 = px.box(data_frame=df, y=y, x=x, color=color_value, title = 'Box Plot')
        if radio2 == 'Density Contour':
            plot2 = px.density_contour(data_frame=df, x=x, y=y, color=color_value, histfunc='sum', title = 'Density Contour')
        if radio2 == 'Density Heatmap':
            plot2 = px.density_heatmap(data_frame=df, x=x, y=y, histfunc='sum', title = 'Density Heatmap')

    except Exception as e:
        print(e)

    container1 = st.container()
    col1, col2 = st.columns(2)

    with container1:
        with col1:
            st.plotly_chart(plot1, use_container_width=True)

        with col2:
            st.plotly_chart(plot2, use_container_width=True)
