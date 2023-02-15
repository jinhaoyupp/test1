import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/BMAresults/extremeIndex/thresholds.xlsx', sheet_name=8, header=0)
threshold = data['threshold']
day1 = data['day1']
day2 = data['day2']
day3 = data['day3']
day4 = data['day4']
day5 = data['day5']
day6 = data['day6']
day7 = data['day7']
day8 = data['day8']
day9 = data['day9']
day10 = data['day10']

plt.plot(threshold, day1, color='red', label='Day1', marker='*', linestyle='-', linewidth=2)
plt.plot(threshold, day2, color='orange', label='Day2', marker='.', linestyle='--', linewidth=2)
plt.plot(threshold, day3, color='green', label='Day3', marker='<', linestyle='-.', linewidth=2)
plt.plot(threshold, day4, color='cyan', label='Day4', marker='1', linestyle=':', linewidth=2)
plt.plot(threshold, day5, color='blue', label='Day5', marker='s', linestyle='-', linewidth=2)
plt.plot(threshold, day6, color='purple', label='Day6', marker='p', linestyle='--', linewidth=2)
plt.plot(threshold, day7, color='black', label='Day7', marker='h', linestyle='-.', linewidth=2)
plt.plot(threshold, day8, color='lime', label='Day8', marker='+', linestyle=':', linewidth=2)
plt.plot(threshold, day9, color='gray', label='Day9', marker='x', linestyle='-', linewidth=2)
plt.plot(threshold, day10, color='navy', label='Day10', marker='d', linestyle='--', linewidth=2)

plt.legend(fontsize=10)
plt.xlabel('Threshold', fontsize=15)
plt.ylabel('S index', fontsize=15)
plt.tick_params(labelsize=15)
plt.title('(i)', fontsize=15)
plt.show()













