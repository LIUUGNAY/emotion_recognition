import os
import pickle

import numpy
import numpy as np
import scipy.signal as signal
from scipy import interpolate


# 判定当前的时间序列是否是单调序列
def ismonotonic(x):
    max_peaks = signal.argrelextrema(x, np.greater)[0]
    min_peaks = signal.argrelextrema(x, np.less)[0]
    all_num = len(max_peaks) + len(min_peaks)
    if all_num > 0:
        return False
    else:
        return True


# 寻找当前时间序列的极值点
def findpeaks(x):
    return signal.argrelextrema(x, np.greater)[0]


# 判断当前的序列是否为 IMF 序列
def isImf(x):
    N = np.size(x)
    pass_zero = np.sum(x[0:N - 2] * x[1:N - 1] < 0)  # 过零点的个数
    peaks_num = np.size(findpeaks(x)) + np.size(findpeaks(-x))  # 极值点的个数
    if abs(pass_zero - peaks_num) > 1:
        return False
    else:
        return True


# 获取当前样条曲线
def getspline(x):
    N = np.size(x)
    peaks = findpeaks(x)
    print
    '当前极值点个数：', len(peaks)
    if (len(peaks) <= 3):
        if (len(peaks) < 2):
            peaks = np.concatenate(([0], peaks))
            peaks = np.concatenate((peaks, [N - 1]))  # 这里是为了防止样条次数不够，无法插值的情况
        t = interpolate.splrep(peaks, y=x[peaks], w=None, xb=None, xe=None, k=len(peaks) - 1)
        return interpolate.splev(np.arange(N), t)
    t = interpolate.splrep(peaks, y=x[peaks])
    return interpolate.splev(np.arange(N), t)


#     f=interp1d(np.concatenate(([0,1],peaks,[N+1])),np.concatenate(([0,1],x[peaks],[0])),kind='cubic')
#     f=interp1d(peaks,x[peaks],kind='cubic')
#     return f(np.linspace(1,N,N))


# 经验模态分解方法
def emd(x):
    count = 0
    imf = []
    while not ismonotonic(x):
        x1 = x
        sd = np.inf
        while sd > 0.1 or (not isImf(x1)):
            print
            isImf(x1)
            s1 = getspline(x1)
            s2 = -getspline(-1 * x1)
            x2 = x1 - (s1 + s2) / 2
            sd = np.sum((x1 - x2) ** 2) / np.sum(x1 ** 2)
            x1 = x2
            count += 1
            # if count > 30:
            #     break

        imf.append(x1)
        x = x - x1
    imf.append(x)
    return imf





# process = 'D:/python/预处理数据集/data_subBand_python/s01/s01.dat'
# s = open(process, "rb")
# # s1 = open(process1, "rb")
# num = pickle.load(s, encoding="latin1")
# # for i in range(0, 32):
# #     print(len(emd(num['Gamma'][i])))
# #     print(i)
# Theta = num['Gamma'][2]
# print(len(Theta))
# print(emd(Theta))
# imf1 = emd(Theta)

# print(emd(Theta))
# for m in range(0, 2560):
#     for n in range(1, len(imf1)):
#         imf1[0][m] += imf1[n][m]
# print(len(imf1))
# print(imf1[0])

# num_list_Theta = numpy.zeros((32, 2560))
# num_list_Alpha = numpy.zeros((32, 2560))
# num_list_Gamma = numpy.zeros((32, 2560))
# num_list_Beta = numpy.zeros((32, 2560))
# for p in range(10, 32):
#     print(p)
#     Theta = num['Theta'][p]
#     Alpha = num['Alpha'][p]
#     Beta = num['Beta'][p]
#     Gamma = num['Gamma'][p]
#
#     imf1_Theta = emd(Theta)
#     imf1_Alpha = emd(Alpha)
#     imf1_Beta = emd(Beta)
#     imf1_Gamma = emd(Gamma)
#
#     for m in range(0, 2560):
#         for n in range(1, len(imf1_Theta)):
#             imf1_Theta[0][m] += imf1_Theta[n][m]
#         print("Theta" + str(p))
#         for n in range(1, len(imf1_Alpha)):
#             imf1_Alpha[0][m] += imf1_Alpha[n][m]
#         print("Alpha" + str(p))
#         for n in range(1, len(imf1_Beta)):
#             imf1_Beta[0][m] += imf1_Beta[n][m]
#         print("Beta" + str(p))
#         for n in range(1, len(imf1_Gamma)):
#             imf1_Gamma[0][m] += imf1_Gamma[n][m]
#         print("Gamma" + str(p))
#
#     num_list_Theta[p] = imf1_Theta[0]
#     num_list_Alpha[p] = imf1_Alpha[0]
#     num_list_Beta[p] = imf1_Beta[0]
#     num_list_Gamma[p] = imf1_Gamma[0]
#
# print(num_list_Theta)
# print(num_list_Alpha)
# print(num_list_Beta)
# print(num_list_Gamma)
# print(len(num_list_Theta))
# print(num_list_Theta)