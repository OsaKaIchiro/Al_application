from sqlalchemy import Column, Integer, String, Float, DateTime
from app.db import Base


class User(Base):
    """
    ユーザモデル
    """

    __tablename__ = 'users'
    __table_args__ = {
        'comment': 'ユーザー情報のマスターテーブル'
    }

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    username = Column('username', String(200))
    password = Column('password', String(200))

