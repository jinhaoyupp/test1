import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data = pd.read_excel('/Users/jinhaoyu/Downloads/extremePreExpo/rainfall/CompareDivise.xlsx', sheet_name=3)

similarity = data['small']  # similarity of action
divergence = data['area2']  # js diversity
labels = ['SSP585 90-90', 'SSP585 90-95', 'SSP585 90-99']

plt.rcParams['axes.labelsize'] = 14  # xy轴label的size
plt.rcParams['xtick.labelsize'] = 14  # x轴ticks的size
plt.rcParams['ytick.labelsize'] = 14  # y轴ticks的size
# plt.rcParams['legend.fontsize'] = 12  # 图例的size

# 设置柱形的间隔
width = 0.3  # 柱形的宽度
x1_list = []
x2_list = []
for i in range(len(similarity)):
    x1_list.append(i)
    x2_list.append(i + width)

# 创建图层
fig, ax1 = plt.subplots()

# 设置左侧Y轴对应的figure
ax1.set_ylabel('Risk margin(%)')
# ax1.set_ylim(0, 2.5)  # large
ax1.set_ylim(-1.6, 0)  # small
ax1.bar(x1_list, similarity, width=width, color='deepskyblue', align='edge', label='Risk margin')

ax1.set_xticklabels(ax1.get_xticklabels())  # 设置共用的x轴
# plt.legend(frameon=False)

# 设置右侧Y轴对应的figure
ax2 = ax1.twinx()
ax2.set_ylabel('Area ratio(100%)')
ax2.set_ylim(0, 1)
ax2.bar(x2_list, divergence, width=width, color='blueviolet', align='edge', tick_label=labels, label='Area ratio')

plt.tight_layout()
# plt.savefig("similarity.png")
plt.title('(d2)', fontsize=14)
# plt.legend(loc='upper right', bbox_to_anchor=(0.97, 0.93), frameon=False)
plt.show()












