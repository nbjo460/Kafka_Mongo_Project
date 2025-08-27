from datetime import datetime
from kafka import KafkaConsumer
import parameters as params
from dal import Dal
import json

class Consumer:
    def __init__(self):
        self.dal = Dal()
        self.TOPIC = params.KAFKA_TOPIC

    def get_consumer_events(self):
        # The consumer object contains the topic name, json deserializer,Kafka servers
        # and kafka time out in ms, Stops the iteration if no message after 1 sec
        consumer = KafkaConsumer(self.TOPIC,
                                 group_id='my-group',
                                 value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                                 bootstrap_servers=[f'{params.KAFKA_HOST}:{params.KAFKA_PORT}']
                                 )
        return consumer


    def processor_messages(self, events):
        # Iterate through the messages
        for message in events:
            print(message.offset)
            timestamp = datetime.timestamp(datetime.now())
            message_json = {str(timestamp) :message.value}
            self.dal.send_message(message_json)


    def consumer_with_auto_commit(self):
        """

        :param topic: Topic to consume message from
        :return:
        """
        #Create consumer object which consumes any message from the topic

        events = self.get_consumer_events()
        self.processor_messages(events)

    def listen_messages(self):
        print(f"listen to {self.TOPIC} messages")
        self.consumer_with_auto_commit()

