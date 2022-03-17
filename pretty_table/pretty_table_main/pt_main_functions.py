import menu.shared_files.shared_variables as mv
from prettytable import PrettyTable

def main_menu_body():
    pt_menu = PrettyTable()
    pt_menu.field_names = ["Action", "Input"]
    pt_menu.title = "Menu"
    pt_menu.add_row(["Show All", mv.SHOW_ALL])
    pt_menu.add_row(["Wallet", mv.WALLET_OPTIONS])
    pt_menu.add_row(["Options", mv.OPTIONS])
    # y.add_row(["Melbourne", 1566])
    # y.add_row(["Perth", 5386])
    pt_menu.add_row(["Exit", mv.EXIT])

    pt_menu.hrules = 1

    print(pt_menu)
