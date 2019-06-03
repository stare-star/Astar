# @Time  : 2019/5/23 0023 21:07
# @Author: LYX
# @File  : station.py
from DAO.Trains import get_route


class Station:

    def __init__(self, station_name):
        self.station_name = station_name

    def getNeighbor(self, timestampStart, timestampEnd):
        '''
        #获取该站在所给时间内的所有的可达路线
        :param timestampStart:
        :param timestampEnd:
        :return: from DAO.Train_number import  get_route   Train_number
        '''
        trains = get_route(timestampStart, timestampEnd, self.station_name)
        neighbors = [Station(i.arrive_where) for i in trains]
        return neighbors

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
    station = Station("长春站")

    for i in station.getNeighbor(20190529, 20190530):
        print(i.station_name)
