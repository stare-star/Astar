#@Time  : 2019/4/17 0017 12:30
#@Author: LYX
#@File  : net_leran.py
# 读取时刻表  转换为有向图

#
# import matplotlib.pyplot as plt
# # import networkx as nx
# # G = nx.Graph()
# # G.add_node(1)
# # G.add_node('A')
# # G.add_nodes_from([2, 3])
# # G.add_edges_from([(1,2),(1,3),(2,4),(2,5),(3,6),(4,8),(5,8),(3,7)])
# # H = nx.path_graph(10)
# # G.add_nodes_from(H)
#
# # import matplotlib.pyplot as plt
# import networkx as nx
# # G = nx.Graph()
# # H = nx.path_graph(10)
# # G.add_nodes_from(H)
# # nx.draw(G, with_labels=True)
# # plt.show()
#
# G=nx.Graph()
# #导入所有边，每条边分别用tuple表示
# G.add_edges_from([(1,2),(1,3),(2,4),(2,5),(3,6),(4,8),(5,8),(3,7)])
# nx.draw(G, with_labels=True, edge_color='b', node_color='y', node_size=1000)
# plt.show()
# import matplotlib.pyplot as plt
# import networkx as nx
# # H = nx.path_graph(10)
# # G.add_nodes_from(H)
# # G = nx.Graph()
# # G.add_cycle([0,1,2,3,4])
# # nx.draw(G, with_labels=True)
# # plt.show()
#
# # import networkx as nx
# # import matplotlib.pyplot as plt
# # #画图！
# # G=nx.Graph()
# # G.add_node(1)
# # G.add_nodes_from([2,3,4,5])
# # for i in range(5):
# #     for j in range(i):
# #         if (abs(i-j) not in (1,4)):
# #             G.add_edge(i+1, j+1)
# # nx.draw(G,
# #         with_labels=True, #这个选项让节点有名称
# #         edge_color='b', # b stands for blue!
# #         pos=nx.circular_layout(G), # 这个是选项选择点的排列方式，具体可以用 help(nx.drawing.layout) 查看
# #      # 主要有spring_layout  (default), random_layout, circle_layout, shell_layout
# #      # 这里是环形排布，还有随机排列等其他方式
# #         node_color='r', # r = red
# #         node_size=1000, # 节点大小
# #         width=3, # 边的宽度
# #        )
# # plt.show()
#
# # import random
# # G = nx.gnp_random_graph(10,0.3)
# # for u,v,d in G.edges(data=True):
# #     d['weight'] = random.random()
# #
# # edges,weights = zip(*nx.get_edge_attributes(G,'weight').items())
# #
# # pos = nx.spring_layout(G)
# # nx.draw(G, pos, node_color='b', edgelist=edges, edge_color=weights, width=10.0, edge_cmap=plt.cm.Blues)
# # # plt.savefig('edges.png')
# # plt.show()
#
# # import matplotlib.pyplot as plt
# # import networkx as nx
# #
# # G = nx.Graph()
# #
# # G.add_edge('a', 'b', weight=0.6)
# # G.add_edge('a', 'c', weight=0.2)
# # G.add_edge('c', 'd', weight=0.1)
# # G.add_edge('c', 'e', weight=0.7)
# # G.add_edge('c', 'f', weight=0.9)
# # G.add_edge('a', 'd', weight=0.3)
# #
# # elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 0.5]
# # esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 0.5]
# #
# # pos = nx.spring_layout(G)  # positions for all nodes
# #
# # # nodes
# # nx.draw_networkx_nodes(G, pos, node_size=700)
# #
# # # edges
# # nx.draw_networkx_edges(G, pos, edgelist=elarge,
# #                        width=6)
# # nx.draw_networkx_edges(G, pos, edgelist=esmall,
# #                        width=6, alpha=0.5, edge_color='b', style='dashed')
# #
# # # labels
# # nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
# #
# # plt.axis('off')
# # plt.show()


import networkx as nx
import matplotlib.pyplot as plt
G = nx.DiGraph() #or G = nx.MultiDiGraph()
G.add_node('A')
G.add_node('B')
G.add_edge('A', 'B', length = 2)
G.add_edge('A', 'B', length1 = 20)
G.add_edge('B', 'A', length = 3)

pos = nx.spring_layout(G)
nx.draw(G, pos)
edge_labels=dict([((u,v,),d['length'])
             for u,v,d in G.edges(data=True)])
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.3, font_size=7)
plt.show()
