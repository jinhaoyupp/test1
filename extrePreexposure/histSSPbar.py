import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data1 = pd.read_excel('/Users/jinhaoyu/Downloads/extremePreExpo/rainfall/Compare.xlsx', sheet_name=5)
obs = data1['obs']
ssp126 = data1['ssp126']
ssp245 = data1['ssp245']
ssp370 = data1['ssp370']
ssp585 = data1['ssp585']

# ATT_LSTM = [0.8892,0.861,0.9243]
# MATT_CNN = [0.8966,0.8556,0.9316]
# ATT_RLSTM = [0.8867,0.8543,0.9344]
# CNN_RLSTM = [0.9016,0.8636,0.9435]
#x = ['REST','LAPT','AUTO']

x = np.arange(3) #总共有几组，就设置成几，我们这里有三组，所以设置为3
total_width, n = 0.7, 5 # 有多少个类型，只需更改n即可，比如这里我们对比了四个，那么就把n设成4
width = total_width / n
x = x - (total_width - width) / 2
plt.bar(x, obs, color = "r",width=width,label='Observation ')
plt.bar(x + width, ssp126, color = "y",width=width,label='SSP126')
plt.bar(x + 2 * width, ssp245 , color = "c",width=width,label='SSP245')
plt.bar(x + 3 * width, ssp370 , color = "lime",width=width,label='SSP370')
plt.bar(x + 4 * width, ssp585 , color = "g",width=width,label='SSP585')

# plt.xlabel("dataset")
plt.ylabel("Risk(%)", fontsize=13)
# Precipitation(mm)
# Number(100%)
# Risk(100%)
# Joint probability(100%)
# Risk(%)
plt.legend(loc = "best")
plt.xticks([0,1,2],['10-year','20-year','100-year'], fontsize=13)

# my_y_ticks = np.arange(0.8, 0.95, 0.02)
# plt.ylim((0.8, 0.95))
# plt.yticks(my_y_ticks)
plt.tick_params(labelsize=13)
plt.title('(b)', fontsize=13)
plt.show()

















