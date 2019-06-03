# @Time  : 2019/6/1 0001 20:12
# @Author: LYX
# @File  : pandas_io.py
import time

import pandas as pd
from DAO.connect import engine

# s=time.time()
# data=pd.read_sql('rank',engine)
# e=time.time()
# print(s - e)
# s=time.time()
# print(data.loc(1))
# e=time.time()
# print(s - e)
import numpy as np
s=time.time()
for i in range(100):
   fd=np.random.rand(3,3)*np.random.rand(3,3)
e=time.time()
print(e-s)

s=time.time()
for i in range(100):
   fd=3*3*3*3*3*3*3
e=time.time()
print(e-s)