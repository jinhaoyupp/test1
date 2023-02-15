from sklearn.datasets import load_boston
from keras.models import Sequential
from keras.layers import Dense, Conv1D, Flatten
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


def nse(predictions, targets):
    nsexs = (1-(np.sum((predictions-targets)**2)/np.sum((targets-np.mean(targets))**2)))
    return nsexs


data = pd.read_csv('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/'
                   'dataprocess/tigge/dayCPnn/UKMO/cfpfcp7.csv', header=0)

datav = data.values
X = datav[:, 1:19]
y = datav[:, 19:20]
# CMA 14 CPTEC 14 ECMWF 50 JMA 26 KMA 24 NCEP 20 UKMO 17
# cma 1:16 16:17
# cptec 1:16 16:17
# ecmwf 1:52 52:53
# JMA 1:28 28:29
# KMA 1:26 26:27
# NCEP 1:22 22:23
# UKMO 1:19 19:20

PredictorScaler = StandardScaler()
TargetVarScaler = StandardScaler()

# Storing the fit object for later reference
PredictorScalerFit = PredictorScaler.fit(X)
TargetVarScalerFit = TargetVarScaler.fit(y)

# Generating the standardized values of X and y
X = PredictorScalerFit.transform(X)
y = TargetVarScalerFit.transform(y)

X_train = X[0:123,:]  # 0:113 113:134    0:123 123:144
X_test = X[123:144,:]
y_train = y[0:123,:]
y_test = y[123:144,:]

X_trainr = X_train.reshape(123, 18, 1)  # change
X_testr = X_test.reshape(21, 18, 1)

model = Sequential()
model.add(Conv1D(32, 2, activation="relu", input_shape=(18, 1)))
# change
model.add(Flatten())
model.add(Dense(64, activation="relu"))
model.add(Dense(1))
model.compile(loss="mse", optimizer="adam")
model.summary()
model.fit(X_trainr, y_train, batch_size=12, epochs=200, verbose=0)

ypred = model.predict(X_testr)
y_trainpre = model.predict(X_trainr)

ypredorig = TargetVarScalerFit.inverse_transform(ypred)
y_testorig = TargetVarScalerFit.inverse_transform(y_test)

ytrainorig = TargetVarScalerFit.inverse_transform(y_train)
y_trainpredorig = TargetVarScalerFit.inverse_transform(y_trainpre)

print(model.evaluate(X_trainr, y_train))

print("MSE: %.4f" % mean_squared_error(y_testorig, ypredorig))
print("NSE: %.4f" % nse(ypredorig.reshape(-1, 1), y_testorig))

print("MSE: %.4f" % mean_squared_error(ytrainorig, y_trainpredorig))
print("NSE: %.4f" % nse(y_trainpredorig.reshape(-1, 1), ytrainorig))

x_ax = range(len(ypred))
plt.plot(x_ax, y_testorig, lw=0.8, color="blue", label="original")
plt.plot(x_ax, ypredorig, lw=0.8, color="red", label="predicted")
plt.legend()
plt.show()

x_ax2 = range(len(y_trainpre))
plt.figure()
plt.plot(x_ax2, ytrainorig, lw=0.8, color="blue", label="original")
plt.plot(x_ax2, y_trainpredorig, lw=0.8, color="red", label="predicted")
plt.legend()
plt.show()












