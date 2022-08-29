import pathlib

import pandas as pd
import streamlit as st

import barplot as barp
import boxplot as boxp
import boxplot_total as boxpt
import filter_dataframe as fildf

quiz = pd.DataFrame()


def upload_file(output_file):
    with st.spinner('Carregando...'):

        file_extension = pathlib.Path(output_file.name).suffix
        if file_extension == ".csv":
            dataframe = pd.read_csv(output_file)

        if file_extension == ".xlsx":
            dataframe = pd.read_excel(output_file)

        dataframe = dataframe[dataframe.status_aprendiz == 'Concluído']
        dataframe = dataframe[dataframe.titulo_objeto.str.startswith("Quiz")]
        dataframe = dataframe.reset_index().drop(columns='index')
        st.success('Dados carregados com sucesso!')
        return dataframe


def filter_dataframe(dataframe):
    dataframe = fildf.filter_dataframe(dataframe)
    return dataframe


def render_main_app(dataframe):
    st.write(dataframe)
    vis_option = st.selectbox(
        'Selecione o tipo de visualização.',
        ('', 'Bar Plot', 'Box Plot', 'Box Plot - Total'))
    if vis_option == 'Box Plot':
        boxp.plot_quiz_box(dataframe, 5, 3)
    if vis_option == 'Box Plot - Total':
        boxpt.plot_quiz_box_total(dataframe)
    if vis_option == 'Bar Plot':
        metric_option = st.radio(
            'Selecione a métrica.',
            ('Média', 'Mediana'))
        if metric_option == 'Média':
            metric = 'mean'
            st.write('Voçê selecionou média.')
            quiz_metrics = barp.create_quiz_metrics_dataset(dataframe)
            barp.plot_quiz_bar(quiz_metrics, metric, 5, 3)
        if metric_option == 'Mediana':
            metric = 'median'
            st.write('Voçê selecionou mediana.')
            quiz_metrics = barp.create_quiz_metrics_dataset(dataframe)
            barp.plot_quiz_bar(quiz_metrics, metric, 5, 3)


with st.sidebar:
    output_file = st.file_uploader("Selecione o arquivo.")
    if output_file is not None:
        quiz = upload_file(output_file)
        quiz = filter_dataframe(quiz)

if not quiz.empty:
    render_main_app(quiz)
