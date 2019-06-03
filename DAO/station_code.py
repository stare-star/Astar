# @Time  : 2019/5/22 0022 21:45
# @Author: LYX
# @File  : station_code.py

# coding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

from DAO.connect import engine,Base


class Station_code(Base):
    __tablename__ = 'station_code'

    id = Column(Integer, primary_key=True)
    code = Column(String(5), nullable=False, index=True)
    station = Column(String(10), nullable=False)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.station)

    def getAllStation(self):
        import re
        import requests
        from urllib.parse import urlencode

        headers = {'user-agent': 'Mozilla/5.0'}
        station_code_url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9006'  # 车站对应代码web
        station_code_url_response = requests.get(station_code_url, headers=headers)
        stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', station_code_url_response.text)
        station_code = dict(stations)
        code_station = {v: k for k, v in station_code.items()}
        Session = sessionmaker(bind=engine)
        session = Session()
        for v, k in code_station.items():
            print(v, k)
            e = Station_code(code=v, station=k)
            session.add(e)
        session.commit()



def code2Station(code):
    Session = sessionmaker(bind=engine)
    session = Session()
    Station = (session
               .query(Station_code.station)
               .filter(Station_code.code == code)
               .one()
               )

    return Station


if __name__ == '__main__':
    print(code2Station(code="SHH"))
