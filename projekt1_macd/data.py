import pandas as pd


def get_data():
    data = pd.read_csv('cdr_d.csv')
    return data
