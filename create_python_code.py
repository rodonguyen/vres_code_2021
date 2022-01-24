dataset_length = [0,10,20,11,10,10,10,10,12,50,100,500,1000,\
    2000,4000,6000,8000,10000,50000,100000,500000,1000000,\
    5000000,10000000,50000000]


def lr_readline(dataset_length, num_files, folder_tail= '', dataset_dir = 'dataset'):
    for i in range(1,num_files+1):
        filename = "./linear_regression_readline/code_length_"+str(dataset_length)+folder_tail+"/lr_ds%02d.py" % (i)
        f = open(filename, "w") 
        f.write(                          
"""from sklearn import linear_model

x_values = []
y_values = []

n = %d

with open('./"""% (dataset_length) + dataset_dir + """/dataset_%d.csv') as f:
    for i in range(0, n):
        x,y = f.readline().replace('\\n','').split(',')
        x, y = float(x), float(y)
        x_values.append([x,y])
        y_values.append(y)

# Create linear regression object
regression = linear_model.LinearRegression()

# Train the model using the training sets
regression.fit(x_values, y_values)

print("Coefficients: \\n", regression.coef_)
""" % (i))
        f.close()


def lr_readline_length_increase(num_files):
    for i in range(0,num_files+1):
        n = dataset_length[i]
        filename = "./linear_regression_readline/lr_ds%02d.py" % (i)
        f = open(filename, "w") 
        f.write(                      
"""from sklearn import linear_model

x_values = []
y_values = []

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

print("Coefficients: \\n", regression.coef_)
""" %  (n, i))
        f.close()

def lr_pandas(dataset_length):
    for i in range(1,dataset_length+1):
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

print("Coefficients: \\n", regression.coef_)
""" % i)
        f.close()



# Run with v2 dataset_length_increase
def lr_pandas_length_increase():
    for i in range(2,6):
        for j in range(1,11):
            filename = "lr_ds_%02d_%02d.py" % (i,j)
            f = open('./linear_regression_pandas/code/dataset_length_increase/'+filename, "w")
            f.write(
"""import pandas as pd
from sklearn import linear_model

df = pd.read_csv('./dataset_length_increase/dataset_%02d_%02d.csv', header=None)
x = df.values
y = df[0].values

# Create linear regression object
regression = linear_model.LinearRegression()

# Train the model using the training sets
regression.fit(x, y)

print("Coefficients: \\n", regression.coef_)""" % (i, j))
            f.close()


# Run with v2 dataset_length_increase
def lr_readline_length_increase():
    for i in range(2,6):
        for j in range(1,11):
            filename = "lr_ds_%02d_%02d.py" % (i,j)
            f = open('./linear_regression_readline/code/dataset_length_increase/'+filename, "w")
            f.write(
"""from sklearn import linear_model

x_values = []
y_values = []
n = 0

with open('./dataset_length_increase/dataset_%02d_%02d.csv') as f:
    for i in range(0, n):
        x, y = f.readline().replace('\\n','').split(',')
        x, y = float(x), float(y)
        x_values.append([x,y])
        y_values.append(y)

# Create linear regression object
regression = linear_model.LinearRegression()

# Train the model using the training sets
regression.fit(x_values, y_values)

print("Coefficients: \\n", regression.coef_)""" % (i, j))
            f.close()


##############################################################################################

# lr_pandas_length_increase()
# lr_readline_length_increase()

# lr_pandas(90)
# lr_readline(1,90)
# lr_readline(100,12)
# lr_readline(10000,21)
# lr_readline_length_increase(24)
# lr_readline(10,13,'_add1', 'dataset_length_10_add1')
# lr_readline(10,13,'_negative1', 'dataset_length_10_negative1')
# lr_readline(100,12,'_add1', 'dataset_length_100_add1')
# lr_readline(100,12,'_negative1', 'dataset_length_100_negative1')
# lr_readline(10000,21,'_add1', 'dataset_length_10000_add1')
# lr_readline(10000,21,'_negative1', 'dataset_length_10000_negative1')
