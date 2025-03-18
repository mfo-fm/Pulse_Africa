from kafka import KafkaProducer
import json
import os

#configuring Kafka
KAFKA_BROKER = "localhost:9092" 
TOPIC = "user_interactions"

#path to the JSON files
DATA_DIR = r'C:\Users\ADMIN\Desktop\Personal\Pulse_Assessment'

#Initializing Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

#This function sends each JSON record to Kafka
def produce_messages():
    for file in os.listdir(DATA_DIR):
        if file.endswith(".json"):
            with open(os.path.join(DATA_DIR, file), "r") as f:
                records = json.load(f)
                for record in (records if isinstance(records, list) else [records]):
                    producer.send(TOPIC, record)
                    print(f"Sent: {record}")

    producer.flush()

if __name__ == "__main__":
    produce_messages()
    print("Kafka Producer Finished Sending Messages.")
