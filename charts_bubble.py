import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv("data/mpg.csv").filter(
    ["mpg", "cylinders", "horsepower", "name", "weight"], axis=1)

data = [
    go.Scatter(
        x=df["horsepower"],
        y=df["mpg"],
        text=df['name'],
        mode="markers",
        marker=dict(
            size=(df["weight"] / 100),
            color=df["cylinders"],
            showscale=True)
    )
]
layout = go.Layout(title="MPG vs. Horsepower")

fig = go.Figure(data=data, layout=layout)
fig.show()
