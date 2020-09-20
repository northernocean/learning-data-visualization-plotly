import os
import base64
import dash
import dash_core_components as core
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

df = pd.read_csv("data/wheels.csv")
print(df)

app = dash.Dash()


def encode_image(file_path):
    encoded = base64.b64encode(open(file_path, "rb").read())
    return f"data:image/png;base64,{encoded.decode()}"


app.layout = html.Div(
    [
        # Radio Button
        html.Div(
            className="dash-app",
            children=[
                core.RadioItems(
                    id="wheels",
                    options=[
                        {"label": i, "value": i} for i in df["wheels"].unique()
                    ],
                    value=1
                )
            ]
        ),
        # output for number of wheels
        html.Div(
            className="dash-app",
            id="wheels-output",
        ),
        # Color Dropdown
        html.Div(
            className="dash-app",
            children=[
                core.RadioItems(
                    id="colors",
                    options=[
                        {"label": i, "value": i} for i in df["color"].unique()
                    ],
                    value="blue"
                )

            ]
        ),
        # output for number of colors
        html.Div(
            className="dash-app",
            id="colors-output",
        ),
        html.Img(
            className="dash-app",
            id="display-image",
            src="children",
            height=300

        )
    ]
)


@app.callback(
    Output("wheels-output", "children"),
    [Input("wheels", "value")])
def callback_wheels(wheels_value):
    return wheels_value


@app.callback(
    Output("colors-output", "children"),
    [Input("colors", "value")])
def callback_colors(colors_value):
    return colors_value


@app.callback(
    Output("display-image", "src"),
    [Input("wheels", "value"), Input("colors", "value")]
)
def callback_image(wheel, color):
    path = df[(df["wheels"] == wheel) & (df["color"] == color)].iloc[0]["image"]
    path = os.path.join("data", "images", path)
    return encode_image(path)


if __name__ == '__main__':
    app.run_server()
