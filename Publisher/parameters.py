import os

INTERESTING_COLLECTION = "interesting"
NOT_INTERESTING_COLLECTION = "not_interesting"
KAFKA_PORT = os.getenv("KAFKA_PORT", 9092)
KAFKA_HOST = os.getenv("KAFKA_HOST", "localhost")
SELF_PORT = os.getenv("SELF_PORT", 8001)
