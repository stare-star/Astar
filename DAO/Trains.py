# coding: utf-8

import random
from faker import Factory

from sqlalchemy import create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from utils import logger
from sqlalchemy import Column, String, Integer, Text, DateTime
from sqlalchemy.orm import sessionmaker, relationship
from DAO.connect import Base, engine


class Train(Base):
    __tablename__ = 'trains'

    id = Column(Integer, primary_key=True)
    number = Column(String(255), nullable=False, index=True)
    start_time = Column(DateTime(255), nullable=False)
    time = Column(String(255), nullable=False)
    arrive_time = Column(DateTime(255), nullable=False)
    start_where = Column(String(255), nullable=False)
    arrive_where = Column(String(255), nullable=False)
    price = Column(Integer, nullable=True)
    date = Column(String(255), nullable=False)
    arrive_where_city = Column(String(255), nullable=False)
    start_where_city = Column(String(255), nullable=False)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.number)


@logger
def get_route_trains(DateStart, DateEnd, station):
    Session = sessionmaker(bind=engine)
    session = Session()
    query = (session
             .query(Train)
             .filter_by(start_where=station)
             .filter(Train.start_time >= DateStart)
             .filter(Train.start_time <= DateEnd)
             .limit(10000)
             .offset(0).all()
             )
    session.close()
    # for i in query:
    return query

@logger
def get_route_trains_city(DateStart, DateEnd, station):
    Session = sessionmaker(bind=engine)
    session = Session()
    city = (session
            .query(Train.start_where_city)
            .filter_by(start_where=station)
            .first()
            )
    query = (session
             .query(Train)
             .filter_by(start_where_city=city[0])
             .filter(Train.start_time >= DateStart)
             .filter(Train.start_time <= DateEnd)
             .all()
             )
    return query


def get_price(id):
    Session = sessionmaker(bind=engine)
    session = Session()
    query = (session
             .query(Train)
             .filter(Train.id == id)
             .all()
             )
    session.close()
    # for i in query:
    return query


# session.commit()
if __name__ == '__main__':
    print(len(get_route_trains_city("2019-05-30 00:04:59", "2019-05-30 20:05:00", "长春站")))
    # print(len((get_route_trains("2019-05-30 00:04:59", "2019-05-30 20:05:00", "长春站"))))
    # print(get_price(1)[0].price)
