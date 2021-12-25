x_values = []
y_values = []
n = 100000

with open('../dataset/dataset_15.csv') as f:
    for i in range(0, n):
        x, y = f.readline().replace('\n','').split(",")
        x_values.append(x)
        y_values.append(y)

print("x values: ", x_values)
print("y values: ", y_values)
