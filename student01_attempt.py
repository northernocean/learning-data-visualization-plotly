import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

df_of = pd.read_csv('data/OldFaithful.csv')
print(df_of)

data = [
    go.Scatter(
        x=df_of["X"],
        y=df_of["Y"],
        mode="markers"
    )
]
layout = go.Layout(
    title='Old Faithful Eruption Intervals vs. Durations',
    xaxis={
        "title": "Duration of eruption [mins]"
    },
    yaxis={
        "title": "Interval to next eruption [mins]"
    }
)
fig_sc = go.Figure(
    data=data,
    layout=layout
)
app = dash.Dash()
app.layout = html.Div(
    [
        dcc.Graph(
            id="Scatter_old_faithful",
            figure={
                "data": data,
                "layout": layout
            }
        )
    ]
)

if __name__ == "__main__":
    app.run_server()
