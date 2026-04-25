from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys

sys.path.append('/opt/airflow')

from scripts.extract import main as extract_main
from scripts.transform import main as transform_main
from scripts.load import main as load_main

default_args = {
    "start_date": datetime(2024, 1, 1),
    "retries": 1
}

with DAG(
    dag_id="crypto_etl_pipeline",
    default_args=default_args,
    schedule_interval="*/5 * * * *",
    catchup=False
) as dag:

    extract_task = PythonOperator(
        task_id="extract",
        python_callable=extract_main
    )

    transform_task = PythonOperator(
        task_id="transform",
        python_callable=transform_main
    )

    load_task = PythonOperator(
        task_id="load",
        python_callable=load_main
    )

    extract_task >> transform_task >> load_task
