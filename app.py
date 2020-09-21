#######
# This shows the mpg.csv dataset as a spread out scatter plot
# that sends hoverData to another graph via callback, and to
# a Markdown component through a second callback.
######
import os
import datetime
import dash
import dash_core_components as core
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import pandas_datareader as data
from numpy import random

try:
    df = pd.read_csv('data/stocks.csv', index_col=None)
except FileNotFoundError:
    df = None

if df is None:
    print('Retrieving data from yahoo api...')
    tickers = ['WORK', 'HA', 'NGVC']
    start_date = pd.to_datetime('2020-01-01')
    end_date = pd.to_datetime('today')

    df = []
    for ticker in tickers:
        temp = data.DataReader(ticker, 'yahoo', start_date, end_date)
        if temp is not None:
            temp.insert(0, 'Ticker', ticker)
            temp.reset_index(level=0, inplace=True)
            df.append(temp)
    if df:
        df = pd.concat(df, ignore_index=True)
        df.to_csv('data/stocks.csv', index=False)

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
                            id="ddl_stocks",
                            children=[
                                "Select Stock Ticker: ",
                                core.Dropdown()
                            ]
                        ),
                        html.Div(
                            className="2e6006",
                            id="dtp_dates",
                            children=[
                                "Select Start and End Dates: ",
                                core.DatePickerRange()
                            ]
                        ),
                        html.Div(
                            className="2e6009",
                            id="btnSubmit",
                            children=[
                                html.Button("Submit")
                            ]
                        )
                    ]
                ),
                html.Div(
                    className="42c090",
                    children=[
                        core.Graph(
                            id="stocks_graph",
                            figure={
                                "data": [
                                    {
                                        "x": [1, 2, 3],
                                        "y": [5, 7, 6]
                                    }
                                ],
                                "layout": {
                                    "title": "Stocks Graph"
                                }
                            }
                        )
                    ]
                )
            ]
        )
    ]
)


@app.callback(
    Output("stocks_graph", "figure"),
    [Input("ddl_stocks", "value")]
)
def update_title(arg):
    if arg is None:
        arg = "Foo"
    figure = {
        "data": [
            {
                "x": [1, 2, 3],
                "y": [5, 7, 8]
            }
        ],
        "layout": {
            "title": arg
        }
    }
    return figure


if __name__ == '__main__':
    app.run_server()
