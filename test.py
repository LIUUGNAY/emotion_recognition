import pickle
import numpy as np
process = 'D:/python/预处理数据集/data_SubBand_python/s01/s09.dat'
# process1 = 'D:/python/预处理数据集/data_SubBand_python/s01/s09.dat'
s = open(process, "rb")
# s1 = open(process1, "rb")
num = pickle.load(s, encoding="latin1")
# num1 = pickle.load(s1, encoding="latin1")
Theta = num['Theta']
# print(num)
Theta_pccMatrix = np.corrcoef(Theta)
print(Theta_pccMatrix)
# print(Theta)