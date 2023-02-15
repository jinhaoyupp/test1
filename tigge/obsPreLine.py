import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
import pandas as pd
from sklearn.linear_model import LinearRegression
from statsmodels.formula.api import ols
from scipy.interpolate import interp1d
import matplotlib.ticker as mticker


data = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/acfHB5_9/CPTEC/cf.xlsx', header=0)

plt.figure()
ax = plt.subplot(111)
# x=np.arange(1,40,1)
# y=np.array([0,1,3,2,4,5,7,6,21,15,
#             19,23,27,14,10,5,4,7,5,
#             8,3,9,11,22,29,31,34,27,
#             40,52,33,20,19,16,14,60,
#             55,54,5])

x = np.arange(0, 153, 1)
y = data['obs']

xnew=np.linspace(0,152,100)
f=interpolate.interp1d(x,y,kind='quadratic')
ynew=f(xnew)
points=np.array([xnew,ynew]).T.reshape(-1,1,2)
lw=1
# cmap=plt.get_cmap('Reds')
cmap=plt.get_cmap('Spectral_r')

ystd = np.std(y)
ymean = np.mean(y)
x_in = np.array(x).reshape(-1, 1)
y_in = np.array(y).reshape(-1, 1)
lreg = LinearRegression()
lreg.fit(x_in, y_in)
y_prd = lreg.predict(x_in)

data = pd.DataFrame({'x': x, 'y': y})
model = ols('y~x', data).fit()
print(model.summary())
print(ymean, ystd)

linear_interp = interp1d(x, y_prd.transpose()[0], kind='linear')
computed = np.linspace(min(x), max(x), 20)
linear_results = linear_interp(computed)


for i,c in zip(range(points.shape[0]),ynew):
    if i<range(points.shape[0])[-2]:
        ax.plot((points[i,0,0],points[i+1,0,0]),
                (points[i,0,1],points[i+1,0,1]),
                color='k',lw=lw)
        ax.fill_between((points[i,0,0],points[i+1,0,0]),
                        (points[i,0,1],points[i+1,0,1]),
                        facecolor=cmap((ynew[i]+ynew[i+1])/2/max(ynew)),
                        interpolate=True,zorder=5)
    else:
        ax.plot((points[i-1,0,0],points[i,0,0]),
                (points[i-1,0,1],points[i,0,1]),
                color='k',lw=lw)
        ax.fill_between((points[i-1,0,0],points[i,0,0]),
                        (points[i-1,0,1],points[i,0,1]),
                        facecolor=cmap(c/max(ynew)),interpolate=True,zorder=5)

# 线性拟合结果
# plt.plot(computed, linear_results, linestyle='--', color='lime', label='Trend line', linewidth=2)  # lime green

plt.ticklabel_format(style='plain', axis='x', useOffset=False)
plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(1))
# surge
# plt.text(1985, 0.03, 'y=0.0002x-0.6303, R$^2$=0.126 \n P-value=0.0466 \n Mean=-0.185, STD=0.007',
#          color='blue')
# plt.ylim([-0.3, 0.10])

# date
# plt.text(2003, 31, 'y=-0.0458x+118.1910, R$^2$=0.011 \n P-value=0.670 \n Mean=26.230, STD=2.395',
#          color='blue')

plt.ylim([0, 37])

plt.axvline(x=123, ymin=0, ymax=37, color='b', linestyle='-.')
plt.axvline(x=127, ymin=0, ymax=37, color='#BA55D3', linestyle='--')
plt.axvline(x=134, ymin=0, ymax=37, color='#BA55D3', linestyle='--')


# plt.legend()
plt.xticks([0, 31, 61, 92, 123], ['2019-5-1', '2019-6-1', '2019-7-1', '2019-8-1', '2019-9-1'])
plt.xlabel('Date', color='b')
# plt.colorbar()
# plt.ylabel('Surge(m)', color='b')
plt.ylabel('Precipitation(mm)', color='b')
plt.xticks(color='b', rotation=0)
plt.yticks(color='b')
# plt.title('(a)')
plt.show()























