import requests
import json
from entity.data import Data
from dotenv import load_dotenv

load_dotenv()


class Crawler():

    def __init__(self, url: str):
        self.__url: str = url

    def run(self) -> list[Data]:
        events_data_list: list[Data] = []

        response = requests.get(self.__url)
        events = response.json()["content"]["feeds"]

        for event in events:
            title = event['feed']['title']
            url = event["feedLink"]["mobile"]
            contents = ""

            try:
                for data in json.loads(event['feed']["contents"])["document"]["components"][1]["value"]:
                    contents += data['nodes'][0]['value']
            except:
                pass

            events_data_list.append(Data(title, contents, url))

        return events_data_list
