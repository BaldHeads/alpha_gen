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
tickers=[]
with open("data\sp10.csv",'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        tickers.append(row[2])

db_file = "sp10_current.db"
conn = db.create_connection(db_file)
sql_insert = "INSERT INTO historical(symbol, timestamp, close) VALUES(?,?,?)"
cur = conn.cursor()

#create default table in the db
db.create_initial_db(conn)

# Grab data for June 2021
start = pd.Timestamp(f"2021-06-01", tz="America/New_York").isoformat()
end = pd.Timestamp(f"2021-07-01", tz="America/New_York").isoformat()

for ticker in tickers:
    print(ticker)
    df = alpaca.get_bars(ticker, tradeapi.rest.TimeFrame.Hour, start=start, end=end, limit=1000).df
    time.sleep(5)
    for i in range(0,len(df)):
        cur.execute(sql_insert, (ticker, df.index[i].isoformat() , df.iloc[i]["close"]))

db.close_connection(conn)