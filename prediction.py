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

    pprint(to_remove)
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

av = Average_true_range_values(symbol=symbol)
# pprint(av.get_all())

dict1, dict2 = sync_dates(dt.get_all(), av.get_all())
# pprint(dt.get_all().keys())

# if dict1 not in list(dt.get_all()):
# print("Ayyyy")
