from sqlalchemy.orm import sessionmaker
import sqlalchemy as db
import json

import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(__location__ + '/config.json', "r")
config = json.loads(f.read())


def get_db_engine(key):
    try:
        if config[key]:
            url = config[key]
            datamart_engine = db.create_engine(url)
            datamart_engine.connect()
            print("Successfully connected to db")
            return datamart_engine
        else:
            print("Keep data_mart_url in config variables")
    except Exception as e:
        print("Unable to connect to db:: " + repr(e))


db_engine = get_db_engine('url')


def get_db_session():
    return sessionmaker(bind=db_engine)()


def get_db_engine():
    return db_engine
