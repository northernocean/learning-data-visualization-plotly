import datetime
import dash
import dash_core_components as core
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()


def inner_text(n):
    return(
        "Refreshed " + str(n) + " times."
        + "<p>The time is: " + str(datetime.datetime.now())
    )


app.layout = html.Div(
    [
        html.H4(
            id="3d602"
        ),
        core.Interval(
            id="a0982",
            interval=2000,
            n_intervals=0
        )
    ]
)


@app.callback(
    Output("3d602", "children"),
    [
        Input(
            "a0982", "n_intervals"
        )
    ]
)
def update_layout(n):
    return inner_text(n)


if __name__ == "__main__":
    app.run_server()


