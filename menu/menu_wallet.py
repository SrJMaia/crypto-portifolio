from wallet.files_manipulation.files_manipulation_function import save_wallet_to_csv
from data_extraction.binance_api.binance_data import get_last_price_available
import pretty_table.pretty_table_wallet.pt_wallet_functions as ptwf
from miscellaneous_functions.prints_functions import clear_prints
from wallet.wallet_functions import get_wallets
from menu.shared_functions import get_menu_action
import wallet.wallet_variables as wv
import menu.menu_variables as mv
import menu.menu_main as mmf

def wallet_menu():


    ptwf.wallet_menu_body()

    action = get_menu_action("wallet")

    clear_prints()

    if action != mv.PREVIOUS_MENU:
        wallet, wallet_information = get_wallets()

    clear_prints()

    if action == mv.PREVIOUS_MENU:
        mmf.menu()
    elif action == mv.SHOW_WALLET:
        clear_prints()
        ptwf.print_wallet(wallet)
    elif action == mv.CHANGE_ANY_AMMOUNT:
        change_any_ammount(wallet)    
    elif action == mv.ADD_CRYPTO:
        add_crypto(wallet)
    
    wallet_menu()


""" GENERAL """

def check_confirmation_input_y_n_wallet(input_answer, wallet):
    if input_answer not in mv.CHECK_CONFIRMATION:
        print("\nIncorrect option.")
        return False
    
    clear_prints()

    if input_answer == mv.CHECK_YES:
        return

    change_any_ammount(wallet)


""" ADD CRYPTO """

def add_crypto(wallet):
    while True:
        input_action = input("\nEnter the crypto ticker: ").upper().replace(" ","")

        price = get_last_price_available(input_action)

        if price[0] == mv.INVALID_PRICE:
            print(f"\nInvalid input. Ticker: {input_action} | Price: {price}. Enter a valid one")
            continue
        
        message = f"\nWould you like to add Crypto: {input_action} | Ticker: {price[1]} | Last Price: ${price[0]}? y/n: "

        input_confirmation = input(message).lower().replace(" ","")

        check_confirmation_input_y_n_wallet(input_confirmation, wallet)

        wallet[input_action] = wv.COIN.copy()

        save_wallet_to_csv(wallet)

        print(f"\nAdded {input_action} successfully.")

        return


""" CHANGE ANY AMMOUNT """

def change_any_ammount(wallet):
    # Get crypto name for wallet key
    crypto_name_option = get_crypto_key(wallet)
    # Get key from wallet[crypto_name]
    crypto_value_option = get_value_key(wallet, crypto_name_option)
    # Confirm before continue
    confirm_crypto_and_option(crypto_name_option, crypto_value_option, wallet)
    # Get ammount and normalize
    new_ammount_now = get_ammount(crypto_name_option, crypto_value_option)
    # Confirm before continue
    confirm_new_and_old_value(crypto_name_option, crypto_value_option, new_ammount_now, wallet)
    # Change value
    wallet[crypto_name_option][crypto_value_option] = new_ammount_now

    save_wallet_to_csv(wallet)

    clear_prints()

    
def confirm_new_and_old_value(crypto, option, new_value, wallet):
    old_value = wallet[crypto][option]
    while True:
        input_action = input(f"\nWould you like to change from {old_value} to {new_value}? y/n: ").lower().replace(" ","")
        
        check_confirmation_input_y_n_wallet(input_action, wallet)

        return


def confirm_crypto_and_option(crypto, option, wallet):
    while True:
        input_action = input(f"\nWould you like to update {crypto} - {option.replace('_', ' ').title()}? y/n: ").lower().replace(" ","")
        
        check_confirmation_input_y_n_wallet(input_action, wallet)

        return


def get_value_key(wallet, crypto_name):
    crypto_data = ptwf.wallet_change_any_value_values_body(wallet, crypto_name)
    while True:

        input_action = input("\nEnter the input relateded to a crypto: ")

        if not input_action.isnumeric():
            print("\nThe input isn't a number or an integer.")
            continue

        input_action = int(input_action)

        if input_action not in range(len(crypto_data)+1):
            print("\nThe input is out of range.")
            continue

        clear_prints()
        if input_action == mv.PREVIOUS_MENU:
            change_any_ammount(wallet)

        return crypto_data[input_action-1]


def get_ammount(crypto_name, crypto_value_field):
    while True:
        input_action = input(f"\nUpdate {crypto_name} - {crypto_value_field.replace('_', ' ').title()}: ")

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

        input_action = int(input_action)

        if input_action not in range(len(cryptos_list)+1):
            print("\nThe input is out of range.")
            continue

        clear_prints()
        if input_action == mv.PREVIOUS_MENU:
            wallet_menu()

        return cryptos_list[input_action-1]