import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


city = pd.read_csv('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/cityruraldata/csjcity365y.csv', header=None)
rural = pd.read_csv('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/cityruraldata/csjrural365y.csv', header=None)
# jjjcity365y csjcity365y zsjcity365y
# jjjrural365y csjrural365y zsjrural365y

cityYpre = np.sum(city, axis=0)
ruralYpre = np.sum(rural, axis=0)
axis = np.linspace(1961, 2019, 59)
cityYprem = np.mean(cityYpre)
ruralYprem = np.mean(ruralYpre)

plt.figure()
plt.plot(axis, cityYpre, color='red', linewidth=2, label='Urban')
plt.plot(axis, ruralYpre, color='blue', linewidth=2, label='Rural')
plt.axhline(cityYprem, color='#B8860B', linestyle='--', label='Urban mean')
plt.text(1980, cityYprem+5, '%.2f' % cityYprem, fontsize=13, color='#B8860B')
plt.axhline(ruralYprem, color='#008B8B', linestyle='--', label='Rural mean')
plt.text(1990, ruralYprem+5, '%.2f' % ruralYprem, fontsize=13, color='#008B8B')

plt.xlabel('Year', fontsize=13)
plt.ylabel('Precipitation(mm)', fontsize=13)
plt.legend(ncol=2)
plt.title('(c) PRD', fontsize=13)
# Beijing-Tianjin-Hebei BTH
# Yangtze River Delta YRD
# Pearl River Delta PRD
plt.show()

cityYprejz = np.array(cityYpre)
ruralYprejz = np.array(ruralYpre)
axist = axis.T

cityYprejzre = np.reshape(cityYprejz, [len(cityYprejz), 1])
ruralYprejzre = np.reshape(ruralYprejz, [len(cityYprejz), 1])
axistre = np.reshape(axist, [len(cityYprejz), 1])

cityrural3 = np.hstack([axistre, cityYprejzre, ruralYprejzre])

# np.savetxt('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/cityruraldata/yearpre/csj.csv', cityrural3, delimiter=',')












