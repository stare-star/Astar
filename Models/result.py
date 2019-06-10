# @Time  : 2019/6/8 0008 21:21
# @Author: LYX
# @File  : result.py
from sqlalchemy import Column, String, Integer, Text, DateTime
from sqlalchemy.orm import sessionmaker, relationship
from DAO.connect import Base, engine
from utils import logfun


class query_result():

    def __init__(self, start=None, target=None):
        self.start = start
        self.target = target
        self.stations = []

    def add_stations(self, number, start_where, arrive_where, price, start_time, arrive_time, name, time, rate, company,
                     airplane_type):
        station = {"number": number, "price": price, "start_where": start_where, "arrive_where": arrive_where,
                   "start_time": start_time, "arrive_time": arrive_time, "name": name, "time": time, "rate": rate,
                   "company": company, "airplane_type": airplane_type}
        self.stations.append(station)

    def to_json(self):
        pass

    def to_string(self):
        res = "{\"plans\":[{\"id\":\"1\"," + "\"start_station\":" + "\"" + self.start + "\"" + "," + "\"steps\":["
        price = 0
        for i in self.stations:
            res += "{\"name\":" + "\"" + str(i["name"]) + "\"" + ",\"start_time\":" + "\"" + str(
                i["start_time"]) + "\"" + ",\"number\":" + "\"" + str(
                i['number']) + "\"" + ",\"start_where\":" + "\"" + str(
                i['start_where']) + "\"" + ",\"arrive_where\":" + str(
                "\"" + i['arrive_where']) + "\"" + ",\"arrive_time\":" + "\"" + str(i['arrive_time']) + "\"" + \
                   ",\"price\":" + "\"" + str(i["price"]) + "\"" + ",\"time\":" + "\"" + str(
                i["time"]) + "\"" + ",\"rate\":" + "\"" + str(i["rate"]) + "\"" + ",\"company\":" + "\"" + str(
                i["company"]) + "\"" + ",\"airplane_type\":" + "\"" + str(i["airplane_type"]) + "\"""},"
            # price += int(i["price"])
        res = res[:-1]

        res += "]," + "\"arrive_station\":" + "\"" + self.target + "\"" + "}]}"
        return res


class Result(Base):
    __tablename__ = 'result'
    id = Column(Integer, primary_key=True)
    start_time = Column(DateTime(255), nullable=False)
    arrive_time = Column(DateTime(255), nullable=False)
    start_where = Column(String(255), nullable=False)
    arrive_where = Column(String(255), nullable=False)
    result_json = Column(String(2550), nullable=False)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.result_json)


def add_result(start_time,
               arrive_time,
               start_where,
               arrive_where,
               result_json):
    print(start_time,
          arrive_time,
          start_where,
          arrive_where,
          result_json)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = Result(start_time=start_time,
                    arrive_time=arrive_time,
                    start_where=start_where,
                    arrive_where=arrive_where,
                    result_json=result_json)
    session.add(result)
    session.commit()
    session.close()

@logfun
def get_result(start_time,
               arrive_time,
               start_where,
               arrive_where
               ):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = (session
                   .query(Result)
                   .filter(Result.start_where == start_where)
                   .filter(Result.arrive_where == arrive_where)
                   .filter(Result.start_time == start_time)
                   .filter(Result.arrive_time == arrive_time)
                   .first()
                   )
    if result is  None:
        return 0

    return (result.result_json)
    session.close()


if __name__ == '__main__':
    # add_result("2019-05-30 00:04:59", "2019-05-31 20:05:00", "重庆站", "武昌站", "test")
    print(get_result("2019-05-30 00:04:59", "2019-05-31 20:05:00", "重庆", "武昌站"))
