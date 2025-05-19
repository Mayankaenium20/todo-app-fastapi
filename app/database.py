import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

engine = create_engine(DATABASE_URL)                    #handles the low level db coms

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)             #provides a medium for the fast api to communicate with the db:
#bind: handle low level db operations via the session
#autoflush: changes aren't inflicted unless told to do so.
#autocommit: saving all changes perm

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()