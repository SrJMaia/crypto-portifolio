from miscellaneous_functions.prints_functions import clear_prints
from prettytable import PrettyTable
from menu.menu_function import get_menu_action
import menu.menu_variables as mv
import time
from tqdm import tqdm
from menu.menu_wallet_functions import wallet_menu

def temporary_function(action):
    """
    Futuramente remover isso e manter apenas get_menu_action do comentario
    """
    while True:

        if action in [mv.WALLET_OPTIONS, mv.EXIT]:
            return action
        print("\nUnder construction...")

        action = get_menu_action("main")


def menu():

    clear_prints()

    main_menu_body()

    action = get_menu_action("main")

    # Futuramente remover junto com temporary_function
    action = temporary_function(action)

    clear_prints()

    if action == mv.EXIT:
        print("\nClosing...\n")
        for i in tqdm(range(100)):
            time.sleep(0.02)
        clear_prints()
        return
    elif action == mv.SHOW_ALL:
        pass
    elif action == mv.WALLET_OPTIONS:
        wallet_menu()            


def main_menu_body():
    pt_menu = PrettyTable()
    pt_menu.field_names = ["Action", "Input"]
    pt_menu.title = "Menu"
    pt_menu.add_row(["Show All", mv.SHOW_ALL])
    pt_menu.add_row(["Wallet", mv.WALLET_OPTIONS])
    # y.add_row(["Hobart", 1357])
    # y.add_row(["Sydney", 2058])
    # y.add_row(["Melbourne", 1566])
    # y.add_row(["Perth", 5386])
    pt_menu.add_row(["Exit", mv.EXIT])

    pt_menu.hrules = 1

    print(pt_menu)