# using this file to test different adjustments to the app layout


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{"name":"viewport","content":"width-device-width, initial-scale=1.0"}]
                )

# card image will be stock/crypto symbol asset
# first row tbd - some kind of indicator
# 2nd row graph with lines representing actual and predicted with models
# 3rd row metrics

# Huge section of tab builders
tab1_content = dbc.Col([
        dbc.Row([
            dbc.Card(
                [
                    dbc.CardImg(
                        src="/assets/apple.png",
                        top=True,
                        style={"width": "6rem"},
                    ),

                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(id='apple_roi', figure={},
                                          config={'displayModeBar':False})
                            ])
                        ]),
                    ]),
                ],
                style={"width": "24rem"},
                className="mt-3"
            ),
            dbc.Card(
                [
                    dbc.CardImg(
                        src="/assets/amazon.png",
                        top=True,
                        style={"width": "6rem"},
                    ),

                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(id='amzn_roi', figure={},
                                          config={'displayModeBar':False})
                            ])
                        ]),
                    ]),
                ],
                style={"width": "24rem"},
                className="mt-3"
            ),
            dbc.Card(
                [
                    dbc.CardImg(
                        src="/assets/berkshire-hathaway.png",
                        top=True,
                        style={"width": "6rem"},
                    ),

                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(id='brkb_roi', figure={},
                                          config={'displayModeBar':False})
                            ])
                        ]),
                    ]),
                ],
                style={"width": "24rem"},
                className="mt-3"
            ),
        ]),
        dbc.Row([
            dbc.Card(
                [
                    dbc.CardImg(
                        src="/assets/facebook.png",
                        top=True,
                        style={"width": "6rem"},
                    ),

                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(id='fb_roi', figure={},
                                          config={'displayModeBar':False})
                            ])
                        ]),
                    ]),
                ],
                style={"width": "24rem"},
                className="mt-3"
            ),
            dbc.Card(
                [
                    dbc.CardImg(
                        src="/assets/google.png",
                        top=True,
                        style={"width": "6rem"},
                    ),

                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(id='googl_roi', figure={},
                                          config={'displayModeBar':False})
                            ])
                        ]),
                    ]),
                ],
                style={"width": "24rem"},
                className="mt-3"
            ),
            dbc.Card(
                [
                    dbc.CardImg(
                        src="/assets/jnj.png",
                        top=True,
                        style={"width": "6rem"},
                    ),

                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(id='jnj_roi', figure={},
                                          config={'displayModeBar':False})
                            ])
                        ]),
                    ]),
                ],
                style={"width": "24rem"},
                className="mt-3"
            ),
        ]),
        dbc.Row([
            dbc.Card(
                [
                    dbc.CardImg(
                        src="/assets/jpmorgan.png",
                        top=True,
                        style={"width": "6rem"},
                    ),

                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(id='jpm_roi', figure={},
                                          config={'displayModeBar':False})
                            ])
                        ]),
                    ]),
                ],
                style={"width": "24rem"},
                className="mt-3"
            ),
            dbc.Card(
                [
                    dbc.CardImg(
                        src="/assets/microsoft.png",
                        top=True,
                        style={"width": "6rem"},
                    ),

                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(id='msft_roi', figure={},
                                          config={'displayModeBar':False})
                            ])
                        ]),
                    ]),
                ],
                style={"width": "24rem"},
                className="mt-3"
            ),
            dbc.Card(
                [
                    dbc.CardImg(
                        src="/assets/nvidia.png",
                        top=True,
                        style={"width": "6rem"},
                    ),

                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(id='nvda_roi', figure={},
                                          config={'displayModeBar':False})
                            ])
                        ]),
                    ]),
                ],
                style={"width": "24rem"},
                className="mt-3"
            ),
        ]),
        dbc.Row([
            dbc.Card(
                [
                    dbc.CardImg(
                        src="/assets/tesla.png",
                        top=True,
                        style={"width": "6rem"},
                    ),

                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(id='tsla_roi', figure={},
                                          config={'displayModeBar':False})
                            ])
                        ]),
                    ]),
                ],
                style={"width": "24rem"},
                className="mt-3"
            ),
            dbc.Card(
                [
                    dbc.CardImg(
                        src="/assets/bitcoin.png",
                        top=True,
                        style={"width": "6rem"},
                    ),

                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(id='btc_roi', figure={},
                                          config={'displayModeBar':False})
                            ])
                        ]),
                    ]),
                ],
                style={"width": "24rem"},
                className="mt-3"
            ),
            dbc.Card(
                [
                    dbc.CardImg(
                        src="/assets/ethereum.png",
                        top=True,
                        style={"width": "6rem"},
                    ),

                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(id='eth_roi', figure={},
                                          config={'displayModeBar':False})
                            ])
                        ]),
                    ]),
                ],
                style={"width": "24rem"},
                className="mt-3"
            ),
        ])
    ])

# add content for metrics bar plots
# tab2_content = dbc.Row([dbc.])

# overall structure of app    
tabs = dbc.Tabs(
    [
        dbc.Tab(tab1_content, label="ROI vs Time"),
        dbc.Tab(
            "TBA", label="Summary Metrics"),
    ]
)

# app layout functionality
app.layout = tabs

# Lines
# Metrics

if __name__=='__main__':
    app.run_server(debug=True, port=3000)