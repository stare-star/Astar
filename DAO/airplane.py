# @Time  : 2019/5/25 0025 17:10
# @Author: LYX
# @File  : airplane.py
from Mylog import logging
from sqlalchemy import Column, String, Integer, Text, DateTime, Float
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
    airplane_type = Column(String(255), nullable=True)
    start_time = Column(DateTime(255), nullable=False)
    start_where_city = Column(String(255), nullable=False, index=True)
    arrive_where_city = Column(String(255), nullable=False, index=True)
    start_where = Column(String(255), nullable=False, index=True)
    arrive_where = Column(String(255), nullable=False, index=True)
    arrive_time = Column(DateTime(255), nullable=False)
    price = Column(Integer, nullable=True)
    rate = Column(String(255), nullable=False)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.number)


def get_route_air(DateStart, DateEnd, station):
    Session = sessionmaker(bind=engine)
    session = Session()
    query = (session
             .query(Airplane)
             .filter_by(start_where=station)
             .filter(Airplane.start_time >= DateStart)
             .filter(Airplane.start_time <= DateEnd)
             .limit(10000)
             .offset(0).all()
             )
    session.close()
    return query


def get_route_air_city(DateStart, DateEnd, station):
    Session = sessionmaker(bind=engine)
    session = Session()
    city = (session
            .query(Airplane.start_where_city)
            .filter_by(start_where=station)
            .first()
            )
    query = (session
             .query(Airplane)
             .filter_by(start_where_city=city[0])
             .filter(Airplane.start_time >= DateStart)
             .filter(Airplane.start_time <= DateEnd)
             .all()
             )
    return query


if __name__ == '__main__':
    print((get_route_air("2019-05-30 00:04:59", "2019-05-30 20:05:00", "首都国际机场T2航站楼")))
    print((get_route_air_city("2019-05-30 00:04:59", "2019-05-30 20:05:00", "首都国际机场T2航站楼")))
