from crawl.crawler import Crawler
from handle.handler import Handler
from notify.notifier import Notifier


class Monitor():

    def __init__(self, crawler: Crawler, handler: Handler, notifier: Notifier):
        self.crawler = crawler
        self.handler = handler
        self.notifier = notifier

    def run(self):
        crawling_data = self.crawler.run()
        print(f"crawling data : ", crawling_data)

        new_data = self.handler.compare_from_db(crawling_data)
        print(f"new data: ", new_data)

        if new_data:
            self.handler.save(new_data)
            self.notifier.push(new_data)
