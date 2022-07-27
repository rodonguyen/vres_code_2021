import pandas as pd
from sklearn import linear_model

def function_start():
    print('---')

def function_end():
    print('---')

############################################
function_start()

# RANDOM_SEED = 42

df = pd.read_csv('data/reg/car.csv')
x = df.iloc[:,1:-1]
y = df.iloc[:,-1:]

# Create linear regression object
regression = linear_model.LinearRegression()
# Train the model using the training sets
regression.fit(x, y)

print("Row 1 prediction: " + str(regression.predict([x.iloc[0,:]] )))
print("Dataset shape: \n", df.shape, x.shape, y.shape)

function_end()
############################################