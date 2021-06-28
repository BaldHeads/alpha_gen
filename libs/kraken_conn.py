import ccxt
import os

kraken = ccxt.kraken({
    "apiKey": os.getenv("kraken_public"), 
    "secret": os.getenv("kraken_secret")
})