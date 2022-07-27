import pandas as pd
from sklearn import linear_model

df = pd.read_csv('./dataset/dataset_71_pandas.csv')
x = df.values
y = df['y'].values

# Create linear regression object
regression = linear_model.LinearRegression()

# Train the model using the training sets
regression.fit(x, y)

print(regression.predict([[10000,10000]]))
print("Coefficients: \n", regression.coef_)
