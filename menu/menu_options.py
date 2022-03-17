import menu.support_files.files_manipulation.files_manipulation_function as manage_time_file
import pretty_table.pretty_table_options.pt_options_functions as ptof
from miscellaneous_functions.prints_functions import clear_prints
from menu.shared_files.shared_functions import get_menu_action
import menu.shared_files.shared_variables as mv
import menu.menu_main as mmf
from time import sleep

def options_menu():

    clear_prints()

    ptof.options_menu_body()

    action = get_menu_action("options")

    clear_prints()

    if action == mv.PREVIOUS_MENU:
        mmf.menu()
    elif action == mv.CHANGE_WALLET_REFRESH_TIME:
        change_wallet_refresh_time()
        
    
    options_menu()


""" GENERAL """

def check_confirmation_input_y_n_options(input_answer):
    if input_answer not in mv.CHECK_CONFIRMATION:
        print("\nIncorrect option.")
        return False
    
    clear_prints()

    if input_answer == mv.CHECK_YES:
        return True

    options_menu()


""" CHANGE WALLET REFRESH TIME """
    
from time import sleep
def change_wallet_refresh_time():
    clear_prints()

    ptof.change_refresh_time_body()

    while True:

        input_action = input("\nEnter the input relateded to a crypto: ")

        if not input_action.isnumeric():
            print("\nThe input isn't a number or an integer.")
            continue

        input_action = int(input_action)

        if input_action == mv.PREVIOUS_MENU:
            return

        if input_action not in mv.CHANGE_TIME_MINUTES_INPUT:
            print("\nThe input is out of range.")
            continue

        _, old_time = manage_time_file.get_time_and_wait_time_from_file()

        new_time = mv.CHANGE_TIME_MINUTES_MIN[input_action-1]

        message = f"\nWould you like to change the refresh time from {old_time} minutes to {new_time} minutes? y/n: "

        input_confirmation = input(message).lower().replace(" ","")

        flag_check_input = check_confirmation_input_y_n_options(input_confirmation)

        if not flag_check_input:
            continue

        manage_time_file.save_only_wait_time_to_file(new_time)

        print(f"\nChanging from {old_time} minutes to {new_time} minutes...")

        sleep(2)

        clear_prints()

        return
