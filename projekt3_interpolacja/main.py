from data import *
from interpolation_funcs import transform_data
from plots import *

data = get_data_deptak()
# x, y = zip(*data)
x = data["Dystans (m)"]
y = data["Wysokość (m)"]
plot_data(x, y, x, y, "", x, y, "", x, y, "")

x_new, a = transform_data(x)
plot_data(x_new, y, x_new, y, f"{a}", x_new, y, "", x_new, y, "")

