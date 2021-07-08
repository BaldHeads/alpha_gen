# using this file to test different adjustments to the app layout


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import get_roi_px

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO],
                meta_tags=[{"name":"viewport","content":"width-device-width, initial-scale=1.0"}]
                )

# card image will be stock/crypto symbol asset
# first row tbd - some kind of indicator
# 2nd row graph with lines representing actual and predicted with models
# 3rd row metrics

# Huge section of tab builders
tab1_content = dbc.Col([
        dbc.Row([
            dbc.Card([
                    dbc.Row([
                        dbc.Col([
                            dbc.CardImg(
                                src="/assets/apple.png",
                                top=True,
                                style={"width": "6rem"},),
                        ]),
                        dbc.Col([
                            dbc.Row([html.H5("Model Precision")]),
                            dbc.Row([dbc.Table.from_dataframe(get_roi_px.gen_table("aapl"), striped=True,bordered=True, dark=True)]),
                        ])   
                    ]),

                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(id='aapl_roi', figure=get_roi_px.get_roi_plot('aapl_roi'),
                                          config={'displayModeBar':False})
                            ])
                        ]),
                    ]),
                ],
                style={"width": "36rem"},
                className="mt-3"
            ),
            dbc.Card([
                    dbc.Row([
                        dbc.Col([
                            dbc.CardImg(
                                src="/assets/amazon.png",
                                top=True,
                                style={"width": "6rem"},),
                        ]),
                        dbc.Col([
                            dbc.Row([html.H5("Model Precision")]),
                            dbc.Row([dbc.Table.from_dataframe(get_roi_px.gen_table("amzn"), striped=True,bordered=True, dark=True)]),
                        ])   
                    ]),

                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(id='amzn_roi', figure=get_roi_px.get_roi_plot('amzn_roi'),
                                          config={'displayModeBar':False})
                            ])
                        ]),
                    ]),
                ],
                style={"width": "36rem"},
                className="mt-3"
            ),
            dbc.Card([
                    dbc.Row([
                        dbc.Col([
                            dbc.CardImg(
                                src="/assets/berkshire-hathaway.png",
                                top=True,
                                style={"width": "6rem"},),
                        ]),
                        dbc.Col([
                            dbc.Row([html.H5("Model Precision")]),
                            dbc.Row([
                                dbc.Table.from_dataframe(get_roi_px.gen_table("brk.b"), 
                                    size="sm", striped=True,bordered=True, dark=True)]), 
                        ])   
                    ]),

                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(id='brkb_roi', figure=get_roi_px.get_roi_plot('brk.b_roi'),
                                          config={'displayModeBar':False})
                            ])
                        ]),
                    ]),
                ],
                style={"width": "36rem"},
                className="mt-3"
            ),
        ]),
        dbc.Row([
            dbc.Card([
                    dbc.Row([
                        dbc.Col([
                            dbc.CardImg(
                                src="/assets/facebook.png",
                                top=True,
                                style={"width": "6rem"},),
                        ]),
                        dbc.Col([
                            dbc.Row([html.H5("Model Precision")]),
                            dbc.Row([dbc.Table.from_dataframe(get_roi_px.gen_table("fb"), striped=True,bordered=True, dark=True)]),
                        ])   
                    ]),

                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(id='fb_roi', figure=get_roi_px.get_roi_plot('fb_roi'),
                                          config={'displayModeBar':False})
                            ])
                        ]),
                    ]),
                ],
                style={"width": "36rem"},
                className="mt-3"
            ),
            dbc.Card([
                    dbc.Row([
                        dbc.Col([
                            dbc.CardImg(
                                src="/assets/google.png",
                                top=True,
                                style={"width": "6rem"},),
                        ]),
                        dbc.Col([
                            dbc.Row([html.H5("Model Precision")]),
                            dbc.Row([dbc.Table.from_dataframe(get_roi_px.gen_table("googl"), striped=True,bordered=True, dark=True)]),
                        ])   
                    ]),

                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(id='googl_roi', figure=get_roi_px.get_roi_plot('googl_roi'),
                                          config={'displayModeBar':False})
                            ])
                        ]),
                    ]),
                ],
                style={"width": "36rem"},
                className="mt-3"
            ),
            dbc.Card([
                    dbc.Row([
                        dbc.Col([
                            dbc.CardImg(
                                src="/assets/jnj.png",
                                top=True,
                                style={"width": "6rem"},),
                        ]),
                        dbc.Col([
                            dbc.Row([html.H5("Model Precision")]),
                            dbc.Row([dbc.Table.from_dataframe(get_roi_px.gen_table("jnj"), striped=True,bordered=True, dark=True)]),
                        ])   
                    ]),

                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(id='jnj_roi', figure=get_roi_px.get_roi_plot('jnj_roi'),
                                          config={'displayModeBar':False})
                            ])
                        ]),
                    ]),
                ],
                style={"width": "36rem"},
                className="mt-3"
            ),
        ]),
        dbc.Row([
            dbc.Card([
                    dbc.Row([
                        dbc.Col([
                            dbc.CardImg(
                                src="/assets/jpmorgan.png",
                                top=True,
                                style={"width": "6rem"},),
                        ]),
                        dbc.Col([
                            dbc.Row([html.H5("Model Precision")]),
                            dbc.Row([dbc.Table.from_dataframe(get_roi_px.gen_table("jpm"), striped=True,bordered=True, dark=True)]),
                        ])   
                    ]),

                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(id='jpm_roi', figure=get_roi_px.get_roi_plot('jpm_roi'),
                                          config={'displayModeBar':False})
                            ])
                        ]),
                    ]),
                ],
                style={"width": "36rem"},
                className="mt-3"
            ),
            dbc.Card([
                    dbc.Row([
                        dbc.Col([
                            dbc.CardImg(
                                src="/assets/microsoft.png",
                                top=True,
                                style={"width": "6rem"},),
                        ]),
                        dbc.Col([
                            dbc.Row([html.H5("Model Precision")]),
                            dbc.Row([dbc.Table.from_dataframe(get_roi_px.gen_table("msft"), striped=True,bordered=True, dark=True)]),
                        ])   
                    ]),

                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(id='msft_roi', figure=get_roi_px.get_roi_plot('msft_roi'),
                                          config={'displayModeBar':False})
                            ])
                        ]),
                    ]),
                ],
                style={"width": "36rem"},
                className="mt-3"
            ),
            dbc.Card([
                    dbc.Row([
                        dbc.Col([
                            dbc.CardImg(
                                src="/assets/nvidia.png",
                                top=True,
                                style={"width": "6rem"},),
                        ]),
                        dbc.Col([
                            dbc.Row([html.H5("Model Precision")]),
                            dbc.Row([dbc.Table.from_dataframe(get_roi_px.gen_table("nvda"), striped=True,bordered=True, dark=True)]),
                        ])   
                    ]),

                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(id='nvda_roi', figure=get_roi_px.get_roi_plot('nvda_roi'),
                                          config={'displayModeBar':False})
                            ])
                        ]),
                    ]),
                ],
                style={"width": "36rem"},
                className="mt-3"
            ),
        ]),
        dbc.Row([
            dbc.Card([
                    dbc.Row([
                        dbc.Col([
                            dbc.CardImg(
                                src="/assets/tesla.png",
                                top=True,
                                style={"width": "6rem"},),
                        ]),
                        dbc.Col([
                            dbc.Row([html.H5("Model Precision")]),
                            dbc.Row([dbc.Table.from_dataframe(get_roi_px.gen_table("tsla"), striped=True,bordered=True, dark=True)]),
                        ])   
                    ]),

                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(id='tsla_roi', figure=get_roi_px.get_roi_plot('tsla_roi'),
                                          config={'displayModeBar':False})
                            ])
                        ]),
                    ]),
                ],
                style={"width": "36rem"},
                className="mt-3"
            ),
            dbc.Card([
                    dbc.Row([
                        dbc.Col([
                            dbc.CardImg(
                                src="/assets/bitcoin.png",
                                top=True,
                                style={"width": "6rem"},),
                        ]),
                        dbc.Col([
                            dbc.Row([html.H5("Model Precision")]),
                            dbc.Row([dbc.Table.from_dataframe(get_roi_px.gen_table("btc"), striped=True,bordered=True, dark=True)]),
                        ])   
                    ]),

                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(id='btc_roi', figure=get_roi_px.get_crypto_roi_plot('btc_roi'),
                                          config={'displayModeBar':False})
                            ])
                        ]),
                    ]),
                ],
                style={"width": "36rem"},
                className="mt-3"
            ),
            dbc.Card([
                    dbc.Row([
                        dbc.Col([
                            dbc.CardImg(
                                src="/assets/ethereum.png",
                                top=True,
                                style={"width": "6rem"},),
                        ]),
                        dbc.Col([
                            dbc.Row([html.H5("Model Precision")]),
                            dbc.Row([dbc.Table.from_dataframe(get_roi_px.gen_table("eth"), striped=True,bordered=True, dark=True)]),
                        ])   
                    ]),

                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(id='eth_roi', figure=get_roi_px.get_crypto_roi_plot('eth_roi'),
                                          config={'displayModeBar':False})
                            ])
                        ]),
                    ]),
                ],
                style={"width": "36rem"},
                className="mt-3"
            ),
        ])
    ])

tab2_content = dbc.Card([
    dbc.CardImg(
        src="/assets/bitcoin.png",
        style={"width": "54rem"})])

# overall structure of app    
tabs = dbc.Tabs(
    [
        dbc.Tab(tab2_content, label="Home"),
        dbc.Tab(tab1_content, label="ROI vs Time"),
    ]
)

# app layout functionality
app.layout = tabs

# Lines
# Metrics

if __name__=='__main__':
    app.run_server(debug=True, port=3000)