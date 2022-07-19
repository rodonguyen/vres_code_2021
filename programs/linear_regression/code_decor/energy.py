import pandas as pd
from sklearn import linear_model

def function_start():
    print('---')

def function_end():
    print('---')


############################################
function_start()

df = pd.read_csv('data/reg/energy.csv')
x = df.iloc[:,:-2]
y = df.iloc[:,-2:]

# Create linear regression object
regression = linear_model.LinearRegression()

# Train the model using the training sets
regression.fit(x, y)

print("Dataset shape: \n", df.shape)

function_end()
############################################