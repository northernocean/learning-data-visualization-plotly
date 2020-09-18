import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv("data/mpg.csv")

data = [
    go.Histogram(
        x=df["mpg"],
    )
]

layout = go.Layout(title="Histogram")
fig = go.Figure(data=data, layout=layout)
fig.show()
