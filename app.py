import dash
import dash_core_components as core
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div(
    [
        core.Input(
            id="4f20",
            value="type some text here",
            type="text"
        ),
        html.Div(
            id="51e3"
        )

    ]
)


@app.callback(
    Output(component_id="51e3", component_property="children"),
    [Input(component_id="4f20", component_property="value")])
def update_output_div(input_value):
    return input_value


if __name__ == '__main__':
    app.run_server()
