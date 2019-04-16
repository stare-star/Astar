#@Time  : 2019/4/16 0016 13:18
#@Author: LYX
#@File  : cla.py
class Cell:

    def __init__(self, x, y, id, passable):
        self.x = x
        self.y = y
        self.id = id
        self.passable = passable
cell =Cell(1 ,2,5,1)
cell.p=Cell(1 ,54,27,1)
print(cell.p.y)