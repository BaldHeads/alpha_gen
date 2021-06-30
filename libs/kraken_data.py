from libs.kraken_conn import kraken
import pandas as pd

def get_price(pair="BTC/USD"):
        
        response = kraken.fetch_ticker(pair)
        return pd.DataFrame({
            "datetime":[response["datetime"]],
            "close":[response["close"]]
            })

# fetchTrades (symbol[, since[, [limit, [params]]]])
def get_historical(pair="BTC/USD"):
    df = pd.DataFrame(kraken.fetch_OHLCV('BTC/USD', "1h"))
    return df[["datetime", "price"]].set_index("datetime").rename(columns={"price":"close"})