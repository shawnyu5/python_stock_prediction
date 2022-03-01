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


x = []
Y = []
for key, value in dt.get_all().items():
    # {'1. open': '73.8300', '2. high': '74.6500', '3. low': '71.1500', '4. close': '71.2700', '5. volume': '371926'}
    obj = {}
    try:
        obj["date"] = key
        obj["open"] = float(value["1. open"])
        obj["high"] = value["2. high"]
        obj["low"] = float(value["3. low"])
        if key in av:
            price = list(av[key].values())[0]
            obj["atr"] = float(price)
            # print(type(price))
        x.append(obj)

        Y.append(value["4. close"])
        # Y.append(value["4. close"])

    except:
        continue

# pprint(x)
# pprint(Y)

# train, test = train_test_split(x, test_size=0.20, shuffle=True)
x_train = pd.DataFrame(data=x, columns=["date", "high", "low", "open", "atr"])
y_train = pd.DataFrame(data=Y, columns=["closing"])
x_train.drop("date", axis=1, inplace=True)
# print(x_train.info())
# exit()
# print(x_train.head())

x_train = x_train.to_numpy().astype("float32")
# convert all y_train values to floats
y_train = [float(current) for current in y_train.closing.values]
y_train = np.array(y_train)


# print(x_train[0])

# feature_df = np.column_stack(
# (
# feature_df.date.values,
# feature_df.high.values,
# feature_df.low.values,
# feature_df.open.values,
# feature_df.atr.values,
# )
# )
# print(x_train.shape)
# print(y_train.shape)
# print(f" x_train.shape[0]: {str(x_train.shape[0])}")  # __AUTO_GENERATED_PRINT_VAR__
# x_train = x_train.reshape((x_train.shape[0], x_train.shape[1], 1))
# y_train = y_train.reshape((y_train.shape[0], y_train.shape[1], 1))

# print(x_train)
# print(y_train.closing.values)

# exit()


# Building the LSTM Model
model = keras.Sequential(
    [
        (keras.layers.LSTM(units=32, return_sequences=True, input_shape=(x_train.shape[1], 1), activation="relu")),
        (keras.layers.LSTM(units=32, return_sequences=True, activation="relu")),
        (keras.layers.Dense(units=1, activation="relu")),
        # (keras.layers.Dense(units=16, activation="sigmoid")),
        # (keras.layers.Dense(units=16, activation="sigmoid")),
    ]
)

model.compile(optimizer="adam", loss="mean_squared_error")

print(f" x_train: {str(x_train)}")  # __AUTO_GENERATED_PRINT_VAR__
print(f" y_train: {str(y_train)}")  # __AUTO_GENERATED_PRINT_VAR__

model.fit(x_train, y_train, epochs=50, batch_size=4, verbose=1)

# testing


