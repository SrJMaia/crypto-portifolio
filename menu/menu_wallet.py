from wallet.files_manipulation.files_manipulation_function import save_wallet_to_csv
import pretty_table.pretty_table_wallet.pt_wallet_functions as ptwf
from miscellaneous_functions.prints_functions import clear_prints
from wallet.wallet_functions import get_wallets, adjust_interest
from menu.shared_functions import get_menu_action
import menu.menu_variables as mv
import menu.menu_main as mmf

def wallet_menu():

    ptwf.wallet_menu_body()

    action = get_menu_action("wallet")

    clear_prints()

    if action != 0:
        wallet, wallet_information = get_wallets()

        if wallet == 0:
            wallet_menu()

    if action == mv.PREVIOUS_MENU:
        mmf.menu()
        return
    elif action == mv.SHOW_WALLET:
        clear_prints()
        ptwf.print_wallet(wallet)
    elif action == mv.CHANGE_ANY_AMMOUNT:
        clear_prints()
        change_any_ammount(wallet)
        clear_prints()
    
    wallet_menu()


""" CHANGE ANY AMMOUNT """

def change_any_ammount(wallet):
    # Get crypto name for wallet key
    crypto_name_option = get_crypto_key(wallet)
    clear_prints()
    # Get key from wallet[crypto_name]
    crypto_value_option = get_value_key(wallet, crypto_name_option)
    # Get ammount and normalize
    new_ammount_now = get_ammount(crypto_name_option, crypto_value_option)
    # Change value
    wallet[crypto_name_option][crypto_value_option] = new_ammount_now

    save_wallet_to_csv(wallet)


def get_value_key(wallet, crypto_name):
    crypto_data = ptwf.wallet_change_any_value_values_body(wallet, crypto_name)
    while True:

        input_action = input("\nEnter the input relateded to a crypto: ")

        if not input_action.isnumeric():
            print("\nThe input isn't a number or an integer.")
            continue

        input_action = int(input_action) - 1

        if input_action not in range(len(crypto_data)):
            print("\nThe input is out of range.")
            continue

        return crypto_data[input_action]


def get_ammount(crypto_name, crypto_value_field):
    while True:

        input_action = input(f"\nUpdate {crypto_name} - {crypto_value_field}: ")

        if not input_action.isnumeric():
            print("\nThe input isn't a number.")
            continue
        
        input_action = float(input_action)

        if crypto_value_field in mv.ROUND_TO_FOUR:
            return round(input_action, 4)
        elif crypto_value_field in mv.ROUND_TO_SIX:
            return round(input_action, 6)
        return round(input_action, 2)


def get_crypto_key(wallet):
    cryptos_list = ptwf.wallet_change_any_value_cryptos_body(wallet)
    while True:

        input_action = input("\nEnter the input relateded to a crypto: ")

        if not input_action.isnumeric():
            print("\nThe input isn't a number or an integer.")
            continue

        input_action = int(input_action) - 1

        if input_action not in range(len(cryptos_list)):
            print("\nThe input is out of range.")
            continue

        return cryptos_list[input_action]