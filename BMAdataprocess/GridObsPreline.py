import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/ensembleBMAdata/ensembleCF/CFday1.xlsx', header=0)
obs = data['obs']

axis = np.linspace(1, 8874, 8874)
plt.plot(axis, obs, color='#20B2AA')
plt.xlabel('Grid points', fontsize=16)
plt.ylabel('Precipitation(mm)', fontsize=16)
plt.tick_params(labelsize=16)
plt.title('(a)', fontsize=16)
plt.show()

axis2 = np.linspace(3364, 3421, 58)
pre65 = obs[3364:3422]
plt.plot(axis2, pre65, color='#7B68EE')
plt.fill_between(axis2, 0, pre65, facecolor='#6495ED', alpha=0.3)
plt.axhline(y=10, linestyle='--', color='#BC8F8F')
plt.axhline(y=25, linestyle='--', color='#F08080')
plt.axhline(y=50, linestyle='--', color='#A52A2A')
plt.xlabel('Grid points', fontsize=16)
plt.ylabel('Precipitation(mm)', fontsize=16)
plt.tick_params(labelsize=16)
plt.title('(b)', fontsize=16)
plt.show()

# interploation















