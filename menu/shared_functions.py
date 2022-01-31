import menu.menu_variables as mv

def get_menu_action(mode):
    while True:

        input_action = input("\nEnter the input relateded to an action: ")

        if not input_action.isnumeric():
            print("\nThe input isn't a number or an integer.")
            continue

        input_action = int(input_action)

        if input_action == mv.EXIT:
            return int(input_action)

        if mode == "main":
            if input_action not in [mv.SHOW_ALL ,mv.WALLET_OPTIONS]:
                print("\nInvalid option.")
                continue
        elif mode == "wallet":
            if input_action not in [mv.SHOW_WALLET, mv.CHANGE_ANY_AMMOUNT]:
                print("\nInvalid option.")
                continue

        return int(input_action)