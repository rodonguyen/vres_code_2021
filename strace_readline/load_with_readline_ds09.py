x_values = []
y_values = []

# [50,100,500,1000,2000,4000,6000,8000,10000,100000]   
n = 50

with open('./dataset/dataset_9.csv') as f:
    for i in range(0, n):
        x,y = f.readline().replace('\n','').split(",")
        x_values.append(x)
        y_values.append(y)

print(x_values)
print(y_values)
