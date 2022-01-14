import random




def create_dataset():
    # Change variables here
    # ends = [50,100,500,1000,2000,10000,100000]
    ends = [50000, 10**6, 10**6*5, 10**7, 10**7*5, 10**8, 10**8*5, 10**9, 10**9*5, 10**10, 10*10*5, 10**11]
    filenames = [17,18,19,20,21, 22,23,24,25,26, 27,28]

    # Code
    for i in range(len(ends)):
        f = open('dataset_' + str(filenames[i]) + "_pandas.csv", "w")
        f.write('x,y')
        for j in range(1,ends[i]+1):
            f.write("\n%d,%d" % (j,j) )
        f.close()


def only_one_value_pandas():
    # Change variables 
    dataset_number = 1
    # Code
    for i in range(2,150):
        f = open('dataset_' + str(dataset_number) + "_pandas.csv", "w")
        f.write('x,y\n')
        f.write("%d,%d" % (1,10**i) )
        f.close()
        dataset_number += 1

def only_one_value():
    dataset_number = 1
    # Code
    for i in range(1,150):
        f = open('dataset_' + str(dataset_number) + ".csv", "w")
        f.write("%d,%d" % (1,10**i) )
        f.close()
        dataset_number += 1

def change_value_pandas():
    dataset_number = 1
    dataset_length = 10000
    number_of_copies = 21
    random_item_number = 1
    a = 1
    b = 1
    c = 2
    random_item_number_step = 100 # add this to random_item_number if you want equal steps
    alist = list(range(1,dataset_length+1))
    
    # Original dataset
    filename = './dataset_length_' + str(dataset_length) + '/dataset_1_pandas.csv'
    info_file = open('./dataset_length_' + str(dataset_length) + '/datasetinfo_pandas.txt', 'w')
    f = open(filename, 'w')

    f.write('x,y\n')
    for j in range(1,dataset_length+1):
        f.write("%d,%d\n" % (j,j) )
    f.close()
    dataset_number += 1


    # Changed datasets
    for i in range(2,number_of_copies+1):
        filename = './dataset_length_' + str(dataset_length) + '/dataset_' + str(dataset_number) + '_pandas.csv'
        f = open(filename, 'w')  
        random_items = random.sample(alist, random_item_number)
        info_file.write('DS: {0}, random_item_number: {1}\nRandom_items: {2}'.format(i, random_item_number, sorted(random_items)))

        f.write('x,y\n')
        for j in range(1,dataset_length+1):
            values = [j, j]
            values = randomize_item(j, random_items, values)
            f.write("%d,%d\n" % (values[0],values[1]) )

        f.close()

        c = a + b
        if c <= 10000:
            random_item_number = c 
        else: 
            random_item_number = 10000
            print('\nDS: {0}, random_item_number is greater than 10000 ({1}) and set to 10000'.format(i+1, c))
        a = b
        b = c
        dataset_number += 1





def change_value_readline():
    dataset_number = 1
    dataset_length = 10000
    number_of_copies = 21
    random_item_number = 1
    a = 1
    b = 1
    c = 2
    random_item_number_step = 100 # add this to random_item_number if you want equal steps
    alist = list(range(1,dataset_length+1))
    
    # Original dataset
    filename = './dataset_length_' + str(dataset_length) + '/dataset_1.csv'
    info_file = open('./dataset_length_' + str(dataset_length) + '/datasetinfo.txt', 'w')
    f = open(filename, 'w')
    
    for j in range(1,dataset_length+1):
        f.write("%d,%d\n" % (j,j) )
    f.close()
    dataset_number += 1

    # Changed datasets
    for i in range(2,number_of_copies+1):
        filename = './dataset_length_' + str(dataset_length) + '/dataset_' + str(dataset_number) + '.csv'
        f = open(filename, 'w')  
        random_items = random.sample(alist, random_item_number)
        info_file.write('DS: {0}, random_item_number: {1}\nRandom_items: {2}'.format(i, random_item_number, sorted(random_items)))

        for j in range(1,dataset_length+1):
            values = [j, j]
            values = randomize_item(j, random_items, values)
            f.write("%d,%d\n" % (values[0],values[1]) )

        f.close()

        c = a + b
        if c <= 10000:
            random_item_number = c 
        else: 
            random_item_number = 10000
            print('\nDS: {0}, random_item_number is greater than 10000 ({1}) and set to 10000'.format(i+1, c))
        a = b
        b = c
        dataset_number += 1


def randomize_item(i, random_items, values):
    if i in random_items:
        values[random.randint(0,1)] += random.randint(1,10)*random.choice([1,-1])
    return values

change_value_pandas()
change_value_readline()
# create_dataset()
# only_one_value_pandas()
# only_one_value()
