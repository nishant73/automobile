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

        try:
            df = pd.read_csv(uploaded_file)
        except Exception as e:
            print(e)
            df = pd.read_excel(uploaded_file)

    global numeric_columns
    global non_numeric_columns
    global time_columns
    try:
        st.write(df)
        numeric_columns = list(df.select_dtypes(['float', 'int']).columns)
        non_numeric_columns = list(df.select_dtypes(['object']).columns)
        all_columns = list(df.select_dtypes(['float', 'int', 'object']).columns)
        length_of_options = len(all_columns)
        length_of_options -= 1
        non_numeric_columns.append(None)
    except Exception as e:
        print(e)
        st.write("Please upload file to the application.")
    txt = st.text_area('Enter your query', placeholder = 'Eg. Compare ... with ... against ... ( ... stands for the column name)')
    try:
        txt_array = txt.split(" ")
        temp = ''
        for i in range(len(txt_array)):
            temp = temp+txt_array[i][0].upper()
            for j in range(1, len(txt_array[i])):
                temp = temp+txt_array[i][j].lower()
            txt_array[i] = temp
            temp=''
    except Exception as e:
        print(e)
    nc1 = 0
    nc2 = 0
    nc3 = 0
    nnc1 = 0
    nnc2 = 0
    nnc3 = 0
    try:
        for i in range(len(all_columns)):
            if txt_array[1] == all_columns[i]:
                for j in range(len(numeric_columns)):
                    if txt_array[1] == numeric_columns[j]:
                        nc1 = 1
                    if txt_array[1] == non_numeric_columns[j]:
                        nnc1 = 1
    except Exception as e:
        print(e)
    try:
        for i in range(len(all_columns)):
            if txt_array[3] == all_columns[i]:
                for j in range(len(numeric_columns)):
                    if txt_array[3] == numeric_columns[j]:
                        nc2 = 1
                    if txt_array[3] == non_numeric_columns[j]:
                        nnc2 = 1
    except Exception as e:
        print(e)
    try:
        for i in range(len(all_columns)):
            if txt_array[5] == all_columns[i]:
                for j in range(len(numeric_columns)):
                    if txt_array[5] == numeric_columns[j]:
                        nc3 = 1
                    if txt_array[5] == non_numeric_columns[j]:
                        nnc3 = 1
    except Exception as e:
        print(e)
    try:
        if nc1 == 1 and nc2 == 1:
            plot = px.scatter(data_frame=df, x=txt_array[1], y=txt_array[3], color=txt_array[5])
            st.plotly_chart(plot)
        if nnc1 == 1 and nnc2 == 1 and nc3 == 1:
            plot = px.sunburst(data_frame=df, path=[txt_array[1],txt_array[3]], values=txt_array[5], color=txt_array[5])
            st.plotly_chart(plot)
        if nnc1 == 1 and nnc2 == 1 and nnc3 == 1:
            plot = px.box(data_frame=df, y=txt_array[3], x=txt_array[1], color=txt_array[1])
            st.plotly_chart(plot)
        if nnc1 == 1 and nc2 == 1:
            plot = px.density_heatmap(data_frame=df, x=txt_array[1], y=txt_array[3], histfunc='sum')
            st.plotly_chart(plot)
        if nc1 == 1 and nnc2 == 1:
            plot = px.histogram(data_frame=df, x=txt_array[1], y=txt_array[3], color=txt_array[5], histfunc='sum')
            st.plotly_chart(plot)
    except Exception as e:
        print(e)
