#@Time  : 2019/5/23 0023 20:11
#@Author: LYX
#@File  : connect.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from CONF.config import url

engine = create_engine(url)
Base = declarative_base()
# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()