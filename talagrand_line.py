import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
# plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))

data = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/talagrand.xlsx', sheet_name=12, header=0)
# 7-13
tg1 = data['talagrand1']
tg2 = data['talagrand2']
tg3 = data['talagrand3']
tg4 = data['talagrand4']
tg5 = data['talagrand5']
tg6 = data['talagrand6']
tg7 = data['talagrand7']
tg8 = data['talagrand8']
tg9 = data['talagrand9']
tg10 = data['talagrand10']

axis = np.linspace(start=1, stop=len(tg1), num=len(tg1))
axis2 = np.arange(1, 1+len(tg1)).astype(dtype=np.int)

# '-', '--', '-.', ':'
#
ideap = 1/len(tg1)


plt.plot(axis2, tg1, ls='-', marker='o', linewidth=2, markersize=6, color='red', label='1 day')
plt.plot(axis2, tg2, ls='-.', marker='v', linewidth=2, markersize=6, color='green', label='2 day')
plt.plot(axis2, tg3, ls='--', marker='s', linewidth=2, markersize=6, color='orange', label='3 day')
plt.plot(axis2, tg4, ls=':', marker='p', linewidth=2, markersize=6, color='purple', label='4 day')
plt.plot(axis2, tg5, ls='-', marker='*', linewidth=2, markersize=6, color='black', label='5 day')
plt.plot(axis2, tg6, ls='-.', marker='h', linewidth=2, markersize=6, color='blue', label='6 day')
plt.plot(axis2, tg7, ls='--', marker='H', linewidth=2, markersize=6, color='gray', label='7 day')
plt.plot(axis, tg8, ls=':', marker='+', linewidth=2, markersize=6, color='cyan', label='8 day')
plt.plot(axis, tg9, ls='-', marker='x', linewidth=2, markersize=6, color='#9370DB', label='9 day')
plt.plot(axis, tg10, ls='-.', marker='D', linewidth=2, markersize=6, color='#FF00FF', label='10 day')

plt.axhline(y=ideap, ls='--', linewidth=2, color='#8f8ce7', label='Ideal probability')

plt.ylim([0, 1])
plt.legend(ncol=2, fontsize=12)
plt.xlabel('Ensemble rank', fontsize=15)
plt.ylabel('Probability(100%)', fontsize=15)
plt.tick_params(labelsize=13)
plt.title('(f)', fontsize=15)
plt.show()



