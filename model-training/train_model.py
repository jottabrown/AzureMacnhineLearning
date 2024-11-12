# train_model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

def train_model(data_path, model_output_path="model.pkl"):
    """
    Treina um modelo Random Forest.
    - data_path: Caminho para os dados preparados (arquivo CSV).
    - model_output_path: Caminho para salvar o modelo treinado.
    """
    # Carregar os dados
    data = pd.read_csv(data_path)
    X = data.drop("target", axis=1)
    y = data["target"]

    # Dividir os dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Treinar o modelo
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Avaliar o modelo
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Acurácia do modelo: {accuracy:.2f}")

    # Salvar o modelo
    joblib.dump(model, model_output_path)
    print(f"Modelo salvo em {model_output_path}")

# Teste
if __name__ == "__main__":
    train_model("caminho_para_seus_dados.csv")
