# @Time  : 2019/4/17 0017 16:02
# @Author: LYX
# @File  : read.py


with open("high", "r", encoding="utf-8")as f:
    result = list()
    for line in f:
        line = f.readline()
        line = line.split()
        result.append(line)
    print(result)
    f.close()
