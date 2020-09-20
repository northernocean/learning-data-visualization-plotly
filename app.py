import dash
import dash_core_components as core
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

df = pd.read_csv('data/mpg.csv')
print(df)

features = df.columns

# ------------------------------------------
# Two Dropdowns and Graph
# First Dropdown: Select x value to graph
# Second Dropdown : Select y value to graph
# The values for the dropdowns will be keyed
#   to the feature names of the dataset
# ------------------------------------------
app.layout = html.Div(
    [
        html.Div(
            [
                core.Graph(id='feature-graphic')
            ],
            style={'margin-top': '40px'}
        ),
        html.Div(
            [
                core.Dropdown(
                    id='xaxis',
                    options=[{'label': i.title(), 'value': i} for i in features],
                    value='displacement'
                )
            ],
            style={'width': '48%', 'margin-bottom': '10px', 'margin-top': '40px'}
        ),
        html.Div(
            [
                core.Dropdown(
                    id='yaxis',
                    options=[{'label': i.title(), 'value': i} for i in features],
                    value='acceleration'
                )
            ],
            style={'width': '48%', 'margin': '40 0'}
        )
    ], style={'padding': 10}
)


@app.callback(
    Output('feature-graphic', 'figure'),
    [
        Input('xaxis', 'value'),
        Input('yaxis', 'value')
    ]
)
def update_graph(xaxis_name, yaxis_name):
    return {
        'data': [go.Scatter(
            x=df[xaxis_name],
            y=df[yaxis_name],
            text=df['name'],
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {
                    'width': 0.5,
                    'color': 'white'}
            }
        )],
        'layout': go.Layout(
            xaxis={
                'title': xaxis_name.title()
            },
            yaxis={
                'title': yaxis_name.title()
            },
            margin={
                'l': 40,
                'b': 40,
                't': 10,
                'r': 0
            },
            hovermode='closest'
        )
    }


if __name__ == '__main__':
    app.run_server()
