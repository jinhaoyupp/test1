import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/'
                     'dayprenn/preProcessNN/DP/UKMO/NNpreProcessArrary.xlsx', sheet_name=4, header=0)
# 0-4
jz = data.values
jzd = jz[0:8, 1:18]
# jzd = np.array(jzd)
jzd[jzd == 'nan'] = np.nan
jzd = np.array(jzd, dtype=np.float)

df = pd.DataFrame(jzd)

mask = df.isnull()

models = ['9/5', '9/6', '9/7', '9/8', '9/9',
          '9/10', '9/11', '9/12', '9/13', '9/14', '9/15', '9/16', '9/17', '9/18', '9/19',
          '9/20', '9/21']   #7个

days = ['9/12', '9/11', '9/10', '9/9', '9/8',
        '9/7', '9/6', '9/5']   #5个

# df = pd.DataFrame({'Model':kind,'Indictor': region,'values':jzd})


f, ax1 = plt.subplots(figsize=(14, 7))
ax = sns.heatmap(df, annot=True, ax=ax1, cmap="jet",
            annot_kws={'size':14,'weight':'bold', 'color':'magenta'},
            cbar_kws={'label': 'Precipitation(mm)'}, mask=mask,
                 vmin=0, vmax=27)  # , vmin=0, vmax=20
# MAE(mm) RMSE(mm) NSE(100%) R2(100%) R$^2$(100%)
# Forecast underestimate rate(FUR(100%))
# Small forecast error(SFE(mm))
# Over Forecast rate(OFR(100%))
# Over Forecast error(OFE(mm))

ax.figure.axes[-1].yaxis.label.set_size(18)
ax1.set_yticklabels(days, fontsize = 18, rotation = 360, horizontalalignment='right')
ax1.set_xticklabels(models, fontsize = 18, horizontalalignment='center')
# ax1.set_title('(h)', fontsize = 18)
ax1.set_ylabel('Date', fontsize = 24)
ax1.set_xlabel('Date', fontsize = 24) #横变成y轴，跟矩阵原始的布局情况是一样的
plt.show()






















