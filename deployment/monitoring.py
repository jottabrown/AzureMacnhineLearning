# monitoring.py
from azureml.core import Webservice, Workspace
import requests

def monitor_service(service_name):
    ws = Workspace.from_config()
    service = Webservice(workspace=ws, name=service_name)
    uri = service.scoring_uri

    # Exemplo de chamada para o endpoint
    data = {"input_data": [[5.1, 3.5, 1.4, 0.2]]}
    headers = {'Content-Type': 'application/json'}

    response = requests.post(uri, json=data, headers=headers)
    print("Resposta do modelo:", response.json())

# Teste
if __name__ == "__main__":
    monitor_service("ml-service")
