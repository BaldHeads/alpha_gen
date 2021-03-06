from os import lseek
import sqlite3
from sqlite3 import Error
import pandas as pd
import csv
import time
import alpaca_trade_api as tradeapi

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def close_connection(conn):
    """ close a database connection to the SQLite database
        specified by the conn
    :param conn: a Sqlite3 connection
    :return: None
    """
    conn.commit()
    conn.close()

def create_initial_db(conn):
    """ Create the tables into the inital database for loading alpaca data
    :param conn: a Sqlite3 connection
    :return: None
    """
    sql_create_ticker_table = """CREATE TABLE IF NOT EXISTS historical (
        id integer PRIMARY KEY,
        symbol TEXT NOT NULL,
        timestamp TEXT NOT NULL,
        close REAL NOT NULL
    );"""
    c = conn.cursor()
    c.execute(sql_create_ticker_table)
    conn.commit()

def populate_initial_db(conn, alpaca, tickers):
    """ grab data from alpaca from 2017 to June 25, 2021 by hour for each ticker in tickers
        This data is not normalized
    :param conn: a Sqlite3 connection
    :param alpaca: an initialized alpaca REST object
    :param tickers: a list of ticker symbols
    :return: None
    """
    sql_insert = "INSERT INTO historical(symbol, timestamp, close) VALUES(?,?,?)"
    cur = conn.cursor()
    for year in range(2017,2021+1):
        for month in range(1,12+1):
            if year == 2021 and month > 3:
                break

            start = pd.Timestamp(f"{year}-{month}-{1}", tz="America/New_York").isoformat()
            if month == 12:
                month = 0
                year += 1
            end = pd.Timestamp(f"{year}-{month+1}-{1}", tz="America/New_York").isoformat()
            for ticker in tickers:
                df = alpaca.get_bars(ticker, tradeapi.rest.TimeFrame.Hour, start=start, end=end, limit=1000).df
                print(ticker, end)
                time.sleep(2)
                for i in range(0,len(df)):
                    cur.execute(sql_insert, (ticker, df.index[i].isoformat() , df.iloc[i]["close"]))
    conn.commit()

def df_from_db(conn):
    """ convert the sqlite database into a pandas DataFrame
    :param conn: a Sqlite3 connection
    :return: pandas DataFrame directly from database
    """
    return pd.read_sql_query("SELECT * FROM historical", conn)

def get_tickers(ticker_file):
    """ return a list of stock tickers from the 3rd column of the provided csv
    :param ticker_file: a Sqlite3 connection
    :return tickers: a list of ticker symbols
    """

    tickers=[]
    with open(ticker_file,'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)
        for row in csvreader:
            tickers.append(row[2])
    return tickers
