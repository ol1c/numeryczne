import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from data import *
from macd_func import *

data = get_data()
data['MACD'] = get_macd(data['Zamkniecie'])
data['SIGNAL'] = get_signal(data['MACD'])

plt.figure(figsize=(16, 10))
#plt.plot(data['Data'], data['Zamkniecie'], color='k', label='Wartości')
plt.plot(data['Data'], data['MACD'], color='b', label='MACD')
plt.plot(data['Data'], data['SIGNAL'], color='r', label='SIGNAL')
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=14))
plt.xticks(rotation=90)
plt.legend()
plt.show()
