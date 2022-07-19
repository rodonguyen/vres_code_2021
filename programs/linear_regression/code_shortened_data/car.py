import pandas as pd
from sklearn import linear_model

def function_start():
    print('---')

def function_end():
    print('---')

############################################
function_start()

df = pd.read_csv('data/reg/car_shortened.csv')
x = df.iloc[:,:-1]
y = df.iloc[:,-1]

regression = linear_model.LinearRegression()
regression.fit(x, y)

print("Row 1 prediction: " + str(regression.predict([x.iloc[0,:]])))
print("Dataset shape: ", df.shape, x.shape, y.shape)

function_end()
############################################