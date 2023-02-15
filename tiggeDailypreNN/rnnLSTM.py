from math import sqrt
from numpy import concatenate
from matplotlib import pyplot
from pandas import read_csv
from pandas import DataFrame
from pandas import concat
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import pandas as pd
import numpy as np
### Sandardization of data ###
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import GridSearchCV
from keras.layers import LSTM, Dense, Dropout


def build_classifier(optimizer):
    grid_model = Sequential()
    grid_model.add(LSTM(units = 64,input_shape = (15,1)))
    grid_model.add(Dropout(0.4))
    grid_model.add(Dense(1))

    grid_model.compile(loss = 'mse',optimizer = optimizer, metrics = ['mean_squared_error'])
    return model


def create_model():
    # create model
    # model = Sequential()
    # model.add(Dense(12, input_shape=(8,), activation='relu'))
    # model.add(Dense(1, activation='sigmoid'))
    # # Compile model
    # model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    # return model
    model = Sequential()
    # model.add(Dense(64, input_shape=(15,1), activation='relu'))
    model.add(LSTM(64, input_shape=(15, 1)))
    # model.add(Dense(1, activation='sigmoid'))
    model.add(Dense(64, activation="relu"))
    model.add(Dense(1))
    model.add(Dropout(0.3))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


def nse(predictions, targets):
    nsexs = (1-(np.sum((predictions-targets)**2)/np.sum((targets-np.mean(targets))**2)))
    return nsexs

data = pd.read_csv('/Users/jinhaoyu/Downloads/Chinasurfacepcpv2/'
                   'dataprocess/tigge/dayCPnn/CPTEC/cfpfcp2.csv', header=0)

datav = data.values
X = datav[:, 1:16]
y = datav[:, 16:17]
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

X_trainr = X_train.reshape(123, 15, 1)  # change
X_testr = X_test.reshape(21, 15, 1)


# design network
model = Sequential()
model.add(LSTM(64, input_shape=(X_trainr.shape[1], X_trainr.shape[2])))
model.add(Dense(64, activation="relu"))
model.add(Dense(1))
model.add(Dropout(0.3))
model.compile(loss='mae', optimizer='adam')

# fit network
history = model.fit(X_trainr, y_train, epochs=1500, batch_size=150, validation_data=(X_testr, y_test), verbose=2, shuffle=False)
# 50 72 600 100
# plot history
pyplot.plot(history.history['loss'], label='train')
pyplot.plot(history.history['val_loss'], label='test')
pyplot.legend()
pyplot.show()

# make a prediction
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


# grid_model = KerasClassifier(build_fn=build_classifier)
# parameters = {'batch_size' : [20, 50],
#               'epochs' : [500, 700],
#               'optimizer' : ['adam','Adadelta'] }
#
# grid_search  = GridSearchCV(estimator = grid_model,
#                             param_grid = parameters,
#                             scoring = 'accuracy',
#                             cv = 2)
#
# grid_search = grid_search.fit(X_trainr, y_train)
# best_parameters = grid_search.best_params_
# best_accuracy = grid_search.best_score_

# # create model
# model1 = KerasClassifier(build_fn=create_model, verbose=0)
# # define the grid search parameters
# batch_size = [30, 20, 40, 80, 120, 160]
# epochs = [500, 700, 1200]
# param_grid = dict(batch_size=batch_size, epochs=epochs)
# grid = GridSearchCV(estimator=model1, param_grid=param_grid, n_jobs=-1, cv=3)
# grid_result = grid.fit(X_trainr, y_train)
# # summarize results
# print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
# means = grid_result.cv_results_['mean_test_score']
# stds = grid_result.cv_results_['std_test_score']
# params = grid_result.cv_results_['params']
# for mean, stdev, param in zip(means, stds, params):
#     print("%f (%f) with: %r" % (mean, stdev, param))
#





