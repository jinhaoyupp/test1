import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel('/Users/jinhaoyu/Downloads/hanjiangdata/non_stationary/monthlydata/results/AICBICselectmodel.xlsx',
                     sheet_name=2, header=0)
data2 = data.drop('BIC', axis=1)

x_axis_labels = ['HZ','FP','ZA','SQ','AK','SZ','XX','YX','YUX','FX','LHK','NY','ZY','ZX'] # labels for x-axis
y_axis_labels = ['Model0','Model1','Model2','Model3','Model4','Model5','Model6','Model7','Model8','Model9','Model10','Model11','Model12',
                 'Model13','Model14','Model15','Model16'] # labels for y-axis

# plt.figure(figsize=(14, 12))
# sn.heatmap(data2, annot=True, fmt='0.1f', xticklabels=x_axis_labels, yticklabels=y_axis_labels,
#            cmap='RdBu_r', cbar_kws={"shrink":.8, "label": "AIC(100%)"})
# plt.show()

sns.set()
fig, ax = plt.subplots(figsize=(15, 13))
ax=sns.heatmap(data2, annot=True, fmt='0.1f', xticklabels=1, ax = ax, robust=True, square=True,cmap='jet',
               cbar_kws={"shrink":.70, "label": "BIC(100%)"},
               annot_kws={"fontsize":15}) # RdBu_r
ax.set_title('(b)', fontsize=25, fontdict={})

#configure the x and y ticks
plt.xticks(fontsize="25")
plt.yticks(np.arange(17)+0.5,y_axis_labels,
           rotation=0, fontsize="25",
           va="center") # center bottom top
# ('Model0','Model1','Model2','Model3','Model4','Model5','Model6','Model7','Model8','Model9','Model10','Model11','Model12')
ax.figure.axes[-1].yaxis.label.set_size(20)
#set labelsize of the colorbar
cbar = ax.collections[0].colorbar
cbar.ax.tick_params(labelsize=20)

plt.show()






































