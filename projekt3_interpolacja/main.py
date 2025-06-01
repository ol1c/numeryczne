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


# deptak = get_data_deptak()
# analysis(deptak, lagrange, 16, fine_nodes, f"Interpolacja trasy 1 dla N={16} węzłów")


kanion = get_data_kanion()
analysis(kanion, lagrange, 16, fine_nodes, f"Interpolacja trasy 2 dla N={16} węzłów")
analysis(kanion, lagrange, 16, chebyshev_nodes, f"Interpolacja trasy 2 dla N={16} węzłów")
