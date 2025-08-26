import fastapi
from newsgroups import NewsGroups


app = fastapi.FastAPI()
news_manager = NewsGroups()
@app.get("/")
def root():
    return {"status" : "HELLO"}

@app.get("/submit-message/{news_num}")
def submit_message(news_num):
    """
    For load the data.
    :return:
    """
    news_num = int(news_num)
    news_manager.send_news(news_num)
    return {"status" : f"Succeed submit {news_num*2} news."}
