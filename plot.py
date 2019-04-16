#@Time  : 2019/4/15 0015 22:55
#@Author: LYX
#@File  : plot.py

import matplotlib.pyplot as plt

from matplotlib.patches import Rectangle
size=50
ax = plt.gca()
ax.set_xlim([0, size])
ax.set_ylim([0,size])

for i in range(size):
    for j in range(size):
        if i==24 or j==15 or i+j==50:
            rec = Rectangle((i, j), width=1, height=1, color='gray')
            ax.add_patch(rec)
        else:
            rec = Rectangle((i, j), width=1, height=1, edgecolor='gray', facecolor='w')
            ax.add_patch(rec)

rec = Rectangle((0, 0), width = 1, height = 1, facecolor='b')
ax.add_patch(rec)

rec = Rectangle((size-1, size-1), width = 1, height = 1, facecolor='r')
ax.add_patch(rec)

plt.axis('equal')
plt.axis('off')
plt.tight_layout()

rec = Rectangle((25, 25), width = 11, height = 1, facecolor='r')
ax.add_patch(rec)

plt.draw()
plt.savefig('1')