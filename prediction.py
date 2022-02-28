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
pprint(dt.get_all())

