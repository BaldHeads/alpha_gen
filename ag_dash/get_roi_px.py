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

