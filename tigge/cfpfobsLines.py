import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


cma = pd.read_csv('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/dayCPnn/UKMO/cfpfcp7.csv', header=0)
# CMA 14 CPTEC 14 ECMWF 50 JMA 26 KMA 24 NCEP 20 UKMO 17 data
date = cma['date']
cf = cma['cf']
obs = cma['obs']

plt.plot(date, cf)
plt.plot(date, obs)
plt.show()

plt.figure()
cma.plot()
plt.legend(['CF', 'PF1', 'PF2', 'PF3', 'PF4', 'PF5', 'PF6',
            'PF7', 'PF8', 'PF9', 'PF10', 'PF11', 'PF12', 'PF13',
            'PF14', 'PF15', 'PF16', 'PF17', 'Obs'], ncol=4)


'''
'PF15', 'PF16', 'PF17', 'PF18', 'PF19', 'PF20', 'PF21', 'PF22',
'PF23', 'PF24', 'PF25', 'PF26', 'PF27', 'PF28', 'PF29', 'PF30',
'PF31', 'PF32', 'PF33', 'PF34', 'PF35', 'PF36', 'PF37', 'PF38',
'PF39', 'PF40', 'PF41', 'PF42', 'PF43', 'PF44', 'PF45', 'PF46',
'PF47', 'PF48', 'PF49', 'PF50',
'''

# CMA 14 CPTEC 14 ECMWF 50 JMA 26 KMA 24 NCEP 20 UKMO 17 data

plt.xticks([0, 31, 61, 92, 123], ['2019-5-1', '2019-6-1', '2019-7-1', '2019-8-1', '2019-9-1'])
plt.xlabel('Date', fontsize=13)
plt.ylabel('Precipitation(mm)', fontsize=13)
plt.title('(c7)', fontsize=13)
plt.tick_params(labelsize=13)
plt.show()






