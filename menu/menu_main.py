from pretty_table.pretty_table_main.pt_main_functions import main_menu_body
from miscellaneous_functions.prints_functions import clear_prints
from menu.shared_functions import get_menu_action
from menu.menu_wallet import wallet_menu
import menu.menu_variables as mv
from tqdm import tqdm
import time

def menu():

    clear_prints()

    main_menu_body()

    action = get_menu_action("main")

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
