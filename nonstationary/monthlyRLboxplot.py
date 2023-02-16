import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

prob = pd.read_excel('/Users/jinhaoyu/Downloads/hanjiangdata/non_stationary/monthlydata/results/a257134RL.xlsx', sheet_name=0, header=0)
p25 = prob['X2.year.level']  # 2 10 20 50 100
p252 = np.array(p25)
p252[p252 < 0] = 0
p253 = pd.Series(p252)

# stationary = [65.64223,99.02469,109.92495,122.71255,131.40488]
stationary = [71.1763,115.0636,130.8981,150.6655,164.9575]
# stationary = [58.73631,88.80507,98.72478,110.43623,118.44755]
# stationary = [70.38576,112.01684,126.88264,145.3205,158.56582]
# stationary = [65.17878,102.6461,115.89365,132.2231,143.88213]
# stationary = [52.72759,77.76217,85.71221,94.88023,101.00659]
# stationary = [73.96242,124.86501,144.8487,171.16456,191.22212]
# stationary = [65.14373,112.3752,131.70902,157.85897,178.32151]
# stationary = [65.40556,108.84015,125.94009,148.49887,165.72328]
# stationary = [60.80451,91.31094,101.40591,113.34689,121.53064]
# stationary = [67.14281,109.76663,126.14172,147.41048,163.40252]
# stationary = [78.02396,144.27267,173.37311,214.5687,248.27892]
# stationary = [81.42606,153.458,186.28096,233.87197,273.73799]
# stationary = [86.79833,157.89679,189.04194,233.05349,269.00514]


over = 0
year60 = []
for i in range(1, 61):
    print(i)
    # year = 1959+i
    # yu = divmod(year, 4)
    # yu1 = yu[1]
    # if yu1 == 0:
    #     over = over + 366
    #     day = 366
    # else:
    #     over = over + 365
    #     day = 365
    over = over+12
    day = 12
    start = over-day
    yeardata = p253[start:over]
    yeardata = yeardata.to_frame()
    yeardata  = yeardata.values
    # if yu1 != 0:
    #     yeardata = np.append(yeardata, np.nan)
    #     yeardata = yeardata.reshape(366, -1)
    year60.append(yeardata)


year60array = np.array(year60)
year60array = year60array.reshape(60, 12)

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
plt.axhline(y=stationary[0], color = 'purple', linestyle = '-.', linewidth=2)
plt.text(1, stationary[0]*1.05, '%.4f' % stationary[0], fontsize=15)

plt.xticks(np.linspace(1, 12, 12), ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", '11', '12'])
# plt.ylim([0, 0.8])
# plt.ylim([0, 0.5])
# plt.ylim([0, 0.3])
# plt.ylim([0, 0.2])
# plt.ylim([0, 0.07])
plt.ylabel('Precipitation(mm)', fontsize=15)
plt.xlabel('Month', fontsize=15)
plt.title('(b1)', fontsize=15)

ax.tick_params(axis='both', which='major', labelsize=15, width=2, length=5)
# make the axis lines width larger
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
plt.show()










































































