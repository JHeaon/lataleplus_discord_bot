from abc import ABC, abstractmethod


class Notifier(ABC):
    def __init__(self, url):
        self.url: str = url

    @abstractmethod
    def push(self, data_list):
        pass



