from sklearn.datasets import fetch_20newsgroups
import producer

class NewsGroups:
    def __init__(self):
        self.interesting_categories=['alt.atheism',
         'comp.graphics',
         'comp.os.ms-windows.misc',
         'comp.sys.ibm.pc.hardware',
         'comp.sys.mac.hardware',
         'comp.windows.x',
         'misc.forsale',
         'rec.autos',
         'rec.motorcycles',
         'rec.sport.baseball']

        self.not_interesting_categories=['rec.sport.hockey',
         'sci.crypt',
         'sci.electronics',
         'sci.med',
         'sci.space',
         'soc.religion.christian',
         'talk.politics.guns',
         'talk.politics.mideast',
         'talk.politics.misc',
         'talk.religion.misc']

        self.newsgroups_interesting=fetch_20newsgroups(subset='all',categories=self.interesting_categories)
        self.newsgroups_not_interesting=fetch_20newsgroups(subset='all',categories=self.not_interesting_categories)

        self.interesting_news_length = len (self.newsgroups_interesting.data)
        self.not_interesting_news_length = len (self.newsgroups_not_interesting.data)

        # to allow send different num of news
        # self.index_interesting_news = 0
        # self.index_not_interesting_news = 0

        self.index_news = 0

    def send_news(self, news_num : int):
        index = 0
        for i in range(self.index_news ,news_num+self.index_news):
            if i < self.interesting_news_length and i < self.not_interesting_news_length:
                producer.send_interesting_message(self.newsgroups_interesting.data[i])
                producer.send_not_interesting_message(self.newsgroups_not_interesting.data[i])
                index = i
            else:
                break
        self.index_news += index

        print(f"Sent {news_num*2} news to the server.")




