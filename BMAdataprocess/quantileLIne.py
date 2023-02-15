import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# /Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/BMAresults/CF/day10/quantileT2.xlsx
# /Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/BMAresults/PF/CMA/day1/quantileT2.xlsx
# /Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/BMAresults/CFPF/day1/quantileT2.xlsx

data = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/BMAresults/CFPF/day10/quantileT2.xlsx', sheet_name=0, header=None)
obsdata = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/BMAresults/20190628obspre.xlsx', header=0)
obs = obsdata['obs']
x = np.linspace(1, 58, num=58)

q0_025 = data[0]
q0_05 = data[1]
q0_1 = data[2]
q0_15 = data[3]
q0_25 = data[4]
q0_5 = data[5]
q0_75 = data[6]
q0_85 = data[7]
q0_90 = data[8]
q0_95 = data[9]
q0_975 = data[10]

plt.fill_between(x, q0_025, q0_975, alpha=0.5, color='blue', edgecolor=None,
                label='95% confidence interval')
plt.fill_between(x, q0_05, q0_95, alpha=0.5, color='green', edgecolor=None,
                label='90% confidence interval')
plt.fill_between(x, q0_1, q0_90, alpha=0.5, color='orange', edgecolor=None,
                label='80% confidence interval')
plt.fill_between(x, q0_15, q0_85, alpha=0.5, color='cyan', edgecolor=None,
                label='70% confidence interval')
plt.fill_between(x, q0_25, q0_75, alpha=0.5, color='purple', edgecolor=None,
                label='50% confidence interval')

plt.plot(x, q0_5, color='red', linestyle='-.', linewidth=2, label='Q50')
plt.plot(x, obs, color='black', linestyle='-', linewidth=2, label='Observation')
plt.legend(ncol=2)
plt.xlabel('Grid points', fontsize=14)
plt.ylabel('Precipitation(mm)', fontsize=14)
plt.title('(j)', fontsize=14)
plt.show()












