# @Time  : 2019/4/24 0024 21:18
# @Author: LYX
# @File  : star.py
import sys
import time

from Models.station import Station
from DAO.distance import get_distance


class QueryRoute:
    openList = []
    closedList = []

    def __init__(self, start, target, timestamp_start, timestamp_end):
        self.start = start  # 设置起点
        self.target = target  # 目的地
        self.timestamp_start = timestamp_start
        self.timestamp_end = timestamp_end

        self.min_cost = sys.maxsize

    def getWhere(self):  # 当前所在位置

        return self.where

    def setWhere(self, where):  # 当前所在位置

        self.where = where

    def total_cost(self, station):  # 总的代价
        # print(self.base_cost(station), self.heuristic_cost(station), self.change_cost(station))
        return (self.base_cost(station)) +(self.heuristic_cost(station)) + (self.change_cost(station))

    def base_cost(self, station):  # 已走距离
        # print("get_distance:", station.station_name, self.start.station_name)
        if station.station_name == self.start.station_name:
            return int(0)
        return get_distance(station.station_name, self.start.station_name) * 0.33

    def heuristic_cost(self, station):  # 启发函数  距离
        # print("get_distance:", station.station_name, self.target.station_name)

        if station.station_name == self.target.station_name:
            return int(0)
        return get_distance(station.station_name, self.target.station_name) * 0.33

    def change_cost(self, station):  # 计算起点到当前点中转代价
        if self.start == station:
            station.change_cost = 0
        else:
            station.change_cost = station.parent.change_cost + 100
        return station.change_cost

    def price_cost(self, station):  # 计算起点到当前点费用
        if self.start == station:
            station.price_cost = 0
        else:
            station.price_cost = station.parent.price_cost + station.price
        return station.price_cost

    def chose_min(self):
        min_cost = sys.maxsize
        for i in self.openList:
            i.cost = self.total_cost(i)
            if i.cost < min_cost:
                # min_cost = i.cost
                min_i = i
        print("openlist大小", len(self.openList), "openlist中代价最小的车站:", min_i.station_name)
        return min_i  # 返回openlist中代价最小的车站

    def stationRoute(self, station):
        """

        :param station:
        :return:  返回该站的可行路线
        """
        pass

        return

    def process_station(self, station, parent):
        '''
        处理各路线的代价和
        :param station:
        :param parent:
        :return:
        '''
        if station is None:
            return  # Do nothing for invalid point
        # if station.passable == 0:
        #     return  # Do nothing for invalid point

        if station in self.closedList:
            return  # Do nothing for visited point
        # print('Process Point [', station.station_name, ',]', ', cost: ', 'station.cost')
        if station not in self.openList:
            station.parent = parent
            station.cost = self.total_cost(station)
            self.openList.append(station)

    def BuildPath(self, station):
        path = []
        while True:
            path.insert(0, station)  # Insert first  头插法
            if self.start == station:
                break
            else:
                station = station.parent
        for i in path:
            print(i)

    def search(self):

        start_time = time.time()
        start_station = self.start
        start_station.cost = 0
        self.openList.append(start_station)

        while True:
            station = self.chose_min()
            if station == None:
                print('No path found, algorithm failed!!!')
                return

            # rec = Rectangle((cell.x, cell.y), 1, 1, color='c')
            # self.ax.add_patch(rec)
            # self.SaveImage()

            if self.target.station_name == station.station_name:
                end_time = time.time()
                print('===== Algorithm finish in', int(end_time - start_time), ' seconds')
                return self.BuildPath(station)

            self.openList.remove(station)
            self.closedList.append(station)

            # Process all neighbors
            neighbors = station.getNeighbor(self.timestamp_start, self.timestamp_end)
            k = 0
            for i in neighbors:
                # print(k, len(neighbors))
                # k += 1
                # print(i.station_name)
                self.process_station(i, station)

            # self.processPoint(self.cellNeighbor(cell, 1, 0), cell)
            # self.processPoint(self.cellNeighbor(cell, 0, 1), cell)
            # self.processPoint(self.cellNeighbor(cell, -1, 0), cell)
            # self.processPoint(self.cellNeighbor(cell, 0, -1), cell)
            # self.processPoint(self.cellNeighbor(cell, 1, 1), cell)
            # self.processPoint(self.cellNeighbor(cell, -1, 1), cell)
            # self.processPoint(self.cellNeighbor(cell, -1, -1), cell)
            # self.processPoint(self.cellNeighbor(cell, 1, -1), cell)


start = Station("长春站")
target = Station("北京站")
timestamp_start = 20190529
timestamp_end = 20190530
route = QueryRoute(start, target, timestamp_start, timestamp_end)
route.search()
