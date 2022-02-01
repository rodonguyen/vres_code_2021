import os

count = 1
for i in range(2,6):
    for j in range(1,10):
        old_name = './vpython_ds_%02d.txt' % (count)
        new_name = './vpython_ds_%02d_%02d.txt' % (i,j)
        os.rename(old_name, new_name)
        count += 1
        print("File renamed |    %s    >    %s" % (old_name, new_name))

# 37
os.rename('./vpython_ds_37.txt', './vpython_ds_06_01.txt')
print('File renamed |    /vpython_ds_37.txt    >    ./vpython_ds_06_01.txt')