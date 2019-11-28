import pickle

import numpy as np
import os


def createFile():
    if os.path.exists(dirPath):
        pass
        print("目录" + dirPath + "已经存在")
    else:
        os.mkdir(dirPath)
    file_path = dirPath + filename
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
        ThetaData = num['Theta']
        AlphaData = num['Alpha']
        BetaData = num['Beta']
        GammaData = num['Gamma']
        labels = num['labels']

        # 计算 pccmatrix
        Theta_pccMatrix = np.corrcoef(ThetaData)
        Alpha_pccMatrix = np.corrcoef(AlphaData)
        Beta_pccMatrix = np.corrcoef(BetaData)
        Gamma_pccMatrix = np.corrcoef(GammaData)

        dirPath = "D:/python/预处理数据集/data_PCCMatrix_python/" + process_name + "/"
        if j < 9:
            filename = "s0" + str(j + 1) + ".dat"
        else:
            filename = "s" + str(j + 1) + ".dat"
        # dic = {'data': data, 'labels': labels}
        dic = {'Theta_pccMatrix': Theta_pccMatrix, 'Alpha_pccMatrix': Alpha_pccMatrix, 'Beta_pccMatrix': Beta_pccMatrix,
               'Gamma_pccMatrix': Gamma_pccMatrix, 'labels': labels}
        createFile()
