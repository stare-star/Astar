# @Time  : 2019/4/15 0015 21:39
# @Author: LYX
# @File  : Astar.py
import random
import sys
import time

import numpy as np
import matplotlib.pyplot as plt

from matplotlib.patches import Rectangle


class Cell:

    def __init__(self, x, y, id, passable):
        self.x = x
        self.y = y
        self.id = id
        self.passable = passable
        self.cost = sys.maxsize


class Cat():
    def __init__(self, x, y, L, W):
        self.x = x
        self.y = y
        self.map = self.createMap(L, W)
        self.target = self.choseCell(L - 1, W - 1)  # 目的地   右上角
        self.start = self.choseCell(0, 0)  # 设置起点  左下角
        self.min_cost = sys.maxsize

    openList = []
    closedList = []

    def getX(self):  # 当前所在位置
        return self.x

    def getY(self):
        return self.y

    def createMap(self, L, W):  # 创建地图 L*W
        cells = [[] for i in range(L)]
        id = 0
        passable = 1
        for l in range(L):
            for w in range(W):
                if (l == 10 and w > 10 and w < 25)or (w == 38 and l > 9 and l < 40) or (w == 15 and l > 5 and l < 20)or (w==20 and l>2):  # 设置障碍物
                    passable = 0

                if (w > 5and w < 45 and l>5 and l<45):
                    passable=random.randint(0,1)
                cells[l].append(Cell(l, w, id, passable))
                id = id + 1
                passable = 1

        return cells

    def SaveImage(self):
        millis = int(round(time.time() * 1000))
        filename = './png/' + str(millis) + '.png'
        plt.savefig(filename)

    def choseCell(self, x, y):
        L = len(self.map)
        W = len(self.map[0])
        for i in range(L):
            for j in range(W):
                if (self.map[i][j].x == x and self.map[i][j].y == y):
                    return self.map[i][j]

    def choseMinH(self):
        # try:
        #     print(self.min.x,self.min.y,self.min.cost,'min--------------------')
        # except:
        #     pass
        min_i = self.openList[0]
        self.min_cost=sys.maxsize
        for i in self.openList:
            i.cost = self.totalCost(i)
            # print(i.x,i.y,i.cost,self.min_cost)
            if i.cost <= self.min_cost:
                self.min_cost = i.cost
                self.min=i
                min_i = i

        return min_i

    def baseCost(self, cell):  # 起点到当前点的代价
        x_dis = cell.x - self.start.x
        y_dis = cell.y - self.start.y
        # Distance to start point
        # return x_dis + y_dis
        # return np.sqrt(x_dis * x_dis + y_dis * y_dis)
        # return x_dis + y_dis + (np.sqrt(2) - 2) * min(x_dis, y_dis)

        if self.start ==cell :
            cell.bcost=0
        else :
            cell.bcost=cell.parent.bcost+1
        return cell.bcost

    def heuristicCost(self, cell):  # 启发函数
        x_dis = self.target.x - cell.x
        y_dis = self.target.y - cell.y
        # Distance to end point
        # return x_dis+y_dis
        return x_dis + y_dis + (np.sqrt(2) - 2) * min(x_dis, y_dis)
        # return np.sqrt(x_dis * x_dis +y_dis * y_dis)

    def totalCost(self, cell):  # 总的代价
        return self.baseCost(cell) + self.heuristicCost(cell)

    def processPoint(self, cell, parent):

        if cell == None:
            return  # Do nothing for invalid point
        if cell.passable == 0:
            return  # Do nothing for invalid point

        if cell in self.closedList:
            return  # Do nothing for visited point
        print('Process Point [', cell.x, ',', cell.y, ']', ', cost: ', cell.cost)
        if cell not in self.openList:
            cell.parent = parent
            cell.cost = self.totalCost(cell)
            self.openList.append(cell)

    def BuildPath(self, cell, start_time):
        path = []
        while True:
            path.insert(0, cell)  # Insert first  头插法
            if self.start == cell:
                break
            else:
                cell = cell.parent
        for cell in path:
            rec = Rectangle((cell.x, cell.y), 1, 1, color='g')
            self.ax.add_patch(rec)
            plt.draw()
        self.SaveImage() #mark 加入循环画动图
        end_time = time.time()
        print('===== Algorithm finish in', int(end_time - start_time), ' seconds')

    def drawMap(self):
        L = len(self.map)
        W = len(self.map[0])
        self.ax = plt.gca()
        self.ax.set_xlim([0, L])  # 二维数组的长宽
        self.ax.set_ylim([0, W])

        for i in range(L):
            for j in range(W):
                if (self.map[i][j].passable == 0):
                    rec = Rectangle((i, j), width=1, height=1, edgecolor='gray', facecolor='gray')
                    self.ax.add_patch(rec)
                else:
                    rec = Rectangle((i, j), width=1, height=1, edgecolor='gray', facecolor='w')
                    self.ax.add_patch(rec)

        rec = Rectangle((self.start.x, self.start.y), width=1, height=1, facecolor='b')
        self.ax.add_patch(rec)

        rec = Rectangle((self.target.x, self.target.y), width=1, height=1, facecolor='r')
        self.ax.add_patch(rec)

        plt.axis('equal')
        plt.axis('off')
        plt.tight_layout()

    def search(self):

        start_time = time.time()

        start_point = self.start
        start_point.cost = 0
        self.openList.append(start_point)

        while True:
            cell = self.choseMinH()
            if cell == None:
                print('No path found, algorithm failed!!!')
                return

            rec = Rectangle((cell.x, cell.y), 1, 1, color='c')
            self.ax.add_patch(rec)
            # self.SaveImage()

            if self.target == cell:

                end_time = time.time()
                print('===== Algorithm finish in', int(end_time - start_time), ' seconds')
                return self.BuildPath(cell, start_time)

            self.openList.remove(cell)
            self.closedList.append(cell)

            # Process all neighbors

            self.processPoint(self.cellNeighbor(cell, 1, 0), cell)
            self.processPoint(self.cellNeighbor(cell, 0, 1), cell)
            self.processPoint(self.cellNeighbor(cell, -1, 0), cell)
            self.processPoint(self.cellNeighbor(cell, 0, -1), cell)
            self.processPoint(self.cellNeighbor(cell, 1, 1), cell)
            self.processPoint(self.cellNeighbor(cell, -1, 1), cell)
            self.processPoint(self.cellNeighbor(cell, -1, -1), cell)
            self.processPoint(self.cellNeighbor(cell, 1, -1), cell)


    def cellNeighbor(self, cell, x, y):
        if cell.x + x > -1 and cell.y + y > -1 and cell.x + x < len(self.map) and cell.y + y < len(self.map[0]):
            return self.map[cell.x + x][cell.y + y]
        return


cat = Cat(1, 2, 50, 50)
cat.drawMap()
cat.search()


