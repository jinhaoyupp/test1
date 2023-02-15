# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd


name_list = ['CF', 'CMA', 'CPTEC', 'ECMWF', 'JMA', 'KMA', 'NCEP', 'UKMO', 'CFPF']
data = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/BMAresults/metrics/quantileRank/OBCItotalModels.xlsx')
q50 = data['ci95']
q70 = data['ci90']
q90 = data['ci80']
q95 = data['ci70']
q99 = data['ci50']

#
# num_list = [1.5, 0.6, 7.8, 6]
# num_list1 = [1, 2, 3, 1]
x = list(range(len(q50)))
total_width, n = 0.6, 4
width = total_width / n

plt.bar(x, q50, width=width, label='95% CI', fc='red')

for i in range(len(x)):
    print(i)
    x[i] = x[i] + width


plt.bar(x, q70, width=width, label='90% CI', fc='orange')
for i in range(len(x)):
    print(i)
    x[i] = x[i] + width
plt.bar(x, q90, width=width, label='80% CI', tick_label=name_list, fc='green')
for i in range(len(x)):
    print(i)
    x[i] = x[i] + width
plt.bar(x, q95, width=width, label='70% CI', fc='blue')
for i in range(len(x)):
    print(i)
    x[i] = x[i] + width
plt.bar(x, q99, width=width, label='50% CI', fc='purple')
plt.legend(ncol=2)
plt.ylabel('OBCI')
plt.show()






















