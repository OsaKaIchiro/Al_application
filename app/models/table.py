
from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime
from sqlalchemy.orm import relationship
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
    username = Column('username', String(200), nullable = False, unique=True)
    password = Column('password', String(200), nullable = False)
    credits = Column('credits', Integer)
    practice_rank = Column('practice_rank', Integer)
    casual_rank = Column('casual_rank', Integer)
    date = Column('date', Date)

    # Relationship to Practice_context
    practices = relationship("Practice_context", back_populates="user")


class Practice_context(Base):
    """
    practice_mode
    """

    __tablename__ = 'practice'
    __table_args__ = {
        'comment': 'ユーザー情報の投稿情報'
    }

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    username = Column('username', String(200), ForeignKey('users.username'), nullable=False)
    context = Column('context', String(500), nullable=False)

    # Relationship to User
    user = relationship("User", back_populates="practices")



