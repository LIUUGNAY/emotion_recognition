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
    pickle.dump(dic, file)
    file.close()


def Classified_HAHV(data, state):
    if state == 'Theta':
        Theta_HAHV.append(data)
    if state == 'Alpha':
        Alpha_HAHV.append(data)
    if state == 'Beta':
        Beta_HAHV.append(data)
    if state == 'Gamma':
        Gamma_HAHV.append(data)


def Classified_HALV(data, state):
    if state == 'Theta':
        Theta_HALV.append(data)
    if state == 'Alpha':
        Alpha_HALV.append(data)
    if state == 'Beta':
        Beta_HALV.append(data)
    if state == 'Gamma':
        Gamma_HALV.append(data)


def Classified_LAHV(data, state):
    if state == 'Theta':
        Theta_LAHV.append(data)
    if state == 'Alpha':
        Alpha_LAHV.append(data)
    if state == 'Beta':
        Beta_LAHV.append(data)
    if state == 'Gamma':
        Gamma_LAHV.append(data)


def Classified_LALV(data, state):
    if state == 'Theta':
        Theta_LALV.append(data)
    if state == 'Alpha':
        Alpha_LALV.append(data)
    if state == 'Beta':
        Beta_LALV.append(data)
    if state == 'Gamma':
        Gamma_LALV.append(data)


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
        s = open(process_name1 + filename, "rb")
        num = pickle.load(s, encoding="latin1")
        ThetaData = num['Theta']
        # ThetaData1 = num['Theta']['ThetaData1']
        # ThetaData2 = num['Theta']['ThetaData2']
        # ThetaData3 = num['Theta']['ThetaData3']
        # ThetaData4 = num['Theta']['ThetaData4']
        AlphaData = num['Alpha']
        # AlphaData1 = num['Alpha']['AlphaData1']
        # AlphaData2 = num['Alpha']['AlphaData2']
        # AlphaData3 = num['Alpha']['AlphaData3']
        # AlphaData4 = num['Alpha']['AlphaData4']
        BetaData = num['Beta']
        # Beta1Data1 = num['Beta1']['Beta1Data1']
        # Beta1Data2 = num['Beta1']['Beta1Data2']
        # Beta1Data3 = num['Beta1']['Beta1Data3']
        # Beta1Data4 = num['Beta1']['Beta1Data4']
        GammaData = num['Gamma']
        # Beta2Data1 = num['Beta2']['Beta2Data1']
        # Beta2Data2 = num['Beta2']['Beta2Data2']
        # Beta2Data3 = num['Beta2']['Beta2Data3']
        # Beta2Data4 = num['Beta2']['Beta2Data4']

        labels = num['labels']
      #  Theta_data = np.array(ThetaData)
        # Theta_data1 = np.array(ThetaData1)    # 转换为数组存储
        # Theta_data2 = np.array(ThetaData2)
        # Theta_data3 = np.array(ThetaData3)
        # Theta_data4 = np.array(ThetaData4)
       #  Alpha_data = np.array(AlphaData)
        # Alpha_data1 = np.array(AlphaData1)
        # Alpha_data2 = np.array(AlphaData2)
        # Alpha_data3 = np.array(AlphaData3)
        # Alpha_data4 = np.array(AlphaData4)
       # Beta_data = np.array(BetaData)
        # Beta1_data1 = np.array(Beta1Data1)
        # Beta1_data2 = np.array(Beta1Data1)
        # Beta1_data3 = np.array(Beta1Data1)
        # Beta1_data4 = np.array(Beta1Data1)
        # Gamma_data = np.array(GammaData)
        # Beta2_data1 = np.array(Beta2Data1)
        # Beta2_data2 = np.array(Beta2Data2)
        # Beta2_data3 = np.array(Beta2Data3)
        # Beta2_data4 = np.array(Beta2Data4)

        Theta_HAHV = []
        Alpha_HAHV = []
        Beta_HAHV = []
        Gamma_HAHV = []

        # 高效价高唤醒度
        if labels[4] == 2 and labels[5] == 2:
            Classified_HAHV(ThetaData, 'Theta')
            Classified_HAHV(AlphaData, 'Alpha')
            Classified_HAHV(BetaData, 'Beta')
            Classified_HAHV(GammaData, 'Gamma')
            # Classified_HAHV(Theta_data1, 'Theta')
            # Classified_HAHV(Theta_data2, 'Theta')
            # Classified_HAHV(Theta_data3, 'Theta')
            # Classified_HAHV(Theta_data4, 'Theta')

            # Classified_HAHV(Alpha_data1, 'Alpha')
            # Classified_HAHV(Alpha_data2, 'Alpha')
            # Classified_HAHV(Alpha_data3, 'Alpha')
            # Classified_HAHV(Alpha_data4, 'Alpha')

            # Classified_HAHV(Beta1_data1, 'Beta1')
            # Classified_HAHV(Beta1_data2, 'Beta1')
            # Classified_HAHV(Beta1_data3, 'Beta1')
            # Classified_HAHV(Beta1_data4, 'Beta1')

            # Classified_HAHV(Beta2_data1, 'Beta2')
            # Classified_HAHV(Beta2_data2, 'Beta2')
            # Classified_HAHV(Beta2_data3, 'Beta2')
            # Classified_HAHV(Beta2_data4, 'Beta2')

        #   高唤醒度低效价
        Theta_HALV = []
        Alpha_HALV = []
        Beta_HALV = []
        Gamma_HALV = []

        if labels[4] == 1 and labels[5] == 2:
            Classified_HALV(ThetaData, 'Theta')
            Classified_HALV(AlphaData, 'Alpha')
            Classified_HALV(BetaData, 'Beta')
            Classified_HALV(GammaData, 'Gamma')
            # Classified_HALV(Theta_data1, 'Theta')
            # Classified_HALV(Theta_data2, 'Theta')
            # Classified_HALV(Theta_data3, 'Theta')
            # Classified_HALV(Theta_data4, 'Theta')
            #
            # Classified_HALV(Alpha_data1, 'Alpha')
            # Classified_HALV(Alpha_data2, 'Alpha')
            # Classified_HALV(Alpha_data3, 'Alpha')
            # Classified_HALV(Alpha_data4, 'Alpha')
            #
            # Classified_HALV(Beta1_data1, 'Beta1')
            # Classified_HALV(Beta1_data2, 'Beta1')
            # Classified_HALV(Beta1_data3, 'Beta1')
            # Classified_HALV(Beta1_data4, 'Beta1')
            #
            # Classified_HALV(Beta2_data1, 'Beta2')
            # Classified_HALV(Beta2_data2, 'Beta2')
            # Classified_HALV(Beta2_data3, 'Beta2')
            # Classified_HALV(Beta2_data4, 'Beta2')

        # LAHV
        Theta_LAHV = []
        Alpha_LAHV = []
        Beta_LAHV = []
        Gamma_LAHV = []

        if labels[4] == 2 and labels[5] == 1:
            Classified_LAHV(ThetaData, 'Theta')
            Classified_LAHV(AlphaData, 'Alpha')
            Classified_LAHV(BetaData, 'Beta')
            Classified_LAHV(GammaData, 'Gamma')
            # Classified_LAHV(Theta_data1, 'Theta')
            # Classified_LAHV(Theta_data2, 'Theta')
            # Classified_LAHV(Theta_data3, 'Theta')
            # Classified_LAHV(Theta_data4, 'Theta')
            #
            # Classified_LAHV(Alpha_data1, 'Alpha')
            # Classified_LAHV(Alpha_data2, 'Alpha')
            # Classified_LAHV(Alpha_data3, 'Alpha')
            # Classified_LAHV(Alpha_data4, 'Alpha')
            #
            # Classified_LAHV(Beta1_data1, 'Beta1')
            # Classified_LAHV(Beta1_data2, 'Beta1')
            # Classified_LAHV(Beta1_data3, 'Beta1')
            # Classified_LAHV(Beta1_data4, 'Beta1')
            #
            # Classified_LAHV(Beta2_data1, 'Beta2')
            # Classified_LAHV(Beta2_data2, 'Beta2')
            # Classified_LAHV(Beta2_data3, 'Beta2')
            # Classified_LAHV(Beta2_data4, 'Beta2')

        # LALV
        Theta_LALV = []
        Alpha_LALV = []
        Beta_LALV = []
        Gamma_LALV = []

        if labels[4] == 1 and labels[5] == 1:
            Classified_LALV(ThetaData, 'Theta')
            Classified_LALV(AlphaData, 'Alpha')
            Classified_LALV(BetaData, 'Beta')
            Classified_LALV(GammaData, 'Gamma')
            # Classified_LALV(Theta_data1, 'Theta')
            # Classified_LALV(Theta_data2, 'Theta')
            # Classified_LALV(Theta_data3, 'Theta')
            # Classified_LALV(Theta_data4, 'Theta')
            #
            # Classified_LALV(Alpha_data1, 'Alpha')
            # Classified_LALV(Alpha_data2, 'Alpha')
            # Classified_LALV(Alpha_data3, 'Alpha')
            # Classified_LALV(Alpha_data4, 'Alpha')
            #
            # Classified_LALV(Beta1_data1, 'Beta1')
            # Classified_LALV(Beta1_data2, 'Beta1')
            # Classified_LALV(Beta1_data3, 'Beta1')
            # Classified_LALV(Beta1_data4, 'Beta1')
            #
            # Classified_LALV(Beta2_data1, 'Beta2')
            # Classified_LALV(Beta2_data2, 'Beta2')
            # Classified_LALV(Beta2_data3, 'Beta2')
            # Classified_LALV(Beta2_data4, 'Beta2')

        dirPath = "D:/python/预处理数据集/data_emotionState_python/" + process_name + "/"
        if j < 9:
            pathname = "s0" + str(j + 1) + ".dat"
        else:
            pathname = "s" + str(j + 1) + ".dat"

        dic = {'Theta': {' HAHV ': Theta_HAHV, 'HALV': Theta_HALV, 'LAHV': Theta_LAHV, 'LALV': Theta_LALV},
               'Alpha': {' HAHV ': Alpha_HAHV, 'HALV': Alpha_HALV, 'LAHV': Alpha_LAHV, 'LALV': Alpha_LALV},
               'Beta': {' HAHV ': Beta_HAHV, 'HALV': Beta_HALV, 'LAHV': Beta_LAHV, 'LALV': Beta_LALV},
               'Gamma': {' HAHV ': Gamma_HAHV, 'HALV': Gamma_HALV, 'LAHV': Gamma_LAHV, 'LALV': Gamma_LALV},
               'labels': labels
               }
        createFile()



