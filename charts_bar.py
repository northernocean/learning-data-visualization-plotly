import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv("data/2018WinterOlympics.csv")
print(df.head())

# Bar Chart of Total Medals
data = [
    go.Bar(
        x=df['NOC'],
        y=df['Total']
    )
]
layout = go.Layout(
    title="Medals"
)
fig = go.Figure(data=data, layout=layout)
fig.show()

# Nested Bar Chart
traces = []
traces.append(
    go.Bar(
        x=df['NOC'],
        y=df['Gold'],
        name='Gold',
        marker={'color': '#ffd700'}))
traces.append(
    go.Bar(
        x=df['NOC'],
        y=df['Silver'],
        name='Silver',
        marker={'color': '#9ea0a1'}))
traces.append(
    go.Bar(
        x=df['NOC'],
        y=df['Bronze'],
        name='Bronze',
        marker={'color': '#cd7f32'}))
fig = go.Figure(data=traces, layout=layout)
fig.show()

# Stacked Bar Chart
layout = go.Layout(title="Medals", barmode="stack")
fig = go.Figure(data=traces, layout=layout)
fig.show()
