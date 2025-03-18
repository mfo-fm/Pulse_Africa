from kafka import KafkaConsumer
import json
import psycopg2

#configuring Kafka
KAFKA_BROKER = "localhost:9092"
TOPIC = "user_interactions"

#My Database Connection Parameters
DB_PARAMS = {
    "dbname": "postgres",
    "user": "farouqo",
    "password": "**********",
    "host": "localhost",
    "port": "5432"
}

#Initializing Kafka Consumer
consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=KAFKA_BROKER,
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    auto_offset_reset="earliest",
    enable_auto_commit=True,
)

#This function processes the messages and inserts into PostgreSQL
def consume_messages():
    conn = psycopg2.connect(**DB_PARAMS)
    cursor = conn.cursor()
    
    insert_query = """
    INSERT INTO user_interactions (user_id, timestamp, page_url, action, device_type, referrer, session_id)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (user_id, timestamp) DO NOTHING;
    """

    for message in consumer:
        record = message.value
        cursor.execute(insert_query, (
            record["user_id"], record["timestamp"], record["page_url"],
            record["action"], record["device_type"], record["referrer"], record["session_id"]
        ))
        conn.commit()
        print(f"Inserted: {record}")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    consume_messages()
