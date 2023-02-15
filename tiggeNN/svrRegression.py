from sklearn.datasets import load_boston
from keras.models import Sequential
from keras.layers import Dense, Conv1D, Flatten
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
import time


def nse(predictions, targets):
    nsexs = (1-(np.sum((predictions-targets)**2)/np.sum((targets-np.mean(targets))**2)))
    return nsexs

svr = GridSearchCV(
    SVR(kernel="rbf", gamma=0.1),
    param_grid={"C": [1e0, 1e1, 1e2, 1e3], "gamma": np.logspace(-2, 2, 5),
                "epsilon":np.logspace(-2, 2, 5)},
)


data = pd.read_csv('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/dataprocess/tigge/cfpfNN/UKMO/withdate/cfpfnn8.csv', header=0)

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

X_train = X[0:114,:]  # 0:104 104:134    0:114 114:144
X_test = X[114:144,:]
y_train = y[0:114,:]
y_test = y[114:144,:]

regr = make_pipeline(StandardScaler(), SVR(C=1.0, epsilon=0.2))
regr.fit(X_train, y_train)


# Use the forest's predict method on the test data
ypred = regr.predict(X_test)
y_trainpred = regr.predict(X_train)

ypredorig = TargetVarScalerFit.inverse_transform(ypred)
y_trainpredorig = TargetVarScalerFit.inverse_transform(y_trainpred)

y_testorig = TargetVarScalerFit.inverse_transform(y_test)
y_trainorig = TargetVarScalerFit.inverse_transform(y_train)

print("MSE: %.4f" % mean_squared_error(y_testorig, ypredorig))
print("NSE: %.4f" % nse(ypredorig.reshape(-1, 1), y_testorig))

print("MSE: %.4f" % mean_squared_error(y_trainorig, y_trainpredorig))
print("NSE: %.4f" % nse(y_trainpredorig.reshape(-1, 1), y_trainorig))

x_ax = range(len(ypred))
plt.plot(x_ax, y_testorig, lw=0.8, color="blue", label="original")
plt.plot(x_ax, ypredorig, lw=0.8, color="red", label="predicted")
plt.legend()
plt.show()

x_ax2 = range(len(y_trainpred))
plt.figure()
plt.plot(x_ax2, y_trainorig, lw=0.8, color="blue", label="original")
plt.plot(x_ax2, y_trainpredorig, lw=0.8, color="red", label="predicted")
plt.legend()
plt.show()

# t0 = time.time()
# svr.fit(X_train, y_train)
# svr_fit = time.time() - t0
# print(f"Best SVR with params: {svr.best_params_} and R2 score: {svr.best_score_:.3f}")
# print("SVR complexity and bandwidth selected and model fitted in %.3f s" % svr_fit)







