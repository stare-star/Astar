# coding: utf-8

import random
import threading
from Mythread import MyThread
from utils import logger
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
                print(i.distance, station)
                return i.distance


        print(station, "找不到距离")
        return 9999999999


@logger
def get_distance_all(station):
    """
    :param station:站名
    :return: 两地距离
    A到所有其他地方的距离   list
    """

    Session = sessionmaker(bind=engine)
    session = Session()

    city = (session
            .query(Train.start_where_city)
            .filter_by(start_where=station)
            .first()
            )

    stations = (session
                .query(Train.start_where)
                .filter_by(start_where_city=city[0])
                .distinct()
                .all()
                )
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
        return int(999999999)
    return Q


@logger
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
    # print(get_distance("北京站", "长春站"))
    Q = get_distance_2_all("北京站", "三亚站")
    print(Q[0][0].arrive)
    print(get_distance_from_list(Q[0], "重庆站"))
