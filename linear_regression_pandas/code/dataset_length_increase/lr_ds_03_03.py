import pandas as pd
from sklearn import linear_model

df = pd.read_csv('./dataset_length_increase/dataset_03_03.csv', header=None)
x = df.values
y = df[0].values

# Create linear regression object
regression = linear_model.LinearRegression()

# Train the model using the training sets
regression.fit(x, y)

print("Coefficients: \n", regression.coef_)