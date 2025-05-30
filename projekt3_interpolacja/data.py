import pandas as pd


def get_data_deptak():
    data = pd.read_csv('data/SpacerniakGdansk.csv')
    return data

def get_data_chelm():
    data = pd.read_csv('data/chelm.csv')
    return data

def get_data_kanion():
    data = pd.read_csv('data/WielkiKanionKolorado.csv')
    return data
