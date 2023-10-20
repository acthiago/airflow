from airflow import DAG
from airflow.providers.git.operators.git_clone import GitCloneOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Defina os parâmetros da DAG
default_args = {
    'owner': 'seu_nome',
    'start_date': datetime(2023, 10, 20),
    'retries': 1,
}

# Crie a DAG
dag = DAG('azure_devops_test', default_args=default_args, schedule_interval=None)

# Define a função a ser executada após a clonagem do repositório
def list_files_in_directory(repo_path, **kwargs):
    import os
    file_list = os.listdir(repo_path)
    for file in file_list:
        print(f'Arquivo no diretório: {file}')

# Cria um operador para clonar o repositório Git do Azure DevOps
git_clone_task = GitCloneOperator(
    task_id='git_clone_task',
    repo_url='URL_do_repositório_git',
    target_directory='/tmp/cloned_repo',
    branch='main',  # Nome da branch que você deseja clonar
    dag=dag,
)

# Cria um operador para listar os arquivos no diretório clonado
list_files_task = PythonOperator(
    task_id='list_files_task',
    python_callable=list_files_in_directory,
    op_args=['/tmp/cloned_repo'],  # Diretório clonado
    provide_context=True,
    dag=dag,
)

# Define a ordem das tarefas
git_clone_task >> list_files_task
