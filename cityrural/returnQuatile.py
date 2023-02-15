import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rp = [2, 10, 20, 50, 200, 500]

# yearly pre
# bthu = [551.5, 728.4, 786.7, 856.9, 953.7, 1013.5]
# bthr = [544.6, 710.6, 766.5, 834.4, 928.8, 987.6]
# yrdu = [1051.4, 1318.3, 1426.8, 1579.4, 1840.2, 2037.3]
# yrdr = [1125.2, 1391.2, 1495.0, 1637.9, 1874.3, 2047.5]
# prdu = [1564.8, 1943.3, 2053.3, 2173.5, 2315.1, 2388.5]
# prdr = [1670.0, 2018.2, 2111.6, 2208.7, 2315.8, 2367.5]
# max daily pre
# bthu = [48.8, 86.5, 106.7, 140.2, 212.7, 281.1]
# bthr = [46.4, 78.6, 94.7, 120.4, 173.1, 220.3]
# yrdu = [60.6, 102.1, 119.1, 141.3, 174.3, 196.0]
# yrdr = [54.3, 89.0, 102.5, 119.8, 145.3, 161.7]
# prdu = [91.3, 131.3, 148.9, 174.7, 221.8, 259.6]
# prdr = [70.2, 92.9, 100.0, 108.0, 118.0, 123.5]
# max CP
bthu = [79.4,134.1,163.3,211.9,317.1,416.5]
bthr = [75.9,124.3,149.4,190.3,276.3,355.4]
yrdu = [113.9,170.6,196.9,236.8,313.1,377.2]
yrdr = [110.9,166.2,188.0,216.9,261.4,291.6]
prdu = [170.1,254.0,291.6,345.5,438.9,509.8]
prdr = [161.8,210.5,230.1,257.5,304.0,338.8]

plt.plot(rp, bthu, color='darkblue', linestyle='-', linewidth=2, label='BTH Urban')
plt.plot(rp, bthr, color='lightblue', linestyle='--', linewidth=2, label='BTH Rural')
plt.plot(rp, yrdu, color='darkred', linestyle='-', linewidth=2, label='YRD Urban')
plt.plot(rp, yrdr, color='red', linestyle='--', linewidth=2, label='YRD Rural')
plt.plot(rp, prdu, color='darkgreen', linestyle='-', linewidth=2, label='PRD Urban')
plt.plot(rp, prdr, color='lightgreen', linestyle='--', linewidth=2, label='PRD Rural')


plt.legend()
plt.xlabel('Return period(year)')
plt.ylabel('Precipitation(mm)')
plt.tick_params(labelsize=10)
plt.show()
















