import dash
import dash_core_components as core
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()

app.layout = html.Div(
    [
        "this is the outermost div",
        html.Div(
            "this is an inner div",
            style={
                "color": "red"
            }
        ),
        html.Div(
            "another inner div",
            style={
                "color": "blue",
                "border": "3px solid blue"
            }
        )
    ],
    style={
        "color": "green",
        "border": "6px solid green"
    }
)

if __name__ == "__main__":
    app.run_server()
