import pandas as pd
from sklearn import linear_model

def function_start():
    print('--- start')

def function_end():
    print('--- end')


############################################
function_start()

df = pd.read_csv('dataset_real/energy.csv')
x = df.iloc[:,:-2]
y = df.iloc[:,-2:]

# Create linear regression object
regression = linear_model.LinearRegression()

# Train the model using the training sets
regression.fit(x, y)

print("Dataset shape: \n", df.shape)

function_end()
############################################

















########################## INITIAL FULL CODE ###########################

# import pandas as pd
# import numpy as np
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.linear_model import LinearRegression
# from sklearn.naive_bayes import GaussianNB
# import math


# df = pd.read_csv('dataset_additional/energy.csv')

# from scipy import stats as st
# z = np.abs(st.zscore(df))

# train, validate, test = np.split(df.sample(frac=1, random_state=42),
#                                 [int(.6*len(df)), int(.8*len(df))])



# #now i split x columns and y columns
# x_train = train.iloc[:,:-2]
# y_train = train.iloc[:,8:]
# x_valid = validate.iloc[:,:-2]
# y_valid = validate.iloc[:,8:]
# x_test = test.iloc[:,:-2]
# y_test = test.iloc[:,8:]

# def rmse(x,y):
#     return math.sqrt(((x-y)**2).mean())

# def print_score(m):
#     m.fit(x_train,y_train)
#     print(f"R^2 of train set: {m.score(x_train, y_train)}")
#     print(f"R^2 of validation set: {m.score(x_valid, y_valid)}")


# m = RandomForestRegressor(n_estimators=10, n_jobs=-1, max_features = .5, max_leaf_nodes=10)
# m.fit(x_train, y_train)
# m.score(x_train, y_train)
# m.score(x_valid, y_valid)

# #max leaf and features=0.5
# m1_1 = RandomForestRegressor(n_estimators=10, n_jobs=-1, max_features = .5)
# #max leaf and max features
# m1_2 = RandomForestRegressor(n_estimators=10, n_jobs=-1)
# #25 leaf and max faeatures
# m1_3 = RandomForestRegressor(n_estimators=10, n_jobs=-1,max_leaf_nodes=25)
# #50 leaf and features=0.75
# m1_4 = RandomForestRegressor(n_estimators=10, n_jobs=-1, max_leaf_nodes=50
#                             , max_features = .75)
# #50 leaf and features=0.25
# m1_5 = RandomForestRegressor(n_estimators=10, n_jobs=-1, max_leaf_nodes=100
#                             , max_features = .25)



# m = RandomForestRegressor(n_estimators=10, n_jobs=-1, max_features = .5, max_leaf_nodes=10)
# m.fit(x_train, y_train)
# m.score(x_train, y_train)
# m.score(x_valid, y_valid)

# print_score(m1_1)


# m10 = RandomForestRegressor(n_estimators=10, n_jobs=-1, max_leaf_nodes=25)

# #max leaf and features=0.5
# m2_1 = RandomForestRegressor(n_estimators=20, n_jobs=-1, max_features = .5)
# #max leaf and max features
# m2_2 = RandomForestRegressor(n_estimators=20, n_jobs=-1)
# #25 leaf and max faeatures
# m2_3 = RandomForestRegressor(n_estimators=20, n_jobs=-1,max_leaf_nodes=25)
# #50 leaf and features=0.75
# m2_4 = RandomForestRegressor(n_estimators=20, n_jobs=-1, max_leaf_nodes=50
#                             , max_features = .75)
# #50 leaf and features=0.25
# m2_5 = RandomForestRegressor(n_estimators=20, n_jobs=-1, max_leaf_nodes=100
#                             , max_features = .25)

# m20 = RandomForestRegressor(n_estimators=20, n_jobs=-1,max_leaf_nodes=25)

# #max leaf and features=0.5
# m3_1 = RandomForestRegressor(n_estimators=30, n_jobs=-1, max_features = .5)
# #max leaf and max features
# m3_2 = RandomForestRegressor(n_estimators=30, n_jobs=-1)
# #25 leaf and max faeatures
# m3_3 = RandomForestRegressor(n_estimators=30, n_jobs=-1,max_leaf_nodes=25)
# #50 leaf and features=0.75
# m3_4 = RandomForestRegressor(n_estimators=30, n_jobs=-1, max_leaf_nodes=50
#                             , max_features = .75)
# #50 leaf and features=0.25
# m3_5 = RandomForestRegressor(n_estimators=30, n_jobs=-1, max_leaf_nodes=100
#                             , max_features = .25)



# m30 = RandomForestRegressor(n_estimators=30, n_jobs=-1,max_leaf_nodes=25)

# #max leaf and features=0.5
# m4_1 = RandomForestRegressor(n_estimators=40, n_jobs=-1, max_features = .5)
# #max leaf and max features
# m4_2 = RandomForestRegressor(n_estimators=40, n_jobs=-1)
# #25 leaf and max faeatures
# m4_3 = RandomForestRegressor(n_estimators=40, n_jobs=-1,max_leaf_nodes=25)
# #50 leaf and features=0.75
# m4_4 = RandomForestRegressor(n_estimators=40, n_jobs=-1, max_leaf_nodes=50
#                             , max_features = .75)
# #50 leaf and features=0.25
# m4_5 = RandomForestRegressor(n_estimators=40, n_jobs=-1, max_leaf_nodes=100
#                             , max_features = .25)

# m40 = RandomForestRegressor(n_estimators=40, n_jobs=-1,max_leaf_nodes=25)
# #max leaf and features=0.5
# m5_1 = RandomForestRegressor(n_estimators=50, n_jobs=-1, max_features = .5)
# #max leaf and max features
# m5_2 = RandomForestRegressor(n_estimators=50, n_jobs=-1)
# #25 leaf and max faeatures
# m5_3 = RandomForestRegressor(n_estimators=50, n_jobs=-1,max_leaf_nodes=25)
# #50 leaf and features=0.75
# m5_4 = RandomForestRegressor(n_estimators=50, n_jobs=-1, max_leaf_nodes=50
#                             , max_features = .75)
# #50 leaf and features=0.25
# m5_5 = RandomForestRegressor(n_estimators=50, n_jobs=-1, max_leaf_nodes=100
#                             , max_features = .25)


# m50 = RandomForestRegressor(n_estimators=50, n_jobs=-1,max_leaf_nodes=25)



# #max leaf and features=0.5
# m6_1 = RandomForestRegressor(n_estimators=150, n_jobs=-1, max_features = .5)
# #max leaf and max features
# m6_2 = RandomForestRegressor(n_estimators=150, n_jobs=-1)
# #25 leaf and max faeatures
# m6_3 = RandomForestRegressor(n_estimators=150, n_jobs=-1,max_leaf_nodes=25)
# #50 leaf and features=0.75
# m6_4 = RandomForestRegressor(n_estimators=150, n_jobs=-1, max_leaf_nodes=50
#                             , max_features = .75)
# #50 leaf and features=0.25
# m6_5 = RandomForestRegressor(n_estimators=150, n_jobs=-1, max_leaf_nodes=100
#                             , max_features = .25)


# #max leaf and features=0.5
# m7_1 = RandomForestRegressor(n_estimators=100, n_jobs=-1, max_features = .5)
# #max leaf and max features
# m7_2 = RandomForestRegressor(n_estimators=100, n_jobs=-1)
# #25 leaf and max faeatures
# m7_3 = RandomForestRegressor(n_estimators=100, n_jobs=-1,max_leaf_nodes=25)
# #50 leaf and features=0.75
# m7_4 = RandomForestRegressor(n_estimators=100, n_jobs=-1, max_leaf_nodes=50
#                             , max_features = .75)
# #50 leaf and features=0.25
# m7_5 = RandomForestRegressor(n_estimators=100, n_jobs=-1, max_leaf_nodes=100
#                             , max_features = .25)

# md1 = RandomForestRegressor(n_estimators=100, n_jobs=-1,max_leaf_nodes=25)
# md2 = RandomForestRegressor(n_estimators=90, n_jobs=-1,max_leaf_nodes=25)
# md3 = RandomForestRegressor(n_estimators=80, n_jobs=-1,max_leaf_nodes=25)
# md4 = RandomForestRegressor(n_estimators=70, n_jobs=-1,max_leaf_nodes=25)
# md5 = RandomForestRegressor(n_estimators=60, n_jobs=-1,max_leaf_nodes=25)
# md6 = RandomForestRegressor(n_estimators=50, n_jobs=-1,max_leaf_nodes=25)
# md7 = RandomForestRegressor(n_estimators=110, n_jobs=-1,max_leaf_nodes=25)
# md8 = RandomForestRegressor(n_estimators=120, n_jobs=-1,max_leaf_nodes=25)
# md9 = RandomForestRegressor(n_estimators=130, n_jobs=-1,max_leaf_nodes=25)
# md10 = RandomForestRegressor(n_estimators=140, n_jobs=-1,max_leaf_nodes=25)
# md11 = RandomForestRegressor(n_estimators=150, n_jobs=-1,max_leaf_nodes=25)


# m70 = RandomForestRegressor(n_estimators=70, n_jobs=-1,max_leaf_nodes=25)


# rfr_model1 = m50
# rfr_model2 = m70

# lr_model = LinearRegression()
# lr_model.fit(x_train, y_train)
# print_score(lr_model)




# print("RandomForestRegressor with 50 n_estimators")
# print()
# print_score(rfr_model1)
# print()
# print("*********************")
# print()
# print("RandomForestRegressor with 70 n_estimators")
# print()
# print_score(rfr_model2)
# print()
# print("*********************")
# print()
# print("Linear Regression")
# print()
# print_score(lr_model)
# print()


# def print_score2(m):
#     m.fit(x_train,y_train)
    
#     print(f"R^2 of train set: {m.score(x_train, y_train)}")
#     print(f"R^2 of validation set: {m.score(x_valid, y_valid)}")
#     print(f"R^2 of test set: {m.score(x_test, y_test)}")

# print("RandomForestRegressor with 50 n_estimators")
# print()
# print_score2(rfr_model1)
# print()
# print("*********************")
# print()
# print("RandomForestRegressor with 70 n_estimators")
# print()
# print_score2(rfr_model2)
# print()
# print("*********************")
# print()
# print("Linear Regression")
# print()
# print_score2(lr_model)
# print()
