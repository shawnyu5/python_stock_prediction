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
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split


load_dotenv(verbose=True)
key = os.getenv("key")

techindicators = TechIndicators(key)
timeSeries = TimeSeries(key)


symbol = "lspd"
dt = Daily_timeSeries(symbol=symbol)
av = Average_true_range_values(symbol=symbol).get_all()


data = []
for key, value in dt.get_all().items():
    # {'1. open': '73.8300', '2. high': '74.6500', '3. low': '71.1500', '4. close': '71.2700', '5. volume': '371926'}
    obj = {}
    try:
        obj["date"] = key
        obj["open"] = float(value["1. open"])
        obj["high"] = float(value["2. high"])
        obj["low"] = float(value["3. low"])
        obj["close"] = float(value["4. close"])
        if key in av:
            price = list(av[key].values())[0]
            obj["atr"] = float(price)
        data.append(obj)

    except:
        continue

train, test = train_test_split(data, test_size=0.20, shuffle=True)
x_train_df = pd.DataFrame(data=train, columns=["high", "low", "open", "atr"])
y_train_df = pd.DataFrame(data=train, columns=["close"])

x_test_df = pd.DataFrame(data=test, columns=["high", "low", "open", "atr"])
y_test_df = pd.DataFrame(data=test, columns=["close"])

#  print(x_train_df.head())
#  print(y_train_df.head())

x_train_df = x_train_df.to_numpy().astype("float32")
# convert all y_train values to floats
#  y_train_df = [float(current) for current in y_train_df.closing.values]
y_train_df = np.array(y_train_df)


# Building the LSTM Model
model = keras.Sequential(
    [
        (
            keras.layers.LSTM(
                units=32,
                return_sequences=True,
                input_shape=(x_train_df.shape[1], 1),
                activation="relu",
            )
        ),
        (keras.layers.LSTM(units=32, return_sequences=True, activation="relu")),
        (keras.layers.Dense(units=1, activation="relu")),
        # (keras.layers.Dense(units=16, activation="sigmoid")),
        # (keras.layers.Dense(units=16, activation="sigmoid")),
    ]
)

model.compile(optimizer="adam", loss="mean_squared_error")


model.fit(x_train_df, y_train_df, epochs=50, batch_size=4, verbose=1)

# testing
print("EVALUATION")
model.evaluate(x_test_df, y_test_df)

