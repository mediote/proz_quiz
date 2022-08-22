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

    option = st.selectbox(
        'Selecione o tipo de visualização desejado.',
        ('', 'Histograma', 'Box Plot'))

    if option == 'Histograma':
        hist.plot_quiz_hist(quiz, 5, 3)
    if option == 'Box Plot':
        boxp.plot_quiz_box(quiz, 5, 3)
    if option == 'Bar Plot':
        barp.plot_quiz_bar(quiz, 5, 5)
