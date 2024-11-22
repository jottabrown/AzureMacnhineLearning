import os
from argparse import ArgumentParser
from azureml.core import Workspace
from azureml.pipeline.core import Schedule, PipelineRun
from guardian.logger import Logger
from publish import authenticate

# Criando o Logger para mensagens
logger = Logger.get_logger(__name__)

def list_schedules(workspace: Workspace, schedule_name_filter=None):
    """List all active schedules in the Azure Machine Learning Workspace with detailed information."""
    logger.info("Listing active schedules in the workspace.")
    schedules = Schedule.list(workspace, active_only=True)
    
    # Filtro por nome
    if schedule_name_filter:
        schedules = [s for s in schedules if schedule_name_filter in s.name]

    print(f"{'-'*60}")
    print(f"Workspace Name:      {workspace.name}")
    print(f"Schedules Found:     {len(schedules)}")
    print(f"{'-'*60}")
    
    if not schedules:
        print("No schedules found matching the criteria.")
        return

    for schedule in schedules:
        print(f"Schedule Name:       {schedule.name}")
        print(f"Schedule ID:         {schedule.id}")
        print(f"Current Status:      {schedule.status}")
        
        # Verifica atributos opcionalmente disponíveis
        last_modified = getattr(schedule, 'updated_time', "Not available")
        print(f"Last Modified:       {last_modified}")
        
        pipeline_id = getattr(schedule, 'pipeline_id', "Not available")
        print(f"Pipeline ID:         {pipeline_id}")
        
        # Frequência e intervalo
        recurrence = schedule.recurrence
        if recurrence:
            print(f"Frequency:           {recurrence.frequency}")
            print(f"Interval:            {recurrence.interval}")
        else:
            print("Recurrence:          Not available")

        # Última execução do pipeline
        if pipeline_id and pipeline_id != "Not available":
            try:
                pipeline = workspace.pipelines.get(pipeline_id)
                runs = list(pipeline.get_runs())
                if runs:
                    print(f"Last Run Status:     {runs[0].status}")
                    print(f"Last Run Start Time: {runs[0].start_time}")
                    print(f"Last Run End Time:   {runs[0].end_time}")
                else:
                    print("Last Run:            No runs found for this pipeline.")
            except Exception as e:
                print(f"Error retrieving pipeline runs: {e}")
        else:
            print("Pipeline:            Not associated with any pipeline.")
        
        # Verifica tags
        tags = getattr(schedule, 'tags', "No tags available")
        print(f"Tags:                {tags}")
        print(f"{'-'*60}")

def main():
    parser = ArgumentParser(description="List all active schedules in the workspace")
    parser.add_argument(
        "--config",
        dest="cfg_path",
        type=str,
        required=False,
        default="../../../config.json",
    )
    parser.add_argument(
        "--name-filter",
        dest="name_filter",
        type=str,
        required=False,
        help="Filter schedules by name"
    )
    args = parser.parse_args()

    logger.info("Authenticating.")
    auth = authenticate()

    # Autenticando e carregando o Workspace
    ws = Workspace.from_config(auth=auth, path=args.cfg_path)
    
    # Listando os schedules ativos
    list_schedules(ws, schedule_name_filter=args.name_filter)


if __name__ == "__main__":
    main()
