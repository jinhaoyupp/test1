import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/BMAresults/extremeIndex/Grid1CDFextreIndex.xlsx', header=0)
axis = np.linspace(0, 97, 98)
ecdf = data['grid1']
cdf1 = data['day1']
cdf2 = data['day2']
cdf3 = data['day3']
cdf4 = data['day4']
cdf5 = data['day5']
cdf6 = data['day6']
cdf7 = data['day7']
cdf8 = data['day8']
cdf9 = data['day9']
cdf10 = data['day10']

plt.plot(axis, ecdf, color='gray', label='Empirical CDF', marker='o', linestyle='-', linewidth=2)
plt.plot(axis, cdf1, color='red', label='Day1 CDF', marker='*', linestyle='-', linewidth=2)
plt.plot(axis, cdf2, color='orange', label='Day2 CDF', marker='.', linestyle='--', linewidth=2)
plt.plot(axis, cdf3, color='sandybrown', label='Day3 CDF', marker='<', linestyle='-.', linewidth=2)
plt.plot(axis, cdf4, color='green', label='Day4 CDF', marker='1', linestyle=':', linewidth=2)
plt.plot(axis, cdf5, color='cyan', label='Day5 CDF', marker='s', linestyle='-', linewidth=2)
plt.plot(axis, cdf6, color='blue', label='Day6 CDF', marker='p', linestyle='--', linewidth=2)
plt.plot(axis, cdf7, color='purple', label='Day7 CDF', marker='h', linestyle='-.', linewidth=2)
plt.plot(axis, cdf8, color='black', label='Day8 CDF', marker='+', linestyle=':', linewidth=2)
plt.plot(axis, cdf9, color='navy', label='Day9 CDF', marker='x', linestyle='-', linewidth=2)
plt.plot(axis, cdf10, color='lime', label='Day10 CDF', marker='d', linestyle='--', linewidth=2)

plt.xlabel('Precipitation(mm)', fontsize=15)
plt.ylabel('CDF(100%)', fontsize=15)
plt.legend()
plt.tick_params(labelsize=15)
plt.show()















