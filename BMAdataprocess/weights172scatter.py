import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

w1 = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/BMAresults/CFPF/weight/weight.xlsx', sheet_name=6, header=None)
# w2 = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/BMAresults/CFPF/weight/weight.xlsx', sheet_name=1, header=None)



xais = np.linspace(1, 172, 172)
plt.scatter(xais, w1[1], s=10, c='blue', marker='*')
# plt.scatter(xais, w2[1], s=10, c='red', marker='s')
plt.axvline(x=14.5, color='#32CD32', linestyle='--')
plt.axvline(x=28.5, color='#32CD32', linestyle='--')
plt.axvline(x=78.5, color='#32CD32', linestyle='--')
plt.axvline(x=104.5, color='#32CD32', linestyle='--')
plt.axvline(x=128.5, color='#32CD32', linestyle='--')
plt.axvline(x=148.5, color='#32CD32', linestyle='--')
plt.axvline(x=165.5, color='#32CD32', linestyle='--')

plt.ylabel('Weights(100%)', fontsize=13)
plt.xlabel('Ensemble members', fontsize=13)
plt.title('(h)', fontsize=13)
plt.show()

























