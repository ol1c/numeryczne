import numpy as np

from data import *
from macd_func import *
from display_func import *


data = get_data()
data['MACD'] = get_macd(data['Value'])
data['SIGNAL'] = get_signal(data['MACD'])
buy, sell = find_buy_and_sell_points(data)

plot_data(data, buy, sell)
