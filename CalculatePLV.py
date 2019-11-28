import os
import pickle
from scipy.signal import hilbert
import numpy as np


def PLV(y1, y2):
    ch1 = hilbert(y1)
    ch1_ph = np.unwrap(np.angle(ch1, deg=False))
    ch2 = hilbert(y2)
    ch2_ph = np.unwrap(np.angle(ch2, deg=False))
    complex_phase_diff = np.exp(np.complex(0, 1) * (ch1_ph - ch2_ph))
    _plv = np.abs(np.sum(complex_phase_diff)) / len(ch2_ph)
    return _plv


def createFile():
    if os.path.exists(dirPath):
        pass
        # print("目录" + dirPath + "已经存在")
    else:
        os.mkdir(dirPath)
        # print("创建目录" + dirPath)
    file_path = dirPath + pathname
    file = open(file_path, "wb")
    pickle.dump(dic, file)  # 将python数据转换并保存到pickle格式的文件中
    file.close()



for i in range(0, 32):
    process_file = 'D:/python/预处理数据集/data_subBand_python/'
    if i < 9:
        process_name = "s0" + str(i + 1)
    else:
        process_name = "s" + str(i + 1)
    process_name1 = process_file + process_name + "/"
    for j in range(0, 40):
        if j < 9:
            filename = "s0" + str(j + 1) + ".dat"
        else:
            filename = "s" + str(j + 1) + ".dat"
        s = open(process_name1 + filename, "rb")  # 以bytes类型正常读取文件
        print(process_name + filename)
        num = pickle.load(s, encoding="latin1")
        labels = num['labels']
        num_Theta = num['Theta']
        num_Alpha = num['Alpha']
        num_Beta = num['Beta']
        num_Gamma = num['Gamma']
        array_plv_Theta = np.zeros((32, 32))
        array_plv_Alpha = np.zeros((32, 32))
        array_plv_Beta = np.zeros((32, 32))
        array_plv_Gamma = np.zeros((32, 32))
        for p in range(0, 32):
            for q in range(p, 32):
                num_plv_Theta = PLV(num_Theta[p], num_Theta[q])
                array_plv_Theta[p][q] = num_plv_Theta

                num_plv_Alpha = PLV(num_Alpha[p], num_Alpha[q])
                array_plv_Alpha[p][q] = num_plv_Alpha

                num_plv_Beta = PLV(num_Beta[p], num_Beta[q])
                array_plv_Beta[p][q] = num_plv_Beta

                num_plv_Gamma = PLV(num_Gamma[p], num_Gamma[q])
                array_plv_Gamma[p][q] = num_plv_Gamma

        array_plv_Theta += array_plv_Theta.T - np.diag(array_plv_Theta.diagonal())
        array_plv_Alpha += array_plv_Alpha.T - np.diag(array_plv_Alpha.diagonal())
        array_plv_Beta += array_plv_Beta.T - np.diag(array_plv_Beta.diagonal())
        array_plv_Gamma += array_plv_Gamma.T - np.diag(array_plv_Gamma.diagonal())

        dirPath = "D:/python/预处理数据集/SubBandData_PLV_python/" + process_name + "/"
        if j < 9:
            pathname = "s0" + str(j + 1) + ".dat"
        else:
            pathname = "s" + str(j + 1) + ".dat"

        dic = {'PLV_Theta': array_plv_Theta, 'PLV_Alpha': array_plv_Alpha, 'PLV_Beta': array_plv_Beta, 'PLV_Gamma': array_plv_Gamma, 'labels': labels}
        createFile()
