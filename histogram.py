from plotly.subplots import make_subplots
import plotly.graph_objects as go
import streamlit as st


def plot_quiz_hist(quiz_data, n_rows, n_cols):

    quiz_range = len(
        quiz_data[quiz_data.titulo_objeto.str.endswith("D")].titulo_objeto.unique())

    fig = make_subplots(
        rows=n_rows,
        cols=n_cols,
        subplot_titles=([(lambda x: f'Quiz {x} / {x} D'.format(x))(x)
                        for x in range(1, quiz_range + 1)])
    )

    subplots_rows = 1
    subplots_cols = 1

    for i in range(1, quiz_range + 1):
        x0 = quiz_data[quiz_data.titulo_objeto ==
                       f'Quiz {i}'.format(i)].pontuacao

        x1 = quiz_data[quiz_data.titulo_objeto ==
                       f'Quiz {i} D'.format(i)].pontuacao

        y0 = quiz_data[quiz_data.titulo_objeto ==
                       f'Quiz {i}'.format(i)]

        y1 = quiz_data[quiz_data.titulo_objeto ==
                       f'Quiz {i} D'.format(i)]
        q_number = i

        fig.add_trace(
            go.Histogram(
                x=x0,
                y=y0,
                name=f'Quiz {q_number}'.format(q_number),
                nbinsx=10,
                marker_color='#FF7F00'
            ),
            row=subplots_rows, col=subplots_cols
        )

        fig.add_trace(
            go.Histogram(
                x=x1,
                y=y1,
                name=f'Quiz {q_number} D'.format(q_number),
                nbinsx=10,
                marker_color='#593493',
                opacity=0.55
            ),
            row=subplots_rows, col=subplots_cols
        )

        if subplots_cols == n_cols:
            subplots_cols = 1
            subplots_rows += 1
        else:
            subplots_cols += 1

    fig.update_layout(barmode='overlay', height=1000, width=1250,
                      title_text="Quiz", showlegend=False)
    fig.update_traces(histnorm="density")
    fig.update_xaxes(range=[0, 100], tick0=0, dtick=20)
    fig.update_yaxes(range=[0, 1], tick0=0, dtick=0.2)
    st.plotly_chart(fig, use_container_width=True)
