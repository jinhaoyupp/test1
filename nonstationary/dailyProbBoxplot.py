import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

prob = pd.read_excel('/Users/jinhaoyu/Downloads/hanjiangdata/non_stationary/resultsProb_RL/a1457378P.xlsx', sheet_name=0, header=0)
p25 = prob['FCprobs5']

# stationary = [0.3369807519, 0.0711399272, 0.0190378593, 0.0060649352, 0.0008935225]
# stationary = [0.324564575, 0.071232871, 0.021040856, 0.007587485, 0.001464003]
# stationary = [0.2841018690, 0.0485326051, 0.0111267434, 0.0031473214, 0.0003901043]
# stationary = [0.351756393, 0.083928427, 0.026056520, 0.009698386, 0.001938204]
# stationary = [0.3320317675, 0.0666881780, 0.0167117829, 0.0049520598, 0.0006285295]
# stationary = [2.768720e-01, 3.918271e-02, 6.718951e-03, 1.348889e-03, 7.912468e-05]
# stationary = [0.34272236, 0.08599441, 0.02938694, 0.01221411, 0.00305360]
# stationary = [0.273268416, 0.055205845, 0.015541175, 0.005438097, 0.001015171]
# stationary = [0.242660328, 0.052592229, 0.016544862, 0.006525490, 0.001534547]
# stationary = [0.2551739032, 0.0429680547, 0.0097872472, 0.0027622716, 0.0003430407]
# stationary = [0.227028716, 0.049825663, 0.015671033, 0.006150312, 0.001425656]
# stationary = [0.279109636, 0.082288474, 0.033689915, 0.016657561, 0.005673583]
# stationary = [0.285046960, 0.080226162, 0.032026473, 0.015582525, 0.005204333]
stationary = [0.255057161, 0.074514616, 0.031253585, 0.015957592, 0.005803747]


over = 0
year60 = []
for i in range(1, 61):
    print(i)
    year = 1959+i
    yu = divmod(year, 4)
    yu1 = yu[1]
    if yu1 == 0:
        over = over + 366
        day = 366
    else:
        over = over + 365
        day = 365

    start = over-day
    yeardata = p25[start:over]
    yeardata = yeardata.to_frame()
    yeardata  = yeardata.values
    if yu1 != 0:
        yeardata = np.append(yeardata, np.nan)
        yeardata = yeardata.reshape(366, -1)
    year60.append(yeardata)


year60array = np.array(year60)
year60array = year60array.reshape(60, 366)

fig, ax = plt.subplots() # 子图
ax.boxplot(year60array,
           boxprops = {'color':'blue'},
           flierprops = {'marker':'o','markerfacecolor':'red','markeredgecolor':'red','markersize':3},
           medianprops = {'linestyle':'-','color':'orange'},
           whiskerprops={'color': "green"},  # 设置须的颜色，黑色
           capprops={'color': "green"}  # 设置箱线图顶端和末端横线的属性，颜色为绿色
           )
# ax.set_xticklabels(["1", "41", "81", "121", "161", "201", "241", "281", "281", "321", "361"])

# specifying horizontal line type
plt.axhline(y=stationary[4], color = 'purple', linestyle = '-.', linewidth=2)
plt.text(35, stationary[4]*0.85, '%.4f' % stationary[4], fontsize=15)

plt.xticks(np.linspace(1, 361, 10), ["1", "41", "81", "121", "161", "201", "241", "281", "321", "361"])
# plt.ylim([0, 0.8])
# plt.ylim([0, 0.5])
# plt.ylim([0, 0.3])
# plt.ylim([0, 0.2])
# plt.ylim([0, 0.07])
plt.ylabel('Probability(100%)', fontsize=15)
plt.xlabel('Date(day)', fontsize=15)
plt.title('(n5)', fontsize=15)

ax.tick_params(axis='both', which='major', labelsize=15, width=2, length=5)
# make the axis lines width larger
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
plt.show()





















