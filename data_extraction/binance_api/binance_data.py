from binance import Client
import pandas as pd

api_key = "YyFyNwsMj9x8O4rTLAUlxmHlwLR5irddOZJnCyREvcByidIpS2AZO3o2V8DonG7c"
api_secret = "pwYWNmuUiib7GPEUt410ER9XapW999dBZvTaUBPJhbH4w6Fw3VW309UAtCZXZKxJ"

def login_binance():
    return Client(api_key, api_secret)


def get_historical_prices_df(symbol, interval):
    """
    Get whole historical data
    # valid intervals - 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M

    client -- binance class
    pair -- valid pair
    interval -- time interval
    """

    client = login_binance()

    try:
        timestamp = client._get_earliest_valid_timestamp(f"{symbol}USDT", interval)
        bars = client.get_historical_klines(f"{symbol}USDT", interval, timestamp, limit=1000)
    except:
        timestamp = client._get_earliest_valid_timestamp(f"USDT{symbol}", interval)
        bars = client.get_historical_klines(f"USDT{symbol}", interval, timestamp, limit=1000)

    for line in bars:
        del line[6:]

    data = pd.DataFrame(bars, columns=['date', 'open', 'high', 'low', 'close', 'volume'])
    data.set_index('date', inplace=True)
    data.index = pd.to_datetime(data.index, unit='ms')

    return data


def get_last_price_available(symbol):
    """
    Get last available price from binance

    client: binance class
    symbol: must be the ticker
    """

    price = 0.0

    client = login_binance()

    try:
        price = client.get_symbol_ticker(symbol=f"{symbol}USDT")
    except:
        price = client.get_symbol_ticker(symbol=f"USDT{symbol}")
    finally:
        if price != 0:
            return float(price["price"]), price["symbol"]
        return price, price

