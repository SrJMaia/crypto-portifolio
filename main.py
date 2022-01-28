import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from wallet.wallet_functions import read_transactions_to_wallet
from prettytable import PrettyTable

wallet, wallet_information = read_transactions_to_wallet()

dt = pd.DataFrame(data=wallet)
dt.loc["interest_earned",:] = dt.loc["ammount_bought",:] - dt.loc["ammount_now",:]
dt.loc["growth_interest",:] = dt.loc["ammount_now",:] / dt.loc["ammount_bought",:] - 1
dt.loc["average_price",:] = dt.loc["bought_prices_sum",:] / dt.loc["bought_prices_times",:]
dt.drop("bought_prices_sum",inplace=True)
dt.drop("bought_prices_times",inplace=True)
dt.drop("pair_name",inplace=True)
dt.index = dt.index.str.replace("_"," ")
dt.index = dt.index.str.title()

INVESTED = 0
AMMOUNT_BOUGHT = 1
AMMOUNT_NOW = 2
INTEREST_EARNED = 3
GROWTH_INTEREST = 4
PRICE_TODAY = 5
INVESTMENT_NOW = 6
GAIN_FIAT = 7
GROWTH_FIAT = 8
ACTUAL_ALLOCATION = 9
DEFAULT_ALLOCATION = 10
NEXT_DEPOSIT = 11
PREVIOUS_DEPOSIT = 12
DEPOSIT_IMPPACT = 13
AVERAGE_PRICE = 14 
data_ls = [
    [
        "Infos",
        dt.index.to_list()
    ]
]
index_flag = True
for i in wallet.keys():
    temporary_list = []
    temporary_list.append(i.replace("-"," ").title())
    temporary_list.append([])
    index_to_loop = 0
    for j in wallet[i].values():
        if index_to_loop in [INVESTED, INVESTMENT_NOW, GAIN_FIAT, NEXT_DEPOSIT, PREVIOUS_DEPOSIT, AVERAGE_PRICE]:
            temporary_list[1].append(round(j,2))
        elif index_to_loop == PRICE_TODAY:
            temporary_list[1].append(round(j,4))
        elif index_to_loop in [AMMOUNT_BOUGHT, AMMOUNT_NOW, INTEREST_EARNED]:
            temporary_list[1].append(round(j,6))
        elif index_to_loop in [GROWTH_INTEREST, GROWTH_FIAT, ACTUAL_ALLOCATION, DEFAULT_ALLOCATION, DEPOSIT_IMPPACT]:
            temporary_list[1].append(round(j*100,2))
        index_to_loop += 1
        
    data_ls.append(temporary_list)

x = PrettyTable()
for i in data_ls:
    x.add_column(i[0],i[1])
print(x)

"""
columsDf = ["Type", 
            "Name", 
            "Invested", 
            "Bought", 
            "Now", 
            "Gain-Interest", 
            "Growth-Interest", 
            "Price-Today",
            "Total-Today",
            "Gain-Fiat",
            "Growth-Fiat",
            "Today-Allocation",
            "Default-Allocation",
            "Next-Deposit",
            "Previous-Deposit",
            "Deposit-Impact"]
x = pd.DataFrame(columns=columsDf, index=range(31))
x

y = pd.DataFrame(columns=["Investment-Type"], index=range(11))
y.loc[:, "Investment-Type"] = "none"
y, y.dtypes

y.to_csv("/home/someone/Documents/project/csv-files/investment-type.csv", index=False)

a = pd.read_csv("/home/someone/Documents/project/csv-files/investment-type.csv")
a.loc[:, "Investment-Type"] = a.loc[:, "Investment-Type"].astype("string")
# converter para string
a, a.dtypes

print("Select investment type.")
for i, v in enumerate(a.loc[:, "Investment-Type"].to_numpy()):
    print(f"{i} = {v}", end=" ")
input("Select one option: ")

Selecionar o csv especifico para transações
csv para despesas
csv para reserva e casa/projetos?

em vez de webscrapping para pegar o ultimo valor
usar binance apy

* Futuramente diminuir o tempo de pegar os dados com binance e scrapping?

3 - adicionar modificação do now com a quantidade de moedas
4 - adicionar aportes com impacto e distribuição do aporte
5 - adicionar adição de transação
5.1 - adicionar o dry-in e fix-income-in
5.2 - em change DayOrMonth adicionar a mudança do ano
6 - usar google trends para nalise
https://lazarinastoy.com/the-ultimate-guide-to-pytrends-google-trends-api-with-python/
https://alternative.me/crypto/trends/
            # https://www.youtube.com/watch?v=i1Wn3mWrLME


fazer uma correlção do preço do bitcoin com ofear greed index
futuramente achar uma forma de mudar a alocação, sem definir uma constante

"""