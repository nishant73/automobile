import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

def app():
    st.sidebar.subheader("Visualization Settings")

    uploaded_file = st.sidebar.file_uploader(
                        label="Upload your CSV or Excel file. (200MB max)",
                         type=['csv', 'xlsx'])

    global df
    if uploaded_file is not None:
        print(uploaded_file)
        print("hello")

        try:
            df = pd.read_csv(uploaded_file)
        except Exception as e:
            print(e)
            df = pd.read_excel(uploaded_file)

    global numeric_columns
    global non_numeric_columns
    try:
        st.write(df)
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
    chart_select = st.sidebar.selectbox(label="Select the chart type",
    options=['Scatterplots', 'Lineplots', 'Histogram', 'Boxplot', 'Violin plots', 'Sunburst', 'Tree maps', 'Pie Charts', 'Density contour', 'Density heatmaps', 'Area charts', 'Bar charts'])

    if chart_select == 'Scatterplots':
        st.sidebar.subheader("Scatterplot Settings")
        try:
            x_values = st.sidebar.selectbox('X axis', options=all_columns)
            y_values = st.sidebar.selectbox('Y axis', options=all_columns)
            color_value = st.sidebar.selectbox("Color", options=all_columns)
            plot = px.scatter(data_frame=df, x=x_values, y=y_values, color=color_value)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)

    if chart_select == 'Lineplots':
        st.sidebar.subheader("Line Plot Settings")
        try:
            x_values = st.sidebar.selectbox('X axis', options=all_columns)
            y_values = st.sidebar.selectbox('Y axis', options=all_columns)
            color_value = st.sidebar.selectbox("Color", options=all_columns)
            plot = px.line(data_frame=df, x=x_values, y=y_values, color=color_value)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)

    if chart_select == 'Histogram':
        st.sidebar.subheader("Histogram Settings")
        try:
            x = st.sidebar.selectbox('X axis', options=all_columns)
            y = st.sidebar.selectbox('Y axis', options=all_columns)
            bin_size = st.sidebar.slider("Number of Bins", min_value=10,
                                     max_value=100, value=40)
            color_value = st.sidebar.selectbox("Color", options=all_columns)
            hist_func = st.sidebar.selectbox('Histogram aggregation function', index=0,
                                             options=['count','sum', 'avg', 'min', 'max'])
            plot = px.histogram(data_frame=df, x=x, y=y, color=color_value, histfunc=hist_func)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)

    if chart_select == 'Boxplot':
        st.sidebar.subheader("Boxplot Settings")
        try:
            x = st.sidebar.selectbox("X axis", options=all_columns)
            y = st.sidebar.selectbox("Y axis", options=all_columns)
            color_value = st.sidebar.selectbox("Color", options=all_columns)
            plot = px.box(data_frame=df, y=y, x=x, color=color_value)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)
    if chart_select == 'Violin plots':
        st.sidebar.subheader("Violin plots Settings")
        try:
            x = st.sidebar.selectbox("X axis", options=all_columns)
            y = st.sidebar.selectbox("Y axis", options=all_columns)
            color_value = st.sidebar.selectbox("Color", options=all_columns)
            plot = px.violin(data_frame=df, y=y, x=x, color=color_value)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)
    if chart_select == 'Sunburst':
        st.sidebar.subheader("Sunburst Settings")
        try:
            path_value = st.sidebar.multiselect("Path", options=all_columns)
            color_value = st.sidebar.selectbox("Color", options=all_columns)
            values = st.sidebar.selectbox("Value", index=length_of_options, options=all_columns)
            plot = px.sunburst(data_frame=df, path=path_value, values=values, color=color_value)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)
    if chart_select == 'Tree maps':
        st.sidebar.subheader("Tree maps Settings")
        try:
            path_value = st.sidebar.multiselect("Path", options=all_columns)
            color_value = st.sidebar.selectbox("Color", options=all_columns)
            value = st.sidebar.selectbox("Value", index=length_of_options, options=all_columns)
            plot = px.treemap(data_frame=df, path=path_value, values=value, color=color_value)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)
    if chart_select == 'Pie Charts':
        st.sidebar.subheader("Pie Chart Settings")
        try:
            name_value = st.sidebar.selectbox("Name (Selected Column should be categorical)", options=all_columns)
            color_value = st.sidebar.selectbox("Color (Selected Column should be categorical)", options=all_columns)
            value = st.sidebar.selectbox("Value", index=length_of_options, options=all_columns)
            plot = px.pie(data_frame=df, names=name_value, values=value, color=color_value)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)
    if chart_select == 'Density contour':
        st.sidebar.subheader("Density contour Settings")
        try:
            x = st.sidebar.selectbox('X axis', options=all_columns)
            y = st.sidebar.selectbox('Y axis', options=all_columns)
            color_value = st.sidebar.selectbox("Color", options=all_columns)
            hist_func = st.sidebar.selectbox('Contour aggregation function', index=0,
                                             options=['count','sum', 'avg', 'min', 'max'])
            plot = px.density_contour(data_frame=df, x=x, y=y, color=color_value, histfunc=hist_func)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)
    if chart_select == 'Density heatmaps':
        st.sidebar.subheader("Density heatmap Settings")
        try:
            x = st.sidebar.selectbox('X axis', options=all_columns)
            y = st.sidebar.selectbox('Y axis', options=all_columns)
            hist_func = st.sidebar.selectbox('Heatmap aggregation function', index=0,
                                             options=['count','sum', 'avg', 'min', 'max'])
            plot = px.density_heatmap(data_frame=df, x=x, y=y, histfunc=hist_func)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)
    if chart_select == 'Area charts':
        st.sidebar.subheader("Area Chart Settings")
        x_values = st.sidebar.slider("X axis", min_value=10,
                                 max_value=100, value=20)
        y_values = st.sidebar.slider("Y axis", min_value=2,
                                 max_value=100, value=3)
        color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
        chart_data = pd.DataFrame(
             np.random.randn(x_values, y_values))
        plot = st.area_chart(chart_data)
    if chart_select == 'Bar charts':
        st.sidebar.subheader("Bar Chart Settings")
        x_values = st.sidebar.slider("X axis", min_value=10,
                                 max_value=100, value=20)
        y_values = st.sidebar.slider("Y axis", min_value=2,
                                 max_value=100, value=3)
        color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
        chart_data = pd.DataFrame(
             np.random.randn(x_values, y_values))
        plot = st.bar_chart(chart_data)
