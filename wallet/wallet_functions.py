import wallet.files_manipulation.files_manipulation_function as fmf
from miscellaneous_functions.prints_functions import clear_prints
from data_extraction.binance_api import binance_data as bnbdata
from csv_files.functions.transactions import read_transactions
from data_extraction.web_scrapping import cmc_data as cmc
import wallet.wallet_variables as wv
from tqdm import tqdm

def get_wallets():
    try:
        df = read_transactions()
    except:
        print("\nTransactions is empty, please add a transaction.\n")
        return 0, 0

    wallet = {}
    wallet_information = {}
    wallet_information["resume"] = wv.RESUME.copy()

    last_index = fmf.read_last_index_csv()

    if last_index == df.index[-1]:
        wallet_information = read_wallet_information()
        wallet = fmf.read_wallet()
        wallet = convert_wallet_to_float(wallet)
        wallet, wallet_information = update_wallets_data(wallet, wallet_information)
        fmf.save_wallet_to_csv(wallet)
        fmf.save_wallet_information_to_csv(wallet_information)
        return wallet, wallet_information

    wallet, wallet_information = loop_in_transactions(df.iloc[last_index:,:], wallet, wallet_information)

    fmf.write_last_index_csv(df.index[-1])

    wallet = convert_wallet_to_float(wallet)

    wallet = mirror_ammount_bought_now_ifnull(wallet)

    wallet = adjust_interest(wallet)

    fmf.save_wallet_to_csv(wallet)
    fmf.save_wallet_information_to_csv(wallet_information)

    return wallet, wallet_information


def adjust_interest(wallet):
    for i in wallet.keys():
        wallet[i]["interest_earned"] = wallet[i]["ammount_now"] - wallet[i]["ammount_bought"]
        wallet[i]["growth_interest"] = wallet[i]["ammount_now"] / wallet[i]["ammount_bought"] - 1
    return wallet


def mirror_ammount_bought_now_ifnull(wallet):
    """
    If wallet.csv is empty, ammount now receives ammount bought
    """
    for i in wallet.keys():
        if wallet[i]["ammount_now"] == 0:
            wallet[i]["ammount_now"] = wallet[i]["ammount_bought"]
    return wallet


def next_goal(number):
    """
    Calculate next goal in K
    """
    rounded_number = round(number, -3)

    if number > rounded_number:
        return rounded_number + 1000
    return rounded_number


def read_wallet_information():
    """
    Read wallet information and delet unnecessary keys
    """
    read_wallet_info = fmf.read_wallet_informations()
    
    wallet_information = {}
    wallet_information["resume"] = wv.STABLE.copy()
    wallet_information["deposit"] = wv.FIAT.copy()
    wallet_information["USDT"] = wv.STABLE.copy()
    wallet_information["USDC"] = wv.STABLE.copy()

    wallet_information["resume"]["invested"] = float(read_wallet_info["resume"]["invested"])
    wallet_information["resume"]["today_investment"] = float(read_wallet_info["resume"]["today_investment"])
    wallet_information["resume"]["gain"] = float(read_wallet_info["resume"]["gain"])
    wallet_information["resume"]["growth"] = float(read_wallet_info["resume"]["growth"])
    wallet_information["resume"]["pairs_ammount"] = float(read_wallet_info["resume"]["pairs_ammount"])
    wallet_information["resume"]["next_goal"] = float(read_wallet_info["resume"]["next_goal"])
    
    wallet_information["deposit"]["eur"] = float(read_wallet_info["deposit"]["eur"])
    wallet_information["deposit"]["stasis-euro"] = float(read_wallet_info["deposit"]["stasis-euro"])

    wallet_information["USDT"]["invested"] = float(read_wallet_info["USDT"]["invested"])
    wallet_information["USDT"]["ammount_now"] = float(read_wallet_info["USDT"]["ammount_now"])
    wallet_information["USDT"]["interest_earned"] = float(read_wallet_info["USDT"]["interest_earned"])
    wallet_information["USDT"]["actual_allocation"] = float(read_wallet_info["USDT"]["actual_allocation"])
    wallet_information["USDT"]["default_allocation"] = float(read_wallet_info["USDT"]["default_allocation"])
    wallet_information["USDT"]["next_deposit"] = float(read_wallet_info["USDT"]["next_deposit"])
    wallet_information["USDT"]["previous_deposit"] = float(read_wallet_info["USDT"]["previous_deposit"])
    wallet_information["USDT"]["deposit_impact"] = float(read_wallet_info["USDT"]["deposit_impact"])

    wallet_information["USDC"]["invested"] = float(read_wallet_info["USDC"]["invested"])
    wallet_information["USDC"]["ammount_now"] = float(read_wallet_info["USDC"]["ammount_now"])
    wallet_information["USDC"]["interest_earned"] = float(read_wallet_info["USDC"]["interest_earned"])
    wallet_information["USDC"]["actual_allocation"] = float(read_wallet_info["USDC"]["actual_allocation"])
    wallet_information["USDC"]["default_allocation"] = float(read_wallet_info["USDC"]["default_allocation"])
    wallet_information["USDC"]["next_deposit"] = float(read_wallet_info["USDC"]["next_deposit"])
    wallet_information["USDC"]["previous_deposit"] = float(read_wallet_info["USDC"]["previous_deposit"])
    wallet_information["USDC"]["deposit_impact"] = float(read_wallet_info["USDC"]["deposit_impact"])

    return wallet_information


def loop_in_transactions(df, wallet, wallet_information):
    """
    Read transactions to creat or update wallet and wallet informaiton
    """
    for i in df.to_numpy():
        if i[wv.ACTION_TYPE] == "buy":
            if not i[wv.SECONDARY] in wallet.keys():
                # If the coin isn't in wallet, it will be added
                wallet[i[wv.SECONDARY]] = wv.COIN.copy()
                wallet[i[wv.SECONDARY]]["default_allocation"] = wv.ALLOCATION[i[wv.SECONDARY]]
            wallet[i[wv.SECONDARY]]["invested"] += i[wv.AMMOUNT_IN_USD]
            wallet[i[wv.SECONDARY]]["ammount_bought"] += i[wv.SEC_AMMOUNT]
            wallet[i[wv.SECONDARY]]["bought_prices_times"] += 1
            wallet[i[wv.SECONDARY]]["bought_prices_sum"] += i[wv.PRICE_IN_USD]
        elif i[wv.ACTION_TYPE] == "sell":
            wallet[i[wv.PRIMARY]]["invested"] -= i[wv.AMMOUNT_IN_USD]
            wallet[i[wv.PRIMARY]]["ammount_bought"] -= i[wv.PRI_AMMOUNT]
            wallet[i[wv.PRIMARY]]["bought_prices_times"] -= 1
            wallet[i[wv.PRIMARY]]["bought_prices_sum"] -= i[wv.AMMOUNT_IN_USD]
        elif i[wv.ACTION_TYPE] in ["dry-in", "fix-income-in", "deposit"]:
            if i[wv.ACTION_TYPE] == "deposit":
                if not i[wv.ACTION_TYPE] in wallet_information.keys():
                    wallet_information[i[wv.ACTION_TYPE]] = wv.FIAT.copy()
                if i[wv.PRIMARY] == "eur":
                    wallet_information[i[wv.ACTION_TYPE]]["eur"] += i[wv.PRI_AMMOUNT]
            else:
                if not i[wv.PRIMARY] in wallet_information.keys():
                    wallet_information[i[wv.PRIMARY]] = wv.STABLE.copy()
                    wallet_information[i[wv.PRIMARY]]["default_allocation"] = wv.ALLOCATION[i[wv.PRIMARY]]
                wallet_information[i[wv.PRIMARY]]["invested"] += i[wv.PRI_AMMOUNT]
        elif i[wv.ACTION_TYPE] in ["withdraw", "dry-out", "fix-income-out"]:
            if i[wv.ACTION_TYPE] == "withdraw":
                wallet_information[i[wv.PRIMARY]]["eur"] -= i[wv.PRI_AMMOUNT]
                continue
            wallet_information[i[wv.PRIMARY]]["invested"] -= i[wv.PRI_AMMOUNT]

    wallet, wallet_information = update_wallets_data(wallet, wallet_information)

    return wallet, wallet_information

import time

def update_wallets_data(wallet, wallet_information):
    """
    Update wallet informations
    """
    wallet_information["deposit"]["stasis-euro"] = cmc.get_eur_price()
    wallet_information["resume"]["invested"] = 0
    wallet_information["resume"]["today_investment"] = 0
    pbar = tqdm(total=len(wallet.keys()))
    for i in wallet.keys():
        pbar.update(1)
        price, name = bnbdata.get_last_price_available(i)
        wallet[i]["price_today"] = price
        wallet[i]["pair_name"] = name
        wallet[i]["investment_now"] = price * wallet[i]["ammount_bought"]
        wallet[i]["gain_fiat"] = wallet[i]["investment_now"] - wallet[i]["invested"]
        wallet[i]["growth_fiat"] = wallet[i]["gain_fiat"] / wallet[i]["invested"]

        wallet_information["resume"]["invested"] += wallet[i]["invested"]
        wallet_information["resume"]["today_investment"] += wallet[i]["investment_now"]

    pbar.close()

    wallet_information["resume"]["next_goal"] = next_goal(wallet_information["resume"]["today_investment"])

    for i in wallet.keys():
        wallet[i]["actual_allocation"] = wallet[i]["investment_now"] / wallet_information["resume"]["today_investment"]
        wallet[i]["next_deposit"] = wallet[i]["default_allocation"] * wallet_information["resume"]["next_goal"] - wallet[i]["investment_now"]
        wallet[i]["previous_deposit"] = wallet[i]["default_allocation"] * (wallet_information["resume"]["next_goal"]-1000) - wallet[i]["investment_now"]
        wallet[i]["deposit_impact"] = wallet[i]["next_deposit"] / wallet_information["resume"]["next_goal"]

    wallet_information["resume"]["pairs_ammount"] = len(wallet.keys())
    wallet_information["resume"]["gain"] = wallet_information["resume"]["today_investment"] - wallet_information["resume"]["invested"]
    wallet_information["resume"]["growth"] = wallet_information["resume"]["gain"] / wallet_information["resume"]["invested"]

    return wallet, wallet_information


def convert_wallet_to_float(wallet):
    """
    Convert strings numbers to float
    """
    for i in wallet.keys():
        for j in wallet[i]:
            try:
                wallet[i][j] = float(wallet[i][j])
            except:
                continue
    return wallet