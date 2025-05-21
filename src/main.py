import sys
import os
import pandas as pd

# Adiciona o diretório raiz ao sys.path para que o Python consiga encontrar a pasta 'plots'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importando as funções corretamente
from load_data.load_data import loadDatasetRaw
from data_preprocessing.data_preprocessing import remove_nulls, drop_duplicates, rename_columns
from utils.save_data import save_data
from models.model import train_random_forest

def main():
    # Carregando os dados.
    dataset = loadDatasetRaw()
    if dataset is None:
        print("Encerrando execução: dataset não carregado.")
        return
    
    pd.set_option('display.max_columns', None)
    
    # Tratamento dos dados.
    dataset = remove_nulls(dataset)
    dataset = drop_duplicates(dataset)
    dataset = rename_columns(dataset)

    # Salvando os Dados.
    save_data(dataset, 'csv', 'data/processed')
    print(dataset.describe())

    # Modelo.
    train_random_forest()

# Executando o código principal
if __name__ == "__main__":
    main()