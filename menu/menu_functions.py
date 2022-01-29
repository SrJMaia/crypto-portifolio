from prettytable import PrettyTable

def main_menu():

    menu_body()

    action = check_if_action_isint()


def menu_body():
    pt_menu = PrettyTable()
    pt_menu.field_names = ["Action", "Input"]
    pt_menu.title = "Menu"
    pt_menu.add_row(["Show All", 0])
    pt_menu.add_row(["Wallet", 5905])
    # y.add_row(["Darwin", 112])
    # y.add_row(["Hobart", 1357])
    # y.add_row(["Sydney", 2058])
    # y.add_row(["Melbourne", 1566])
    # y.add_row(["Perth", 5386])

    pt_menu.hrules = 1

    print(pt_menu)


def check_if_action_isint():
    while True:

        input_action = input("\nEnter the input relateded to the action: ")

        if not input_action.isnumeric():
            print("\nThe input isn't a number or an integer.")
            continue
        input_action = int(input_action)

        while True:
            final_decision = input("\nYour decision was {input_action}. Is it correct? (y/n): ").strip().lower()
            if not final_decision.isalpha() or final_decision not in ["y","n"]:
                print("\nWrong confirmation option.")
                continue
            break

        if final_decision == "n":
            continue
        break
    
    print(f"\nYour action was: {input_action}")

    return int(input_action)