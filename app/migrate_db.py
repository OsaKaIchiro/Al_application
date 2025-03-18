from sqlalchemy import create_engine, MetaData, Table, text
from sqlalchemy.orm import sessionmaker
from app.models.table import Base

DB_URL = "mysql+pymysql://root@db:3306/demo?charset=utf8"
engine = create_engine(DB_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def drop_foreign_keys():
    conn = engine.connect()
    metadata = MetaData()
    metadata.reflect(bind=conn)
    practice_table = Table('practice', metadata, autoload_with=conn)
    for fk in practice_table.foreign_keys:
        conn.execute(text(f"ALTER TABLE practice DROP FOREIGN KEY {fk.constraint.name}"))
    conn.close()

def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    drop_foreign_keys()
    reset_database()