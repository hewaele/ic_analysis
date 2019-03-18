#分析代码
import pandas as pd
import os

#判断当前id是否正确
def is_true(real, pre_id):
    if str(real) == str(pre_id):
        print(str(real)+'\n' + str(pre_id))
        return True
    else:
        return False

#判断当前id是否多检
def is_extra(real, pre_id):
    if len(str(real)) < len(str(pre_id)):
        return True
    else:
        return False

#判断当前id是否漏检
def is_miss(real, pre_id):
    if len(str(real)) > len(str(pre_id)):
        return True
    else:
        return False

def test(real, pre_id):
    if len(str(real)) == len(str(pre_id)) and str(real) != str(pre_id):
        print(real)
        print(pre_id)

def get_overall_result(cla = 'id'):

    real_result_path = '../analysis_result/'+ 'number' + '/real_result.csv'
    real_id_data = pd.read_csv(real_result_path)['number']
    dic = {}
    for p, n, f in os.walk('../analysis_result/'+ cla + '/'):
        for fi in f:
            print(fi)
            if fi == 'real_result.csv':
                continue
            pre_id_data = pd.read_csv(os.path.join(p, fi))[cla]
            value = fi.split('.')[1][:-4]
            dic[value] = {'total': 0, 'error': 0, 'extra': 0, 'miss': 0}
            for index in range(len(real_id_data)):
                print(index)
                if is_true(real_id_data[index], pre_id_data[index]) is not True:
                    dic[value]['error'] += 1
                if is_extra(real_id_data[index], pre_id_data[index]) is True:
                    dic[value]['extra'] += 1
                if is_miss(real_id_data[index], pre_id_data[index]) is True:
                    dic[value]['miss'] += 1
                #判断是否出现错检
                test(real_id_data[index], pre_id_data[index])

                dic[value]['total'] += 1

    return dic

if __name__ == "__main__":
    #打开真实数据
    dic = get_overall_result(cla = 'number')
    print(dic)

