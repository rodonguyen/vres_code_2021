dataset_length = [10,20,11,10,10,10,10,12,50,100,500,1000,\
    2000,4000,6000,8000,10000,50000,100000,500000,1000000,5000000]


def lr_readline():
    for i in range(2,22+1):
        n = dataset_length[i-1]
        filename = "lr_ds%02d.py" % (i)
        f = open(filename, "w")
        f.write(
"""from sklearn import linear_model

x_values = []
y_values = []

# [50,100,500,1000,2000,4000,6000,8000,10000,100000]   
n = %d

with open('./dataset/dataset_%d.csv') as f:
    for i in range(0, n):
        x,y = f.readline().replace('\\n','').split(',')
        x, y = float(x), float(y)
        x_values.append([x,y])
        y_values.append(y)

# Create linear regression object
regression = linear_model.LinearRegression()

# Train the model using the training sets
regression.fit(x_values, y_values)

print(regression.predict([[1,2]]))
print("Coefficients: \\n", regression.coef_)
""" % (n, i))
        f.close()

def lr_pandas():
    for i in range(1,99+1):
        filename = "lr_ds%02d.py" % (i)
        f = open('./linear_regression_pandas/code/'+filename, "w")
        f.write(
"""import pandas as pd
from sklearn import linear_model

df = pd.read_csv('./dataset/dataset_%d_pandas.csv')
x = df.values
y = df['y'].values

# Create linear regression object
regression = linear_model.LinearRegression()

# Train the model using the training sets
regression.fit(x, y)

print(regression.predict([[10000,10000]]))
print("Coefficients: \\n", regression.coef_)
""" % i)
        f.close()

lr_pandas()