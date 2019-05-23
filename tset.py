#@Time  : 2019/5/22 0022 21:41
#@Author: LYX
#@File  : tset.py

# import re
# import requests
# from urllib.parse import urlencode
# headers = {'user-agent':'Mozilla/5.0'}
# station_code_url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9006' #车站对应代码web
# station_code_url_response = requests.get(station_code_url,headers = headers)
# stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', station_code_url_response.text)
# station_code = dict(stations)
# code_station = {v:k for k,v in station_code.items()}
# print(len(code_station))
import time

print(time.localtime(1558542416146/100000))