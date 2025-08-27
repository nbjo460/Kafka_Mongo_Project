import os
import routes
import uvicorn
from consumer import Consumer
import threading
import parameters as params

app = routes.app
consumer = Consumer()

def uvicorn_start():
    uvicorn.run("main:app", host="0.0.0.0", port=PORT)
def listen_topic():
    consumer.listen_messages()
if __name__ == "__main__":
    PORT = int(params.SELF_PORT)

    t1 = threading.Thread(target=uvicorn_start)
    t2 = threading.Thread(target=listen_topic)

    t1.start()
    t2.start()
