from datetime import datetime
from kafka import KafkaConsumer
import parameters as params
from dal import Dal

import json

dal = Dal()
def get_consumer_events(topic):
    # logging.info("Creating Consumer Object ..")
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
    for message in events:
        timestamp = datetime.timestamp(datetime.now())
        message_json = {timestamp :message.value}

        if message.topic == params.INTERESTING_COLLECTION:
            dal.send_interesting(message_json)
        elif message.topic == params.NOT_INTERESTING_COLLECTION:
            dal.send_not_interesting(message_json)



def consumer_with_auto_commit(topic):
    """

    :param topic: Topic to consume message from
    :return:
    """
    #Create consumer object which consumes any message from the topic

    events = get_consumer_events(topic)
    print_messages(events)

if __name__ == '__main__':
    consumer_with_auto_commit(params.INTERESTING_COLLECTION)
    consumer_with_auto_commit(params.NOT_INTERESTING_COLLECTION)
