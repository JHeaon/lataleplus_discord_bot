from abc import ABC, abstractmethod
import sqlite3
from entity.data import Data


class Handler(ABC):

    def __init__(self, file_address, db_table_name):
        self.__file_address = file_address
        self.__db_table_name = db_table_name

    def save(self, data_list: list[Data]):

        if not data_list:
            return

        con, cur = self.db_connect()

        for event_data in data_list[::-1]:
            cur.execute(f"INSERT INTO {self.__db_table_name} (title, contents, url) VALUES (?, ?, ?)",
                        (event_data.title, event_data.contents, event_data.url))

        con.commit()
        con.close()

    def compare_from_db(self, data_list: list[Data]) -> list[Data]:

        con, cur = self.db_connect()

        # 한번 크롤링 하면 25개의 데이터만 가져옴
        # db에서 25개의 데이터와 현재 받은 데이터를 비교하여 새로 올라온 게시글을 필터링 처리함

        db_data_list = cur.execute(f"SELECT * FROM {self.__db_table_name} ORDER BY id DESC LIMIT 25").fetchall()
        if db_data_list:
            db_data_list = [Data(data[1], data[2], data[3]) for data in db_data_list]
        else:
            return data_list

        new_data = list(filter(lambda data: (data.title not in [db_data.title for db_data in db_data_list]), data_list))

        return new_data

    def db_connect(self):
        con = sqlite3.connect(f'{self.file_address}')
        cur = con.cursor()
        return con, cur

    @property
    def file_address(self):
        return self.__file_address

    @file_address.setter
    def file_address(self, new_file_address):
        self.__file_address = new_file_address
