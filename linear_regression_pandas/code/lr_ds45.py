import pandas as pd
from sklearn import linear_model

df = pd.read_csv('./dataset/dataset_45_pandas.csv')
x = df.values
y = df['y'].values

# Create linear regression object
regression = linear_model.LinearRegression()

# Train the model using the training sets
regression.fit(x, y)

print("Coefficients: \n", regression.coef_)
