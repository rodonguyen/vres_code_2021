import pandas
import sklearn
import sklearn.model_selection

# my_list = [10,100,1000,10_000,100_000,1000_000,10_000_000]
my_list = [10,20,50,75,100,250,500,750,1000,2500,5000,7500,
            10_000,25_000,50_000,75_000,100_000,250_000,500_000,750_000,
            1000_000,1250_000,1500_000,1750_000,2000_000]

columns_to_drop = [
    'Index','Arrival_Time','Creation_Time',
    'User',
    'Model',
    'Device',
    # 'x',
    'y',
    'z',
]

filepaths = [
    'data/activity/Phones_accelerometer.csv',
    'data/activity/Phones_gyroscope.csv',
    # 'data/activity/Watch_accelerometer.csv'
    # 'data/activity/Watch_gyroscope.csv',
]

heads = [
    'pa_1col',
    'pg_1col',
    'wa',
    'wg'
]

for i, filepath in enumerate(filepaths):
    df = pandas.read_csv(filepath)
    # Transform strings to integers
    label_encoder = sklearn.preprocessing.LabelEncoder()
    label_encoder.fit(df.loc[:,'User'])
    df.loc[:,'User'] = label_encoder.transform(df.loc[:,'User'])
    label_encoder = sklearn.preprocessing.LabelEncoder()
    label_encoder.fit(df.loc[:,'Model'])
    df.loc[:,'Model'] = label_encoder.transform(df.loc[:,'Model'])
    label_encoder = sklearn.preprocessing.LabelEncoder()
    label_encoder.fit(df.loc[:,'Device'])
    df.loc[:,'Device'] = label_encoder.transform(df.loc[:,'Device'])
    label_encoder = sklearn.preprocessing.LabelEncoder()
    label_encoder.fit(df.loc[:,'gt'])
    df.loc[:,'gt'] = label_encoder.transform(df.loc[:,'gt'])
    # Drop redundant columns
    df.drop(columns=columns_to_drop, axis=1, inplace=True)
    for row_num in my_list:
        df_crop = df.sample(n=row_num, axis=0, replace=False, ignore_index=True, random_state=10)
        df_crop.to_csv(f"data/activity/{heads[i]}_{row_num}.csv", index=False)


# df = pandas.read_csv('data/activity/Phones_accelerometer.csv')
# # Transform strings to integers
# label_encoder = sklearn.preprocessing.LabelEncoder()
# label_encoder.fit(df.loc[:,'User'])
# df.loc[:,'User'] = label_encoder.transform(df.loc[:,'User'])
# label_encoder = sklearn.preprocessing.LabelEncoder()
# label_encoder.fit(df.loc[:,'Model'])
# df.loc[:,'Model'] = label_encoder.transform(df.loc[:,'Model'])
# label_encoder = sklearn.preprocessing.LabelEncoder()
# label_encoder.fit(df.loc[:,'Device'])
# df.loc[:,'Device'] = label_encoder.transform(df.loc[:,'Device'])
# label_encoder = sklearn.preprocessing.LabelEncoder()
# label_encoder.fit(df.loc[:,'gt'])
# df.loc[:,'gt'] = label_encoder.transform(df.loc[:,'gt'])
# # Drop redundant columns
# df.drop(columns=['Index','Arrival_Time','Creation_Time'], axis=1, inplace=True)
# # Save data
# for row_num in my_list:
#     df_crop = df.sample(n=row_num, axis=0, replace=False, ignore_index=True, random_state=10)
#     df_crop.to_csv(f"data/activity/pa_{row_num}.csv", index=False)


# df = pandas.read_csv('data/activity/Watch_gyroscope.csv')
# # Transform strings to integers
# label_encoder = sklearn.preprocessing.LabelEncoder()
# label_encoder.fit(df.loc[:,'User'])
# df.loc[:,'User'] = label_encoder.transform(df.loc[:,'User'])
# label_encoder = sklearn.preprocessing.LabelEncoder()
# label_encoder.fit(df.loc[:,'Model'])
# df.loc[:,'Model'] = label_encoder.transform(df.loc[:,'Model'])
# label_encoder = sklearn.preprocessing.LabelEncoder()
# label_encoder.fit(df.loc[:,'Device'])
# df.loc[:,'Device'] = label_encoder.transform(df.loc[:,'Device'])
# label_encoder = sklearn.preprocessing.LabelEncoder()
# label_encoder.fit(df.loc[:,'gt'])
# df.loc[:,'gt'] = label_encoder.transform(df.loc[:,'gt'])
# # Drop redundant columns
# df.drop(columns=['Index','Arrival_Time','Creation_Time'], axis=1, inplace=True)
# for row_num in my_list:
#     df_crop = df.sample(n=row_num, axis=0, replace=False, ignore_index=True, random_state=10)
#     df_crop.to_csv(f"data/activity/wg_{row_num}.csv", index=False)


# df = pandas.read_csv('data/activity/Watch_accelerometer.csv')
# # Transform strings to integers
# label_encoder = sklearn.preprocessing.LabelEncoder()
# label_encoder.fit(df.loc[:,'User'])
# df.loc[:,'User'] = label_encoder.transform(df.loc[:,'User'])
# label_encoder = sklearn.preprocessing.LabelEncoder()
# label_encoder.fit(df.loc[:,'Model'])
# df.loc[:,'Model'] = label_encoder.transform(df.loc[:,'Model'])
# label_encoder = sklearn.preprocessing.LabelEncoder()
# label_encoder.fit(df.loc[:,'Device'])
# df.loc[:,'Device'] = label_encoder.transform(df.loc[:,'Device'])
# label_encoder = sklearn.preprocessing.LabelEncoder()
# label_encoder.fit(df.loc[:,'gt'])
# df.loc[:,'gt'] = label_encoder.transform(df.loc[:,'gt'])
# # Drop redundant columns
# df.drop(columns=['Index','Arrival_Time','Creation_Time'], axis=1, inplace=True)
# # Save data
# for row_num in my_list:
#     df_crop = df.sample(n=row_num, axis=0, replace=False, ignore_index=True, random_state=10)
#     df_crop.to_csv(f"data/activity/wa_{row_num}.csv", index=False)