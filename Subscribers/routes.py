import fastapi

from dal import Dal

app = fastapi.FastAPI()



dal = Dal()

@app.get("/")
def root():
    return {"status" : "HELLO"}
@app.get("/get-interesting")
def load_interesting():
    """
    In route: "/get-interesting", load the interesting messages.
    :return: json
    """
    return dal.get_all_messages_interesting()

@app.get("/get-not-interesting")
def load_not_interesting():
    """
    In route: "/get-not-interesting", load the not interesting messages.
    :return: json
    """
    return dal.get_all_messages_not_interesting()

