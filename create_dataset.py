# Change variables here
# ends = [50,100,500,1000,2000,10000,100000]
ends = [4000,6000,8000]
filenames = [14,15,16]

# Code
for i in range(len(ends)):
    f = open('dataset_' + str(filenames[i]) + "_pandas.csv", "w")
    f.write('x,y\n')
    f.write("%d,%d" % (1,1) )
    for j in range(2,ends[i]+1):
        f.write("\n%d,%d" % (j,j) )
    f.close()