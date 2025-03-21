import numpy as np

from data import *
from macd_func import *
from display_func import *


def simulation(buy_points, buy_rate, sell_points, sell_rate, wallet_start, stocks_start, profit):
    transactions = [(date, value, True) for date, value, signal in buy_points]
    transactions += [(date, value, False) for date, value, signal in sell_points]
    transactions.sort(key=lambda x: x[0])
    wallet = wallet_start
    stocks = stocks_start

    for transaction in transactions:
        if transaction[2]:
            trade = wallet // transaction[1] * buy_rate
            if trade != 0:
                stocks = trade + stocks
                wallet = wallet - (trade * transaction[1])
            profit.append((transaction[0], wallet + stocks * transaction[1]))
        else:
            trade = stocks * sell_rate
            if trade != 0:
                wallet = (trade * transaction[1]) + wallet
                stocks = stocks - trade
            profit.append((transaction[0], wallet + stocks * transaction[1]))
        print(profit[-1])

    return profit, wallet, stocks


def example_buy_sell(data, buy, sell, i):
    example_buy = [buy[i]]
    example_sell = [sell[i + 3]]
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

# plot_macd(data, buy, sell, "", 30)
# plot_value(data, buy, sell, "", 30)
#
# example_buy_sell(data, buy, sell, 1)
# example_buy_sell(data, buy, sell, 10)

allin, wallet, stocks = simulation(buy, 1, sell, 1, 0, 1000, [(data['Date'][0], 1000 * data['Value'][0])])
allin.append((data['Date'].iloc[-1], wallet + (stocks * data['Value'].iloc[-1])))

fiftyfifty, wallet, stocks = simulation(buy, 0.5, sell, 0.5, 0, 1000, [(data['Date'][0], 1000 * data['Value'][0])])
fiftyfifty.append((data['Date'].iloc[-1], wallet + (stocks * data['Value'].iloc[-1])))

third, wallet, stocks = simulation(buy, 0.8, sell, 0.2, 0, 1000, [(data['Date'][0], 1000 * data['Value'][0])])
third.append((data['Date'].iloc[-1], wallet + (stocks * data['Value'].iloc[-1])))

none, wallet, stocks = simulation(buy, 0, sell, 0, 0, 1000, [(data['Date'][0], 1000 * data['Value'][0])])
none.append((data['Date'].iloc[-1], wallet + (stocks * data['Value'].iloc[-1])))

plot_profit(allin, "Symulacja kupna i sprzedaży", 14, "All-In", fiftyfifty, "buy/sell 50/50", third, "buy/sell 80/20", none, "Wartość 1000 akcji")
