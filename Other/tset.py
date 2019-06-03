# #@Time  : 2019/5/22 0022 21:41
# #@Author: LYX
# #@File  : tset.py
#
# # import re
# # import requests
# # from urllib.parse import urlencode
# # headers = {'user-agent':'Mozilla/5.0'}
# # station_code_url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9006' #车站对应代码web
# # station_code_url_response = requests.get(station_code_url,headers = headers)
# # stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', station_code_url_response.text)
# # station_code = dict(stations)
# # code_station = {v:k for k,v in station_code.items()}
# # print(len(code_station))
# import time
# import threading
# # print(time.localtime(1558542416146/100000))
# from sqlalchemy.orm import sessionmaker
#
# from DAO.connect import engine
# from DAO.distance import get_distance, Distance
# start="北京站"
# arrive="长春站"
# s=time.time()
#
#
# for i in range(100):
#
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     Q = session.query(Distance) \
#         .filter(Distance.start == start) \
#         .filter(Distance.arrive == arrive).all()
#     session.close()
#     if len(Q) == 0:
#         print(start, arrive, "找不到距离数据")
#
# e=time.time()
# print(e-s)
#
#
# s=time.time()
# Session = sessionmaker(bind=engine)
# session = Session()
#
#
#
# for i in range(100):
#     Q = session.query(Distance) \
#         .filter(Distance.start == start) \
#         .filter(Distance.arrive == arrive).all()
#     session.close()
#     if len(Q) == 0:
#         print(start, arrive, "找不到距离数据")
#
#
# e=time.time()
# print(e-s)
#
# s=time.time()
# for i in range(10):
#     threading.Thread(target=get_distance(start,arrive)).start()
#
#
#
# e=time.time()
# print(e-s)

