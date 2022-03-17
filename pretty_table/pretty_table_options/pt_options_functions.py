import menu.shared_files.shared_variables as mv
from prettytable import PrettyTable

def options_menu_body():
    pt_menu = PrettyTable()
    pt_menu.field_names = ["Action", "Input"]
    pt_menu.title = "Options"
    pt_menu.add_row(["Change Wallet Refresh Time", mv.CHANGE_WALLET_REFRESH_TIME])
    # pt_menu.add_row(["Wallet", mv.WALLET_OPTIONS])
    # y.add_row(["Sydney", 2058])
    # y.add_row(["Melbourne", 1566])
    # y.add_row(["Perth", 5386])
    pt_menu.add_row(["Previous Menu", mv.PREVIOUS_MENU])

    pt_menu.hrules = 1

    print(pt_menu)

def change_refresh_time_body():
    pt_menu = PrettyTable()

    pt_menu.title = "Chage Refresh Time"

    pt_menu.add_column("Minutes", mv.CHANGE_TIME_MINUTES_STR)
    pt_menu.add_column("Input", mv.CHANGE_TIME_MINUTES_INPUT)

    pt_menu.add_row(["Previous Menu", mv.PREVIOUS_MENU])

    pt_menu.hrules = 1

    print(pt_menu)