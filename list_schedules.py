import os
from argparse import ArgumentParser
from azureml.core import Workspace
from azureml.pipeline.core import Schedule
from guardian.logger import Logger
from publish import authenticate

# Criando o Logger para mensagens
logger = Logger.get_logger(__name__)

def list_schedules(workspace: Workspace):
    """List all active schedules in the Azure Machine Learning Workspace."""
    logger.info("Listing all active schedules in the workspace.")
    schedules = Schedule.list(workspace, active_only=True)
    
    if not schedules:
        logger.info("No active schedules found in the workspace.")
    else:
        for schedule in schedules:
            logger.info(f"Schedule Name: {schedule.name}")
            logger.info(f"Schedule ID: {schedule.id}")
            logger.info(f"Status: {schedule.status}")
            logger.info(f"Description: {schedule.description}")
            logger.info("-" * 40)


def main():
    parser = ArgumentParser(description="List all active schedules in the workspace")
    parser.add_argument(
        "--config",
        dest="cfg_path",
        type=str,
        required=False,
        default="../../../config.json",
    )
    args = parser.parse_args()

    logger.info("Authenticating.")
    auth = authenticate()

    # Autenticando e carregando o Workspace
    ws = Workspace.from_config(auth=auth, path=args.cfg_path)
    
    # Listando os schedules ativos
    list_schedules(ws)


if __name__ == "__main__":
    main()
