import os
import csv
import pandas as pd
from dotenv import load_dotenv
import sqlite3
import libs.db as db


load_dotenv()
alpaca_api_key = os.getenv("ALPACA_API_KEY")
alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")

alpaca = tradeapi.REST(
    alpaca_api_key,
    alpaca_secret_key,
    api_version="v2")

#Get tickers
tickers=[]
with open("sp10.csv",'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    print(header)
    for row in csvreader:
        tickers.append(row[2])

db_file = "sp10_not_normalized.db"
conn = db.create_connection(db_file)
sql_insert = "INSERT INTO historical(symbol, timestamp, close) VALUES(?,?,?)"
cur = conn.cursor()

# Grab data from Jan 1 2017 to June 25, 2021 by month and by ticker
# Loop will break after June 2021 and commit to database
# There is a time.sleep(5) after each API call to stay below API limits

for year in range(2017,2021+1):
    for month in range(1,12+1):
        if year == 2021 and month > 6:
            break
        temp_tz = pd.Timestamp(year=year, month=month, day=1)
        start = pd.Timestamp(f"{year}-{month}-{1}", tz="America/New_York").isoformat()
        if year == 2021 and month == 6:
            end = pd.Timestamp(f"{year}-{month}-{25}", tz="America/New_York").isoformat()
        else:
            end = pd.Timestamp(f"{year}-{month}-{temp_tz.daysinmonth}", tz="America/New_York").isoformat()
        print(start, end)

        for ticker in tickers:
            df = alpaca.get_bars(ticker, tradeapi.rest.TimeFrame.Hour, start=start, end=end, limit=1000).df
            time.sleep(5)
            for i in range(0,len(df)):
                cur.execute(sql_insert, (ticker, df.index[i].isoformat() , df.iloc[i]["close"]))

db.close_connection(conn)