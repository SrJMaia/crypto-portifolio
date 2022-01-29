import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from wallet.wallet_functions import read_transactions_to_wallet
from pretty_table.pretty_table_functions import pretty_table_body

wallet, wallet_information = read_transactions_to_wallet()

import menu.menu_functions as mf
mf.main_menu()
