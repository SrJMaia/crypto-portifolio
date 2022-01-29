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
    'ETH':0.3,
    'ADA':0.03,
    'AR':0.01,
    'ATOM':0.05,
    'BTC':0.2,
    'DOT':0.1,
    'INJ':0.02,
    'LINK':0.01,
    'MATIC':0.03,
    'RUNE':0.03,
    'SOL':0.1,
    'HNT':0.03,
    'FTM':0.03,
    'YGG':0.01,
    "USDT":0.05,
    "USDC":0.2,
    "BAT":0.01,
    "MC":0.01,
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