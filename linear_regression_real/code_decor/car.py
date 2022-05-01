import pandas as pd
from sklearn import linear_model

def function_start():
    print('--- start')

def function_end():
    print('--- end')

############################################
function_start()

df = pd.read_csv('dataset_real/car.csv')
x = df.iloc[:,:-1]
y = df.iloc[:,-1:]

# Create linear regression object
regression = linear_model.LinearRegression()
# Train the model using the training sets
regression.fit(x, y)

print("Dataset shape: \n", df.shape)

function_end()
############################################










########################## INITIAL FULL CODE ###########################

# import warnings
# warnings.filterwarnings('ignore')

# #importing the libraries
# import numpy as np
# import pandas as pd

# cars = pd.read_csv('dataset_additional/car.csv')

# CompanyName = cars['CarName'].apply(lambda x : x.split(' ')[0])
# cars.insert(3,"CompanyName",CompanyName)
# cars.drop(['CarName'],axis=1,inplace=True)

# cars.CompanyName = cars.CompanyName.str.lower()

# def replace_name(a,b):
#     cars.CompanyName.replace(a,b,inplace=True)

# replace_name('maxda','mazda')
# replace_name('porcshce','porsche')
# replace_name('toyouta','toyota')
# replace_name('vokswagen','volkswagen')
# replace_name('vw','volkswagen')


# cars['fueleconomy'] = (0.55 * cars['citympg']) + (0.45 * cars['highwaympg'])
# cars['price'] = cars['price'].astype('int')
# temp = cars.copy()
# table = temp.groupby(['CompanyName'])['price'].mean()
# temp = temp.merge(table.reset_index(), how='left',on='CompanyName')
# bins = [0,10000,20000,40000]
# cars_bin=['Budget','Medium','Highend']
# cars['carsrange'] = pd.cut(temp['price_y'],bins,right=False,labels=cars_bin)

# def dummies(x,df):
#     temp = pd.get_dummies(df[x], drop_first = True)
#     df = pd.concat([df, temp], axis = 1)
#     df.drop([x], axis = 1, inplace = True)
#     return df
# # Applying the function to the cars_lr

# cars_lr = cars[['price', 'fueltype', 'aspiration','carbody', 'drivewheel','wheelbase',
#                   'curbweight', 'enginetype', 'cylindernumber', 'enginesize', 'boreratio','horsepower', 
#                     'fueleconomy', 'carlength','carwidth', 'carsrange']]
# cars_lr = dummies('fueltype',cars_lr)
# cars_lr = dummies('aspiration',cars_lr)
# cars_lr = dummies('carbody',cars_lr)
# cars_lr = dummies('drivewheel',cars_lr)
# cars_lr = dummies('enginetype',cars_lr)
# cars_lr = dummies('cylindernumber',cars_lr)
# cars_lr = dummies('carsrange',cars_lr)


# from sklearn.model_selection import train_test_split

# np.random.seed(0)
# df_train, df_test = train_test_split(cars_lr, train_size = 0.7, test_size = 0.3, random_state = 100)

# from sklearn.preprocessing import MinMaxScaler

# scaler = MinMaxScaler()
# num_vars = ['wheelbase', 'curbweight', 'enginesize', 'boreratio', 'horsepower','fueleconomy','carlength','carwidth','price']
# df_train[num_vars] = scaler.fit_transform(df_train[num_vars])

# y_train = df_train.pop('price')
# X_train = df_train

# from sklearn.linear_model import LinearRegression


# lm = LinearRegression()
# lm.fit(X_train,y_train)

# print("Coefficients: \n", lm.coef_)