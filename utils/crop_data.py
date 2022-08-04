import pandas

df = pandas.read_csv('data/activity/Phones_gyroscope.csv')


row_num = 10
df_crop = df.sample(n=row_num, axis=0, replace=False, ignore_index=True, random_state=10)
df_crop.to_csv(f"data/activity/pg_{row_num}.csv", index=False)

row_num = 100
df_crop = df.sample(n=row_num, axis=0, replace=False, ignore_index=True, random_state=10)
df_crop.to_csv(f"data/activity/pg_{row_num}.csv", index=False)

row_num = 1000
df_crop = df.sample(n=row_num, axis=0, replace=False, ignore_index=True, random_state=10)
df_crop.to_csv(f"data/activity/pg_{row_num}.csv", index=False)

row_num = 10_000
df_crop = df.sample(n=row_num, axis=0, replace=False, ignore_index=True, random_state=10)
df_crop.to_csv(f"data/activity/pg_{row_num}.csv", index=False)

row_num = 100_000
df_crop = df.sample(n=row_num, axis=0, replace=False, ignore_index=True, random_state=10)
df_crop.to_csv(f"data/activity/pg_{row_num}.csv", index=False)

row_num = 1_000_000
df_crop = df.sample(n=row_num, axis=0, replace=False, ignore_index=True, random_state=10)
df_crop.to_csv(f"data/activity/pg_{row_num}.csv", index=False)

row_num = 10_000_000
df_crop = df.sample(n=row_num, axis=0, replace=False, ignore_index=True, random_state=10)
df_crop.to_csv(f"data/activity/pg_{row_num}.csv", index=False)