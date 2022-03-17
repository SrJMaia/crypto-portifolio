from tracemalloc import start
from menu.support_files.files_manipulation.files_manipulation_function import write_if_program_started
from menu.support_files.support_wallet.wallet_functions import starting_first_time_wallet
from pretty_table.pretty_table_main.pt_main_functions import main_menu_body
from miscellaneous_functions.prints_functions import clear_prints
from menu.shared_files.shared_functions import get_menu_action
import menu.shared_files.shared_variables as mv
from menu.menu_options import options_menu
from menu.menu_wallet import wallet_menu
from tqdm import tqdm
import time
import sys

def menu():

    clear_prints()

    print("Starting program...\n")

    starting_first_time_wallet()

    clear_prints()

    main_menu_body()

    action = get_menu_action("main")

    clear_prints()

    if action == mv.EXIT:
        print("\nClosing...\n")
        for i in tqdm(range(100)):
            time.sleep(0.02)
        clear_prints()
        write_if_program_started(mv.PROGRAM_OFF)
        sys.exit()
    elif action == mv.SHOW_ALL:
        pass
    elif action == mv.WALLET_OPTIONS:
        wallet_menu()  
    elif action == mv.OPTIONS:
        options_menu()  
            
