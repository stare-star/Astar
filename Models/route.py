# @Time  : 2019/5/23 0023 21:07
# @Author: LYX
# @File  : route.py
from DAO.Trains import get_route
from utils import logger


class Route:

    def __init__(self, arrive_where, arrive_where_city=None, id=None, number=None, start_time=None, time=None,
                 arrive_time=None,
                 start_where=None, price=None, date=None, start_where_city=None):
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
        self.date = date
        self.parent = None
    def get_next_route(self, timestampStart, timestampEnd):
        '''
        #获取该站在所给时间内的所有的可达路线
        :param timestampStart:
        :param timestampEnd:
        :return: from DAO.Train_number import  get_route   Train_number
        '''

        if self != None:
            if self.arrive_time:
                time_limit = self.arrive_time
                print(time_limit)
                print(type(time_limit), "p")
            else:
                time_limit = "0"
                print(type(time_limit), "s")

        else:
            time_limit = "0"
            print(type(time_limit), "s")

        trains = get_route(timestampStart, timestampEnd, self.arrive_where)
        next_routes = [
            Route(i.arrive_where, i.arrive_where_city, i.id, i.number, i.start_time, i.time, i.arrive_time,
                  i.start_where, i.price, i.date, i.start_where_city)
            for i in trains if i.start_time > time_limit]
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


if __name__ == '__main__':
    station = Route("长春站")

    for i in station.get_next_route(20190529, 20190530):
        print(i.arrive_where)
