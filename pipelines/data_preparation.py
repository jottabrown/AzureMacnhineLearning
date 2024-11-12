# data_preparation.py
import pandas as pd

def prepare_data(data_path):
    """
    Carrega e prepara os dados.
    - data_path: Caminho para o arquivo CSV contendo os dados.
    """
    data = pd.read_csv(data_path)
    # Limpeza básica dos dados
    data = data.dropna()  # Remove valores nulos
    data = data[data['target'] > 0]  # Filtra exemplos com target positivo
    
    # Normalização
    numeric_features = data.select_dtypes(include=['float64', 'int64']).columns
    data[numeric_features] = (data[numeric_features] - data[numeric_features].mean()) / data[numeric_features].std()
    
    return data

# Teste
if __name__ == "__main__":
    data = prepare_data("caminho_para_seu_arquivo.csv")
    print(data.head())
