from datetime import datetime
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


def read_if_program_started():
    with open('/home/someone/Documents/project/csv_files/files/start-program-flag.txt', "r") as f:
        return int(f.read())


def write_if_program_started(mode):
    with open('/home/someone/Documents/project/csv_files/files/start-program-flag.txt', 'w') as f:
        f.write(str(mode))


def read_wallet():
    """
    Read wallet csv file
    """
    wallet = pd.read_csv("/home/someone/Documents/project/csv_files/files/full-wallet.csv").rename(columns={"Unnamed: 0":""}).set_index("").to_dict()
    return wallet


def read_wallet_informations():
    wallet_information = pd.read_csv("/home/someone/Documents/project/csv_files/files/full-wallet-information.csv").rename(columns={"Unnamed: 0":""}).set_index("").to_dict()
    return wallet_information


def save_time_now_and_wait_time_to_file(wait_time=10):
    now = datetime.now()
    string_to_save = now.strftime("%Y_%m_%d-%I:%M:%S_%p")
    string_to_save += f",{wait_time}"
    with open('/home/someone/Documents/project/csv_files/files/last-hour.txt', 'w') as f: # Mudar
        f.write(string_to_save)


def save_only_wait_time_to_file(wait_time):
    saved_date, _ = get_time_and_wait_time_from_file()
    string_to_save = saved_date.strftime("%Y_%m_%d-%I:%M:%S_%p")
    string_to_save += f",{wait_time}"
    with open('/home/someone/Documents/project/csv_files/files/last-hour.txt', 'w') as f: # Mudar
        f.write(string_to_save)


def save_only_time_now_to_file():
    now = datetime.now()
    date_string = now.strftime("%Y_%m_%d-%I:%M:%S_%p")
    _, saved_wait_time = get_time_and_wait_time_from_file()
    string_to_save = f"{date_string},{saved_wait_time}"
    with open('/home/someone/Documents/project/csv_files/files/last-hour.txt', 'w') as f: # Mudar
        f.write(string_to_save)

    
def get_time_and_wait_time_from_file():
    with open('/home/someone/Documents/project/csv_files/files/last-hour.txt', "r") as f:
        read_data_file = f.read().split(",")
        read_date = datetime.strptime(read_data_file[0], "%Y_%m_%d-%I:%M:%S_%p")
        read_wait_time = int(read_data_file[1])
        return read_date, read_wait_time