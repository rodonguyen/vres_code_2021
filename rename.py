import os

count = 1
for i in range(2,6):
    for j in range(1,11):
        os.rename('./vpython_ds_'+count+'.txt', './vpython_ds_%02d_%02d.txt')
        count += 1
        print("File renamed!")