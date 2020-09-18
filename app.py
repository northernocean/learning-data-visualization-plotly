import dash
import dash_core_components as core
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()

example_to_run = 2

if example_to_run == 1:

    # PART 1 - Dictionary-Style

    colors = {
        "background": "#111111",
        "text": "#7fdbff"
    }

    app.layout = html.Div(
        children=[
            html.H1(
                "Hello Dash",
                style={
                    "textAlign": "center",
                    "color": colors["text"]
                }
            ),
            html.Div("Dash: Web Dashboards with Python"),
            core.Graph(
                id="example",
                figure={
                    "data": [
                        {
                            "x": [1, 2, 3],
                            "y": [4, 1, 2],
                            "type": "bar",
                            "name": "SF"
                        },
                        {
                            "x": [1, 2, 3],
                            "y": [2, 4, 5],
                            "type": "bar",
                            "name": "NYC"
                        }
                    ],
                    "layout": {
                        "title": "Bar Plots",
                        "plot_bgcolor": colors["background"],
                        "paper_bgcolor": colors["background"],
                        "font": {
                            "color": colors["text"]
                        }
                    }
                }
            )
        ],
        style={
            "backgroundColor": colors["background"]
        }
    )

if example_to_run == 2:

    # PART 2 - Plotly-Style

    np.random.seed(42)

    xs = []
    ys = []
    for _ in range(0, 2):
        xs.append(np.random.randint(1, 101, 100))
        ys.append(np.random.randint(1, 101, 100))

    app.layout = html.Div(
        [
            # First Graph Object
            core.Graph(
                id="scatterplot1",
                figure={
                    "data": [
                        go.Scatter(
                            x=xs[0],
                            y=ys[0],
                            mode="markers",
                            marker=dict(
                                size=12,
                                color="rgb(51, 204,153)",
                                symbol="pentagon",
                                line={"width": 2}
                            )
                        )
                    ],
                    "layout": go.Layout(
                        title="Scatterplot",
                        xaxis=dict(
                            title="X axis"
                        )
                    )
                }
            ),
            # second graph object
            core.Graph(
                id="scatterplot2",
                figure={
                    "data": [
                        go.Scatter(
                            x=xs[1],
                            y=ys[1],
                            mode="markers",
                            marker=dict(
                                size=12,
                                color="rgb(200, 204,53)",
                                symbol="pentagon",
                                line={"width": 2}
                            )
                        )
                    ],
                    "layout": go.Layout(
                        title="Scatterplot",
                        xaxis=dict(
                            title="X axis"
                        )
                    )
                }
            )
        ]
    )

if __name__ == "__main__":
    app.run_server()
