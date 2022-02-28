import os
import tensorflow as tf
from tensorflow import keras
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.fundamentaldata import FundamentalData
from dotenv import load_dotenv
from pprint import pprint
from average_true_range_values import Average_true_range_values
from daily_timeSeries import Daily_timeSeries


load_dotenv()
key = os.getenv("key")

techindicators = TechIndicators(key)
timeSeries = TimeSeries(key)

symbol = "lspd"

dt = Daily_timeSeries(symbol=symbol)
# pprint(dt.get_all())

# average_true_range_values = Average_true_range_values(symbol=symbol)
# pprint(average_true_range_values.get_dates())


# X = []
# Y = []
# for key, value in dt.get_all().items():
# # {'1. open': '73.8300', '2. high': '74.6500', '3. low': '71.1500', '4. close': '71.2700', '5. volume': '371926'}
# obj = {}
# try:
# obj["date"] = key
# obj["open"] = value["1. open"]
# obj["high"] = value["2. high"]
# obj["low"] = value["3. low"]
# Y.append(value["4. close"])
# X.append(obj)
# except:
# continue

# pprint(X)
# pprint(Y)

# model = keras.Sequential()
# model.add(keras.layers.LSTM(units=50,return_sequences=True))
# model.add(keras.Dropout(0.2))
# model.add(keras.LSTM(units=50,return_sequences=True))
# model.add(keras.Dropout(0.2))
# model.add(keras.LSTM(units=50,return_sequences=True))
# model.add(keras.Dropout(0.2))
# model.add(keras.LSTM(units=50))
# model.add(keras.Dropout(0.2))
# model.add(keras.Dense(units=1))

# model.compile(
# optimizer="adam",
# metrics=["accuracy"]
# )

# model.fit()
