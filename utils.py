# @Time  : 2019/5/22 0022 16:11
# @Author: LYX
# @File  : utils.py

import time
import threading

date = "20190530"
clock = "00:24"
timed = date + clock


def mktimestamp(timeformat):  # "2019053000:24"

    return time.mktime(time.strptime(timeformat, '%Y%m%d%H:%M'))  # 10位时间戳


from functools import wraps


def logfun(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        ts = time.time()
        result = fn(*args, **kwargs)
        te = time.time()
        print("function      = {0}".format(fn.__name__))
        print("    arguments = {0} {1}".format(args, kwargs))
        # print("    return    = {0}".format(result))
        print("    time      = %.6f sec" % (te - ts))
        return result

    return wrapper


def job1():
    print('start_1')
    for i in range(20):
        time.sleep(0.1)
    print('finish_1')
    # print(threading.current_thread())


def job2():
    print('2')
    print(threading.current_thread())

def main():
    s = threading.Thread(target=job1(), name="1j")
    s.start()
    print("end")

if __name__ == '__main__':
    s = threading.Thread(target=job1, name="1j")
    s.start()
    print("end")


    # @logfun
    # def multipy(x, y):
    #     print(1111)
    #     return x * y
    #
    #
    # @logfun
    # def sum_num(n):
    #     s = 0
    #     for i in range(n + 1):
    #         s += i
    #     return s


    # print(threading.active_count())
    # print(threading.enumerate())
    # print(threading.current_thread())


