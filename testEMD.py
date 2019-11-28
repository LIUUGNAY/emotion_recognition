import os
import pickle

import numpy

from EMD import emd


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

        num_list_Theta = numpy.zeros((32, 2560))
        num_list_Alpha = numpy.zeros((32, 2560))
        num_list_Beta = numpy.zeros((32, 2560))
        num_list_Gamma = numpy.zeros((32, 2560))
        for p in range(0, 32):
            Theta = num['Theta'][p]
            Alpha = num['Alpha'][p]
            Beta = num['Beta'][p]
            Gamma = num['Gamma'][p]
            imf1_Theta = emd(Theta)
            print(1)
            imf1_Alpha = emd(Alpha)
            print(2)
            imf1_Beta = emd(Beta)
            print(3)
            imf1_Gamma = emd(Gamma)
            print(4)
            for m in range(0, 2560):
                for n in range(1, len(imf1_Theta)):
                    imf1_Theta[0][m] += imf1_Theta[n][m]
                print('Theta' + str(p))
                for n in range(1, len(imf1_Alpha)):
                    imf1_Alpha[0][m] += imf1_Alpha[n][m]
                print('Alpha' + str(p))
                for n in range(1, len(imf1_Beta)):
                    imf1_Beta[0][m] += imf1_Beta[n][m]
                print('Beta' + str(p))
                for n in range(1, len(imf1_Gamma)):
                    imf1_Gamma[0][m] += imf1_Gamma[n][m]
                print('Gamma' + str(p))

            num_list_Theta[p] = imf1_Theta[0]
            num_list_Alpha[p] = imf1_Alpha[0]
            num_list_Beta[p] = imf1_Beta[0]
            num_list_Gamma[p] = imf1_Gamma[0]


        dirPath = "D:/python/预处理数据集/data_EMD_python/" + process_name + "/"
        if j < 9:
            pathname = "s0" + str(j + 1) + ".dat"
        else:
            pathname = "s" + str(j + 1) + ".dat"

        dic = {'Theta': num_list_Theta, 'Alpha': num_list_Alpha, 'Beta': num_list_Beta, 'Gamma': num_list_Gamma, 'labels': labels}
        createFile()
