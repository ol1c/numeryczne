import numpy as np

def transform_data(x):
    start = x[0]
    end = x[len(x)-1]
    a = end - start
    copy = x
    for i in range(len(copy)):
        copy[i] = (copy[i] - start) / a
    return copy, a

