from sqlalchemy import Column, Integer, String, Date
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
    username = Column('username', String(200), nullable = False)
    password = Column('password', String(200), nullable = False)
    credits = Column('credits', Integer)
    practice_rank = Column('practice_rank', Integer)
    casual_rank = Column('casual_rank', Integer)
    date = Column('date', Date)

class Pracitce_context(Base):
    """
    practice_mode
    """

    __tablename__ = 'practice'
    __tabele_args__ = {
        'comment': 'ユーザー情報の投稿情報'
    }


    username = Column('username', String(200), nullable=False)
    number = Column('id', Integer, primary_key=True, autoincrement=True)    
    context = Column('context', String(500), nullable=False)
