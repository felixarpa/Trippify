from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from src import *


def connect(user, password, database, host, port):
    url_string = 'postgresql://{}:{}@{}:{}/{}'
    url = url_string.format(user, password, host, port, database)
    _engine = create_engine(url, client_encoding='utf8')
    _meta = MetaData(bind=_engine, reflect=True)
    return _engine, _meta


# Connect to the database.
engine, meta = connect(TRIPPIFY_DB_USER, TRIPPIFY_DB_PASSWORD, TRIPPIFY_DB_DB, TRIPPIFY_DB_HOST, TRIPPIFY_DB_PORT)
db_session = scoped_session(sessionmaker(bind=engine))

# Declare base.
Base = declarative_base()
Base.query = db_session.query_property()
