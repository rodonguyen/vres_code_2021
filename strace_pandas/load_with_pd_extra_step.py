import pandas as pd

i = 3
df = pd.read_csv("../dataset/dataset_" + i + "_pandas.csv")
x_values = df['x'].values
y_values = df['y'].values

print(x_values)
print(y_values)