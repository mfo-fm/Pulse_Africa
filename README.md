# Pulse_Africa
As part of the recruitment process, this assessment was provided to evaluate my capabilities and approach to problem-solving. The task aims to demonstrate my skills in handling real-world data challenges.

# Assignment 2
# User Interaction Data Pipeline

## Overview
This project implements an ETL pipeline to process user interaction data from JSON files, transform it, and store it in PostgreSQL. It also includes a real-time ingestion system using Apache Kafka.

## Technologies Used
- Python (ETL processing)
- PostgreSQL (Data storage)
- Apache Kafka (Real-time ingestion)

## Setup Instructions

### 1️. Prerequisites  
- Install Python 3.12+  
- Install PostgreSQL and create a database  
- Install Apache Kafka and start the Kafka broker  

### 2️. Install Dependencies  
Run the following command to install required Python packages:  
pip install pandas psycopg2 kafka-python

### 3. Running the ETL Pipeline
To extract, transform, and load data:
python etl_pipeline.py

To start Kafka Producer:
python produce_messages.py

To start Kafka Consumer:
python consume_messages.py

### 4. Database Setup and Queries
Run the SQL_Scripts_task2 to create tables and partitions.
Run the SQL_Scripts_task3 to aggregate data & process queries.
Run the SQL_Scripts_task4 for Indexing, materialized views, and optimizations.
