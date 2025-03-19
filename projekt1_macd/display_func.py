import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def plot_settings(day_interval):
    plt.figure(figsize=(12, 7))
    plt.subplots_adjust(bottom=0.15, top=0.95)
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=day_interval))
    plt.xticks(rotation=45)
def plot_macd(data, buy, sell, title, day_interval):
    buy_data, buy_value, buy_signal = zip(*buy)
    sell_data, sell_value, sell_signal = zip(*sell)

    plot_settings(day_interval)
    plt.plot(data['Date'], data['MACD'], color='blue', label='MACD')
    plt.plot(data['Date'], data['SIGNAL'], color='red', label='SIGNAL')
    plt.scatter(buy_data, buy_signal, color='green', label='Zakup', zorder=5)
    plt.scatter(sell_data, sell_signal, color='pink', label='Sprzedaż', zorder=5)
    plt.legend()
    plt.title(title)
    plt.show()

def plot_value(data, buy, sell, title, day_interval):
    buy_data, buy_value, buy_signal = zip(*buy)
    sell_data, sell_value, sell_signal = zip(*sell)

    # plot_settings()
    # plt.plot(data['Date'], data['Value'], color='k', label='Wartości akcji')
    # plt.legend()
    # plt.show()

    plot_settings(day_interval)
    plt.plot(data['Date'], data['Value'], color='k', label='Wartości akcji')
    plt.scatter(buy_data, buy_value, color='green', label='Zakup', zorder=5)
    plt.scatter(sell_data, sell_value, color='red', label='Sprzedaż', zorder=5)
    plt.legend()
    plt.title(title)
    plt.show()
