import pandas as pd
import numpy as np  # 计算用
import matplotlib.pyplot as plt  # 绘图用
from scipy.interpolate import interp1d  # 插值用
from scipy.misc import derivative  # 求导用

data = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/cityruraldata/GDP.xlsx', sheet_name=1, header=0)

year = data['year']
gdp = data['GDP']
pergdp = data['Per capita GDP']

# plt.figure()
# plt.plot(year, gdp)
# plt.show()
#
# plt.figure()
# plt.plot(year, pergdp)
# plt.show()


plt.figure()  # figsize=[12, 8]
plt.plot(year, gdp, color='blue', marker='+', markersize=12)  # #3CB371
plt.fill_between(year, 0, gdp, facecolor='lightblue', alpha=0.3)  # #7FFFD4
# plt.xticks(year, labels, rotation=30)
# plt.ylim([840, 920])
plt.xlabel('Year', fontsize=18)
plt.ylabel('GDP per capita', fontsize=18)   # GDP per capita
plt.title('(b1)', fontsize=18)
# plt.rc('xtick', labelsize=13)
# plt.rc('ytick', labelsize=13)

plt.tick_params(labelsize=13)
plt.show()



# # 画时间序列散点图
# t=np.linspace(-0.2, 0.5, 840)#横轴
# yy = np.sin(t)            # x_test[3,0,:]  # 纵轴-0.2s~0.5s的840个数据点
# plt.scatter(t,yy,marker=".")
# plt.show()
# # 画插值拟合的曲线图
# f=interp1d(t,yy,kind="cubic")  # 'linear','zero', 'slinear', 'quadratic', 'cubic', 4, 5
# xx=np.linspace(t.min(), t.max(), 5000)
# yynew=f(xx)
# plt.plot(xx, yynew)
# plt.show()
# # 挨个求导画图
# a=np.empty((839))
# for i in range(839):
#     a[i] = derivative(f, -0.2+1/1200+1/1200*i, 1/1200)#求导，第二个参数是求导位置，第三个参数是dx
# tt = np.linspace(-0.2, 0.5-1/1200, 839)
# plt.plot(tt, a)
# plt.show()

# 画时间序列散点图
t = year  # 横轴
yy = pergdp            # x_test[3,0,:]  # 纵轴-0.2s~0.5s的840个数据点
# plt.scatter(t, yy, marker=".")
# plt.show()
# 画插值拟合的曲线图
f = interp1d(t, yy, kind="cubic")  # 'linear','zero', 'slinear', 'quadratic', 'cubic', 4, 5
xx = np.linspace(t.min(), t.max(), 5000)
yynew = f(xx)
# plt.plot(xx, yynew)
# plt.show()
# 挨个求导画图
a = np.empty((59))
for i in range(59):
    a[i] = derivative(f, 1960+1+1*i, 1)  # 求导，第二个参数是求导位置，第三个参数是dx

tt = np.linspace(1960, 2020, 59)
# plt.plot(tt, a)
# plt.show()

plt.figure()  # figsize=[12, 8]
plt.plot(tt, a, color='blue', marker='+', markersize=12)  # #3CB371
plt.fill_between(tt, 0, a, facecolor='lightblue', alpha=0.3)  # #7FFFD4
# plt.xticks(year, labels, rotation=30)
# plt.ylim([840, 920])
plt.xlabel('Year', fontsize=18)
plt.ylabel('First derivative', fontsize=18)
plt.title('(b2)', fontsize=18)
# plt.rc('xtick', labelsize=13)
# plt.rc('ytick', labelsize=13)

plt.tick_params(labelsize=13)
plt.show()




