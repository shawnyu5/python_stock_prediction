import os

# import tensorflow as tf
# from tensorflow import keras
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.fundamentaldata import FundamentalData
from dotenv import load_dotenv
from pprint import pprint
from average_true_range_values import Average_true_range_values
from daily_timeSeries import Daily_timeSeries
import pandas as pd


def sync_dates(dict1, dict2):
    to_remove = []
    for date1, _ in dict1.items():
        # c = 0
        # same = True
        # for date2, _ in dict2.items():
        try:
            dict2[date1]
        except:
            to_remove.append(date1)
            continue

        # if not same:
        # to_remove.append(date1)

    # pprint(to_remove)
    # remove dates from both dictionary
    for date in to_remove:
        del dict1[date]
        # del dict2[date]

    # pprint(to_remove)
    return dict1, dict2


load_dotenv(verbose=True)
key = os.getenv("key")

techindicators = TechIndicators(key)
timeSeries = TimeSeries(key)


symbol = "lspd"
dt = Daily_timeSeries(symbol=symbol)
# pprint(dt.get_all())

av = Average_true_range_values(symbol=symbol).get_all()


# dict1, dict2 = sync_dates(dt.get_all(), av.get_all())
# pprint(dt.get_all().keys())

x = []
Y = []
for key, value in dt.get_all().items():
    # {'1. open': '73.8300', '2. high': '74.6500', '3. low': '71.1500', '4. close': '71.2700', '5. volume': '371926'}
    obj = {}
    try:
        obj["date"] = key
        obj["open"] = value["1. open"]
        obj["high"] = value["2. high"]
        obj["low"] = value["3. low"]
        if key in av:
            price = list(av[key].values())[0]
            obj["atr"] = price
        x.append(obj)

        Y.append((obj["date"], value["4. close"]))
        # Y.append(value["4. close"])

    except:
        continue

# pprint(x)
# pprint(Y)

feature_df = pd.DataFrame(data=x, columns=["date", "high", "low", "open", "atr"])
label_df = pd.DataFrame(data=Y, columns=["date", "closing"])
print(feature_df.head())
print(label_df.head())


# if dict1 not in list(dt.get_all()):
# print("Ayyyy")
