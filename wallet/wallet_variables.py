DATE = 0
ACTION_TYPE = 1
PRIMARY = 2
PRI_AMMOUNT = 3
FEE = 4
FEE_COIN = 5
SECONDARY = 6
SEC_AMMOUNT = 7
SEC_COIN_PRICE = 8
PRICE_IN_USD = 9
AMMOUNT_IN_USD = 10
DRY_POWDER = "dry_powder"
FIX_INCOME = "fix_income"

ALLOCATION = {
    'ethereum':0.3,
    'cardano':0.03,
    'arweave':0.01,
    'cosmos':0.05,
    'bitcoin':0.2,
    'polkadot':0.1,
    'injective-protocol':0.02,
    'chainlink':0.01,
    'polygon':0.03,
    'thorchain':0.03,
    'solana':0.1,
    'helium':0.03,
    'fantom':0.03,
    'yield-guild-games':0.01,
    "tether":0.05,
    "usd-coin":0.2,
    "basic-attention-token":0.01,
    "merit-circle":0.01,
}

COIN = {
    "invested":0.0, # in $
    "ammount_bought":0.0, 
    "ammount_now":0.0, 
    "interest_earned":0.0, 
    "growth_interest":0.0,
    "price_today":0.0, 
    "investment_now":0.0, # how much is worth it now
    "gain_fiat":0.0, # in $
    "growth_fiat":0.0, # in %
    "actual_allocation":0.0, # 
    "default_allocation":0.0, # 
    "next_deposit":0.0, # how much to deposit for the next k
    "previous_deposit":0.0, # previous ammount to deposit
    "deposit_impact":0.0, # in $
    "bought_prices_sum":0.0, # average buy price - sold
    "bought_prices_times":0, # times bought - sold
    "pair_name":""
}

STABLE = {
    "invested":0.0,
    "ammount_now":0.0,
    "interest_earned":0.0,
    "actual_allocation":0.0, 
    "default_allocation":0.0,
    "next_deposit":0.0, 
    "previous_deposit":0.0, 
    "deposit_impact":0.0
}

FIAT = {
    "eur":0.0, # in € 
    "stasis-euro":0.0
}

RESUME = {
    "invested":0.0,
    "today_investment":0.0,
    "gain":0.0,
    "growth":0.0,
    "pairs_ammount":0,
    "next_goal":0.0
}