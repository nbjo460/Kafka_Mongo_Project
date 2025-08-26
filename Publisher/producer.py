"""
This file contains the sample code which publishes message to the Kafka brokers.

1. publish_message function pushes the message to the topic
2. publish_message_with_key pushes the message with key

"""

# Import all the required packages
import json
from kafka import KafkaProducer
import parameters as params

def get_producer_config():
    # The Producer object requires the Kafka server, Json serializer
    url = f'{params.KAFKA_HOST}:{params.KAFKA_PORT}'
    produce = KafkaProducer(bootstrap_servers=[url],
                             value_serializer=lambda x:
                             json.dumps(x).encode('utf-8'))
    return produce

# Publish json messages
def publish_message(producer, topic, message):
    """
    This function will publish message to the topic which is received as a parameter
    :param producer: producer object to publish the message to Kafka servers
    :param topic: The topic to which the message will be published
    :param message: The event message
    :return: None
    """
    producer.send(topic, message)


# Publish json messages with key
def publish_message_with_key(producer,topic,key,message):
    """

    :param producer: producer object to publish the message to Kafka servers
    :param topic: The topic to which the message will be published
    :param key: The key to enable hashed partitioning
    :param message: The event message
    :return: None
    """
    producer.send(topic, key=key, value=message)

def send_interesting_message(message):
    produce = get_producer_config()
    publish_message(produce, params.INTERESTING_COLLECTION, message)
    produce.flush()

def send_not_interesting_message(message):
    produce = get_producer_config()
    publish_message(produce, params.NOT_INTERESTING_COLLECTION, message)
    produce.flush()

if __name__ == '__main__':

    # Create the producer object with basic configurations
    producer = get_producer_config()

    #Publish message to a topic

    #Publish message to a topic with key to enable hashed partitioning
    publish_message_with_key(get_producer_config(),"topic1",b"client1", {3:3})

    # block until all async messages are sent
    producer.flush()