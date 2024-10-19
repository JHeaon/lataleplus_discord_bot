import os

from sqlalchemy import Column, Integer, String, create_engine, text, select
from sqlalchemy.orm import declarative_base, sessionmaker

# db 연결을 위한 engine
engine = create_engine(f"postgresql:///{os.environ.get("DB")}")

# 모델 생성을 위한 세팅
Base = declarative_base()


class Data(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    contents = Column(String)
    url = Column(String)


class Announcement(Data):
    __tablename__ = "announcement"


class DeveloperNote(Data):
    __tablename__ = "developer_note"


class Event(Data):
    __tablename__ = "event"


class EventWinner(Data):
    __tablename__ = "event_winner"


class FreeBulletInBoard(Data):
    __tablename__ = "free_bullet_in_board"


class InspectionUpdate(Data):
    __tablename__ = "inspection_update"


def get_session():
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(engine)
