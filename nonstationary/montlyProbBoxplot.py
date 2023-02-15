import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

prob = pd.read_excel('/Users/jinhaoyu/Downloads/hanjiangdata/non_stationary/monthlydata/results/a1457378P.xlsx', sheet_name=0, header=0)
p25 = prob['FCprobs5']

# stationary = [0.5350128305,0.1813980065,0.0523774145,0.0121760320,0.0002205334]
# stationary = [0.569300843,0.215595150,0.078192618,0.027050356,0.002756114]
# stationary = [4.485953e-01,1.288189e-01,3.021514e-02,5.351331e-03,3.685737e-05]
# stationary = [0.519785068,0.190377470,0.065990358,0.021510010,0.001840902]
# stationary = [0.4910185515,0.1628475219,0.0499926858,0.0140416711,0.0007975643]
# stationary = [4.306227e-01,1.006335e-01,1.617558e-02,1.376063e-03,5.391396e-09]
# stationary = [0.490728448,0.185746613,0.071675503,0.028175078,0.004589619]
# stationary = [0.518714637,0.169579840,0.059029669,0.021733018,0.003410373]
# stationary = [0.497057892,0.158862792,0.052276308,0.017685747,0.002188099]
# stationary = [5.380754e-01,1.583259e-01,3.855396e-02,7.248120e-03,6.678176e-05]
# stationary = [0.467004165,0.153081101,0.050438060,0.016703619,0.001859861]
# stationary = [0.50709449,0.20292087,0.08819761,0.04107092,0.01052418]
# stationary = [0.56870111,0.22878177,0.10183289,0.04914653,0.01380872]
stationary = [0.54902648,0.23078955,0.10436169,0.05019264,0.01350498]


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
    yeardata = p25[start:over]
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
plt.axhline(y=stationary[4], color = 'purple', linestyle = '-.', linewidth=2)
plt.text(1, stationary[4]*1.05, '%.4f' % stationary[4], fontsize=15)

plt.xticks(np.linspace(1, 12, 12), ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", '11', '12'])
# plt.ylim([0, 0.8])
# plt.ylim([0, 0.5])
# plt.ylim([0, 0.3])
# plt.ylim([0, 0.2])
# plt.ylim([0, 0.07])
plt.ylabel('Probability(100%)', fontsize=15)
plt.xlabel('Month', fontsize=15)
plt.title('(n5)', fontsize=15)

ax.tick_params(axis='both', which='major', labelsize=15, width=2, length=5)
# make the axis lines width larger
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_linewidth(2)
ax.spines['top'].set_linewidth(2)
plt.show()


#
#










































