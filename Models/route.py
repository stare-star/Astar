# @Time  : 2019/5/23 0023 21:07
# @Author: LYX
# @File  : route.py
import datetime

from Mylog import logger

from DAO.Trains import get_route_trains_city, get_train_city
from DAO.airplane import get_route_air, get_route_air_city, get_air_city
from Mythread import MyThread
from utils import logfun
from sqlalchemy import Column, String, Integer, Text, DateTime


class Route:

    def __init__(self, arrive_where, arrive_where_city=None, id=None, number=None, start_time=None, time=None,
                 arrive_time=None,
                 start_where=None, price=None, start_where_city=None, rate=None, airplane_type=None,
                 company=None,
                 ):
        self.id = id
        self.number = number
        self.start_time = start_time
        self.time = time
        self.arrive_time = arrive_time
        self.start_where = start_where
        self.arrive_where = arrive_where
        self.start_where_city = start_where_city
        self.arrive_where_city = arrive_where_city
        self.price = price
        self.rate = rate
        self.parent = None
        self.company = company
        self.airplane_type = airplane_type
        self.next_route_cache = {}

    def get_next_route(self, timestampStart, timestampEnd, next_route_cache=None):
        '''
        #获取该站在所给时间内的所有的可达路线
        :param timestampStart:
        :param timestampEnd:
        :param  next_route_cache
        :return: from DAO.Train_number import  get_route_trains_city   Train_number
        '''
        if self is not None:
            if self.arrive_time:
                time_limit = self.arrive_time+datetime.timedelta(hours=0)
                # print(time_limit)
                # print(type(time_limit), "p")
            else:
                time_limit =datetime.datetime(2000, 1, 1)
                # todo datetime
                # print(type(time_limit), "s")
        #
        # else:
        #     time_limit = "0"
        #     print(type(time_limit), "s")

        self.get_station_city()
        traffic = []
        self.next_route_cache = next_route_cache
        tra = self.get_route_from_cache()  # self.arrive_where_city
        if tra is not None:
            traffic.extend(tra)
        else:
            t1 = MyThread(target=get_route_trains_city,
                          args=(timestampStart, timestampEnd, self.arrive_where_city,))
            t2 = MyThread(target=get_route_air_city,
                          args=(timestampStart, timestampEnd, self.arrive_where_city,))
            t1.start()
            t2.start()
            traffic.extend(t1.get_result())
            traffic.extend(t2.get_result())
            next_route_cache.update({self.arrive_where_city: traffic})
        # logger.info(traffic)
        next_routes = [
            Route(arrive_where=i.arrive_where, arrive_where_city=i.arrive_where_city, id=i.id, number=i.number,
                  start_time=i.start_time, time=i.arrive_time - i.start_time, arrive_time=i.arrive_time,
                  start_where=i.start_where, price=i.price, start_where_city=i.start_where_city)
            for i in traffic if i.start_time > time_limit]
        return next_routes

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        """

        :param parent: 上一站
        :return: none
        """
        self._parent = parent

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, cost):
        """
        :param cost: 到达此站的代价
        :return: none
        """
        self._cost = cost

    def get_station_city(self):

        logger.debug("trainbegin")

        city = get_train_city(self.arrive_where)
       # self.arrive_where_city = get_train_city(self.arrive_where)
        logger.debug("train")
        if city is None:
            if self.arrive_where=="重庆江北国际机场T2航站楼":
                self.arrive_where="重庆江北国际机场T2B航站楼"
            city = get_air_city(self.arrive_where)
            logger.debug("air")
        self.arrive_where_city=city
        # logger.info(str(self.arrive_where)+"所在城市是"+str(self.arrive_where_city))

    def get_route_from_cache(self):
        cache = self.next_route_cache.get(self.arrive_where_city)
        if cache is None:
            print(self.arrive_where_city, "cache is None")
        else:
            print(self.arrive_where_city, "get cache ")

        return cache


def get_station_city(where):
    try:
        city = get_train_city(where)
    except:
        city = get_air_city(where)
    logger.info(str() + "所在城市是" + str(where))
    return city


if __name__ == '__main__':
    station = Route("长春站")

    for i in station.get_next_route(20190529, 20190530):
        print(i.arrive_where)
