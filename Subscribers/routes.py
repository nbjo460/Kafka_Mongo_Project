import fastapi

app = fastapi.FastAPI()


class Routes:
    def __init__(self):
        pass
    @app.get("/")
    def root(self):
        return {}
    @app.get("/load")
    def load_db(self):
        """
        For load the data.
        :return:
        """
        return Manager().get_data()
