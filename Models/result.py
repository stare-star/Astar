# @Time  : 2019/6/8 0008 21:21
# @Author: LYX
# @File  : result.py
class query_result():
    def __init__(self, start, target):
        self.start = start
        self.target = target
        self.stations = []

    def add_stations(self, number, start_where, arrive_where, price, start_time, arrive_time, name,time,rate,company,airplane_type):
        station = {"number": number, "price": price, "start_where": start_where, "arrive_where": arrive_where,
                   "start_time": start_time, "arrive_time": arrive_time,"name":name ,"time":time,"rate":rate,"company":company,"airplane_type":airplane_type}
        self.stations.append(station)

    def to_json(self):
        pass

    def to_string(self):
        res = "{\"plans\":[{\"id\":\"1\","+"\"start_station\":" + "\"" + self.start + "\"" + "," + "\"steps\":["
        price = 0
        for i in self.stations:
            res += "{\"name\":"+ "\"" + str(i["name"])+"\""+",\"start_time\":" + "\"" + str(i["start_time"]) + "\"" + ",\"number\":" + "\"" + str(
                i['number']) + "\"" + ",\"start_where\":" + "\"" + str(
                i['start_where']) + "\"" + ",\"arrive_where\":" + str(
                "\"" + i['arrive_where']) + "\"" + ",\"arrive_time\":" + "\"" + str(i['arrive_time']) + "\"" + \
                   ",\"price\":" + "\"" + str(i["price"]) + "\"" + ",\"time\":" + "\"" + str(i["time"]) + "\"" +  ",\"rate\":" + "\"" + str(i["rate"]) + "\"" + ",\"company\":" + "\"" + str(i["company"]) + "\"" +",\"airplane_type\":" + "\"" + str(i["airplane_type"]) + "\"""},"
            # price += int(i["price"])
        res = res[:-1]

        res += "]," + "\"arrive_station\":" + "\"" + self.target + "\""+"}]}"
        return res
