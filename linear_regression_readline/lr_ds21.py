from sklearn import linear_model

x_values = []
y_values = []

# [50,100,500,1000,2000,4000,6000,8000,10000,100000]   
n = 1000000

with open('./dataset/dataset_21.csv') as f:
    for i in range(0, n):
        x,y = f.readline().replace('\n','').split(',')
        x, y = float(x), float(y)
        x_values.append([x,y])
        y_values.append(y)

# Create linear regression object
regression = linear_model.LinearRegression()

# Train the model using the training sets
regression.fit(x_values, y_values)

print(regression.predict([[1,2]]))
print("Coefficients: \n", regression.coef_)
