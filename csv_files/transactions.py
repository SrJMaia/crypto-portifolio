import pandas as pd

def read_transactions():
    """
    Read transaction csv file and formating dtype
    """
    df = pd.read_csv("/home/someone/Documents/project/csv_files/transactions.csv")
    df.loc[:,"date"] = pd.to_datetime(df.loc[:, "date"])
    df.loc[:, "type"] = df.loc[:, "type"].astype("string")
    df.loc[:, "primary"] = df.loc[:, "primary"].astype("string")
    df.loc[:, "pri-ammount"] = df.loc[:, "pri-ammount"].astype("float64")
    df.loc[:, "primary"] = df.loc[:, "primary"].astype("string")
    df.loc[:, "fee"] = df.loc[:, "fee"].astype("float64")
    df.loc[:, "fee-coin"] = df.loc[:, "fee-coin"].astype("string")
    # df.loc[:, "fee-coin"].fillna("none", inplace=True)
    df.loc[:, "secondary"] = df.loc[:, "secondary"].astype("string")
    # df.loc[:, "secondary"].fillna("none", inplace=True)
    df.loc[:, "sec-ammount"] = df.loc[:, "sec-ammount"].astype("float64")
    df.loc[:, "sec-coin-price"] = df.loc[:, "sec-coin-price"].astype("float64")
    df.loc[:, "price-in-usd"] = df.loc[:, "price-in-usd"].astype("float64")
    df.loc[:, "ammount-in-usd"] = df.loc[:, "ammount-in-usd"].astype("float64")
    return df

def save_transactions(df):
    """
    Save transactions csv file
    """
    df.to_csv("/home/someone/Documents/project/csv_files/transactions.csv", index=False)