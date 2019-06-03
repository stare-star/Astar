# coding: utf-8

import random
from faker import Factory

from sqlalchemy import create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import sessionmaker, relationship

from DAO.Trains import Train
from DAO.connect import Base, engine


class Distance(Base):
    __tablename__ = 'distance'

    id = Column(Integer, primary_key=True)
    start = Column(String(255), nullable=False)
    arrive = Column(String(255), nullable=False)
    distance = Column(String(255), nullable=False)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.number)


def get_distance(start, arrive):
    """
    :param start:
    :param arrive:
    :return: 两地距离
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    Q = session.query(Distance) \
        .filter(Distance.start == start) \
        .filter(Distance.arrive == arrive).all ()
    session.close()
    if  len(Q)==0:


        print(start, arrive,"找不到距离数据")
        return int(999999999)

    return int(Q[0].distance)/1000

def get_distance_pro(station,DateStart, DateEnd):
    """
    :param start:
    :param arrive:
    :return: 两地距离
    """

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


    Q = session.query(Distance) \
        .filter(Distance.start == start) \
        .filter(Distance.arrive ==list).all ()
    session.close()
    if  len(Q)==0:


        print(start, arrive,"找不到距离数据")
        return int(999999999)

    return int(Q[0].distance)/1000


if __name__ == '__main__':
    # print(get_distance("北京站", "长春站"))
    print(get_distance_pro("北京站", "长春站"))