# coding: utf-8

import random
import threading

from DAO.airplane import Airplane
from Mythread import MyThread
from utils import logfun
from Mylog import logger
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
        return '%s(%r)' % (self.__class__.__name__, self.id)


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
        .filter(Distance.arrive == arrive).all()
    session.close()
    if len(Q) == 0:
        print(start, arrive, "找不到距离数据")
        return int(999999999)

    return int(Q[0].distance) / 1000


def get_distance_from_list(sub_list, station):
    for i in sub_list:
        if i.arrive == station:
            return i.distance

    logger.warning(station+ "找不到距离")
    return 9999999999


@logfun
def get_distance_all(city):
    """
    :param station: 城市
    :return: 两地距离
    A到所有其他地方的距离   list
    """

    Session = sessionmaker(bind=engine)
    session = Session()
    train_stations = (session
                .query(Train.start_where)
                .filter_by(start_where_city=city)
                .distinct()
                .all()
                )
    air_stations=(session
                     .query(Airplane.start_where)
                     .filter_by(start_where_city=city)
                     .distinct()
                     .all()
                     )
    stations=[]
    stations.extend(train_stations)
    stations.extend(air_stations)
    print(len(stations))
    Q = []

    for foo_station in stations:
        Q.extend(session
                 .query(Distance)
                 .filter(Distance.start == foo_station)
                 .limit(10000)
                 .offset(0).all()
                 )
    session.close()

    if len(Q) == 0:
        print("找不到距离数据")
        return int(9999999999)
    return Q


@logfun
def get_distance_2_all(start_station, end_station):
    '''

    :param start_station:
    :param end_station:
    :return: 到两地的所有距离
    '''
    t1 = MyThread(target=get_distance_all, args=(start_station,))
    t2 = MyThread(target=get_distance_all, args=(end_station,))
    t1.start()
    t2.start()
    dis_list = []
    dis_list.insert(0, t1.get_result())
    dis_list.insert(1, t2.get_result())
    return dis_list


if __name__ == '__main__':
    print(get_distance_all("北京"))
    Q = get_distance_2_all("北京", "三亚")
    print(Q[0][0].arrive)
    print(get_distance_from_list(Q[0], "重庆站"))
