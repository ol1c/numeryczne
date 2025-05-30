import matplotlib.pyplot as plt


def plot_data(x_og, y_og, x1, y1, label1, x2, y2, label2, x3, y3, label3):
    plt.figure(figsize=(12, 7))
    plt.subplots_adjust(bottom=0.15, top=0.95)
    plt.plot(x_og, y_og, label="dane orginalne")
    plt.plot(x1, y1, label=label1, color='green')
    plt.scatter(x1, y1, color='green')
    plt.plot(x2, y2, label=label2, color='blue')
    plt.scatter(x2, y2, color='blue')
    plt.plot(x3, y3, label=label3, color='red')
    plt.scatter(x3, y3, color='red')
    plt.xlabel("Iteracje")
    plt.ylabel("Norma residuum")
    plt.title("Zmiana normy residuum")
    plt.legend()
    plt.grid()
    plt.show()