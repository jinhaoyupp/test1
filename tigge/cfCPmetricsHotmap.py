import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/acfHB5_9/metrics.xlsx', sheet_name=7, header=0)
# 0-7
jz = data.values
jzd = jz[0:10, 1:8]

models = ['CMA','CPTEC', 'ECMWF', 'JMA', 'KMA',
          'NCEP', 'UKMO']   #7个

days = ['Day1', 'Day2', 'Day3', 'Day4', 'Day5',
        'Day6', 'Day7', 'Day8', 'Day9', 'Day10']   #5个

# df = pd.DataFrame({'Model':kind,'Indictor': region,'values':jzd})


f, ax1 = plt.subplots(figsize=(7, 7))
ax = sns.heatmap(jzd, annot=True, ax=ax1, cmap="YlGnBu",
            annot_kws={'size':9,'weight':'bold', 'color':'red'},
            cbar_kws={'label': 'OFE(mm)'})  # , vmin=0, vmax=20
# MAE(mm) RMSE(mm) NSE(100%) R2(100%) R$^2$(100%)
# Forecast underestimate rate(FUR(100%))
# Small forecast error(SFE(mm))
# Over Forecast rate(OFR(100%))
# Over Forecast error(OFE(mm))

ax.figure.axes[-1].yaxis.label.set_size(15)
ax1.set_yticklabels(days, fontsize = 12, rotation = 360, horizontalalignment='right')
ax1.set_xticklabels(models, fontsize = 12, horizontalalignment='center')
ax1.set_title('(h)', fontsize = 18)
ax1.set_ylabel('Days', fontsize = 18)
ax1.set_xlabel('Models', fontsize = 18) #横变成y轴，跟矩阵原始的布局情况是一样的
plt.show()


