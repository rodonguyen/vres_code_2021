import pandas as pd

df = pd.read_csv("./dataset/dataset_3_pandas.csv")
x_values = df['x'].values
y_values = df['y'].values

print(x_values)
print(y_values)