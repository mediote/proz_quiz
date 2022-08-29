import pandas as pd
import streamlit as st

import barplot as barp
import boxplot as boxp
import boxplot_total as boxpt
import filter_dataframe as fil

uploaded_file = st.file_uploader("Selecione o arquivo.")
if uploaded_file is not None:
    with st.spinner('Wait for it...'):
        quiz = pd.read_csv(uploaded_file)

        quiz = quiz[quiz.status_aprendiz == 'Concluído']
        quiz = quiz[quiz.titulo_objeto.str.startswith("Quiz")]
        quiz = quiz.reset_index().drop(columns='index')

        st.write(quiz)
        st.success('Done!')

    quiz = fil.filter_dataframe(quiz)

    if not quiz.empty:
        vis_option = st.selectbox(
            'Selecione o tipo de visualização.',
            ('', 'Bar Plot', 'Box Plot', 'Box Plot - Total'))

        if vis_option == 'Box Plot':
            boxp.plot_quiz_box(quiz, 5, 3)

        if vis_option == 'Box Plot - Total':
            boxpt.plot_quiz_box_total(quiz)

        if vis_option == 'Bar Plot':
            metric_option = st.radio(
                'Selecione a métrica.',
                ('Média', 'Mediana'))

            if metric_option == 'Média':
                metric = 'mean'
                st.write('Voçê selecionou média.')
                quiz_metrics = barp.create_quiz_metrics_dataset(quiz)
                barp.plot_quiz_bar(quiz_metrics, metric, 5, 3)

            if metric_option == 'Mediana':
                metric = 'median'
                st.write('Voçê selecionou mediana.')
                quiz_metrics = barp.create_quiz_metrics_dataset(quiz)
                barp.plot_quiz_bar(quiz_metrics, metric, 5, 3)
