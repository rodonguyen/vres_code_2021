import pandas as pd
from sklearn import linear_model

prediction_row = 15
df_original = pd.read_csv('data/reg/vpython_trace.csv')
df = df_original.drop(prediction_row, axis=0)
x = df.iloc[:,:-1]
y = df.iloc[:,-1]

regression = linear_model.LinearRegression()
regression.fit(x, y)

print("Dataset shape: ", df.shape, x.shape, y.shape)
print("df_original:\n " + str(df))
print("Prediction row: " + str(prediction_row) + '\n' + str(df_original.iloc[prediction_row,:]))
print(f"\n>>> Actual: {df_original.iloc[prediction_row,2]}  |  Prediction: {regression.predict([df_original.iloc[prediction_row,:-1]])[0]}")
