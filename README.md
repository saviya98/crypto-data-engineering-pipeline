**Crypto Data Engineering Pipeline (Airflow + Docker + PostgreSQL)**

This project is an end-to-end data engineering pipeline that extracts cryptocurrency data, transforms it using Python, and loads it into a PostgreSQL database. The workflow is fully orchestrated using Apache Airflow and containerized using Docker for production-like reliability.

**Architecture**

Crypto API ------> Extract Script -----> Transform (Pandas) -----> Airflow DAG(Orchestrator) -----> PostgreSQL DB -----> Analysis / SQL 


**Tech Stack**

Python 
Apache Airflow
Docker
PostgreSQL
Pandas

**Pipeline Flow**

1.Extract crypto data from API
2.Transform data using Pandas
3.Load into PostgreSQL
4.Orchestrate using Airflow DAG
5.Run every 5 minutes (scheduled workflow)


