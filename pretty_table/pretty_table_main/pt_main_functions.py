from prettytable import PrettyTable
import menu.menu_variables as mv

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
