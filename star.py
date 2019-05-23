# @Time  : 2019/4/24 0024 21:18
# @Author: LYX
# @File  : star.py
import sys


class Station:

    def __init__(self, id, starting_station, terminus,starting_time,end_time,time,price):
        self.id = id
        self.starting_station = starting_station
        self.terminus = terminus
        self.starting_time = starting_time
        self.end_time = end_time
        self.time=time
        self.price=price  #数组

class Map:
    def __init__(self, data,start,target):
        self.map = self.createMap(data) # 读取各种票的信息，创建节点地图
        self.start = self.choseStation(start)  # 设置起点  左下角
        self.target = self.choseStation(target)  # 目的地   右上角

        openList = []
        closedList = []
        self.min_cost = sys.maxsize


    def totalCost(self, station):  # 总的代价
        return self.baseCost(station) + self.heuristicCost(station)

    def heuristicCost(self, station):  # 启发函数
        pass
    def baseCost(self, cell):  # 起点到当前点的真实代价
        pass

    def choseMinH(self):
        min_cost = sys.maxsize
        for i in self.openList:
            i.cost = self.totalCost(i)
            if i.cost < min_cost:
                #min_cost = i.cost
                min_i = i

        return min_i  #返回openlist中代价最小的车站

    def stationNeighbor(self, station):
        pass
        return