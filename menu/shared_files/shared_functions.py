import menu.shared_files.shared_variables as mv

def get_menu_action(mode):
    while True:

        input_action = input("\nEnter the input relateded to an action: ")

        if not input_action.isnumeric():
            print("\nThe input isn't an option.")
            continue

        input_action = int(input_action)

        if input_action == mv.EXIT:
            return int(input_action)

        if mode == "main":
            if input_action not in mv.MAIN_ACTION_LIST:
                print("\nInvalid option.")
                continue
        elif mode == "wallet":
            if input_action not in mv.WALLET_ACTION_LIST:
                print("\nInvalid option.")
                continue
        elif mode == "options":
            if input_action not in mv.OPTIONS_ACTION_LIST:
                print("\nInvalid option.")
                continue

        return int(input_action)

