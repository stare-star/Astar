#@Time  : 2019/5/25 0025 20:35
#@Author: LYX
#@File  : bus.py


import random
from faker import Factory
from CONF.config import url

from sqlalchemy import create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import sessionmaker, relationship


engine = create_engine(url)
Base = declarative_base()

class Bus(Base):
    __tablename__ = 'bus'

    id = Column(Integer, primary_key=True)
    start_whereCity = Column(String(255), nullable=False, index=True)
    start_where= Column(String(255), nullable=False, index=True)
    arrive_whereCity = Column(String(255), nullable=False, index=True)
    arrive_where = Column(String(255), nullable=False)
    date = Column(String(255), nullable=False)
    price = Column(Integer, nullable=True)
    start_time = Column(String(255), nullable=False)



Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
faker = Factory.create()

bus = Bus(

    start_time = '2019-05-30 12:00:00',
    start_where='2019-05-30 12:00:00',
    arrive_whereCity = '2019-05-30 12:00:00',start_whereCity = '2019-05jhj-30 12:00:00',
    arrive_where ='123',
    date='123',
    price =34,
     )
session.add(bus)
session.commit()
