import pandas as pd

def loadDatasetRaw():
    try:
        dataset = pd.read_csv('data/raw/Students.csv', sep=',',  encoding='utf-8')
        return dataset
    except FileNotFoundError:
        print('Erro ao carregar os dados.')
        return None


def loadDatasetProcessed():
    try:
        dataset = pd.read_csv('data/processed/datasetclean.csv', sep=',', encoding='utf-8')
        return dataset
    except FileNotFoundError:
        print('Erro ao carregar os dados.')
        return None