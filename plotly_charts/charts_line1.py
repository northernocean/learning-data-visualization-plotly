import numpy as np
import plotly.graph_objs as go

rng = np.random.default_rng(42)

xs = np.linspace(0, 1, 100)
ys = rng.normal(0, 1, (100,))

data = []

data.append(
    go.Scatter(
        x=xs,
        y=(ys + 10),
        mode="markers",
        name="graph1"
    )
)

data.append(
    go.Scatter(
        x=xs,
        y=(ys + 5),
        mode="lines",
        name="graph2"
    )
)

data.append(
    go.Scatter(
        x=xs,
        y=ys,
        mode="lines+markers",
        name="graph2"
    )
)

layout = go.Layout(title="Plotly Basics")

fig = go.Figure(data=data, layout=layout)

fig.show()
