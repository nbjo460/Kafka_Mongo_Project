import os
import routes
import uvicorn
import consumer
import threading

app = routes.app

def uvicorn_start():
    uvicorn.run("main:app", host="0.0.0.0", port=PORT)
def listen_not_interesting():
    consumer.listen_interesting()
def listen_interesting():
    consumer.listen_not_interesting()

if __name__ == "__main__":
    PORT = int(os.getenv("PORT", 8000))

    t1 = threading.Thread(target=uvicorn_start)
    t2 = threading.Thread(target=listen_interesting)
    t3 = threading.Thread(target=listen_not_interesting)

    t1.start()
    t2.start()
    t3.start()