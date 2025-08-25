import fastapi
from dal import Dal

app = fastapi.FastAPI()


class Routes:
    def __init__(self):
        self.dal = Dal()

    @app.get("/")
    def root(self):
        return {"status" : "HELLO"}
    @app.get("/get-interesting")
    def load_interesting(self):
        """
        In route: "/get-interesting", load the interesting messages.
        :return: json
        """
        return self.dal.get_all_messages_interesting()

    @app.get("/get-not-interesting")
    def load_not_interesting(self):
        """
        In route: "/get-not-interesting", load the not interesting messages.
        :return: json
        """
        return self.dal.get_all_messages_not_interesting()
