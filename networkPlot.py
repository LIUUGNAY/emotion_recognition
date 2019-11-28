import pickle

import matplotlib.pyplot as plt
import networkx as nx


process = 'D:/python/预处理数据集/PLVData_01Matrix_python/s01/s09.dat'
s = open(process, "rb")
num = pickle.load(s, encoding="latin1")
Theta1 = num['Array01_Theta']

G = nx.Graph()
node_Array = ['FP1', 'AF3', 'F3', 'F7', 'FC5', 'FC1', 'C3', 'T7', 'CP5',
              'CP1', 'P3', 'P7', 'PO3', 'O1', 'Oz', 'Pz', 'FP2', 'AF4',
              'Fz', 'F4', 'F8', 'FC6', 'FC2', 'Cz', 'C4', 'T8', 'CP6',
              'CP2', 'P4', 'P8', 'PO4', 'O2']
for i in range(0, len(node_Array)):
    G.add_node(node_Array[i])

for p in range(0, 31):
    for q in range(p+1, 32):
        if Theta1[p][q] == 1:
            G.add_edge(node_Array[p], node_Array[q])
# G.add_node('FP1')
# G.add_node('AF3')
# G.add_node('F3')
# G.add_node('F7')
# G.add_node('FC5')
# G.add_edge('FP1', 'AF3')
# print("Node Degree")
# for v in G:
#     print(f"{v:4} {G.degree(v):6}")

nx.draw_circular(G, with_labels=True)
plt.show()