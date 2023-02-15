import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sumcorr = [3.57575757575758,3.77696969696970,3.41696969696970,3.33939393939394,2.56242424242424,3.28000000000000,3.48242424242424,3.48242424242424,3.53454545454546]
axis = np.linspace(1, 9, 9)

labels = ['CF', 'CMA', 'CPTEC', 'ECMWF', 'JMA', 'KMA', 'NCEP', 'UKMO', 'CFPF']

color_backup = ['r', 'g', 'b', 'c', 'gray', 'orange', 'lime', 'darkblue', 'lightgreen']
plt.bar(axis, sumcorr, color=color_backup)
plt.xticks(axis, labels, fontsize=10, rotation=30)
plt.xlabel('Models', fontsize=15)
plt.ylabel('AUC(100%)', fontsize=15)
plt.tick_params(labelsize=15)
plt.show()









