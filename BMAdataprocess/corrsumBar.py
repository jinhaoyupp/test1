import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sumcorr = [1.01857805802255, 1.04014833838662, 0.0855789344566343, 0.748754828147658, -1.46418707275641, 0.102743851432570, 0.778531548009949, 0.169901546474199, 0.765863386356120]
axis = np.linspace(1, 9, 9)

labels = ['CF', 'CMA', 'CPTEC', 'ECMWF', 'JMA', 'KMA', 'NCEP', 'UKMO', 'CFPF']

color_backup = ['r', 'g', 'b', 'c', 'gray', 'orange', 'lime', 'darkblue', 'lightgreen']
plt.bar(axis, sumcorr, color=color_backup)
plt.xticks(axis, labels, fontsize=10, rotation=30)
plt.xlabel('Models', fontsize=15)
plt.ylabel('Correlation coefficient(100%)', fontsize=15)
plt.tick_params(labelsize=15)
plt.show()






















