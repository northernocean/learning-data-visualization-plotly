import dash
import dash_core_components as core
import dash_html_components as html

app = dash.Dash()

colors = {
    "background": "#111111",
    "text": "#7fdbff"
}

app.layout = html.Div(
    children=[
        html.H1(
            "Hello Dash",
            style={
                "textAlign": "center",
                "color": colors["text"]
            }
        ),
        html.Div("Dash: Web Dashboards with Python"),
        core.Graph(
            id="example",
            figure={
                "data": [
                    {
                        "x": [1, 2, 3],
                        "y": [4, 1, 2],
                        "type": "bar",
                        "name": "SF"
                    },
                    {
                        "x": [1, 2, 3],
                        "y": [2, 4, 5],
                        "type": "bar",
                        "name": "NYC"
                    }
                ],
                "layout": {
                    "title": "Bar Plots",
                    "plot_bgcolor": colors["background"],
                    "paper_bgcolor": colors["background"],
                    "font": {
                        "color": colors["text"]
                    }
                }
            }
        )
    ],
    style={
        "backgroundColor": colors["background"]
    }
)

if __name__ == "__main__":
    app.run_server()
