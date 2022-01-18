from sklearn import linear_model

x_values = []
y_values = []

n = 10000

with open('./dataset_length_10000_negative1/dataset_8.csv') as f:
    for i in range(0, n):
        x,y = f.readline().replace('\n','').split(',')
        x, y = float(x), float(y)
        x_values.append([x,y])
        y_values.append(y)

# Create linear regression object
regression = linear_model.LinearRegression()

# Train the model using the training sets
regression.fit(x_values, y_values)

print("Coefficients: \n", regression.coef_)
