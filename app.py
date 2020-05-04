import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from src.plots import get_line_plot_data, get_bar_plot, get_gender_plot, get_age_hist
import pandas as pd
app = dash.Dash()

# Reading Data
national_timeseries = pd.read_csv("./data/covid_national_timeseries.csv")
gender_age_data = pd.read_csv("data/covid_raw_gender_age_full.csv")



app.layout = html.Div([


    html.Div([
        dcc.Graph(id="my-line-plot",
                    figure={
                        "data": get_line_plot_data(national_timeseries),
                        "layout": {"title": "Total Cases"}
                    })
    ],
    style={"align": "left", "display": "inline-block"}),

    html.Div([
        dcc.Graph(id="my-bar-plot",
                    figure={
                        "data": get_bar_plot(national_timeseries),
                        "layout": {"title": "Histogram"}
                    })
    ],
    style={"float": "right", "display": "inline-block"}),

    html.Div([
        dcc.Graph(id="my-histogram",
            figure={
                "data": get_age_hist(gender_age_data),
                "layout": {"title": "Age"}
            })
    ],
    style={"align": "left", "display": "inline-block"}),
    html.Div([
        dcc.Graph("my-pie-graph",
            figure={
                "data": get_gender_plot(gender_age_data),
                "layout":{"title":"Gender"}
            })
            ],
            style={"float": "right", "display": "inline-block"}),


])


#### Callback Functions


if __name__=="__main__":
    app.run_server()