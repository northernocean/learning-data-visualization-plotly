import datetime
import dash
import dash_core_components as core
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash.exceptions as dash_exceptions
import pandas_datareader as data


def get_figure(tickers, start_date, end_date, title="Closing Stock Prices"):
    print(tickers)
    traces = []
    for ticker in tickers:
        df = get_data(ticker, start_date, end_date)
        traces.append({"x": df.index, "y": df["Close"], "name": ticker})
    fig = {
        "data": traces,
        "layout": {
            "title": title
        }
    }
    return fig


def get_data(ticker, start_date, end_date):
    df = data.DataReader(ticker, 'yahoo', start_date, end_date)
    if df is not None:
        df.insert(0, 'Ticker', ticker)
        df.reset_index(level=0, inplace=True)
    return df


options = [
    {"label": "WORK", "value": "WORK"},
    {"label": "HA", "value": "HA"},
    {"label": "NGVC", "value": "NGVC"}
]

print(options[0]["value"])
print([options[0]["value"]])
app = dash.Dash()

app.layout = html.Div(
    className="container",
    children=[

        html.Div(
            className="4d7000",
            children=[

                html.Div(
                    className="2e6000",
                    children=[
                        html.Div(
                            className="2e6003",
                            children=[
                                "Select Stock Ticker: ",
                                core.Dropdown(
                                    id="ddl_stocks",
                                    options=options,
                                    multi=True,
                                    value=[options[0]["value"]]
                                )
                            ]
                        ),

                        html.Div(
                            className="2e6006",
                            children=[
                                "Select Start and End Dates: ",
                                core.DatePickerRange(
                                    id="dtp_dates",
                                    min_date_allowed=datetime.date(2015, 1, 1),
                                    max_date_allowed=datetime.date.today(),
                                    start_date=datetime.date(2020, 1, 1),
                                    end_date=datetime.date.today()
                                )
                            ]
                        ),
                        html.Div(
                            className="2e6009",
                            children=[
                                html.Button(
                                    id="btn_submit",
                                    children=[
                                        "Submit"
                                    ]
                                )
                            ]
                        )
                    ]
                ),

                html.Div(
                    className="42c090",
                    children=[
                        core.Graph(
                            id="stocks_graph",
                            figure=get_figure(
                                [options[0]["value"]],
                                '2020-01-01',
                                datetime.date.today().isoformat()
                            )
                        )
                    ]
                )
            ]
        )
    ]
)


@app.callback(
    Output("ddl_stocks", "options"),
    [Input("ddl_stocks", "search_value")],
)
def update_options(search_value):
    if not search_value:
        raise dash_exceptions.PreventUpdate
    return [opt for opt in options if search_value in opt["label"]]


@app.callback(
    Output("stocks_graph", "figure"),
    [Input("btn_submit", "n_clicks")],
    [
        State("ddl_stocks", "value"),
        State("dtp_dates", "start_date"),
        State("dtp_dates", "end_date")
    ]
)
def update_graph(n_clicks, tickers, start_date, end_date):
    fig = get_figure(
        tickers=tickers,
        start_date=start_date,
        end_date=end_date
    )
    return fig


if __name__ == '__main__':
    app.run_server()
