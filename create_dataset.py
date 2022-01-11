# Change variables here
# ends = [50,100,500,1000,2000,10000,100000]
ends = [50000, 10**6, 10**6*5, 10**7, 10**7*5, 10**8, 10**8*5, 10**9, 10**9*5, 10**10, 10*10*5, 10**11]
filenames = [17,18,19,20,21, 22,23,24,25,26, 27,28]

# Code
for i in range(len(ends)):
    f = open('dataset_' + str(filenames[i]) + "_pandas.csv", "w")
    f.write('x,y\n')
    f.write("%d,%d" % (1,1) )
    for j in range(2,ends[i]+1):
        f.write("\n%d,%d" % (j,j) )
    f.close()