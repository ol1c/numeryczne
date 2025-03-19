import numpy as np

def get_ema(data, n):
    alfa = 2 / (n + 1)
    ema_values = [data[0]]

    for i in range(1, len(data)):
        new_value = alfa * data[i] + (1 - alfa) * ema_values[-1]
        ema_values.append(new_value)

    return ema_values

def get_macd(data):
    ema12 = get_ema(data, 12)
    ema26 = get_ema(data, 26)
    return np.array(ema12) - np.array(ema26)

def get_signal(macd):
    return get_ema(macd, 9)

def find_buy_and_sell_points(data):
    buy = []
    sell = []
    for i in range(1, len(data)):
        if data['MACD'][i-1] < data['SIGNAL'][i-1] and data['MACD'][i] > data['SIGNAL'][i] :
            buy.append((data['Date'][i], data['Value'][i], data['SIGNAL'][i]))
        elif data['MACD'][i-1] > data['SIGNAL'][i-1] and data['MACD'][i] < data['SIGNAL'][i]:
            sell.append((data['Date'][i], data['Value'][i], data['SIGNAL'][i]))
    return buy, sell
