import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn

seaborn.set()

cma = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/acfHB5_9/CMA/cfnan.xlsx', header=0)
cmaobs = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/acfHB5_9/CMA/obs.xlsx', header=0)

cptec = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/acfHB5_9/CPTEC/cf.xlsx', header=0)
cptecobs = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/acfHB5_9/CPTEC/obs.xlsx', header=0)

ecmwf = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/acfHB5_9/ECMWF/cf.xlsx', header=0)
ecmwfobs = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/acfHB5_9/ECMWF/obs.xlsx', header=0)

jma = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/acfHB5_9/JMA/cf.xlsx', header=0)
jmaobs = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/acfHB5_9/JMA/obs.xlsx', header=0)

kma = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/acfHB5_9/KMA/cf.xlsx', header=0)
kmaobs = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/acfHB5_9/KMA/obs.xlsx', header=0)

ncep = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/acfHB5_9/NCEP/cf.xlsx', header=0)
ncepobs = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/acfHB5_9/NCEP/obs.xlsx', header=0)

ukmo = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/acfHB5_9/UKMO/cf.xlsx', header=0)
ukmoobs = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/acfHB5_9/UKMO/obs.xlsx', header=0)

cmaobscp = cmaobs['obs1']

cptecobscp = cptecobs['obs10']  # obs1 obs2 obs3 obs4 obs5 obs6 obs7 obs8 obs9 obs10
date = cmaobs['date']
cmacp = cma['day10'][0:144]  # 9:153 8:152 7:151 6:150 5:149 4:148 3:147 2:146 1:145 0:144
cpteccp = cptec['day10'][0:144]  # dayn
ecmwfcp = ecmwf['day10'][0:144]
jmacp = jma['day10'][0:144]
kmacp = kma['day10'][0:144]
ncepcp = ncep['day10'][0:144]
# ukmocp = ukmo['day8'][2:146] # day1-day7

plt.plot(date, cptecobscp, color='black', label='Obs')
plt.plot(date, cmacp, color='blue', label='CMA')
# plt.plot(date, cmaobscp)
plt.plot(date, cpteccp, color='green', label='CPTEC')
plt.plot(date, ecmwfcp, color='red', label='ECMWF')
plt.plot(date, jmacp, color='cyan', label='JMA')
plt.plot(date, kmacp, color='m', label='KMA')
plt.plot(date, ncepcp, color='orange', label='NCEP')
# plt.plot(date, ukmocp, color='skyblue', label='UKMO')

plt.legend(ncol=2)
plt.xlabel('Date')
plt.ylabel('Precipitation(mm)')
plt.title('(j)')
# plt.ylim([0, 70])
plt.show()












