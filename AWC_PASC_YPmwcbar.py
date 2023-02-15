import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


data = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/threeindex/awc_pasc/YP_EPT_EPmwcAwcPasc.xlsx', sheet_name=2)
# 0 1 2
awc = data['awc']
pasc = data['pasc']
#
# # PRE
# ac = [0.3672, 0.3301, 0.3588, 0.3409, 0.3026, 0.4319, 0.3753, 0.2801]
# pasc = [0.0823, 0.0161, 0.0240, 0.0492, 0.0116, 0.0575, 0.0765, 0.0219]
#
# # EP
# # ac = [0.4529, 0.4704, 0.2918, 0.2871, 0.3058, 0.4783, 0.4437, 0.3328]
# # pasc = [0.1158, 0.2340, 0.0335, 0.0260, 0.0397, 0.0971, 0.0885, 0.0674]
#
# # IBEP
# # ac = [0.4255, 0.4259, 0.3646, 0.2751, 0.3054, 0.4571, 0.3762, 0.3321]
# # pasc = [0.1641, 0.2303, 0.0384, 0, 0.0351, 0.1889, 0.0773, 0.0165]
#

similarity = awc  # similarity of action
divergence = pasc  # js diversity
# AMO AO DMI NAO Nino 3.4 NPI PDO SOI
# labels = ['AMO', 'AO', 'DMI', 'NAO', 'Nino 3.4', 'NPI', 'PDO', 'SOI']
labels = data['basin']

plt.rcParams['axes.labelsize'] = 16  # xy轴label的size
plt.rcParams['xtick.labelsize'] = 12  # x轴ticks的size
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
ax1.set_ylabel('AWC(100%)')
ax1.set_ylim(0, 1)
ax1.bar(x1_list, similarity, width=width, color='#7B68EE', align='edge', label='AWC')
# lightseagreen
plt.legend(loc='upper left')
# plt.axhline(0, 0, 6, color='gray', linestyle='--')
ax1.set_xticklabels(ax1.get_xticklabels())  # 设置共用的x轴

# 设置右侧Y轴对应的figure
ax2 = ax1.twinx()
ax2.set_ylabel('PASC(100%)')
ax2.set_ylim(0, 1)
ax2.bar(x2_list, divergence, width=width, color='#40E0D0', align='edge', tick_label=labels, label='PASC')
# tab:blue
plt.tight_layout()

plt.legend()
# plt.title('(a)')
# plt.savefig("/Users/jinhaoyu/Downloads/2篇文章/bigthessiss/大论文/pics/threeVariable/awcPascEPmwc.png")
plt.show()



























