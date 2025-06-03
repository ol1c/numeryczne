import matplotlib.pyplot as plt


def plot_data(x1, y1, x2, y2, label2, nodes_x, nodes_y, title):
    plt.figure(figsize=(12, 7))
    plt.subplots_adjust(bottom=0.15, top=0.95)
    plt.plot(x1, y1, label="dane orginalne", color="black")
    plt.plot(x2, y2, label=label2, color='blue', ls="dotted")
    plt.scatter(nodes_x, nodes_y, label="węzły interpolacji", color='blue')
    plt.xlabel("Dystans [m]")
    plt.ylabel("Wysokość [m n.p.m]")
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.show()
