import dash
import dash_core_components as core
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()

app.layout = html.Div(
    [
        html.Div(
            [
                html.Label("Dropdown"),
                core.Dropdown(
                    options=[
                        {"label": "New York City", "value": "NYC"},
                        {"label": "San Francisco", "value": "SF"}
                    ],
                    value="SF"
                )
            ],
            style={"margin": "40px"}
        ),
        html.Div(
            [
                html.Label("Slider"),
                core.Slider(
                    min=-10,
                    max=10,
                    step=1,
                    value=0,
                    marks={i: i for i in range(-10, 10)}
                )
            ],
            style={"margin": "40px"}
        ),
        html.Div(
            [
                html.Label("Radio"),
                core.RadioItems(
                    options=[
                        {"label": "New York City", "value": "NYC"},
                        {"label": "San Francisco", "value": "SF"},
                    ],
                    value="SF"
                )
            ],
            style={"margin": "40px"}
        )
    ]
)

if __name__ == "__main__":
    app.run_server()
