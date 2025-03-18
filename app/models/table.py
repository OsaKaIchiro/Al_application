<<<<<<< HEAD
from sqlalchemy import Column, Integer, String, Date
=======
from sqlalchemy import Column, Integer, String, Float, DateTime
>>>>>>> photo_add
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
<<<<<<< HEAD
    username = Column('username', String(200), nullable = False)
    password = Column('password', String(200), nullable = False)
    credits = Column('credits', Integer)
    practice_rank = Column('practice_rank', Integer)
    casual_rank = Column('casual_rank', Integer)
    date = Column('date', Date)
=======
    username = Column('username', String(200))
    password = Column('password', String(200))
>>>>>>> photo_add

