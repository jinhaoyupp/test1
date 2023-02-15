import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def moving_average(interval, windowsize):
    window = np.ones(int(windowsize)) / float(windowsize)
    re = np.convolve(interval, window, 'same')
    return re

city = pd.read_csv('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/cityruraldata/zsjcity365y.csv', header=None)
rural = pd.read_csv('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/cityruraldata/zsjrural365y.csv', header=None)
# jjjcity365y csjcity365y zsjcity365y

citycpmax = []
citycpmaxi = []

for i in range(0, 59):
    dayvalue = city[i]
    re = moving_average(dayvalue, 5)
    recp = re*5
    maxcp = max(recp)
    maxcpi = np.argmax(recp)
    citycpmax.append(maxcp)
    citycpmaxi.append(maxcpi)


ruralcpmax = []
ruralcpmaxi = []

for i in range(0, 59):
    dayvalue = rural[i]
    re = moving_average(dayvalue, 5)
    recp = re*5
    maxcp = max(recp)
    maxcpi = np.argmax(recp)
    ruralcpmax.append(maxcp)
    ruralcpmaxi.append(maxcpi)



axis = np.linspace(1961, 2019, 59)
maxurbanm = np.mean(citycpmax)
maxruralm = np.mean(ruralcpmax)

plt.figure()
plt.plot(axis, citycpmax, color='red', linewidth=2, label='Urban')
plt.plot(axis, ruralcpmax, color='blue', linewidth=2, label='Rural')
plt.axhline(maxurbanm, color='#B8860B', linestyle='--', label='Urban maximum')
plt.text(1980, maxurbanm+5, '%.2f' % maxurbanm, fontsize=13, color='#B8860B')
plt.axhline(maxruralm, color='#008B8B', linestyle='--', label='Rural maximum')
plt.text(1990, maxruralm+5, '%.2f' % maxruralm, fontsize=13, color='#008B8B')

plt.xlabel('Year', fontsize=13)
plt.ylabel('Precipitation(mm)', fontsize=13)
plt.legend(ncol=2)
plt.title('(c1) PRD', fontsize=13)
# Beijing-Tianjin-Hebei BTH
# Yangtze River Delta YRD
# Pearl River Delta PRD
plt.show()


maxurbanim = np.mean(citycpmaxi)
maxruralim = np.mean(ruralcpmaxi)

plt.figure()
plt.plot(axis, citycpmaxi, color='red', linewidth=2, label='Urban')
plt.plot(axis, ruralcpmaxi, color='blue', linewidth=2, label='Rural')
plt.axhline(maxurbanim, color='#B8860B', linestyle='--', label='Urban maximum')
plt.text(1980, maxurbanim+5, '%.2f' % maxurbanim, fontsize=13, color='#B8860B')
plt.axhline(maxruralim, color='#008B8B', linestyle='--', label='Rural maximum')
plt.text(1990, maxruralim+5, '%.2f' % maxruralim, fontsize=13, color='#008B8B')

plt.xlabel('Year', fontsize=13)
plt.ylabel('Date(day)', fontsize=13)
plt.legend(ncol=2)
plt.title('(c2) PRD', fontsize=13)
# Beijing-Tianjin-Hebei BTH
# Yangtze River Delta YRD
# Pearl River Delta PRD
plt.show()


cityYprejz = np.array(citycpmax)
ruralYprejz = np.array(ruralcpmax)
axist = axis.T

cityYprejzre = np.reshape(cityYprejz, [len(cityYprejz), 1])
ruralYprejzre = np.reshape(ruralYprejz, [len(cityYprejz), 1])
axistre = np.reshape(axist, [len(cityYprejz), 1])

cityrural3 = np.hstack([axistre, cityYprejzre, ruralYprejzre])

np.savetxt('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/cityruraldata/maxcp/zsjp.csv', cityrural3, delimiter=',')









