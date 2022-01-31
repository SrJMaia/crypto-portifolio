from prettytable import PrettyTable
from colorama import Fore
import pandas as pd
import pretty_table.pretty_table_variables as ptv


def print_wallet(wallet):

    data = pretty_table_data(wallet)

    body = PrettyTable()
    for i in data:
        body.add_column(i[0],i[1])
    body.align = "l"
    body.hrules = 1
    
    print(body)


def prepare_data_to_print(wallet):
    dt = pd.DataFrame(data=wallet)
    dt.loc["average_price",:] = dt.loc["bought_prices_sum",:] / dt.loc["bought_prices_times",:]
    dt.drop("bought_prices_sum",inplace=True)
    dt.drop("bought_prices_times",inplace=True)
    dt.drop("pair_name",inplace=True)
    dt.index = dt.index.str.replace("_"," ")
    dt.index = dt.index.str.title()
    return dt


def pretty_table_data(wallet):

    dt = prepare_data_to_print(wallet)

    data_ls = [
        [
            f"{Fore.LIGHTCYAN_EX}INFOS{Fore.RESET}",
            dt.index.to_list()
        ]
    ]
    
    wallet = dt.to_dict()
    for coin_name in wallet.keys():
        temporary_list = []
        temporary_list.append(f"{Fore.LIGHTCYAN_EX}{coin_name}{Fore.RESET}")
        temporary_list.append([])
        for index, value in enumerate(wallet[coin_name].values()):
            if index in [ptv.INVESTED, ptv.INVESTMENT_NOW, ptv.GAIN_FIAT, ptv.NEXT_DEPOSIT, ptv.PREVIOUS_DEPOSIT, ptv.AVERAGE_PRICE]:
                if index in [ptv.GAIN_FIAT,ptv.NEXT_DEPOSIT,ptv.PREVIOUS_DEPOSIT]:
                    if value > 0:
                        temporary_list[1].append(f"{Fore.LIGHTGREEN_EX}$ {round(value,2)}{Fore.RESET}")
                    elif value < 0:
                        temporary_list[1].append(f"{Fore.LIGHTRED_EX}$ {round(value,2)}{Fore.RESET}")
                    else:
                        temporary_list[1].append(f"$ {round(value,2)}")
                else:
                    temporary_list[1].append(f"$ {round(value,2)}")
            elif index == ptv.PRICE_TODAY:
                temporary_list[1].append(f"$ {round(value,4)}")
            elif index in [ptv.AMMOUNT_BOUGHT, ptv.AMMOUNT_NOW, ptv.INTEREST_EARNED]:
                if index == ptv.INTEREST_EARNED:
                    if value < 0:
                        temporary_list[1].append(f"{Fore.LIGHTRED_EX}{round(value*100,6)}{Fore.RESET}")
                        continue
                    elif value > 0:
                        temporary_list[1].append(f"{Fore.LIGHTGREEN_EX}{round(value*100,6)}{Fore.RESET}")
                        continue
                temporary_list[1].append(round(value,6))
            elif index in [ptv.GROWTH_INTEREST, ptv.GROWTH_FIAT, ptv.ACTUAL_ALLOCATION, ptv.DEFAULT_ALLOCATION, ptv.DEPOSIT_IMPPACT]:
                if index == ptv.DEFAULT_ALLOCATION:
                    if wallet[coin_name]["Actual Allocation"] < value:
                        temporary_list[1][-1] = f"{Fore.LIGHTRED_EX}{round(wallet[coin_name]['Actual Allocation']*100,2)} %{Fore.RESET}"
                    elif wallet[coin_name]["Actual Allocation"] > value:
                        temporary_list[1][-1] = f"{Fore.LIGHTGREEN_EX}{round(wallet[coin_name]['Actual Allocation']*100,2)} %{Fore.RESET}"
                    temporary_list[1].append(f"{round(value*100,2)} %")
                elif index in [ptv.GROWTH_INTEREST, ptv.GROWTH_FIAT, ptv.DEPOSIT_IMPPACT]:
                    if value < 0:
                        temporary_list[1].append(f"{Fore.LIGHTRED_EX}{round(value*100,2)} %{Fore.RESET}")
                    elif value > 0:
                        temporary_list[1].append(f"{Fore.LIGHTGREEN_EX}{round(value*100,2)} %{Fore.RESET}")
                    else:
                        temporary_list[1].append(f"{round(value*100,2)} %")
                else:
                    temporary_list[1].append(f"{round(value*100,2)} %")
        data_ls.append(temporary_list)
    
    return data_ls