
import os
import pickle
from scipy import signal

# 分频段  Theta(4-8Hz)、Alpha(8-12Hz)、Beta1(13-20Hz)、Beta2(20-30Hz)


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
    process_file = 'D:/python/预处理数据集/data_interceptData_python/'
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
        data = num['data']
        labels = num['labels']

        # 带通滤波   bandpass
        # Wn归一化截止频率    Wn = 2*截止频率/采样频率   b: 滤波器的分子系数向量   a: 滤波器的分母系数向量
        # 采样频率为128Hz,截取频率为10Hz以下和400Hz以上,则wn1 = 2*10/128,wn2 = 2*400/128 。 Wn = [wn1 , wn2]
        # Theta 4-7Hz
        b, a = signal.butter(8, [2*4/128, 2*8/128], 'bandpass')
        ThetaData = signal.filtfilt(b, a, data)
        # ThetaData1 = signal.filtfilt(b, a, data1)
        # ThetaData2 = signal.filtfilt(b, a, data2)
        # ThetaData3 = signal.filtfilt(b, a, data3)
        # ThetaData4 = signal.filtfilt(b, a, data4)

        # Alpha 8-12Hz
        b, a = signal.butter(8, [2*8/128, 2*12/128], 'bandpass')
        AlphaData = signal.filtfilt(b, a, data)
        # AlphaData1 = signal.filtfilt(b, a, data1)
        # AlphaData2 = signal.filtfilt(b, a, data2)
        # AlphaData3 = signal.filtfilt(b, a, data3)
        # AlphaData4 = signal.filtfilt(b, a, data4)

        # Beta 13-32Hz
        b, a = signal.butter(8, [2*12/128, 2*32/128], 'bandpass')
        BetaData = signal.filtfilt(b, a, data)
        # Beta1Data1 = signal.filtfilt(b, a, data1)
        # Beta1Data2 = signal.filtfilt(b, a, data2)
        # Beta1Data3 = signal.filtfilt(b, a, data3)
        # Beta1Data4 = signal.filtfilt(b, a, data4)

        # Gamma >32Hz
        b, a = signal.butter(8, [2*32/128, 2*64/128], 'bandpass')
        GammaData = signal.filtfilt(b, a, data)
        # Beta2Data1 = signal.filtfilt(b, a, data1)
        # Beta2Data2 = signal.filtfilt(b, a, data2)
        # Beta2Data3 = signal.filtfilt(b, a, data3)
        # Beta2Data4 = signal.filtfilt(b, a, data4)

        dirPath = "D:/python/预处理数据集/data_subBand_python/" + process_name + "/"
        if j < 9:
            pathname = "s0" + str(j + 1) + ".dat"
        else:
            pathname = "s" + str(j + 1) + ".dat"

        # dic = {'Theta': {'ThetaData1': ThetaData1, 'ThetaData2': ThetaData2, 'ThetaData3': ThetaData3, 'ThetaData4': ThetaData4},
         #      'Alpha': {'AlphaData1': AlphaData1, 'AlphaData2': AlphaData2, 'AlphaData3': AlphaData3, 'AlphaData4': AlphaData4},
          #     'Beta1': {'Beta1Data1': Beta1Data1, 'Beta1Data2': Beta1Data2, 'Beta1Data3': Beta1Data3, 'Beta1Data4': Beta1Data4},
           #    'Beta2': {'Beta2Data1': Beta2Data1, 'Beta2Data2': Beta2Data2, 'Beta2Data3': Beta2Data3, 'Beta2Data4': Beta2Data4},
            #   'labels': labels}

        dic = {'Theta': ThetaData, 'Alpha': AlphaData, 'Beta': BetaData, 'Gamma': GammaData, 'labels': labels}
        createFile()
