import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

cfcount = [321, 284, 155, 231, 207, 202, 168]
pfcount = [282, 302, 134, 263, 190, 234, 163]


cfpart1 = [443, 449, 319, 486, 397, 410, 436]

cflr = [97, 92, 49, 96, 88, 77, 89]
cfmr = [75, 85, 66, 92, 94, 78, 98]
cfhr = [85, 81, 74, 94, 87, 82, 85]
cfrs = [64, 80, 77, 131, 76, 90, 70]

pfpart2 = [431, 528, 273, 496, 396, 413, 403]
pflr = [69, 125, 49, 126, 71, 72, 76]
pfmr = [75, 75, 60, 114, 78, 100, 86]
pfhr = [104, 81, 58, 84, 93, 80, 88]
pfrs = [69, 131, 62, 116, 77, 75, 58]


xais = np.arange(1, 8, 1)
namemodel = ['CMA', 'CPTEC', 'ECMWF', 'JMA', 'KMA', 'NCEP', 'UKMO']

bar1 = plt.bar(xais, pfrs, color=['red', 'orange', 'gold', 'green', 'cyan', 'blue', 'purple'])
for rect in bar1:
    height = rect.get_height()  #获得bar1的高度
    plt.text(rect.get_x() + rect.get_width() / 2, height*1.015, '% i' % height, ha="center", va="bottom", fontsize=13)

# %.2f % i
plt.xticks(xais, namemodel)
plt.ylim([0, 1.2*max(pfrs)])
plt.xlabel('Models', fontsize=13)
plt.ylabel('Count(100%)', fontsize=13)
plt.tick_params(labelsize=13)
plt.title('(d)', fontsize=15)
plt.show()










