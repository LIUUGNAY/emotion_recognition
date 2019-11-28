import os
import pickle
import numpy as np

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
    process_file = 'D:/python/预处理数据集/SubBandData_PLV_python/'
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
        num_Theta = num['PLV_Theta']
        num_Alpha = num['PLV_Alpha']
        num_Beta = num['PLV_Beta']
        num_Gamma = num['PLV_Gamma']
        array_01_Theta = np.zeros((32, 32))
        array_01_Alpha = np.zeros((32, 32))
        array_01_Beta = np.zeros((32, 32))
        array_01_Gamma = np.zeros((32, 32))
        for p in range(0, 32):
            for q in range(p, 32):
                if num_Theta[p][q] > 0.5:
                    array_01_Theta[p][q] = 1
                else:
                    array_01_Theta[p][q] = 0

                if num_Alpha[p][q] > 0.5:
                    array_01_Alpha[p][q] = 1
                else:
                    array_01_Alpha[p][q] = 0

                if num_Beta[p][q] > 0.5:
                    array_01_Beta[p][q] = 1
                else:
                    array_01_Beta[p][q] = 0

                if num_Gamma[p][q] > 0.5:
                    array_01_Gamma[p][q] = 1
                else:
                    array_01_Gamma[p][q] = 0

        array_01_Theta += array_01_Theta.T - np.diag(array_01_Theta.diagonal())
        array_01_Alpha += array_01_Alpha.T - np.diag(array_01_Alpha.diagonal())
        array_01_Beta += array_01_Beta.T - np.diag(array_01_Beta.diagonal())
        array_01_Gamma += array_01_Gamma.T - np.diag(array_01_Gamma.diagonal())

        dirPath = "D:/python/预处理数据集/PLVData_01Matrix_python/" + process_name + "/"
        if j < 9:
            pathname = "s0" + str(j + 1) + ".dat"
        else:
            pathname = "s" + str(j + 1) + ".dat"

        dic = {'Array01_Theta': array_01_Theta, 'Array01_Alpha': array_01_Alpha, 'Array01_Beta': array_01_Beta,
               'Array01_Gamma': array_01_Gamma, 'labels': labels}
        createFile()