import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)

xs = np.linspace(0, 10, 100)
ys = np.sin(xs)

data = [
    go.Scatter(
        x=xs,
        y=ys,
        mode="markers",
        marker=dict(
            size=6,
            color="rgb(51,204,153)",
            symbol="pentagon",
            line={"width": 1})
    )]

layout = go.Layout(
    title="Sine Curve",
    xaxis=dict(title="x-values"),
    yaxis=dict(title="yaxis"),
    hovermode="closest")

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)  # or just fig.show()
