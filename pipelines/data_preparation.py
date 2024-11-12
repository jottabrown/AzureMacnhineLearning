# data_preparation.py
import pandas as pd

def prepare_data(data_path):
    data = pd.read_csv(data_path)
    # Processamento básico
    data.dropna(inplace=True)
    return data