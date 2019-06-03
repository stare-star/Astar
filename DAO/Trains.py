# coding: utf-8

import random
from faker import Factory

from sqlalchemy import create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import sessionmaker, relationship
from DAO.connect import Base, engine


class Train(Base):
    __tablename__ = 'trains'

    id = Column(Integer, primary_key=True)
    number = Column(String(255), nullable=False, index=True)
    start_time = Column(String(255), nullable=False)
    time = Column(String(255), nullable=False)
    arrive_time = Column(String(255), nullable=False)
    start_where = Column(String(255), nullable=False)
    arrive_where = Column(String(255), nullable=False)
    price = Column(Integer, nullable=True)
    date = Column(String(255), nullable=False)
    arrive_where_city= Column(String(255), nullable=False)
    start_where_city= Column(String(255), nullable=False)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.number)





def get_route(DateStart, DateEnd, station):
    Session = sessionmaker(bind=engine)
    session = Session()
    query = (session
             .query(Train)
             .filter(Train.date >= DateStart)
             .filter(Train.date <= DateEnd)
             .filter_by(start_where=station)
             .limit(10000)
             .offset(0).all()
             )
    session.close()
    # for i in query:
    return query
def get_price(id):
    Session = sessionmaker(bind=engine)
    session = Session()
    query = (session
             .query(Train)
             .filter(Train.id==id)
             .all()
             )
    session.close()
    # for i in query:
    return query

# session.commit()
if __name__ == '__main__':
    print((get_route(20190528, 20190530, "长春站"))[0].arrive_time)
    # print(get_price(1)[0].price)
