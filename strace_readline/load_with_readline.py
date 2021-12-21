n = 10
x_values = []
y_values = []

with open('../dataset/dataset_5.csv') as f:
    for i in range(0, n):
        x, y = f.readline().split(",")
        x_values.append(x)
        y_values.append(y[:-1])

print("x values: ", x_values)
print("y values: ", y_values)
