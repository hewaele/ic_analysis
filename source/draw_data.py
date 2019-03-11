import matplotlib.pyplot as plt
import pandas as pd
import os

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

import analysis_fun

dic_list = [str(i) for i in range(72, 96)]

#绘制曲线
def draw(dic, save_img):
    # 绘制错误率 准确率 漏检率 多检率 3 4 5 6
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)


    #获取错误率
    y3 = [dic[li]['error']/dic[li]['total'] for li in dic_list]
    # 获取准确率
    y4 = [(dic[li]['total'] - dic[li]['error']) / dic[li]['total'] for li in dic_list]
    #获取漏检率
    y5 = [dic[li]['miss']/ dic[li]['total'] for li in dic_list]
    #获取多检率
    y6 = [dic[li]['extra']/dic[li]['total'] for li in dic_list]
    # plt.ylim(0, 1.5)
    ax.plot(range(len(dic_list)), y3, '*-', label='error')
    ax.plot(range(len(dic_list)), y4, 'o-', label='accurate')
    ax.plot(range(len(dic_list)), y5, 'd-', label='miss')
    ax.plot(range(len(dic_list)), y6, 'r-', label='extra')

    # ax.plot(range(len(dic_list)),
    #         [(total_char_count - error_char_count) / total_char_count for i in range(len(dic_list))],
    #         '+', label='纯字符准确率')
    # ax.plot(range(len(dic_list)),
    #         [ture_id_count / total_id_count for i in range(len(dic_list))], label='id准确率')

    plt.legend(loc='center right', fontsize='large')
    ax.set_xticks(range(len(dic_list)))
    ax.set_xticklabels(dic_list, rotation=45, fontsize='small')
    ax.set_title(save_img)
    ax.set_xlabel('threshold')
    ax.grid(True)
    plt.savefig('../analysis_result/draw_data/'+save_img+'.png', dpi=300)
    plt.show()

if __name__ == '__main__':
    # 获取不同区域的字典
    id_dic = analysis_fun.get_overall_result('id')
    start_time_dic = analysis_fun.get_overall_result('start_time')
    end_time_dic = analysis_fun.get_overall_result('end_time')
    number_dic = analysis_fun.get_overall_result('number')

    draw(id_dic, 'id')
    draw(start_time_dic, 'start_time')
    draw(end_time_dic, 'end_time')
    draw(number_dic, 'number')

    # 准确率统一体
    dic_list = [str(i) for i in range(72, 96)]
    # 绘制错误率 准确率 漏检率 多检率 3 4 5 6
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # id
    y3 = [(id_dic[li]['total'] - id_dic[li]['error']) / id_dic[li]['total'] for li in dic_list]
    # start
    y4 = [(start_time_dic[li]['total'] - start_time_dic[li]['error']) / start_time_dic[li]['total'] for li in dic_list]
    # end
    y5 = [(end_time_dic[li]['total'] - end_time_dic[li]['error']) / end_time_dic[li]['total'] for li in dic_list]
    # number
    y6 = [(number_dic[li]['total'] - number_dic[li]['error']) / number_dic[li]['total'] for li in dic_list]
    # plt.ylim(0, 1.5)
    ax.plot(range(len(dic_list)), y3, '*-', label='id')
    ax.plot(range(len(dic_list)), y4, 'o-', label='start_time')
    ax.plot(range(len(dic_list)), y5, 'd-', label='end_time')
    ax.plot(range(len(dic_list)), y6, 'r-', label='number')

    # ax.plot(range(len(dic_list)),
    #         [(total_char_count - error_char_count) / total_char_count for i in range(len(dic_list))],
    #         '+', label='纯字符准确率')
    # ax.plot(range(len(dic_list)),
    #         [ture_id_count / total_id_count for i in range(len(dic_list))], label='id准确率')

    plt.legend(loc='center right', fontsize='large')
    ax.set_xticks(range(len(dic_list)))
    ax.set_xticklabels(dic_list, rotation=45, fontsize='small')
    ax.set_title('ic acuurate')
    ax.set_xlabel('threshold')
    ax.grid(True)
    plt.savefig('../analysis_result/draw_data/' + 'ic_acuurate' + '.png', dpi=300)
    plt.show()