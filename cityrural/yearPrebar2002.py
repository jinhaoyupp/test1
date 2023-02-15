import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/cityruraldata/maxcp/zsj.csv', header=0)

urban1 = data['urban'][0:41]
urban2 = data['urban'][41:]

rural1 = data['rural'][0:41]
rural2 = data['rural'][41:]

urban1m = np.mean(urban1)
urban2m = np.mean(urban2)

rural1m = np.mean(rural1)
rural2m = np.mean(rural2)

name_list = ['Urban', 'Rural']

num_list = [urban1m, rural1m]
num_list1 = [urban2m, rural2m]

# x = list(range(len(num_list)))
# total_width, n = 0.4, 2
# width = total_width / n
#
# plt.bar(x, num_list, width=width, label='boy', fc='y')
# for i in range(len(x)):
#     x[i] = x[i] + width
# plt.bar(x, num_list1, width=width, label='girl', tick_label=name_list, fc='r')
# plt.legend()
# plt.show()


x = np.arange(len(name_list))  # x轴刻度标签位置
width = 0.25  # 柱子的宽度
# 计算每个柱子在x轴上的位置，保证x轴刻度标签居中
# x - width/2，x + width/2即每组数据在x轴上的位置
plt.bar(x - width/2, num_list, width, label='Before 2002')
plt.bar(x + width/2, num_list1, width, label='After 2002')
plt.text(-0.23, 130, '%.2f' % urban1m, fontsize=16)
plt.text(0.03, 125, '%.2f' % urban2m, fontsize=16)
plt.text(0.78, 130, '%.2f' % rural1m, fontsize=16)
plt.text(1.03, 125, '%.2f' % rural2m, fontsize=16)

plt.ylabel('Date(day)', fontsize=18)  # Precipitation(mm)  Date(day)
plt.title('(c2)', fontsize=18)
# x轴刻度标签位置不进行计算
plt.xticks(x, labels=name_list, fontsize=18)
plt.legend(loc='lower left', fontsize=18)
plt.tick_params(labelsize=13)
plt.show()

print(num_list, num_list1)



