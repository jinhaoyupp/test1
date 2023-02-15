import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sumcorr = [3.02708333333333,2.91250000000000,2.23125000000000,3.14583333333333,1.88958333333333,2.78541666666667,3.37291666666667,2.10208333333333,2.63541666666667]
axis = np.linspace(1, 9, 9)

labels = ['CF', 'CMA', 'CPTEC', 'ECMWF', 'JMA', 'KMA', 'NCEP', 'UKMO', 'CFPF']

color_backup = ['r', 'g', 'b', 'c', 'gray', 'orange', 'lime', 'darkblue', 'lightgreen']
plt.bar(axis, sumcorr, color=color_backup)
plt.xticks(axis, labels, fontsize=10, rotation=30)
plt.xlabel('Models', fontsize=15)
plt.ylabel('AUC(100%)', fontsize=15)
plt.tick_params(labelsize=15)
plt.show()









