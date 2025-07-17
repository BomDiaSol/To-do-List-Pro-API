from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from environments import constants

connection_string = constants.DATABASE_URL
engine = create_engine(connection_string)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()