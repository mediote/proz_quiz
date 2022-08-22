import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import streamlit as st


def create_quiz_metrics_dataset(quiz_data):
    quiz_range = len(
        quiz_data[quiz_data.titulo_objeto.str.contains("D")].titulo_objeto.unique())

    quiz_list = list()
    for quiz_number in range(1, quiz_range + 1):
        quiz = {
            "quiz": f'Quiz {quiz_number}'.format(quiz_number),
            "mean": quiz_data[quiz_data.titulo_objeto == f'Quiz {quiz_number}'.format(quiz_number)].pontuacao.describe().mean(),
            "median": quiz_data[quiz_data.titulo_objeto == f'Quiz {quiz_number}'.format(quiz_number)].pontuacao.describe().median()
        }

        quiz_d = {
            "quiz": f'Quiz {quiz_number} D'.format(quiz_number),
            "mean": quiz_data[quiz_data.titulo_objeto == f'Quiz {quiz_number} D'.format(quiz_number)].pontuacao.describe().mean(),
            "median": quiz_data[quiz_data.titulo_objeto == f'Quiz {quiz_number} D'.format(quiz_number)].pontuacao.describe().median()
        }
        quiz_list.append(quiz)
        quiz_list.append(quiz_d)

    quiz_metrics = pd.DataFrame(quiz_list)
    return quiz_metrics


def plot_quiz_bar(quiz_data, n_rows, n_cols):

    quiz_range = len(
        quiz_data[quiz_data.quiz.str.contains("D")].quiz.unique())

    fig = make_subplots(
        rows=n_rows,
        cols=n_cols,
        subplot_titles=([(lambda x: f'Quiz {x} / {x} D'.format(x))(x)
                         for x in range(1, quiz_range + 1)])
    )

    subplots_rows = 1
    subplots_cols = 1

    for i in range(1, quiz_range + 1):

        y0 = quiz_data[quiz_data.quiz ==
                       f'Quiz {i}'.format(i)]['mean']
        y1 = quiz_data[quiz_data.quiz ==
                       f'Quiz {i} D'.format(i)]['median']
        q_number = i

        fig.add_trace(
            go.Bar(
                #x=['Media', 'Mediana'],
                y=y0,
                name=f'Quiz {q_number}'.format(q_number),
                marker_color='#FF7F00'
            ),
            row=subplots_rows, col=subplots_cols
        )

        fig.add_trace(
            go.Bar(
                #x=['Media', 'Mediana'],
                y=y1,
                name=f'quiz {q_number} D'.format(q_number),
                marker_color='#593493'
            ),
            row=subplots_rows, col=subplots_cols
        )

        if subplots_cols == n_cols:
            subplots_cols = 1
            subplots_rows += 1
        else:
            subplots_cols += 1

    fig.update_layout(height=1000, width=1250,
                      title_text="Quiz", showlegend=False)
    fig.update_yaxes(range=[0, 100], tick0=0, dtick=20)
    st.plotly_chart(fig, use_container_width=True)
