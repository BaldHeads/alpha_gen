import os
import csv
import time
import pandas as pd
from dotenv import load_dotenv
import sqlite3
import libs.db as db
import alpaca_trade_api as tradeapi
import sys
import libs.db


load_dotenv()
alpaca_api_key = os.getenv("ALPACA_API_KEY")
alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")

alpaca = tradeapi.REST(
    alpaca_api_key,
    alpaca_secret_key,
    api_version="v2")

#Get tickers
tickers=db.get_tickers("data/sp10.csv")

db_file = "sp10_historical.db"
conn = db.create_connection(db_file)

#create default table in the db
db.create_initial_db(conn)

# Grab data from Jan 1 2017 to June 25, 2021 by month and by ticker
# Loop will break after June 2021 and commit to database
# There is a time.sleep(5) after each API call to stay below API limits

db.populate_initial_db(conn, alpaca, tickers)

db.close_connection(conn)