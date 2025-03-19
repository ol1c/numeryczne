import numpy as np

from data import *
from macd_func import *
from display_func import *

def example_buy_sell(data, buy, sell, i):
    example_buy = [buy[i]]
    example_sell = [sell[i+3]]
    start_date = example_buy[0][0]
    end_date = example_sell[0][0]
    mask = (data['Date'] >= start_date) & (data['Date'] <= end_date)
    filtered_data = data[mask]
    profit = example_sell[0][1] - example_buy[0][1]
    plot_macd(filtered_data, example_buy, example_sell, "Profit: " + str(profit), 7)


data = get_data()
data['MACD'] = get_macd(data['Value'])
data['SIGNAL'] = get_signal(data['MACD'])
buy, sell = find_buy_and_sell_points(data)

plot_macd(data, buy, sell, "", 30)
plot_value(data, buy, sell, "", 30)

example_buy_sell(data, buy, sell, 1)
example_buy_sell(data, buy, sell, 10)
