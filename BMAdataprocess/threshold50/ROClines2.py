import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fpr = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/BMAresults/extremeIndex/threshold50mm/falsePositiveRate.xlsx', sheet_name=8, header=0)
tpr = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/BMAresults/extremeIndex/threshold50mm/turePositiveRate.xlsx', sheet_name=8, header=0)

fday1 = fpr['day1']
fday2 = fpr['day2']
fday3 = fpr['day3']
fday4 = fpr['day4']
fday5 = fpr['day5']
fday6 = fpr['day6']
fday7 = fpr['day7']
fday8 = fpr['day8']
fday9 = fpr['day9']
fday10 = fpr['day10']

tday1 = tpr['day1']
tday2 = tpr['day2']
tday3 = tpr['day3']
tday4 = tpr['day4']
tday5 = tpr['day5']
tday6 = tpr['day6']
tday7 = tpr['day7']
tday8 = tpr['day8']
tday9 = tpr['day9']
tday10 = tpr['day10']

fig,ax=plt.subplots(figsize=(7,7))

plt.plot(fday1, tday1, color='red', label='Day1', marker='*', linestyle='-', linewidth=2)
plt.plot(fday2, tday2, color='orange', label='Day2', marker='.', linestyle='--', linewidth=2)
plt.plot(fday3, tday3, color='sandybrown', label='Day3', marker='<', linestyle='-.', linewidth=2)
plt.plot(fday4, tday4, color='green', label='Day4', marker='1', linestyle=':', linewidth=2)
plt.plot(fday5, tday5, color='cyan', label='Day5', marker='s', linestyle='-', linewidth=2)
plt.plot(fday6, tday6, color='blue', label='Day6', marker='p', linestyle='--', linewidth=2)
plt.plot(fday7, tday7, color='purple', label='Day7', marker='h', linestyle='-.', linewidth=2)
plt.plot(fday8, tday8, color='black', label='Day8', marker='+', linestyle=':', linewidth=2)
plt.plot(fday9, tday9, color='navy', label='Day9', marker='x', linestyle='-', linewidth=2)
plt.plot(fday10, tday10, color='lime', label='Day10', marker='d', linestyle='--', linewidth=2)

Axis_line=np.linspace(*ax.get_xlim(),2)
ax.plot(Axis_line,Axis_line,transform=ax.transAxes,linestyle='--',linewidth=2,color='gray',label="1:1 Line")

plt.xlabel('False positive rate(100%)', fontsize=15)
plt.ylabel('True positive rate(100%)', fontsize=15)
plt.legend(ncol=2, fontsize=12)
plt.tick_params(labelsize=15)
plt.title('(i)', fontsize=15)
plt.show()













































