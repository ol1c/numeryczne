from data import *
from interpolation_funcs import *
from plots import *
import numpy as np


def analysis(data, func, N, nodes_pattern, title):
    y = data["Wysokość (m)"]
    x, t_param = transform_data(data["Dystans (m)"])
    nodes_x, nodes_y = get_nodes(x, y, nodes_pattern(N))
    new_x = fine_nodes(1000)
    new_y = func(nodes_x, nodes_y, new_x)
    plot_data(np.array(x) * t_param[1] + t_param[0], y,
              np.array(new_x) * t_param[1] + t_param[0], new_y, "interpolacja",
              np.array(nodes_x) * t_param[1] + t_param[0], nodes_y, title)


def standard_analysis(data, func, title):
    analysis(data, func, 5, fine_nodes, title+f" dla {5} węzłów")
    analysis(data, func, 10, fine_nodes, title+f" dla {10} węzłów")
    analysis(data, func, 20, fine_nodes, title+f" dla {20} węzłów")
    analysis(data, func, 40, fine_nodes, title+f" dla {40} węzłów")


def bonus_analysis(data1, data2, data3):
    analysis(data1, lagrange, 10, chebyshev_nodes, f"Interpolacja wielomianowa trasy 1 dla {10} węzłów chebysheva")
    analysis(data1, lagrange, 40, chebyshev_nodes, f"Interpolacja wielomianowa trasy 1 dla {40} węzłów chebysheva")
    analysis(data1, sklejany, 20, chebyshev_nodes, f"Interpolacja sklejana trasy 1 dla {20} węzłów chebysheva")
    analysis(data2, lagrange, 40, chebyshev_nodes, f"Interpolacja wielomianowa trasy 2 dla {40} węzłów chebysheva")
    analysis(data3, lagrange, 40, chebyshev_nodes, f"Interpolacja wielomianowa trasy 3 dla {40} węzłów chebysheva")


deptak = get_data_deptak()
kanion = get_data_kanion()
chelm = get_data_chelm()

standard_analysis(deptak, lagrange, "Interpolacja wielomianowa trasy 1")
standard_analysis(deptak, sklejany, "Interpolacja sklejana trasy 1")
standard_analysis(kanion, lagrange, "Interpolacja wielomianowa trasy 2")
standard_analysis(kanion, sklejany, "Interpolacja sklejana trasy 2")
standard_analysis(chelm, lagrange, "Interpolacja wielomianowa trasy 3")
standard_analysis(chelm, sklejany, "Interpolacja sklejana trasy 3")
bonus_analysis(deptak, kanion, chelm)


