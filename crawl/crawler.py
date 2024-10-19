import os

import requests
import json
from handle import handler
from dotenv import load_dotenv
from entity.data import Data


class Crawler():

    def __init__(self, url: str, class_name: str):
        self.__url = url
        self.__class = class_name

    def run(self) -> list[Data]:
        """
        크롤링을 시작하여 25개의 게시글 데이터 반환
        """

        response = requests.get(self.__url)
        json_data_list = response.json()["content"]["feeds"]

        data_list = []

        # json_data_list는 크롤링한 게시글 25개
        for json_data in json_data_list:

            title = json_data['feed']['title']
            url = json_data["feedLink"]["mobile"]

            # contents는 순회하면서 값을 가져오지만, 없는 곳도 있어서 예외처리
            contents = ""

            try:
                for data in json.loads(json_data['feed']["contents"])["document"]["components"][1]["value"]:
                    contents += data['nodes'][0]['value']
            except:
                pass

            data_list.append(Data(title, contents, url))

        return data_list
