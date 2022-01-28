def set_movement():
    """
    Input and action
    0 Deposit
    1 Buy
    2 Sell
    
    """
    type = 10
    while type not in [0,1,2]:
        print("0 = Deposit | 1 = Buy | 2 = Sell")
        type = input("Select one option: ").strip().replace(" ","")
        try:
            int(type)
        except:
            print("It's not a valid option.")
        else:
            if not int(type) in range(0,3):
                print("Wrong option!")
                continue
            return int(type)

