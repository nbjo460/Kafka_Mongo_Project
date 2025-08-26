from datetime import datetime
from kafka import KafkaConsumer
import parameters as params
import threading
from dal import Dal

import json

dal = Dal()
def get_consumer_events(topic):
    # The consumer object contains the topic name, json deserializer,Kafka servers
    # and kafka time out in ms, Stops the iteration if no message after 1 sec
    consumer = KafkaConsumer(topic,
                             group_id='my-group',
                             value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                             bootstrap_servers=[f'{params.KAFKA_HOST}:{params.KAFKA_PORT}']
                             )
    return consumer


def print_messages(events):
    # Iterate through the messages
    interesting_messages = []
    not_interesting_messages = []

    for message in events:
        print(message.offset)
        timestamp = datetime.timestamp(datetime.now())
        message_json = {str(timestamp) :message.value}

        if message.topic == params.INTERESTING_COLLECTION:
            interesting_messages.append(message_json)
            dal.send_interesting(message_json)

        elif message.topic == params.NOT_INTERESTING_COLLECTION:
            not_interesting_messages.append(message_json)
            dal.send_not_interesting(message_json)

    # dal.send_messages(interesting_messages, not_interesting_messages)


def consumer_with_auto_commit(topic):
    """

    :param topic: Topic to consume message from
    :return:
    """
    #Create consumer object which consumes any message from the topic

    events = get_consumer_events(topic)
    print_messages(events)

# def listen():
#     t1 = threading.Thread(target=listen_interesting())
#     t2 = threading.Thread(target=listen_not_interesting())
#
#     t1.start()
#     t2.start()

def listen_interesting():
    print("listen to interesting messages")
    consumer_with_auto_commit(params.INTERESTING_COLLECTION)

def listen_not_interesting():
    print("listen to not interesting messages")
    consumer_with_auto_commit(params.NOT_INTERESTING_COLLECTION)
