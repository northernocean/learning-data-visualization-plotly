import os
import base64
import dash
import dash_core_components as core
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import json

app = dash.Dash()

df = pd.read_csv('data/wheels.csv')


def encode_image(file_path):
    encoded = base64.b64encode(open(file_path, "rb").read())
    return f"data:image/png;base64,{encoded.decode()}"


app.layout = html.Div(
    children=[
        html.Div(
            className="dash-app",
            children=[
                core.Graph(
                    id='wheels-plot',
                    figure={
                        'data': [
                            go.Scatter(
                                x=df['color'],
                                y=df['wheels'],
                                dy=1,
                                mode='markers',
                                marker={
                                    'size': 12,
                                    'color': 'rgb(51,204,153)',
                                    'line': {'width': 2}
                                }
                            )
                        ],
                        'layout': go.Layout(
                            title='Wheels & Colors Scatterplot',
                            xaxis={
                                'title': 'Color'
                            },
                            yaxis={
                                'title': '# of Wheels',
                                'nticks': 3
                            },
                            hovermode='closest'
                        )
                    }
                )
            ]
        ),
        html.Div(
            className="dash-app",
            children=[
                html.Pre(
                    id='hover-data'
                )
            ]
        )
        # ,html.Div(
        #     [
        #         html.Img(
        #             id='hover-image',
        #             src='children',
        #             height=300
        #         )
        #     ]
        # )
    ]
)


# output hover data on page
@app.callback(
    Output('hover-data', 'children'),
    [Input('wheels-plot', 'selectedData')]
)
def callback_json(selectedData):
    return json.dumps(selectedData, indent=2)


# output image on page
# @app.callback(
#     Output('hover-image', 'src'),
#     [Input('wheels-plot', 'selectedData')]
# )
# def callback_image(selectedData):
#     wheel = selectedData['points'][0]['y']
#     color = selectedData['points'][0]['x']
#     path = df[(df["wheels"] == wheel) & (df["color"] == color)].iloc[0]["image"]
#     path = os.path.join("data", "images", path)
#     return encode_image(path)


if __name__ == '__main__':
    app.run_server()
