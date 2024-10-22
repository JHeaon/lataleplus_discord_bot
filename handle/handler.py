from abc import ABC
from db import schema
from entity.data import Data
from sqlalchemy.orm import Session


class Handler(ABC):
    def __init__(self, class_name: str):
        self.class_name = class_name

    def save(self, data_list: list[Data]):

        with schema.get_session()() as db:
            # 데이터 베이스에는 역순으로 저장되어야 함.
            for data in data_list[::-1]:
                obj = getattr(schema, self.class_name)(title=data.title, contents=data.contents, url=data.url)
                db.add(obj)

            db.commit()

    def compare_from_db(self, data_list: list[Data]) -> list[Data]:
        session = schema.get_session()

        # 최신 데이터 25개를 가져온다.
        with schema.get_session()() as db:
            obj = getattr(schema, self.class_name)
            db_data_list = db.query(obj).order_by(obj.id.desc()).limit(50).all()

        new_data = []
        db_titles = [db_data.title for db_data in db_data_list]

        if db_data_list is None:
            new_data = data_list
            return new_data

        for crawling_data in data_list:
            if crawling_data.title not in db_titles:
                new_data.append(crawling_data)

        return new_data
