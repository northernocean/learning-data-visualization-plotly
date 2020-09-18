import dash
import dash_core_components as core
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()

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
