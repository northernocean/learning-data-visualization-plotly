import datetime
import dash
import dash_core_components as core
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

count = 0


def refresh_layout():
    global count
    count += 1
    return html.Div(
        [
            html.H4(f"Refreshed {str(count)} times."),
            html.H4('The time is: ' + str(datetime.datetime.now()))
        ]
    )



app.layout = refresh_layout

if __name__ == "__main__":
    app.run_server()


