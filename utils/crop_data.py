import pandas


# my_list = [10,100,1000,10_000,100_000,1000_000,10_000_000]
my_list = [10,50,100,500,1000,5000,10_000,50_000,100_000,250_000,500_000,750_000,1000_000,1500_000,2000_000]

df = pandas.read_csv('data/activity/Phones_gyroscope.csv')
for row_num in my_list:
    df_crop = df.sample(n=row_num, axis=0, replace=False, ignore_index=True, random_state=10)
    df_crop.to_csv(f"data/activity/pg_{row_num}.csv", index=False)

df = pandas.read_csv('data/activity/Phones_accelerometer.csv')
for row_num in my_list:
    df_crop = df.sample(n=row_num, axis=0, replace=False, ignore_index=True, random_state=10)
    df_crop.to_csv(f"data/activity/pa_{row_num}.csv", index=False)