# @Time  : 2019/5/23 0023 21:07
# @Author: LYX
# @File  : route.py
from Mylog import logger

from DAO.Trains import get_route_trains_city, get_train_city
from DAO.airplane import get_route_air, get_route_air_city, get_air_city
from Mythread import MyThread
from utils import logfun


class Route:

    def __init__(self, arrive_where, arrive_where_city=None, id=None, number=None, start_time=None, time=None,
                 arrive_time=None,
                 start_where=None, price=None,  start_where_city=None, rate=None, airplane_type=None,
                 company=None):
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

    def get_next_route(self, timestampStart, timestampEnd):
        '''
        #获取该站在所给时间内的所有的可达路线
        :param timestampStart:
        :param timestampEnd:
        :return: from DAO.Train_number import  get_route_trains_city   Train_number
        '''

        # if self != None:
        #     if self.arrive_time:
        #         time_limit = self.arrive_time
        #         print(time_limit)
        #         print(type(time_limit), "p")
        #     else:
        #         time_limit = "0"
        #         print(type(time_limit), "s")
        #
        # else:
        #     time_limit = "0"
        #     print(type(time_limit), "s")

        # t1 = MyThread(target=get_route_trains_city, args=(timestampStart, timestampEnd, self.arrive_where,))
        # t2 = MyThread(target=get_route_air_city, args=(timestampStart, timestampEnd, self.arrive_where,))
        # t1.start()
        # t2.start()
        # tra_list = []
        # tra_list.insert(0, t1.get_result())
        # tra_list.insert(1, t2.get_result())
        # 获取站点所在城市
        self.get_station_city()

        # 查找当前城市所有可达站点
        trains = get_route_trains_city(timestampStart, timestampEnd, self.arrive_where_city)
        airs = get_route_air_city(timestampStart, timestampEnd, self.arrive_where_city)
        traffic = []
        traffic.extend(airs)
        traffic.extend(trains)
        logger.info(traffic)
        next_routes = [
            Route(arrive_where=i.arrive_where, arrive_where_city=i.arrive_where_city, id=i.id, number=i.number,
                  start_time=i.start_time, time=i.arrive_time - i.start_time, arrive_time=i.arrive_time,
                  start_where=i.start_where, price=i.price, start_where_city=i.start_where_city)
            for i in traffic if True]
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
        try:
            self.arrive_where_city = get_train_city(self.arrive_where)
        except:
            self.arrive_where_city = get_air_city(self.arrive_where)

        logger.info(str(self.arrive_where)+"所在城市是"+str(self.arrive_where_city))



if __name__ == '__main__':
    station = Route("长春站")

    for i in station.get_next_route(20190529, 20190530):
        print(i.arrive_where)
