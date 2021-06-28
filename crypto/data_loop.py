import os
import ccxt
import asyncio
import numpy as np
import pandas as pd
from dotenv import load_dotenv

def initialize(cash=None):
    """Initialize the db, data storage, and account balances."""
    print("Initializing Account and DataFrame")

    # @TODO: Update to build the db
    # Initialize Account
    account = {"balance": cash, "shares": 0}

    # Initialize DataFrame
    # @TODO: We will update this later!
    df = fetch_data()

    # Initialize the db
    build_db(df)

    # @TODO: We will complete the rest of this later!
    return account, df

def build_db(df):
    """Build the db."""

    # @TODO: Build the Initial db, may want to put this in a separate file!
    print("Initializing db")
    # db = df.db(title="Current BTC/USD Price")

    return

def update_db(df):
    """Update the db."""
    # db = df.db(title="Current BTC/USD Price")

    return

def fetch_data():
    """Fetches the latest prices."""
    print("Fetching data...")
    load_dotenv()
    kraken_public_key = os.getenv("KRAKEN_KEY")
    kraken_secret_key = os.getenv("KRAKEN_SECRET")
    kraken = ccxt.kraken({"apiKey": kraken_public_key, "secret": kraken_secret_key})

    close = kraken.fetch_ticker("BTC/USD")["close"]
    datetime = kraken.fetch_ticker("BTC/USD")["datetime"]
    df = pd.DataFrame({"close": [close]})
    df.index = pd.to_datetime([datetime])

    return df

# Initial/update config for asyncio
account, df = initialize(200)

async def main():
    loop = asyncio.get_event_loop()

    while True:
        global account
        global df

        # Fetch new prices data
        new_df = await loop.run_in_executor(None, fetch_data)
        df = df.append(new_df, ignore_index=True)

        await asyncio.sleep(1)


# Python 3.7+
loop = asyncio.get_event_loop()
loop.run_until_complete(main())