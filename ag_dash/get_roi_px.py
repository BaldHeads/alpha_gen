import pandas as pd
import plotly.express as px

def get_roi_plot(id):
    symbol = id.split("_")[0].upper()
    combined_df = pd.read_csv("combined_roi.csv",parse_dates=True, index_col="timestamp")
    combined_df.index = pd.to_datetime(combined_df.index)
    symbol_df = combined_df[[f"LIN_{symbol}",f"GRAD_{symbol}",f"IMB_{symbol}",f"XGB_{symbol}"]]
    #fig = px.line(symbol_df, x="timestamp", y = [f"LIN_{symbol}",f"GRAD_{symbol}",f"IMB_{symbol}",f"XGB_{symbol}"])
    fig = px.line(symbol_df)
    
    return fig

# reqs to make precision tables by model
ag_model_prec = pd.read_csv("ag_model_prec.csv",index_col="model")

transposed = ag_model_prec.T
transposed.reset_index(inplace=True)

# function to generate tables
def gen_table(ticker):
    df_prec = pd.DataFrame()
    df_prec["model"] = transposed["index"]
    df_prec["prec"] = transposed[ticker]
    df_prec_new = pd.pivot_table(df_prec,values="prec",columns="model")
    return df_prec_new

def get_crypto_roi_plot(id):
    symbol = id.split("_")[0].upper()
    combined_df = pd.read_csv("crypto_combined_roi.csv",parse_dates=True, index_col="timestamp")
    combined_df.index = pd.to_datetime(combined_df.index)
    symbol_df = combined_df[[f"LIN_{symbol}",f"GRAD_{symbol}",f"IMB_{symbol}",f"XGB_{symbol}"]]
    #fig = px.line(symbol_df, x="timestamp", y = [f"LIN_{symbol}",f"GRAD_{symbol}",f"IMB_{symbol}",f"XGB_{symbol}"])
    fig = px.line(symbol_df)
    
    return fig

