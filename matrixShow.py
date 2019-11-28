import pickle
from math import exp

from matplotlib import pyplot as plt
from scipy.signal import hilbert
import numpy as np


# def PLV(y1, y2):
#     ch1 = hilbert(y1)
#     ch1_ph = np.unwrap(np.angle(ch1, deg=False))
#     ch2 = hilbert(y2)
#     ch2_ph = np.unwrap(np.angle(ch2, deg=False))
#     complex_phase_diff = np.exp(np.complex(0, 1) * (ch1_ph - ch2_ph))
#     _plv = np.abs(np.sum(complex_phase_diff)) / len(ch2_ph)
#     return _plv


process = 'D:/python/预处理数据集/SubBandData_PLV_python/s01/s09.dat'
process1 = 'D:/python/预处理数据集/PLVData_01Matrix_python/s01/s09.dat'
s = open(process, "rb")
s1 = open(process1, "rb")
num = pickle.load(s, encoding="latin1")
num1 = pickle.load(s1, encoding="latin1")
labels = num['labels']
Theta = num['PLV_Theta']
print(Theta)
Theta1 = num1['Array01_Theta']
Alpha = num['PLV_Alpha']
Alpha1 = num1['Array01_Alpha']
Beta = num['PLV_Beta']
Gamma = num['PLV_Gamma']
plt.imshow(Alpha)
plt.colorbar()
plt.show()

plt.imshow(Alpha1, cmap='gray')
plt.colorbar()
plt.show()
# num_Theta = num['Theta']
# num_Alpha = num['Alpha']
# num_Beta = num['Beta']
# num_Gamma = num['Gamma']
# array_plv_Theta = np.zeros((32, 32))
# array_plv_Alpha = np.zeros((32, 32))
# array_plv_Beta = np.zeros((32, 32))
# array_plv_Gamma = np.zeros((32, 32))
# for p in range(0, 32):
#     for q in range(p, 32):
#         num_plv_Theta = PLV(num_Theta[p], num_Theta[q])
#         array_plv_Theta[p][q] = num_plv_Theta
#
#         num_plv_Alpha = PLV(num_Alpha[p], num_Alpha[q])
#         array_plv_Alpha[p][q] = num_plv_Alpha
#
#         num_plv_Beta = PLV(num_Beta[p], num_Beta[q])
#         array_plv_Beta[p][q] = num_plv_Beta
#
#         num_plv_Gamma = PLV(num_Gamma[p], num_Gamma[q])
#         array_plv_Gamma[p][q] = num_plv_Gamma
#
# array_plv_Theta += array_plv_Theta.T - np.diag(array_plv_Theta.diagonal())
# array_plv_Alpha += array_plv_Alpha.T - np.diag(array_plv_Alpha.diagonal())
# array_plv_Beta += array_plv_Beta.T - np.diag(array_plv_Beta.diagonal())
# array_plv_Gamma += array_plv_Gamma.T - np.diag(array_plv_Gamma.diagonal())
# print(array_plv_Theta)
# print(array_plv_Alpha)
# print(array_plv_Beta)
# print(array_plv_Gamma)

