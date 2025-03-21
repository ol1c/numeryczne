import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def plot_settings(day_interval):
    plt.figure(figsize=(12, 7))
    plt.subplots_adjust(bottom=0.15, top=0.95)
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=day_interval))
    plt.xticks(rotation=45)


def plot_macd(data, buy, sell, title, day_interval):
    buy_date, buy_value, buy_signal = zip(*buy)
    sell_date, sell_value, sell_signal = zip(*sell)

    plot_settings(day_interval)
    plt.plot(data['Date'], data['MACD'], color='blue', label='MACD')
    plt.plot(data['Date'], data['SIGNAL'], color='red', label='SIGNAL')
    plt.scatter(buy_date, buy_signal, color='green', label='Zakup', zorder=5)
    plt.scatter(sell_date, sell_signal, color='pink', label='Sprzedaż', zorder=5)
    plt.legend()
    plt.title(title)
    plt.show()


def plot_value(data, buy, sell, title, day_interval):
    buy_date, buy_value, buy_signal = zip(*buy)
    sell_date, sell_value, sell_signal = zip(*sell)

    # plot_settings()
    # plt.plot(data['Date'], data['Value'], color='k', label='Wartości akcji')
    # plt.legend()
    # plt.show()

    plot_settings(day_interval)
    plt.plot(data['Date'], data['Value'], color='k', label='Wartości akcji')
    plt.scatter(buy_date, buy_value, color='green', label='Zakup', zorder=5)
    plt.scatter(sell_date, sell_value, color='red', label='Sprzedaż', zorder=5)
    plt.legend()
    plt.title(title)
    plt.show()


def plot_profit(profit1, title="", day_interval=30, p1_title='Profit', profit2=None, p2_title='Profit2', profit3=None, p3_title='Profit3', profit4=None, p4_title='Profit4'):
    profit_date, profit_value = zip(*profit1)

    plot_settings(day_interval)
    plt.plot(profit_date, profit_value, color='yellow', label=p1_title)

    if profit2 is not None:
        profit_date, profit_value = zip(*profit2)
        plt.plot(profit_date, profit_value, color='red', label=p2_title)

    if profit3 is not None:
        profit_date, profit_value = zip(*profit3)
        plt.plot(profit_date, profit_value, color='blue', label=p3_title)

    if profit4 is not None:
        profit_date, profit_value = zip(*profit4)
        plt.plot(profit_date, profit_value, color='green', label=p4_title)

    plt.legend()
    plt.title(title)
    plt.show()
