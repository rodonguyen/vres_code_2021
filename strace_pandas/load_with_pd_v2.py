import pandas as pd

# Version 2: Extra 2 steps
i = 1
df = pd.read_csv("../dataset/dataset_" + str(i) + "_pandas.csv")
x_values = df['x'].values
y_values = df['y'].values

print(x_values)
print(y_values)