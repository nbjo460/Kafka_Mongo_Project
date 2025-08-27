import fastapi

from dal import Dal

app = fastapi.FastAPI()



dal = Dal()

@app.get("/")
def root():
    return {"status" : "HELLO"}
@app.get("/get-messages")
def load_interesting():
    """
    In route: "/get-interesting", load the messages.
    :return: json
    """
    return dal.get_all_messages()

