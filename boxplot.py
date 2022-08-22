import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st


def plot_quiz_box(quiz_data, n_rows, n_cols):

    quiz_range = len(
        quiz_data[quiz_data.titulo_objeto.str.contains("D")].titulo_objeto.unique())

    fig = make_subplots(
        rows=n_rows,
        cols=n_cols,
        subplot_titles=([(lambda x: f'Quiz {x}'.format(x))(x)
                        for x in range(1, quiz_range + 1)])
    )

    subplots_rows = 1
    subplots_cols = 1

    for i in range(1, quiz_range + 1):

        y0 = quiz_data[quiz_data.titulo_objeto ==
                       f'Quiz {i}'.format(i)].pontuacao
        y1 = quiz_data[quiz_data.titulo_objeto ==
                       f'Quiz {i} D'.format(i)].pontuacao

        q_number = i

        fig.add_trace(
            go.Box(
                y=y0,
                name=f'Quiz {q_number}'.format(q_number),
                marker_color='#FF7F00'
            ),
            row=subplots_rows, col=subplots_cols
        )

        fig.add_trace(
            go.Box(
                y=y1,
                name=f'Quiz {q_number} D'.format(q_number),
                marker_color='#593493'
            ),
            row=subplots_rows, col=subplots_cols
        )

        if subplots_cols == n_cols:
            subplots_cols = 1
            subplots_rows += 1
        else:
            subplots_cols += 1

    fig.update_layout(title_text="Quiz", showlegend=False,
                      height=1000, width=1250,)
    fig.update_traces(boxmean=True)
    fig.update_traces(orientation='v')
    st.plotly_chart(fig, use_container_width=True)
