import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/dayprenn/nnmetrics/metericsCount.xlsx', sheet_name=0, header=0)
data2 = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/dayprenn/nnmetrics/metericsCount.xlsx', sheet_name=1, header=0)
data3 = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/dayprenn/nnmetrics/metericsCount.xlsx', sheet_name=2, header=0)
data4 = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/dayprenn/nnmetrics/metericsCount.xlsx', sheet_name=3, header=0)
data5 = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/dayprenn/nnmetrics/metericsCount.xlsx', sheet_name=4, header=0)
data6 = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/dayprenn/nnmetrics/metericsCount.xlsx', sheet_name=5, header=0)
data7 = pd.read_excel('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/dayprenn/nnmetrics/metericsCount.xlsx', sheet_name=6, header=0)

# 0-7
datav = data.values
cfv = datav[0:17, 2:3]  # 1:2 2:3
# pfv = datav[0:17, 2:3]
# cfv = cfv.T
# # pfv = pfv.T
# cfvl = cfv.tolist()
# pfvl = pfv.tolist()

datav2 = data2.values
cfv2 = datav2[0:17, 2:3]
# cfv2 = cfv2.T
# cfvl2 = cfv2.tolist()

datav3 = data3.values
cfv3 = datav3[0:17, 2:3]
# cfv3 = cfv3.T
# cfvl3 = cfv3.tolist()

datav4 = data4.values
cfv4 = datav4[0:17, 2:3]
# cfv4 = cfv4.T
# cfvl4 = cfv4.tolist()

datav5 = data5.values
cfv5 = datav5[0:17, 2:3]
# cfv5 = cfv5.T
# cfvl5 = cfv5.tolist()

datav6 = data6.values
cfv6 = datav6[0:17, 2:3]
# cfv6 = cfv6.T
# cfvl6 = cfv6.tolist()

datav7 = data7.values
cfv7 = datav7[0:17, 2:3]
# cfv7 = cfv7.T
# cfvl7 = cfv7.tolist()

hb = np.hstack([cfv, cfv2, cfv3, cfv4, cfv5, cfv6, cfv7])
hb1 = hb[0, :]
hb1 = hb1.tolist()
hb2 = hb[1, :]
hb2 = hb2.tolist()
hb3 = hb[2, :]
hb3 = hb3.tolist()
hb4 = hb[3, :]
hb4 = hb4.tolist()
hb5 = hb[4, :]
hb5 = hb5.tolist()
hb6 = hb[5, :]
hb6 = hb6.tolist()
hb7 = hb[6, :]
hb7 = hb7.tolist()
hb8 = hb[7, :]
hb8 = hb8.tolist()
hb9 = hb[8, :]
hb9 = hb9.tolist()
hb10 = hb[9, :]
hb10 = hb10.tolist()
hb11 = hb[10, :]
hb11 = hb11.tolist()
hb12 = hb[11, :]
hb12 = hb12.tolist()
hb13 = hb[12, :]
hb13 = hb13.tolist()
hb14 = hb[13, :]
hb14 = hb14.tolist()
hb15 = hb[14, :]
hb15 = hb15.tolist()
hb16 = hb[15, :]
hb16 = hb16.tolist()
hb17 = hb[16, :]
hb17 = hb17.tolist()


category_names = ['CMA', 'CPTEC', 'ECMWF', 'JMA', 'KMA', 'NCEP', 'UKMO']

'''
'EM','BREM','MSR','MSREKF','SVMR','RFR','AdaBoost','Xgboost',...
    'GRNN','DLANN','CNN','LSTM','Q50','Q70','Q90','Q95','Q99'
'''

results = {
    'EM': hb1,
    'BREM': hb2,
    'MSR': hb3,
    'MSREKF': hb4,
    'SVMR': hb5,
    'RFR': hb6,
    'AdaBoost': hb7,
    'Xgboost': hb8,
    'GRNN': hb9,
    'DLANN': hb10,
    'CNN': hb11,
    'LSTM': hb12,
    'Q50': hb13,
    'Q70': hb14,
    'Q90': hb15,
    'Q95': hb16,
    'Q99': hb17,

}


def survey(results, category_names):
    labels = list(results.keys())
    # 获取标签
    data = np.array(list(results.values()))
    # 获取具体数值
    data_cum = data.cumsum(axis=1)
    # 逐项加和
    category_colors = plt.get_cmap('RdYlGn')(np.linspace(0.15, 0.85, data.shape[1]))

    """
    在cmmap中取出五组颜色
    category_colors:
        [[0.89888504 0.30549789 0.20676663 1.        ]
         [0.99315648 0.73233372 0.42237601 1.        ]
         [0.99707805 0.9987697  0.74502115 1.        ]
         [0.70196078 0.87297193 0.44867359 1.        ]
         [0.24805844 0.66720492 0.3502499  1.        ]]

    """

    print(category_colors)
    # 常见颜色序列， 在cmap中取色

    fig, ax = plt.subplots(figsize=(15, 9))
    # 绘图
    # ax.invert_xaxis()
    # 使其更符合视觉习惯，index本身从下到上
    # ax.yaxis.set_visible(False)
    ax.set_xticklabels(labels=labels, rotation=30, fontsize=18)
    # 不需要可见
    # ax.set_ylim(0, np.sum(data, axis=1).max())
    ax.set_ylabel('Rank count(100%)', fontsize=18)
    ax.tick_params(labelsize=18)

    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        heights = data[:, i]
        # 取第一列数值
        starts = data_cum[:, i] - heights
        # 取每段的起始点
        ax.bar(labels, heights, bottom=starts, width=0.5,
               label=colname, color=color)
        xcenters = starts + heights / 2
        r, g, b, _ = color
        text_color = '#000080' if r * g * b < 0.5 else '#000080'
        for y, (x, c) in enumerate(zip(xcenters, heights)):
            ax.text(y, x, str(int(c)), ha='center', va='center',
                    color=text_color, rotation=0, fontsize=18)
    ax.legend(fontsize=18, ncol=2)
    return fig, ax


survey(results, category_names)
plt.show()






