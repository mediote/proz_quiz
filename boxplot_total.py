import plotly.graph_objects as go
import streamlit as st


def plot_quiz_box_total(quiz_data):
    y0 = quiz_data[~quiz_data.titulo_objeto.str.endswith("D")].pontuacao
    y1 = quiz_data[quiz_data.titulo_objeto.str.endswith("D")].pontuacao
    fig = go.Figure()
    fig.add_trace(go.Box(y=y0, name='Quiz', marker_color='#FF7F00'))
    fig.add_trace(go.Box(y=y1, name='Quiz D', marker_color='#593493'))
    fig.update_traces(boxmean=True)
    fig.update_traces(orientation='v')
    fig.update_layout(title_text="Quiz", height=400, width=600)
    st.plotly_chart(fig, use_container_width=True)
