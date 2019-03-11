import pandas as pd
import os

#将txt文件转换成csv文件
csv_path = '../analysis_result/'

def txt2csv(source, target = None):
    source_file = open(source, 'r')
    id_list = []
    start_time = []
    end_time = []
    number_list = []

    flag = 0
    for line in source_file.readlines():
        if flag == 0:
            id_list.append(line.strip('\n'))
        if flag == 1:
            start_time.append(line.strip('\n'))
        if flag == 2:
            end_time.append(line.strip('\n'))
        if flag == 3:
            number_list.append(line.strip('\n'))

        flag = (flag + 1) % 4

    # 将信息写入csv文件
    path = csv_path +'id/'+ source_file.name.split('/')[-1][:-4] + '.csv'
    to_csv('id', id_list, path)

    path = csv_path + 'start_time/' + source_file.name.split('/')[-1][:-4] + '.csv'
    to_csv('start_time', start_time, path)

    path = csv_path + 'end_time/' + source_file.name.split('/')[-1][:-4] + '.csv'
    to_csv('end_time', end_time, path)

    path = csv_path + 'number/' + source_file.name.split('/')[-1][:-4] + '.csv'
    to_csv('number', number_list, path)


def to_csv(label, data, csv_path):
    data = pd.DataFrame({label:data})
    data.to_csv(csv_path)


if __name__ == "__main__":
    for p, n, f in os.walk('../pre_result'):
        for fi in f:
            txt2csv(os.path.join(p, fi))
