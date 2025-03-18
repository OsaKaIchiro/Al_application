from sqlalchemy import Column, Integer, String, DateTime, Date
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
    username = Column('username', String(200), nullable = False, unique=True)
    password = Column('password', String(200), nullable = False)
    credits = Column('credits', Integer)
    practice_rank = Column('practice_rank', Integer)
    casual_rank = Column('casual_rank', Integer)
    date = Column('date', Date)


