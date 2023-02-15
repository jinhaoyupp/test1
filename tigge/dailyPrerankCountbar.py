import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 设置中文字体和负号正常显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/dayprenn/nnmetrics/metericsCount.xlsx', sheet_name=6, header=0)

# 0-7
datav = data.values
cfv = datav[0:17, 1:2]
pfv = datav[0:17, 2:3]
cfv = cfv.T
pfv = pfv.T

cfvl = cfv.tolist()
pfvl = pfv.tolist()

# cf = data[0:1]
# cf1 = cf['CMA']
# pf = data.loc['PF']

plt.figure(figsize=(14,6)) #建立图形

name = ['%d月'%x for x in range(1,13)]   #创建月份
namemodel = ['EM', 'BREM', 'MSR', 'MSREKF', 'SVMR', 'RFR', 'AdaBoost',
             'Xgboost', 'GRNN', 'DLANN', 'CNN', 'LSTM', 'Q50', 'Q70',
             'Q90', 'Q95', 'Q99']

# 'EM','BREM','MSR','MSREKF','SVMR','RFR','AdaBoost','Xgboost',...
#     'GRNN','DLANN','CNN','LSTM','Q50','Q70','Q90','Q95','Q99'

value1 = [np.random.randint(10000) for i in range(12)]   #创建随机数字
value1.sort()    #对数字进行排序
value2 = [np.random.randint(10000) for i in range(12)]   #创建随机数字
value2.sort() #对数字进行排序

x = range(17)

"""
绘制条形图
left:长条形中点横坐标
height:长条形高度
width:长条形宽度，默认值0.8
alpha:透明度
color:颜色
label:标签，为后面设置legend准备
"""
bar1 = plt.bar([i - 0.2 for i in x], height = cfvl[0], width = 0.4,
               alpha = 0.8, color = '#BA55D3',label = 'Calibration')                  #第一个图

bar2 = plt.bar([i + 0.2 for i in x],height=pfvl[0],width = 0.4,
               alpha = 0.8,color = '#00FA9A',label = 'Validation')                   #第二个图

plt.xticks(x, namemodel, rotation=30)      #设置x轴刻度显示值
# plt.ylim(0, 10500)       #y轴的范围
plt.title('(g)', fontsize=18)     #标题
plt.xlabel('Models', fontsize=18)       #x轴的标签
plt.ylabel('Rank count(100%)', fontsize=18)       #y轴的标签
plt.legend(fontsize=18)            #设置图例

# MAE(mm) RMSE(mm) NSE(100%) R2(100%) R$^2$(100%)
# Forecast underestimate rate(FUR(100%))
# Small forecast error(SFE(mm))
# Over Forecast rate(OFR(100%))
# Over Forecast error(OFE(mm))


'''
get_height:获取值
get_x：获取x轴的位置
get_width:获取图形的宽度
text(x,y,s,fontsize,ha,va)
    x,y:表示坐标值上的值
    s:表示说明文字
    fontsize:表示字体大小
    ha：垂直显示方式{'centee':'中心', 'right':'右', 'left':'左'}
    va：水平显示方式{'center':'中心', 'top':'下', 'bottom':'上', 'baseline':'基线'}
'''

for rect in bar1:
    height = rect.get_height()  #获得bar1的高度
    plt.text(rect.get_x() + rect.get_width() / 2, height*1.015, height, ha="center", va="bottom", fontsize=13)
for rect in bar2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height*1.015, height, ha="center", va="bottom", fontsize=13)

# %.2f
# plt.ylim([1.2*min([min(cfvl[0]), min(pfvl[0])]), 1.25*max([max(cfvl[0]), max(pfvl[0])])]) # nse
# plt.ylim([1.2*min([min(cfvl[0]), min(pfvl[0])]), 1.25+max([max(cfvl[0]), max(pfvl[0])])]) # small error

plt.ylim([0, 1.25*max([max(cfvl[0]), max(pfvl[0])])])

plt.tick_params(labelsize=18)
plt.show()
















