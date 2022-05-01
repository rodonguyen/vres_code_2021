import pandas as pd
from pyparsing import col
from sklearn import linear_model

df = pd.read_csv('dataset_additional/house.csv')

from sklearn.preprocessing import OrdinalEncoder
ord_enc = OrdinalEncoder()

# df[36:79] = ord_enc.fit_transform(df.loc[:,'MSZoning':'SalePrice'])
def modify_col(col_name):
    df[col_name] = ord_enc.fit_transform(df[[col_name]])
    # df[col_name]= pd.to_numeric(df[col_name], errors='coerce')

cols = list(df.iloc[0:1,36:79])
print(cols)

for i in cols:
    modify_col(i)
# modify_col('CarName')
# modify_col('fueltype')
# modify_col('aspiration')
# modify_col('doornumber')
# modify_col('carbody')
# modify_col('drivewheel')
# modify_col('enginelocation')
# modify_col('enginetype')
# modify_col('cylindernumber')
# modify_col('fuelsystem')

df.to_csv('house.csv', index = False)