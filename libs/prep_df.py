import pandas as pd
import numpy as np

def normalize_df(df):
    """ The original database is not normalized. This function will convert a raw dataframe and normalize it using the pivot function.
        It will also provide some fixups:
            (1) convert the timestamp index to datetime because Sqlite only store dates as strings
            (2) sort on the timestamp index to make sure all values are in order
            (2) replaces NaN with constant values from the row above
    :param db_file: database file
    :return: Connection object or None
    """

    df = df.pivot(index="timestamp", columns="symbol", values="close")
    df.index = pd.to_datetime(df.index)
    df.sort_index(inplace=True)
    df.fillna(method='ffill', inplace=True)
    
    return df