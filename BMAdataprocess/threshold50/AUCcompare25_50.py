import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def drawHistogram():
    matplotlib.rc("font", family='MicroSoft YaHei')
    list1 = np.array([3.57575757575758,3.77696969696970,3.41696969696970,3.33939393939394,2.56242424242424,3.28000000000000,3.48242424242424,3.48242424242424,3.53454545454546])   # 柱状图第一组数据
    list2 = np.array([3.02708333333333,2.91250000000000,2.23125000000000,3.14583333333333,1.88958333333333,2.78541666666667,3.37291666666667,2.10208333333333,2.63541666666667])   # 柱状图第二组数据
    length = len(list1)
    x = np.arange(length)   # 横坐标范围
    listDate = ["CF", "CMA", "CPTEC", "ECMWF", "JMA", "KMA", "NCEP", "UKMO", "CFPF"]

    plt.figure()
    total_width, n = 0.8, 2   # 柱状图总宽度，有几组数据
    width = total_width / n   # 单个柱状图的宽度
    x1 = x - width / 2   # 第一组数据柱状图横坐标起始位置
    x2 = x1 + width   # 第二组数据柱状图横坐标起始位置

    # plt.title("一周每天吃悠哈软糖颗数柱状图")   # 柱状图标题
    # plt.xlabel("星期")   # 横坐标label 此处可以不添加
    plt.ylabel("AUC(100%)", fontsize=15)   # 纵坐标label
    plt.bar(x1, list1, width=width, label="25 mm", color='#a8b504')
    plt.bar(x2, list2, width=width, label="50 mm", color='orange')
    plt.xticks(x, listDate)   # 用星期几替换横坐标x的值
    plt.legend()   # 给出图例
    plt.tick_params(labelsize=15, rotation=30)
    plt.show()

if __name__ == '__main__':
    drawHistogram()
























