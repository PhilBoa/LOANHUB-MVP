import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

load_dotenv()


DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_NAME_TEST = os.getenv("DB_NAME_TEST")

if os.environ.get("FLASK_ENV") == "test":
    DB_URI = f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME_TEST}"
else:
    DB_URI = f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


engine = create_engine(DB_URI)


def init_db(base):
    '''Creates the database tables'''
    base.metadata.create_all(engine)


def session():
    '''
    Creates a new SQLAlchemy session.

    Returns:
    session (sqlalchemy.orm.Session): A new SQLAlchemy session.
    '''
    Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
    session_factory = scoped_session(Session)
    session = session_factory()
    return session
