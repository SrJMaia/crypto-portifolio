from prettytable import PrettyTable
from menu.menu_function import get_menu_action
import menu.main_menu_functions as mmf
import menu.menu_variables as mv
from wallet.wallet_functions import get_wallets, save_wallet_to_csv, adjust_interest
from pretty_table.pretty_table_functions import print_wallet
from miscellaneous_functions.prints_functions import clear_prints

def temporary_function(action):
    """
    Futuramente remover isso e manter apenas get_menu_action do comentario
    """
    while True:

        if action in [mv.SHOW_WALLET, mv.PREVIOUS_MENU, mv.CHANGE_AMMOUNT_NOW]:
            return action
        
        print("\nUnder construction...")

        action = get_menu_action("wallet")


def wallet_menu():

    wallet_menu_body()

    action = get_menu_action("wallet")

    # Futuramente remover junto com temporary_function
    action = temporary_function(action)

    wallet, wallet_information = get_wallets()

    if wallet == 0:
        wallet_menu()

    if action == mv.PREVIOUS_MENU:
        mmf.menu()
        return
    elif action == mv.SHOW_WALLET:
        clear_prints()
        print_wallet(wallet)
    elif action == mv.CHANGE_AMMOUNT_NOW:
        clear_prints()
        cryptos_list = wallet_change_ammount_now_body(wallet)
        crypto_name = get_crypto_selection(cryptos_list)
        new_ammount_now = get_crytpo_ammount(crypto_name)
        wallet[crypto_name]["ammount_now"] = new_ammount_now
        wallet = adjust_interest(wallet)
        save_wallet_to_csv(wallet)
        clear_prints()
        # pedir uma ação e etnão fazer outra
    
    wallet_menu()


def wallet_change_ammount_now_body(wallet):
    pt = PrettyTable()
    cryptos_list = list(wallet.keys())
    pt.add_column("Cryptos", cryptos_list)
    pt.title = "Change Ammount Now"
    pt.add_column("Input", [i+1 for i, v in enumerate(list(wallet.keys()))])
    pt.align = "l"
    pt.hrules = 1
    print(pt)
    return cryptos_list


def wallet_menu_body():
    pt_menu = PrettyTable()
    pt_menu.field_names = ["Action", "Input"]
    pt_menu.title = "Wallet"
    pt_menu.add_row(["Show Wallet", mv.SHOW_WALLET])
    pt_menu.add_row(["Change Ammount Now", mv.CHANGE_AMMOUNT_NOW])
    # y.add_row(["Darwin", 112])
    # y.add_row(["Hobart", 1357])
    # y.add_row(["Sydney", 2058])
    # y.add_row(["Melbourne", 1566])
    pt_menu.add_row(["Previous Menu", mv.PREVIOUS_MENU])

    pt_menu.hrules = 1

    print(pt_menu)


def get_crytpo_ammount(crypto_name):
    while True:

        input_action = input("\nUpdate {crypto_name} ammount now: : ")

        if not input_action.isnumeric():
            print("\nThe input isn't a number.")
            continue
        
        input_action = float(input_action)

        input_action = round(input_action, 6)

        return input_action


def get_crypto_selection(cryptos):
    while True:

        input_action = input("\nEnter the input relateded to a crypto: ")

        if not input_action.isnumeric():
            print("\nThe input isn't a number or an integer.")
            continue

        input_action = int(input_action) - 1

        if input_action not in range(len(cryptos)):
            print("\nThe input is out of range.")
            continue

        return cryptos[input_action]