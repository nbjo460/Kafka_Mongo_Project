import os

INTERESTING_COLLECTION = "Interesting"
NOT_INTERESTING_COLLECTION = "NotInteresting"
KAFKA_PORT = os.getenv("KAFKA_PORT", 9092)
KAFKA_HOST = os.getenv("KAFKA_HOST", "localhost")