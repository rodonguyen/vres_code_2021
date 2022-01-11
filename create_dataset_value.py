# Change variables 
dataset_number = 1
# Code
for i in range(2,150):
    f = open('dataset_' + str(dataset_number) + "_pandas.csv", "w")
    f.write('x,y\n')
    f.write("%d,%d" % (1,10**i) )
    f.close()
    dataset_number += 1