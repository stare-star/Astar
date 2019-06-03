#@Time  : 2019/5/25 0025 17:10
#@Author: LYX
#@File  : airplane.py
from faker import Factory
from sqlalchemy import Column, String, Integer, Text,DateTime,Float
from CONF.config import url
from sqlalchemy import create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine(url)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
class Airplane(Base):
    __tablename__ = 'airplane'
    id = Column(Integer, primary_key=True)
    company = Column(String(255), nullable=True)
    number = Column(String(255), nullable=True)
    type = Column(String(255), nullable=True)
    start_time = Column(DateTime(255), nullable=False)
    start_whereCity = Column(String(255), nullable=False, index=True)
    arrive_whereCity = Column(String(255), nullable=False, index=True)
    start_where = Column(String(255), nullable=False, index=True)
    arrive_where = Column(String(255), nullable=False, index=True)
    arrive_time = Column(DateTime(255), nullable=False)
    price = Column(Integer, nullable=True)
    rate = Column(String(255), nullable=False)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.number)



Base.metadata.create_all(engine, checkfirst=True)

faker = Factory.create()
airplane = [Airplane(

    number=1,
    type =faker.name(),
company =faker.name(),
    start_time = '2019-05-30 12:00:00',
    arrive_whereCity = faker.name(),
    start_where =faker.name(),
    arrive_where = faker.name(),
    arrive_time = '2019-05-30 12:00:00',
    price =34,
    rate ='94% ' ) for _ in range(5)]
session.add_all(airplane)
session.commit()
