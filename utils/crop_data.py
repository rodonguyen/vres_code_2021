from dataclasses import replace
import pandas
import numpy
import sklearn
import sklearn.model_selection


# # mushroom dataset
# df = pandas.read_csv('data/mushroom/mushrooms.csv')
# # Transform strings to integers
# label_encoder = sklearn.preprocessing.LabelEncoder()
# label_encoder.fit(df.loc[:,'class'])
# df.loc[:,'class'] = label_encoder.transform(df.loc[:,'class'])
# label_encoder = sklearn.preprocessing.LabelEncoder()
# label_encoder.fit(df.loc[:,'capshape'])
# df.loc[:,'capshape'] = label_encoder.transform(df.loc[:,'capshape'])
# label_encoder = sklearn.preprocessing.LabelEncoder()
# label_encoder.fit(df.loc[:,'capsurface'])
# df.loc[:,'capsurface'] = label_encoder.transform(df.loc[:,'capsurface'])
# label_encoder = sklearn.preprocessing.LabelEncoder()
# label_encoder.fit(df.loc[:,'capcolor'])
# df.loc[:,'capcolor'] = label_encoder.transform(df.loc[:,'capcolor'])
# label_encoder = sklearn.preprocessing.LabelEncoder()
# label_encoder.fit(df.loc[:,'bruises'])
# df.loc[:,'bruises'] = label_encoder.transform(df.loc[:,'bruises'])
# label_encoder = sklearn.preprocessing.LabelEncoder()
# label_encoder.fit(df.loc[:,'odor'])
# df.loc[:,'odor'] = label_encoder.transform(df.loc[:,'odor'])
# label_encoder = sklearn.preprocessing.LabelEncoder()
# label_encoder.fit(df.loc[:,'gillattachment'])
# df.loc[:,'gillattachment'] = label_encoder.transform(df.loc[:,'gillattachment'])
# label_encoder = sklearn.preprocessing.LabelEncoder()
# label_encoder.fit(df.loc[:,'gillspacing'])
# df.loc[:,'gillspacing'] = label_encoder.transform(df.loc[:,'gillspacing'])
# # Drop redundant columns
# # df.drop(columns=columns_to_drop, axis=1, inplace=True)

# df_crop = df.copy().iloc[:,:8]
# df_crop.to_csv(f"data/mushroom/mushroom_digitised.csv", index=False)

# #########################################################################

# # my_list = [10,100,1000,10_000,100_000,1000_000,10_000_000]
# # my_list = [10,100,1000,10_000,100_000,1000_000] #,10_000_000]
# my_list = [10,20,50,75,100,250,500,750,1000,2500,5000,7500,
#             10_000,25_000,50_000,75_000,100_000,250_000,500_000,750_000,
#             1000_000,1250_000,1500_000,1750_000,2000_000]

# columns_to_drop = [
#     'Index','Arrival_Time','Creation_Time',
#     'User',
#     'Model',
#     'Device',
#     'y',
#     'z',
#     'x',
# ]

# filepaths = [
#     'data/activity/Phones_accelerometer.csv',
#     # 'data/activity/Phones_gyroscope.csv',
#     # 'data/activity/Watch_accelerometer.csv'
#     # 'data/activity/Watch_gyroscope.csv',
# ]

# heads = [
#     'pa',
#     # 'pg_1col',
#     # 'wa',
#     # 'wg'
# ]
# for end_index, column_num in zip(range(3,9), range(7,1,-1)):
#     for i, filepath in enumerate(filepaths):
#         df = pandas.read_csv(filepath)
#         # Transform strings to integers
#         label_encoder = sklearn.preprocessing.LabelEncoder()
#         label_encoder.fit(df.loc[:,'User'])
#         df.loc[:,'User'] = label_encoder.transform(df.loc[:,'User'])
#         label_encoder = sklearn.preprocessing.LabelEncoder()
#         label_encoder.fit(df.loc[:,'Model'])
#         df.loc[:,'Model'] = label_encoder.transform(df.loc[:,'Model'])
#         label_encoder = sklearn.preprocessing.LabelEncoder()
#         label_encoder.fit(df.loc[:,'Device'])
#         df.loc[:,'Device'] = label_encoder.transform(df.loc[:,'Device'])
#         label_encoder = sklearn.preprocessing.LabelEncoder()
#         label_encoder.fit(df.loc[:,'gt'])
#         df.loc[:,'gt'] = label_encoder.transform(df.loc[:,'gt'])
#         # Drop redundant columns
#         df.drop(columns=columns_to_drop[:end_index], axis=1, inplace=True)

#         for row_num in my_list:
#             df_crop = df.sample(n=row_num, axis=0, replace=False, ignore_index=True, random_state=10)
#             df_crop = df_crop.astype(int)
#             df_crop.to_csv(f"data/activity/{heads[i]}_{column_num}col_{row_num}.csv", index=False)


# #########################################################################
# # BITCOIN

# # my_list = [10,100,1000,10_000,100_000,1000_000,10_000_000]
# # my_list = [10,100,1000,10_000,100_000,1000_000] #,10_000_000]
# my_list = [10,20,50,75,100,250,500,750,1000,2500,5000,7500,
#             10_000,25_000,50_000,75_000,100_000,250_000,500_000,750_000,
#             1000_000,1250_000,1500_000,1750_000,2000_000]

# columns_to_drop = [
#     'address',    'year',    'day',    'length',    'weight',
#     'count',    'looped',    'neighbors',  'income',
# ]

# filepaths = [    'data/bitcoin/BitcoinHeistData.csv',]

# heads = [    'bit'   ]

# df = pandas.read_csv(filepaths[0])
# df.drop(columns=columns_to_drop[0], axis=1, inplace=True)
# # df = df_o.copy()

# # Transform strings to integers
# label_encoder = sklearn.preprocessing.LabelEncoder()
# label_encoder.fit(df.loc[:,'year'])
# df.loc[:,'year'] = label_encoder.transform(df.loc[:,'year'])
# label_encoder = sklearn.preprocessing.LabelEncoder()
# label_encoder.fit(df.loc[:,'label'])
# df.loc[:,'label'] = label_encoder.transform(df.loc[:,'label'])

# # Enlarge 'weight' and convert to int
# # df['weight'] = df['weight'] * 10_000
# mu = numpy.mean(df[['weight','income']], axis=0)
# sigma = numpy.std(df[['weight','income']], axis=0)
# df[['weight','income']] = (df[['weight','income']] - mu) / sigma * 100


# for end_index, column_num in zip(range(1,9), range(9,1,-1)):
#     # Drop redundant columns
#     df_dropped = df.drop(columns=columns_to_drop[1:end_index], axis=1, inplace=False)
#     for row_num in my_list:
#         df_crop = df_dropped.sample(n=row_num, axis=0, replace=False, ignore_index=True, random_state=10)
#         df_crop = df_crop.astype(int)
#         df_crop.to_csv(f"data/bitcoin/{heads[0]}_{column_num}col_{row_num}.csv", index=False)


#########################################################################
# Weather

my_row_list = (1234,2300,15151,22000,43000,48000,74000,82820,94444)
# my_row_list = [i*(10**power) for power in range(1, 5) 
#                 for i in range(1, 10)] + [100_000]

filepaths = ('data/weather/w.csv',)

head = 'w'

df = pandas.read_csv(filepaths[0])

# Enlarge 'temp' and convert to int
# df['temp'] = df['temp'] * 100
# df['temp'] = df['temp'].astype(int)
# Round to 2 decimal digits
df['temp'] = df['temp'].round(2)

for row_num in my_row_list:
    print(row_num)
    df_crop = df.sample(
        n=row_num, axis=0, replace=False, ignore_index=True, random_state=10)
    df_crop.to_csv(
        f"data/weather/w_Float2DigitsTemp_2col_{row_num}.csv", index=False)
# w_Float2DigitsTemp_2col_
# w_IntegerX100Temp_2col_
