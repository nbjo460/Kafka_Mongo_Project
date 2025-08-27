import os


SELF_PORT = os.getenv("SELF_PORT", 8000)

KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "")
KAFKA_PORT = os.getenv("KAFKA_PORT", 9092)
KAFKA_HOST = os.getenv("KAFKA_HOST", "localhost")
MONGO_USER = os.getenv("MONGO_USER", "root")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD", "menachemYarhi")
MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_PORT = os.getenv("MONGO_PORT", 27017)
MONGO_URI = os.getenv("MONGO_URI", f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}")
MONGO_DBNAME = os.getenv("MONGO_DBNAME", "KafkaTest")