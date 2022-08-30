import pathlib

import pandas as pd
import streamlit as st

import barplot as barp
import boxplot as boxp
import boxplot_total as boxpt
import filter_dataframe as fildf

df = pd.DataFrame()
metric_option = ''


def upload_file(output_file):
    with st.spinner('Carregando...'):

        df = pd.DataFrame()
        file_extension = pathlib.Path(output_file.name).suffix

        if file_extension == ".csv":
            df = pd.read_csv(output_file)

        if file_extension == ".xlsx":
            df = pd.read_excel(output_file)

        if file_extension != ".xlsx" and file_extension != ".csv":
            st.warning(
                "Extensão não suportada! Favor selecione aquivos CSV ou XLSX.")
        else:
            df = df[df.status_aprendiz == 'Concluído']
            df = df[df.titulo_objeto.str.startswith("Quiz")]
            df = df.reset_index().drop(columns='index')
            # st.success('Dados carregados com sucesso!')
        return df


def filter_dataframe(df):
    df = fildf.filter_dataframe(df)
    return df


def render_main_app(dataframe, vis_option, metric_option):
    with st.expander("Tabela", expanded=True):
        st.write(dataframe)

    if vis_option == 'Box Plot':
        boxp.plot_quiz_box(dataframe, 5, 3)
    if vis_option == 'Box Plot - Total':
        boxpt.plot_quiz_box_total(dataframe)
    if vis_option == 'Bar Plot':

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
    st.markdown('## Opções')
    with st.expander("Upload de arquivos"):
        output_file = st.file_uploader("Selecione o arquivo")

    if output_file is not None:
        df = upload_file(output_file)

        with st.expander("Visualizações"):
            vis_option = st.selectbox(
                'Selecione o tipo de visualização',
                ('', 'Bar Plot', 'Box Plot', 'Box Plot - Total'))

            if vis_option == 'Bar Plot':
                metric_option = st.radio(
                    'Selecione a métrica.',
                    ('Média', 'Mediana'))

        with st.expander("Filtros"):
            df = filter_dataframe(df)


if not df.empty:
    render_main_app(df, vis_option, metric_option)
