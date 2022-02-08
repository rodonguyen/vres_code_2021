import pandas as pd
from sklearn import linear_model

df = pd.read_csv('dataset_additional/house.csv')
x = df.iloc[:,:-1]
y = df.iloc[:,-1:]

# Create linear regression object
regression = linear_model.LinearRegression()

# Train the model using the training sets
regression.fit(x, y)

print("Dataset shape: \n", df.shape)














################################################################

# import numpy as np
# import pandas as pd

# import warnings
# warnings.filterwarnings('ignore')
# pd.set_option('display.max_columns', 500)
# pd.set_option('display.max_rows', 300)
# df = pd.read_csv('dataset_additional/house.csv')


# # null_columns = df.columns[df.isna().any()]
# null_value_count = df[df.columns[df.isna().any()]].isna().sum().sort_values(ascending=False)
# null_percentage = (df[df.columns[df.isna().any()]].isna().sum() * 100 / df.shape[0]).sort_values(ascending=False)

# null_data = pd.concat([null_value_count, null_percentage], axis=1, keys=['Count', 'Percentage'])

# #drop
# df.drop(columns=null_data[ null_data['Percentage'] > 15].index, inplace=True)

# null_data = null_data[null_data['Percentage'] < 15]

# df['GarageType'].fillna('None', inplace=True)
# df['GarageYrBlt'].fillna(df['GarageYrBlt'].median(), inplace=True)
# df['GarageFinish'].fillna('None', inplace=True)
# df['GarageQual'].fillna('None', inplace=True)
# df['GarageCond'].fillna('None', inplace=True)
# df['BsmtExposure'].fillna('None', inplace=True)
# df['BsmtFinType2'].fillna('None', inplace=True)
# df['BsmtFinType1'].fillna('None', inplace=True)
# df['BsmtCond'].fillna('None', inplace=True)
# df['BsmtQual'].fillna('None', inplace=True)
# df['MasVnrArea'].fillna(df['MasVnrArea'].median(), inplace=True)
# df['MasVnrType'].fillna(df['MasVnrType'].mode()[0], inplace=True)
# val = df['Electrical'].mode()[0]
# df['Electrical'].fillna(val, inplace=True)
# null_value_count = df[df.columns[df.isna().any()]].isna().sum().sort_values(ascending=False)
# null_percentage = (df[df.columns[df.isna().any()]].isna().sum() * 100 / df.shape[0]).sort_values(ascending=False)
# null_data = pd.concat([null_value_count, null_percentage], axis=1, keys=['Count', 'Percentage'])

# #drop
# df.drop(columns='Street', inplace=True)
# df.drop(columns='Condition2', inplace=True)
# df.drop(columns='RoofMatl', inplace=True)
# df.drop(columns='Heating', inplace=True)
# df.drop(columns='LowQualFinSF', inplace=True)
# df.drop(columns='3SsnPorch', inplace=True)
# df.drop(columns='ScreenPorch', inplace=True)
# df.drop(columns='PoolArea', inplace=True)
# df.drop(columns='MiscVal', inplace=True)
# df.drop(columns='Utilities', inplace=True)
# df.drop(columns='Id', inplace=True)
# CurrentYear = 2021
# df['Age_Built_Years'] = CurrentYear - df['YearBuilt']
# df['Age_RemodAdd_Years'] = CurrentYear - df['YearRemodAdd']
# df['Age_GarageYrBlt_Years'] = CurrentYear - df['GarageYrBlt']
# df['Age_YrSold_Years'] = CurrentYear - df['YrSold']
# df.drop(columns=['YearBuilt','YearRemodAdd','GarageYrBlt','YrSold'], inplace=True)

# cat_var = df.select_dtypes(include='object').columns
# num_var = df.select_dtypes(exclude='object').columns
# df['SalePrice'].skew()
# df['SalePrice'].kurtosis()


# df['Transformed_SalePrice'] = np.log(df['SalePrice'])

# cat_var = df.select_dtypes(include='object').columns
# df_categorical = df.select_dtypes(include='object')
# df_dummies = pd.get_dummies(df_categorical, drop_first=True)

# df.drop(list(df_categorical.columns), axis=1, inplace=True)

# df = pd.concat([df, df_dummies], axis=1)


# X = df.drop(['SalePrice','Transformed_SalePrice'], axis=1)
# y = df['Transformed_SalePrice']

# from sklearn.model_selection import train_test_split


# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# # Getting numerical variables
# num_var = X_train.select_dtypes(include=['int64', 'float64']).columns

# from sklearn.preprocessing import MinMaxScaler

# # Instantiate an object of MinMaxScaler
# sc = MinMaxScaler()

# # Perform fit and transform on the train dataset
# X_train[num_var] = sc.fit_transform(X_train[num_var])

# # Perform only transform on the test dataset
# X_test[num_var] = sc.transform(X_test[num_var])



# from sklearn.linear_model import LinearRegression
# # Base Model
# regressor = LinearRegression()
# regressor.fit(X_train, y_train)
# coeff = pd.DataFrame(regressor.coef_, X.columns, columns=['Coefficients'])
# y_pred = regressor.predict(X_test)
# df_result = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})

# from sklearn.metrics import r2_score, mean_squared_error
# y_pred_train = regressor.predict(X_train)
# y_pred_test = regressor.predict(X_test)

# metric = []
# r2_train_lr = r2_score(y_train, y_pred_train)
# print(f"Train r2 score is : {r2_train_lr}")
# metric.append(r2_train_lr)

# r2_test_lr = r2_score(y_test, y_pred_test)
# print(f"Test r2 score is : {r2_test_lr}")
# metric.append(r2_test_lr)

# rss1_lr = np.sum(np.square(y_train - y_pred_train))
# print(f"Train RSS score is : {rss1_lr}")
# metric.append(rss1_lr)

# rss2_lr = np.sum(np.square(y_test - y_pred_test))
# print(f"Test RSS score is : {rss2_lr}")
# metric.append(rss2_lr)

# mse_train_lr = mean_squared_error(y_train, y_pred_train)
# print(f"Train MSE score is : {mse_train_lr}")
# metric.append(mse_train_lr**0.5)

# mse_test_lr = mean_squared_error(y_test, y_pred_test)
# print(f"Test MSE score is : {mse_test_lr}")
# metric.append(mse_test_lr**0.5)

















