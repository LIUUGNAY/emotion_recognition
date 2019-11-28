
import os
import pickle
import numpy as np
# for i in range(1, 41):


def createFile():
    if os.path.exists(dirPath):
        pass  # 相当于c/Java中的空语句
        print("目录" + dirPath + "已经存在")
    else:
        os.mkdir(dirPath)
        print("创建目录" + dirPath)
    file_path = dirPath + filename
    #  print("file_path :" + file_path)
    file = open(file_path, "wb")
    #  print(str(array), array.shape)
    #  print(str(num['labels']))
    pickle.dump(dic, file)  # 将python数据转换并保存到pickle格式的文件中
    file.close()
    # file.write(array)
    # file.write(label)


for j in range(0, 32):
    process_file = 'D:/python/预处理数据集/data_preprocessed_python/data_preprocessed_python/'
    if j < 9:
        process_name = "s0" + str(j + 1)
        process_name1 = process_name + ".dat"
    else:
        process_name = "s" + str(j + 1)
        process_name1 = process_name + ".dat"
    s = open(process_file + process_name1, "rb")
    num = pickle.load(s, encoding="latin1")
    process_data = num['data']
    process_label = num['labels']
    # print(num['data'].shape)
    # data_array = np.array(process_data)
    # labels_array = np.array(process_label)
    for i in range(0, 40):
        data = process_data[i, :32, (128*23 + 1): (128 * 43 + 1)]
        # data1 = data_array[i, :32, (128 * 3 + 1): (128 * 18 + 1)]
        # data2 = data_array[i, :32, (128 * 18 + 1): (128 * 33 + 1)]
        # data3 = data_array[i, :32, (128 * 33 + 1): (128 * 48 + 1)]
        # data4 = data_array[i, :32, (128 * 48 + 1): (128 * 63 + 1)]
        labels = process_label[i, :]
        if labels[0] > 5:  # valence
            labels = np.append(labels, 2)   # 数组拼接
        else:
            labels = np.append(labels, 1)
        if labels[1] > 5:    # arousal
            labels = np.append(labels, 2)
        else:
            labels = np.append(labels, 1)
        # print(array)

        dirPath = "D:/python/预处理数据集/data_interceptData_python/" + process_name + "/"
        if i < 9:
            filename = "s0" + str(i + 1) + ".dat"
        else:
            filename = "s" + str(i + 1) + ".dat"
        dic = {'data': data, 'labels': labels}

        createFile()

#  print(filename)

# f = open("D:/python/预处理数据集/data_interceptData_python/s01.dat", "r")
# num1 = pickle.load(f)
# print(num1['data'])
# f.write(str(array))
# f.close

# f = open('D:/python/预处理数据集/data_interceptData_python/s01.dat', "rb")
# f1 = pickle.dump(f)
# num1 = pickle.load(f, encoding="latin1")
