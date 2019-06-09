# @Time  : 2019/6/8 0008 21:21
# @Author: LYX
# @File  : result.py
class query_result():
    def __init__(self, start, target):
        self.start = start
        self.target = target
        self.stations = []

    def add_stations(self, number, start_where, arrive_where, price, start_time, arrive_time, ):
        station = {"number": number, "price": price, "start_where": start_where, "arrive_where": arrive_where,
                   "start_time": start_time, "arrive_time": arrive_time, }
        self.stations.append(station)
    def to_json(self):
        pass


    def to_string(self):
        res = "起始站：" + self.start + "\n"

        price = 0
        for i in self.stations:
            res += "start_time:" + str(i["start_time"]) + "--" + 'number:' + str(
                i['number']) + "--" + 'start_where:' + str(i['start_where']) + "--" + 'arrive_where:' + str(
                i['arrive_where']) + "--" + 'arrive_time:' + str(i['arrive_time']) + "--" + \
                   "price:" + str(i["price"]) + "\n"
            # price += int(i["price"])
        res += "\"终点站:\"" + self.target + "\n" \
               + "\"总价格:\"" + str(price) + "\n" \
               + "\"总时间:\"" + str("?")
        return res
