import pandas as pd
import numpy as np
### Sandardization of data ###
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

def nse(predictions, targets):
    nsexs = (1-(np.sum((predictions-targets)**2)/np.sum((targets-np.mean(targets))**2)))
    return nsexs


# Defining a function to find the best parameters for ANN
def FunctionFindBestParams(X_train, y_train, X_test, y_test):
    # Defining the list of hyper parameters to try
    batch_size_list = [5, 10, 15, 20]
    epoch_list = [5, 10, 50, 100]

    import pandas as pd
    SearchResultsData = pd.DataFrame(columns=['TrialNumber', 'Parameters', 'Accuracy'])

    # initializing the trials
    TrialNumber = 0
    for batch_size_trial in batch_size_list:
        for epochs_trial in epoch_list:
            TrialNumber += 1
            # create ANN model
            model = Sequential()
            # Defining the first layer of the model
            model.add(Dense(units=10, input_dim=X_train.shape[1], kernel_initializer='normal', activation='relu'))

            # Defining the Second layer of the model
            model.add(Dense(units=10, kernel_initializer='normal', activation='relu'))

            # The output neuron is a single fully connected node
            # Since we will be predicting a single number
            model.add(Dense(1, kernel_initializer='normal'))

            # Compiling the model
            model.compile(loss='mean_squared_error', optimizer='adam')

            # Fitting the ANN to the Training set
            model.fit(X_train, y_train, batch_size=batch_size_trial, epochs=epochs_trial, verbose=0)

            # MAPE = np.mean(100 * (np.abs(y_test - model.predict(X_test)) / y_test))
            nsex = nse(model.predict(X_test), y_test)

            # printing the results of the current iteration
            print(TrialNumber, 'Parameters:', 'batch_size:', batch_size_trial, '-', 'epochs:', epochs_trial,
                  'Accuracy:', nsex)

            SearchResultsData = SearchResultsData.append(
                pd.DataFrame(data=[[TrialNumber, str(batch_size_trial) + '-' + str(epochs_trial), nsex]],
                             columns=['TrialNumber', 'Parameters', 'Accuracy']))
    return (SearchResultsData)


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

# creat a ANN model
model = Sequential()
# Defining the Input layer and FIRST hidden layer, both are same!
model.add(Dense(units=10, input_dim=18, kernel_initializer='normal', activation='relu'))
# change input_dim

# Defining the Second layer of the model
# after the first layer we don't have to specify input_dim as keras configure it automatically
model.add(Dense(units=20, kernel_initializer='normal', activation='tanh'))
model.add(Dense(units=25, kernel_initializer='normal', activation='tanh'))
# model.add(Dense(units=10, kernel_initializer='normal', activation='tanh'))
# model.add(Dense(units=10, kernel_initializer='normal', activation='tanh'))
# model.add(Dense(units=25, kernel_initializer='normal', activation='tanh'))
# model.add(Dense(units=35, kernel_initializer='normal', activation='tanh'))

# The output neuron is a single fully connected node
# Since we will be predicting a single number
model.add(Dense(1, kernel_initializer='normal'))

# Compiling the model
model.compile(loss='mean_squared_error', optimizer='adam')

# Fitting the ANN to the Training set
model.fit(X_train, y_train, batch_size=20, epochs=50, verbose=1)

######################################################
# Calling the function
ResultsData = FunctionFindBestParams(X_train, y_train, X_test, y_test)
# matplotlib inline
plt.figure(figsize=(9, 6))
plt.plot(ResultsData['Parameters'], ResultsData['Accuracy'])
plt.show()

# Fitting the ANN to the Training set
model.fit(X_train, y_train ,batch_size = 20, epochs = 50, verbose=1)

# Generating Predictions on testing data
Predictions = model.predict(X_test)
ytrainpre = model.predict(X_train)

# Scaling the predicted Price data back to original price scale
ypredorig = TargetVarScalerFit.inverse_transform(Predictions)
# Scaling the y_test Price data back to original price scale
y_test_orig = TargetVarScalerFit.inverse_transform(y_test)
# Scaling the test data back to original scale
Test_Data=PredictorScalerFit.inverse_transform(X_test)

y_trainpredorig = TargetVarScalerFit.inverse_transform(ytrainpre)
y_train_orig = TargetVarScalerFit.inverse_transform(y_train)

plt.figure()
plt.plot(y_test_orig, color='black')
plt.plot(ypredorig, color='blue')
plt.show()

plt.figure()
plt.plot(y_train_orig, color='black')
plt.plot(y_trainpredorig, color='blue')
plt.show()

nsetest = nse(ypredorig, y_test_orig)
nsetrain = nse(y_trainpredorig, y_train_orig)

print([nsetest, nsetrain])





