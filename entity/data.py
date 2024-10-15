class Data:
    def __init__(self, title, contents, url):
        self.__title: str = title
        self.__contents: str = contents
        self.__url: str = url

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title):
        self.title = new_title

    @property
    def contents(self):
        return self.__contents

    @contents.setter
    def contents(self, new_contents):
        self.__contents = new_contents

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, new_url):
        self.__url = new_url


