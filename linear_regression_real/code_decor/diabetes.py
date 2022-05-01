# Code source: Jaques Grobler
# License: BSD 3 clause
from sklearn import datasets, linear_model
import pandas as pd

def function_start():
    print('--- start')

def function_end():
    print('--- end')


############################################
function_start()

# Load the diabetes dataset
X, y = datasets.load_diabetes(return_X_y=True)

# Create linear regression object
regression = linear_model.LinearRegression()

# Train the model using the training sets
regression.fit(X, y)

print("Dataset shape: \n", X.shape, y.shape)


function_end()
############################################












########################## INITIAL FULL CODE ###########################

# # Code source: Jaques Grobler
# # License: BSD 3 clause

# import numpy as np
# from sklearn import datasets, linear_model
# from sklearn.metrics import mean_squared_error, r2_score

# # Load the diabetes dataset
# diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)
# temp = datasets.load_diabetes(return_X_y=False)
# print(diabetes_X.shape, diabetes_y.shape)

# # Use only one feature
# diabetes_X = diabetes_X[:, np.newaxis, 2]

# # Split the data into training/testing sets
# diabetes_X_train = diabetes_X[:-20]
# diabetes_X_test = diabetes_X[-20:]

# # Split the targets into training/testing sets
# diabetes_y_train = diabetes_y[:-20]
# diabetes_y_test = diabetes_y[-20:]

# # Create linear regression object
# regr = linear_model.LinearRegression()

# # Train the model using the training sets
# regr.fit(diabetes_X_train, diabetes_y_train)

# # Make predictions using the testing set
# diabetes_y_pred = regr.predict(diabetes_X_test)

# # The coefficients
# print("Coefficients: \n", regr.coef_)
# # The mean squared error
# print("Mean squared error: %.2f" % mean_squared_error(diabetes_y_test, diabetes_y_pred))
# # The coefficient of determination: 1 is perfect prediction
# print("Coefficient of determination: %.2f" % r2_score(diabetes_y_test, diabetes_y_pred))