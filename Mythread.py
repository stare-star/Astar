# @Time  : 2019/6/4 0004 21:19
# @Author: LYX
# @File  : thead.py
import threading


class MyThread(threading.Thread):
    def __init__(self, target=None, args=(), **kwargs):
        super(MyThread, self).__init__()
        self._target = target
        self._args = args
        self._kwargs = kwargs

    def run(self):
        if self._target == None:
            return
        self.__result__ = self._target(*self._args, **self._kwargs)

    def get_result(self):
        self.join()  # 当需要取得结果值的时候阻塞等待子线程完成
        return self.__result__
