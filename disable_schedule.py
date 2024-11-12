import os
from azureml.core import Workspace
from azureml.pipeline.core import Schedule
from guardian.logger import Logger
from publish import authenticate

# Criando o Logger para mensagens
logger = Logger.get_logger(__name__)

def disable_schedules(workspace: Workspace, schedule_ids: list):
    """Disable the schedules based on provided schedule IDs."""
    for schedule_id in schedule_ids:
        try:
            logger.info(f"Attempting to disable schedule with ID: {schedule_id}")
            schedule = Schedule.get(workspace, id=schedule_id)
            schedule.disable()
            logger.info(f"Successfully disabled schedule: {schedule_id}")
        except Exception as e:
            logger.error(f"Failed to disable schedule {schedule_id}: {str(e)}")

def main():
    logger.info("Authenticating.")
    auth = authenticate()

    # Autenticando e carregando o Workspace
    ws = Workspace.from_config(auth=auth, path="../../../config.json")
    
    # IDs dos schedules a serem desabilitados
    schedule_ids = [
        "ce876683-11b8-4e75-a7e1-574cbb12efa6",
        "6515a001-1d06-4fac-9256-f88be729b805"
    ]
    
    # Desabilitando os schedules
    disable_schedules(ws, schedule_ids)

if __name__ == "__main__":
    main()
