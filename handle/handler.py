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

        print("데이터 저장 완료")

    def compare_from_db(self, data_list: list[Data]) -> list[Data]:
        new_data = []

        con, cur = self.db_connect()
        data = cur.execute(f"SELECT * FROM {self.__db_table_name} ORDER BY id DESC LIMIT 1").fetchall()

        if data:
            db_first_post_title = data[0][1]
        else:
            db_first_post_title = None

        for data in data_list:
            if data.title != db_first_post_title:
                new_data.append(data)

            else:
                break

        print("추가된 데이터 : ", new_data)

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
