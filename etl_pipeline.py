import os
import json
import pandas as pd
import psycopg2
from psycopg2 import sql

#My Database Connection Parameters
DB_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "farouqo"
DB_PASSWORD = "**********"
DB_PORT = "5432"

#path to the JSON files
DATA_DIR = r'C:\Users\ADMIN\Desktop\Personal\Pulse_Assessment'

def connect_db():
    return psycopg2.connect(
        host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD, port=DB_PORT
    )

#Extraction Function: Here I am reading multiple JSON files and loading them into a DataFrame
def extract_data():
    data = []
    for file in os.listdir(DATA_DIR):
        if file.endswith(".json"):
            with open(os.path.join(DATA_DIR, file), "r") as f:
                records = json.load(f)
                data.extend(records if isinstance(records, list) else [records])
    return pd.DataFrame(data)

#Transform Func: Cleaning and structuring the data
def transform_data(df):
    df.dropna(inplace=True)  #Removing missing values
    df["timestamp"] = pd.to_datetime(df["timestamp"])  #Convert timestamp
    return df

#Load Function
def load_data(df):
    conn = connect_db()
    cursor = conn.cursor()
    insert_query = sql.SQL(
        """
        INSERT INTO user_interactions (user_id, timestamp, page_url, action, device_type, referrer, session_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (user_id, timestamp) DO NOTHING;
        """
    )
    for _, row in df.iterrows():
        cursor.execute(insert_query, tuple(row))
    conn.commit()
    cursor.close()
    conn.close()

def run_pipeline():
    df = extract_data()
    df = transform_data(df)
    load_data(df)
    print("ETL Process Completed Successfully!")

if __name__ == "__main__":
    run_pipeline()
