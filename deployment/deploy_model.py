# deploy_model.py
from azureml.core import Workspace, Model
from azureml.core.webservice import AciWebservice, Webservice
from azureml.core.model import InferenceConfig
import os

def deploy_model(model_path, service_name="ml-service"):
    ws = Workspace.from_config()

    # Registro do modelo
    model = Model.register(workspace=ws, model_name="modelo_ml", model_path=model_path)

    # Configuração de inferência
    inference_config = InferenceConfig(runtime="python", entry_script="score.py")

    # Configuração do serviço
    aci_config = AciWebservice.deploy_configuration(cpu_cores=1, memory_gb=1)

    # Deploy do modelo
    service = Model.deploy(workspace=ws, name=service_name, models=[model], inference_config=inference_config, deployment_config=aci_config)
    service.wait_for_deployment(show_output=True)
    print(f"Modelo implantado em {service.scoring_uri}")

# Teste
if __name__ == "__main__":
    deploy_model("model-training/model.pkl")
