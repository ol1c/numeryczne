import matplotlib.pyplot as plt


def plotSemilogy(x, y, title):
    plt.figure(figsize=(12, 7))
    plt.subplots_adjust(bottom=0.15, top=0.95)
    plt.semilogy(x, y)
    plt.title(title)
    plt.xlabel("Iteracje")
    plt.ylabel("Norma residuum")
    plt.show()

def plotTime(x, time1, time2, time3):
    plt.figure(figsize=(12, 7))
    plt.subplots_adjust(bottom=0.15, top=0.95)
    plt.subplot(2, 1, 1)
    plt.plot(x, time1, label="metoda Jacobiego")
    plt.plot(x, time2, label="metoda Gaussa-Seidla")
    plt.plot(x, time3, label="metoda rozkładu LU")
    plt.legend()
    plt.xlabel("rozmiar macieży N")
    plt.ylabel("czas potrzebny do obliczenia [s]")
    plt.title("Porównanie czasu potzrebnego do rozwiązania równania")
    plt.subplot(2, 1, 2)
    plt.semilogy(x, time1, label="metoda Jacobiego")
    plt.semilogy(x, time2, label="metoda Gaussa-Seidla")
    plt.semilogy(x, time3, label="metoda rozkładu LU")
    plt.legend()
    plt.xlabel("rozmiar macieży N")
    plt.ylabel("czas potrzebny do obliczenia [s]")
    plt.title("Porównanie czasu potzrebnego do rozwiązania równania (skala log)")
    plt.tight_layout()
    plt.show()