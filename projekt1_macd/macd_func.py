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
