#@Time  : 2019/5/23 0023 20:11
#@Author: LYX
#@File  : connect.py
from CONF.config import url
from sqlalchemy import create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
engine = create_engine(url)
Base = declarative_base()
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()