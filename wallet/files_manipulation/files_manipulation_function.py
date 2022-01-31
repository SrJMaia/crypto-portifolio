import pandas as pd

def save_wallet_to_csv(wallet):
    pd.DataFrame(wallet).to_csv("/home/someone/Documents/project/csv_files/files/full-wallet.csv")


def save_wallet_information_to_csv(wallet_information):
    pd.DataFrame(wallet_information).to_csv("/home/someone/Documents/project/csv_files/files/full-wallet-information.csv")


def read_last_index_csv():
    with open('/home/someone/Documents/project/csv_files/files/last-index.txt', "r") as f:
        return int(f.read())


def write_last_index_csv(index):
    with open('/home/someone/Documents/project/csv_files/files/last-index.txt', 'w') as f:
        f.write(str(index))


def read_wallet():
    """
    Read wallet csv file
    """
    wallet = pd.read_csv("/home/someone/Documents/project/csv_files/files/full-wallet.csv").rename(columns={"Unnamed: 0":""}).set_index("").to_dict()
    return wallet


def read_wallet_informations():
    wallet_information = pd.read_csv("/home/someone/Documents/project/csv_files/files/full-wallet-information.csv").rename(columns={"Unnamed: 0":""}).set_index("").to_dict()
    return wallet_information