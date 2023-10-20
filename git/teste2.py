from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Defina os parâmetros da DAG
default_args = {
    'owner': 'Thiago Cordeiro',
    'start_date': datetime(2023, 10, 20),
}

# Crie a DAG
dag = DAG('teste_dag', default_args=default_args, schedule_interval=None)

# Define a função a ser executada pela tarefa
def print_hello():
    print("Olá, esta é uma DAG de teste!teste!teste!")

# Cria uma tarefa que executa a função acima
hello_task = PythonOperator(
    task_id='teste de deg github',
    python_callable=print_hello,
    dag=dag,
)

# Garanta a ordem das tarefas
hello_task
