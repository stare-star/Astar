#@Time  : 2019/5/22 0022 16:11
#@Author: LYX
#@File  : utils.py

import time

date = "20190530"
clock = "00:24"
timed=date + clock
def mktimestamp(timeformat):  #"2019053000:24"

    return time.mktime(time.strptime(timeformat,'%Y%m%d%H:%M'))   #10位时间戳
if __name__ == '__main__':
    print(mktimestamp(timed))
