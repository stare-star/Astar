# @Time  : 2019/4/24 0024 21:18
# @Author: LYX
# @File  : star.py
import sys
import threading
import time
from queue import Queue

from Models.result import query_result, get_result, add_result
from Models.route import Route, get_station_city
from DAO.distance import get_distance_from_list, get_distance_2_all
from Mylog import logger
from Mythread import MyThread


class QueryRoute:
    open_list = []
    closed_list = []

    def __init__(self, start, target, timestamp_start, timestamp_end):
        self.start = start  # 设置起点
        self.target = target  # 目的地
        self.timestamp_start = timestamp_start
        self.timestamp_end = timestamp_end
        self.min_cost = sys.maxsize
        self.route_cache = {}

    def get_total_cost(self, station):  # 总的代价
        # print(self.base_cost(station), self.heuristic_cost(station), self.change_cost(station))
        self.cost = (self.base_cost(station)) + (self.heuristic_cost(station)) + (
            self.change_cost(station)) + self.price_cost(station)
        return self.cost

    def base_cost(self, station):  # 已走距离
        # print("get_distance:", station.station_name, self.start.station_name)
        if station.arrive_where == self.start.arrive_where:
            return int(0)

        base_cost = (int(get_distance_from_list(self.dis_list[0], station.arrive_where)) * 0.33)
        if base_cost == 9999999999:
            logger.debug("找不到距离:" + station.arrive_where)
        return base_cost

    def heuristic_cost(self, station):  # 启发函数  距离
        # print("get_distance:", station.station_name, self.target.station_name)

        if station.arrive_where == self.target.arrive_where:
            return int(0)
        # print(station.arrive_where, self.target.arrive_where)

        return int(get_distance_from_list(self.dis_list[1], station.arrive_where)) * 0.33

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
            station.price_cost = float(station.parent.price_cost) + float(station.price)
        return float(station.price_cost)

    def chose_min(self):
        min_cost = sys.maxsize
        for i in self.open_list:
            # i.cost = self.get_total_cost(i)
            i.cost = self.get_total_cost(i)
            # print(i.cost)
            if i.cost < min_cost:
                min_cost = i.cost
                min_i = i
        print("open_list大小", len(self.open_list), "open_list中代价最小的车站:", min_i.arrive_where)
        return min_i  # 返回open_list中代价最小的车站

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

        if station in self.closed_list:
            return  # Do nothing for visited point
        # print('Process Point [', station.arrive_where, ',]')
        if station not in self.open_list:
            station.parent = parent
            # station.total_cost = self.get_total_cost(station)
            # print(station.total_cost)
            # todo  好像没用
            self.open_list.append(station)

    def build_path(self, station):
        path = []
        while True:
            path.insert(0, station)  # Insert first  头插法
            if self.start == station:
                break
            else:
                station = station.parent
        # res = []
        # for i in path:
        #     res.append([i.arrive_where, i.number, i.id, i.price])
        # print(res)
        res = query_result(self.start.arrive_where, self.target.arrive_where)
        for i in path:
            res.add_stations(i.number, i.start_where, i.arrive_where, i.price, i.start_time, i.arrive_time, i.name,
                             i.time, i.rate, i.company, i.airplane_type)
            print(i.number, i.price, i.start_time, i.arrive_time, i.name)

        json=res.to_string()
        # import json
        # json =json.dumps(path)
        # print(json)

        add_result(timestamp_start, timestamp_end, start.arrive_where, target.arrive_where,json)
        return json

    def search(self):
        cache = get_result(self.timestamp_start, self.timestamp_end, self.start.arrive_where,self.target.arrive_where)
        print(cache)
        if cache != 0:
            return cache
        self.start.get_station_city()
        # start.arrive_time=timestamp_start

        self.target.get_station_city()
        self.dis_list = get_distance_2_all(self.start.arrive_where_city, self.target.arrive_where_city)
        start_time = time.time()
        start_station = self.start
        start_station.cost = 0
        self.open_list.append(start_station)

        while True:
            station = self.chose_min()
            if station is None:
                print('No path found, algorithm failed!!!')
                return

            # rec = Rectangle((cell.x, cell.y), 1, 1, color='c')
            # self.ax.add_patch(rec)
            # self.SaveImage()
            print("比较：", self.target.arrive_where_city, station.arrive_where_city)
            if self.target.arrive_where_city == station.arrive_where_city:
                end_time = time.time()
                logger.info('===== Algorithm finish in' + str(end_time - start_time) + ' seconds')
                return self.build_path(station)

            self.open_list.remove(station)
            self.closed_list.append(station)

            # Process all neighbors
            neighbors = station.get_next_route(self.timestamp_start, self.timestamp_end, self.route_cache)
            # k = 0
            thread_list = []
            for i in neighbors:
                # print(k, len(neighbors))
                # k += 1
                # print(i.arrive_where)
                t1 = threading.Thread(target=self.process_station, args=(i, station,))
                thread_list.append(t1)
                t1.setDaemon(True)
                t1.start()
            for i in thread_list:
                i.join()
            # self.process_station(i, station)


if __name__ == '__main__':
    start = Route("重庆站")
    target = Route("武昌站")
    timestamp_start = ("2019-05-30 00:04:59")
    timestamp_end = ("2019-05-31 20:05:00")

    route = QueryRoute(start, target, timestamp_start, timestamp_end)
    route.search()
# print(route.dis_list[0])
# print(get_distance_from_list(route.dis_list[1], "上海站"))
