import streamlit as st
import pandas as pd

import histogram as hist
import boxplot as boxp
import barplot as barp


uploaded_file = st.file_uploader("Selecione o arquivo.")
if uploaded_file is not None:
    with st.spinner('Wait for it...'):
        quiz = pd.read_csv(uploaded_file)
        st.write(quiz)
        st.success('Done!')

    vis_option = st.selectbox(
        'Selecione o tipo de visualização.',
        ('', 'Histograma', 'Bar Plot', 'Box Plot'))

    if vis_option == 'Histograma':
        hist.plot_quiz_hist(quiz, 5, 3)
    if vis_option == 'Box Plot':
        boxp.plot_quiz_box(quiz, 5, 3)
    if vis_option == 'Bar Plot':
        metric_option = st.radio(
            'Selecione a métrica.',
            ('Média', 'Mediana'))

        if metric_option == 'Média':
            metric = 'mean'
            quiz_metrics = barp.create_quiz_metrics_dataset(quiz)
            barp.plot_quiz_bar(quiz_metrics, metric, 5, 5)
        if metric_option == 'Mediana':
            metric = 'median'
            quiz_metrics = barp.create_quiz_metrics_dataset(quiz)
            barp.plot_quiz_bar(quiz_metrics, metric, 5, 5)
