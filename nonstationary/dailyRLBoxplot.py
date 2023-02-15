import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

prob = pd.read_excel('/Users/jinhaoyu/Downloads/hanjiangdata/non_stationary/resultsProb_RL/a1457378RL.xlsx', sheet_name=0, header=0)
p25 = prob['X100.year.level']   # 2 10 20 50 100
p252 = np.array(p25)
p252[p252 < 0] = 0
p253 = pd.Series(p252)


# stationary = [67.67354, 108.91524, 127.19776, 153.23389, 174.66385]
# stationary = [70.85002, 119.00089, 141.58667, 174.96314, 203.44570 ]
# stationary = [58.65984, 93.45758, 108.83101, 130.67578, 148.61689]
# stationary = [74.21101, 125.18821, 148.99593, 184.07760, 213.93186 ]
# stationary = [65.3304, 103.3998, 119.9359, 143.1751, 162.0567]
# stationary = [52.61449, 79.70383, 90.82805, 105.90495, 117.72651]
# stationary = [76.06135, 136.39114, 166.40959, 212.53669, 253.42591]
# stationary = [63.76117, 107.85675, 128.61747, 159.37223, 185.68030]
# stationary = [66.97202, 119.29982, 145.41387, 185.62054, 221.32993]
# stationary = [59.08196, 93.86800, 109.26710, 131.17693, 149.19447]
# stationary = [67.96244, 120.38990, 146.37561, 186.20322, 221.42003]
# stationary = [85.14847, 173.46078, 222.68193, 304.31619, 382.23393 ]
# stationary = [83.74596, 168.92704, 216.34768, 294.93345, 369.88409]
stationary = [92.89096, 195.69092, 255.58555, 357.97798, 458.60567]


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
    yeardata = p253[start:over]
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
plt.text(35, stationary[4]*0.85, '%.1f' % stationary[4], fontsize=15)

plt.xticks(np.linspace(1, 361, 10), ["1", "41", "81", "121", "161", "201", "241", "281", "321", "361"])
# plt.ylim([0, 0.8])
# plt.ylim([0, 0.5])
# plt.ylim([0, 0.3])
# plt.ylim([0, 0.2])
# plt.ylim([0, 0.07])
plt.ylabel('Precipitation(mm)', fontsize=15)
plt.xlabel('Date(day)', fontsize=15)
plt.title('(n5)', fontsize=15)

ax.tick_params(axis='both', which='major', labelsize=15, width=2, length=5)
# make the axis lines width larger
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
# plt.ylim([0, 190])
plt.show()











































