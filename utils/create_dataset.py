import random

# dataset_length_increase version 2
def dataset_length_increase():
    for i in range(2,6):
        for j in range(1,11):
            f = open('dataset_length_increase/dataset_%02d_%02d.csv' % (i,j), "w")
            f.write('0,0')
            for line in range(j*(10**i)-1):
                f.write("\n1,1")
            f.close()


def only_one_value_pandas():
    # Change variables 
    dataset_number = 1
    # Data points
    for i in range(2,150):
        f = open('dataset_' + str(dataset_number) + "_pandas.csv", "w")
        f.write('x,y\n')
        f.write("%d,%d" % (1,10**i) )
        f.close()
        dataset_number += 1

def only_one_value():
    dataset_number = 1
    # Code
    for i in range(1,60):
        f = open('./dataset_length_1/dataset_' + str(dataset_number) + ".csv", "w")
        f.write("%d,%d" % (1,10**i) )
        f.close()
        dataset_number += 1

def dataset_length_10000_pandas():
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
    info_file = open('./dataset_length_' + str(dataset_length) + '/ds_info_pandas.txt', 'w')
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
        if c <= dataset_length:
            random_item_number = c 
        else: 
            random_item_number = dataset_length
            print('\nDS: {0}, random_item_number is greater than 10000 ({1}) and set to 10000'.format(i+1, c))
        a = b
        b = c
        dataset_number += 1

def dataset_length_10000_readline():
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
    info_file = open('./dataset_length_' + str(dataset_length) + '/ds_info.txt', 'w')
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
        if c <= dataset_length:
            random_item_number = c 
        else: 
            random_item_number = dataset_length
            print('\nDS: {0}, random_item_number is greater than 10000 ({1}) and set to 10000'.format(i+1, c))
        a = b
        b = c
        dataset_number += 1

def randomize_item(i, random_items, values):
    if i in random_items:
        values[random.randint(0,1)] += random.randint(1,10)*random.choice([1,-1])
    return values

def dataset_length_100_pandas():
    dataset_number = 1
    dataset_length = 100
    number_of_copies = 12
    random_item_number = 1
    a = 1
    b = 1
    c = 2
    random_item_number_step = 100 # add this to random_item_number if you want equal steps
    alist = list(range(1,dataset_length+1))
    
    # Original dataset
    filename = './dataset_length_' + str(dataset_length) + '_2/dataset_1_pandas.csv'
    info_file = open('./dataset_length_' + str(dataset_length) + '_2/ds_info_pandas.txt', 'w')
    f = open(filename, 'w')

    f.write('x,y\n')
    for j in range(1,dataset_length+1):
        f.write("%d,%d\n" % (j,j) )
    f.close()
    dataset_number += 1


    # Changed datasets
    for i in range(2,number_of_copies+1):
        filename = './dataset_length_' + str(dataset_length) + '_2/dataset_' + str(dataset_number) + '_pandas.csv'
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
        if c <= dataset_length:
            random_item_number = c 
        else: 
            random_item_number = dataset_length
            print('\nDS: {0}, random_item_number is greater than 10000 ({1}) and set to 10000'.format(i+1, c))
        a = b
        b = c
        dataset_number += 1

def dataset_length_100_readline():
    dataset_number = 1
    dataset_length = 100
    number_of_copies = 12
    random_item_number = 1
    a = 1
    b = 1
    c = 2
    random_item_number_step = 100 # add this to random_item_number if you want equal steps
    alist = list(range(1,dataset_length+1))
    
    # Original dataset
    filename = './dataset_length_' + str(dataset_length) + '_2/dataset_1.csv'
    info_file = open('./dataset_length_' + str(dataset_length) + '_2/ds_info.txt', 'w')
    f = open(filename, 'w')
    
    for j in range(1,dataset_length+1):
        f.write("%d,%d\n" % (j,j) )
    f.close()
    dataset_number += 1

    # Changed datasets
    for i in range(2,number_of_copies+1):
        filename = './dataset_length_' + str(dataset_length) + '_2/dataset_' + str(dataset_number) + '.csv'
        f = open(filename, 'w')  
        random_items = random.sample(alist, random_item_number)
        info_file.write('DS: {0}, random_item_number: {1}\nRandom_items: {2}'.format(i, random_item_number, sorted(random_items)))

        for j in range(1,dataset_length+1):
            values = [j, j]
            values = randomize_item(j, random_items, values)
            f.write("%d,%d\n" % (values[0],values[1]) )

        f.close()

        c = a + b
        if c <= dataset_length:
            random_item_number = c 
        else: 
            random_item_number = dataset_length
            print('\nDS: {0}, random_item_number is greater than 10000 ({1}) and set to 10000'.format(i+1, c))
        a = b
        b = c
        dataset_number += 1


def dataset_length_10_add1_pandas():
    dataset_number = 1
    dataset_length = 10
    number_of_copies = 7
    random_item_number = 1
    a = 1
    b = 1
    c = 2
    alist = list(range(1,dataset_length+1))
    
    # Original dataset
    filename = './dataset_length_' + str(dataset_length) + '_add1/dataset_1_pandas.csv'
    info_file = open('./dataset_length_' + str(dataset_length) + '_add1/ds_info_pandas.txt', 'w')
    f = open(filename, 'w')

    # Original dataset
    f.write('x,y\n')
    f.write('0,0\n')
    for j in range(2,dataset_length+1):
        f.write("1,1\n")
    f.close()
    dataset_number += 1


    # Changed datasets
    for i in range(2,number_of_copies+1):
        filename = './dataset_length_' + str(dataset_length) + '_add1/dataset_' + str(dataset_number) + '_pandas.csv'
        f = open(filename, 'w')  
        random_items = random.sample(alist, random_item_number)
        info_file.write('DS: {0}, random_item_number: {1}\nRandom_items: {2}\n'.format(dataset_number, random_item_number, sorted(random_items)))

        f.write('x,y\n')
        if (j not in random_items): values = '0,0\n' 
        else: values = '0,1\n'
        f.write(values)

        
        for j in range(2,dataset_length+1):
            if (j not in random_items): values = '1,1\n' 
            else: values = '1,2\n'
            f.write(values)
        f.close()

        dataset_number += 1


        # Another dataset with the same random item number
        filename = './dataset_length_' + str(dataset_length) + '_add1/dataset_' + str(dataset_number) + '_pandas.csv'
        f = open(filename, 'w')  
        random_items = random.sample(alist, random_item_number)
        info_file.write('DS: {0}, random_item_number: {1}\nRandom_items: {2}\n'.format(dataset_number, random_item_number, sorted(random_items)))

        f.write('x,y\n')
        if (j not in random_items): values = '0,0\n' 
        else: values = '0,1\n'
        f.write(values)


        for j in range(2,dataset_length+1):
            if (j not in random_items): values = '1,1\n' 
            else: values = '1,2\n'
            f.write(values)
        f.close()

        c = a + b
        if c <= dataset_length:
            random_item_number = c 
        else: 
            random_item_number = dataset_length
            print('\nDS {0} will have random_item_number greater than 10 ({1}) and random_item_number will be set to 10'.format(dataset_number+1, c))
        a = b
        b = c
        dataset_number += 1

def dataset_length_10_add1_readline():
    dataset_number = 1
    dataset_length = 10
    number_of_copies = 7
    random_item_number = 1
    a = 1
    b = 1
    c = 2
    alist = list(range(1,dataset_length+1))
    
    # Original dataset
    filename = './dataset_length_' + str(dataset_length) + '_add1/dataset_1.csv'
    info_file = open('./dataset_length_' + str(dataset_length) + '_add1/ds_info.txt', 'w')
    f = open(filename, 'w')

    f.write('0,0\n')
    for j in range(2,dataset_length+1):
        f.write("1,1\n")
    f.close()
    dataset_number += 1


    # Changed datasets
    for i in range(2,number_of_copies+1):
        filename = './dataset_length_' + str(dataset_length) + '_add1/dataset_' + str(dataset_number) + '.csv'
        f = open(filename, 'w')  
        random_items = random.sample(alist, random_item_number)
        info_file.write('DS: {0}, random_item_number: {1}\nRandom_items: {2}\n'.format(dataset_number, random_item_number, sorted(random_items)))

        if (j not in random_items): values = '0,0\n' 
        else: values = '0,1\n'
        f.write(values)
     
        for j in range(2,dataset_length+1):
            if (j not in random_items): values = '1,1\n' 
            else: values = '1,2\n'
            f.write(values)
        f.close()

        dataset_number += 1


        # Another dataset with the same random item number
        filename = './dataset_length_' + str(dataset_length) + '_add1/dataset_' + str(dataset_number) + '.csv'
        f = open(filename, 'w')  
        random_items = random.sample(alist, random_item_number)
        info_file.write('DS: {0}, random_item_number: {1}\nRandom_items: {2}\n'.format(dataset_number, random_item_number, sorted(random_items)))

        if (j not in random_items): values = '0,0\n' 
        else: values = '0,1\n'
        f.write(values)
        for j in range(2,dataset_length+1):
            if (j not in random_items): values = '1,1\n' 
            else: values = '1,2\n'
            f.write(values)
        f.close()

        # Calculate random_item_number
        c = a + b
        if c <= dataset_length:
            random_item_number = c 
        else: 
            random_item_number = dataset_length
            print('\nDS {0} will have random_item_number greater than 10 ({1}) and random_item_number will be set to 10'.format(dataset_number+1, c))
        a = b
        b = c
        dataset_number += 1


def dataset_length_10_negative1_pandas():
    dataset_number = 1
    dataset_length = 10
    number_of_copies = 7
    random_item_number = 1
    a = 1
    b = 1
    c = 2
    alist = list(range(1,dataset_length+1))
    
    # Original dataset
    filename = './dataset_length_' + str(dataset_length) + '_negative1/dataset_1_pandas.csv'
    info_file = open('./dataset_length_' + str(dataset_length) + '_negative1/ds_info_pandas.txt', 'w')
    f = open(filename, 'w')

    f.write('x,y\n')
    f.write('0,0\n')
    for j in range(2,dataset_length+1):
        f.write("1,1\n")
    f.close()
    dataset_number += 1


    # Changed datasets
    for i in range(2,number_of_copies+1):
        filename = './dataset_length_' + str(dataset_length) + '_negative1/dataset_' + str(dataset_number) + '_pandas.csv'
        f = open(filename, 'w')  
        random_items = random.sample(alist, random_item_number)
        info_file.write('DS: {0}, random_item_number: {1}\nRandom_items: {2}\n'.format(dataset_number, random_item_number, sorted(random_items)))

        f.write('x,y\n')
        if (j not in random_items): values = '0,0\n' 
        else: values = '0,-1\n'
        f.write(values)
        
        for j in range(2,dataset_length+1):
            if (j not in random_items): values = '1,1\n' 
            else: values = '1,-1\n'
            f.write(values)
        f.close()

        dataset_number += 1


        # Another dataset with the same random item number
        filename = './dataset_length_' + str(dataset_length) + '_negative1/dataset_' + str(dataset_number) + '_pandas.csv'
        f = open(filename, 'w')  
        random_items = random.sample(alist, random_item_number)
        info_file.write('DS: {0}, random_item_number: {1}\nRandom_items: {2}\n'.format(dataset_number, random_item_number, sorted(random_items)))

        f.write('x,y\n')
        if (j not in random_items): values = '0,0\n' 
        else: values = '0,-1\n'
        f.write(values)

        for j in range(2,dataset_length+1):
            if (j not in random_items): values = '1,1\n' 
            else: values = '1,-1\n'
            f.write(values)
        f.close()

        c = a + b
        if c <= dataset_length:
            random_item_number = c 
        else: 
            random_item_number = dataset_length
            print('\nDS {0} will have random_item_number greater than 10 ({1}) and random_item_number will be set to 10'.format(dataset_number+1, c))
        a = b
        b = c
        dataset_number += 1

def dataset_length_10_negative1_readline():
    dataset_number = 1
    dataset_length = 10
    number_of_copies = 7
    random_item_number = 1
    a = 1
    b = 1
    c = 2
    alist = list(range(1,dataset_length+1))
    
    # Original dataset
    filename = './dataset_length_' + str(dataset_length) + '_negative1/dataset_1.csv'
    info_file = open('./dataset_length_' + str(dataset_length) + '_negative1/ds_info.txt', 'w')
    f = open(filename, 'w')

    f.write('0,0\n')
    for j in range(2,dataset_length+1):
        f.write("1,1\n")
    f.close()
    dataset_number += 1


    # Changed datasets
    for i in range(2,number_of_copies+1):
        filename = './dataset_length_' + str(dataset_length) + '_negative1/dataset_' + str(dataset_number) + '.csv'
        f = open(filename, 'w')  
        random_items = random.sample(alist, random_item_number)
        info_file.write('DS: {0}, random_item_number: {1}\nRandom_items: {2}\n'.format(dataset_number, random_item_number, sorted(random_items)))

        if (j not in random_items): values = '0,0\n' 
        else: values = '0,-1\n'
        f.write(values)
        
        for j in range(2,dataset_length+1):
            if (j not in random_items): values = '1,1\n' 
            else: values = '1,-1\n'
            f.write(values)
        f.close()
        dataset_number += 1


        # Another dataset with the same random item number
        filename = './dataset_length_' + str(dataset_length) + '_negative1/dataset_' + str(dataset_number) + '.csv'
        f = open(filename, 'w')  
        random_items = random.sample(alist, random_item_number)
        info_file.write('DS: {0}, random_item_number: {1}\nRandom_items: {2}\n'.format(dataset_number, random_item_number, sorted(random_items)))

        if (j not in random_items): values = '0,0\n' 
        else: values = '0,-1\n'
        f.write(values)

        for j in range(2,dataset_length+1):
            if (j not in random_items): values = '1,1\n' 
            else: values = '1,-1\n'
            f.write(values)
        f.close()

        c = a + b
        if c <= dataset_length:
            random_item_number = c 
        else: 
            random_item_number = dataset_length
            print('\nDS {0} will have random_item_number greater than 10 ({1}) and random_item_number will be set to 10'.format(dataset_number+1, c))
        a = b
        b = c
        dataset_number += 1


def dataset_length_100_add1_pandas():
    dataset_number = 1
    dataset_length = 100
    number_of_copies = 12
    random_item_number = 1
    a = 1
    b = 1
    c = 2
    alist = list(range(1,dataset_length+1))
    
    # Original dataset
    filename = './dataset_length_' + str(dataset_length) + '_add1/dataset_1_pandas.csv'
    info_file = open('./dataset_length_' + str(dataset_length) + '_add1/ds_info_pandas.txt', 'w')
    f = open(filename, 'w')

    # Original dataset
    f.write('x,y\n')
    f.write('0,0\n')
    for j in range(2,dataset_length+1):
        f.write("1,1\n")
    f.close()
    dataset_number += 1


    # Changed datasets
    for i in range(2,number_of_copies+1):
        filename = './dataset_length_' + str(dataset_length) + '_add1/dataset_' + str(dataset_number) + '_pandas.csv'
        f = open(filename, 'w')  
        random_items = random.sample(alist, random_item_number)
        info_file.write('DS: {0}, random_item_number: {1}\nRandom_items: {2}\n'.format(dataset_number, random_item_number, sorted(random_items)))

        f.write('x,y\n')
        if (j not in random_items): values = '0,0\n' 
        else: values = '0,1\n'
        f.write(values)


        for j in range(2,dataset_length+1):
            if (j not in random_items): values = '1,1\n' 
            else: values = '1,2\n'
            f.write(values)
        f.close()

        c = a + b
        if c <= dataset_length:
            random_item_number = c 
        else: 
            random_item_number = dataset_length
            print('\nDS {0} will have random_item_number greater than 10 ({1}) and random_item_number will be set to 10'.format(dataset_number+1, c))
        a = b
        b = c
        dataset_number += 1

def dataset_length_100_add1_readline():
    dataset_number = 1
    dataset_length = 100
    number_of_copies = 12
    random_item_number = 1
    a = 1
    b = 1
    c = 2
    alist = list(range(1,dataset_length+1))
    
    # Original dataset
    filename = './dataset_length_' + str(dataset_length) + '_add1/dataset_1.csv'
    info_file = open('./dataset_length_' + str(dataset_length) + '_add1/ds_info.txt', 'w')
    f = open(filename, 'w')

    f.write('0,0\n')
    for j in range(2,dataset_length+1):
        f.write("1,1\n")
    f.close()
    dataset_number += 1


    # Changed datasets
    for i in range(2,number_of_copies+1):
        filename = './dataset_length_' + str(dataset_length) + '_add1/dataset_' + str(dataset_number) + '.csv'
        f = open(filename, 'w')  
        random_items = random.sample(alist, random_item_number)
        info_file.write('DS: {0}, random_item_number: {1}\nRandom_items: {2}\n'.format(dataset_number, random_item_number, sorted(random_items)))

        if (j not in random_items): values = '0,0\n' 
        else: values = '0,1\n'
        f.write(values)
        for j in range(2,dataset_length+1):
            if (j not in random_items): values = '1,1\n' 
            else: values = '1,2\n'
            f.write(values)
        f.close()

        # Calculate random_item_number
        c = a + b
        if c <= dataset_length:
            random_item_number = c 
        else: 
            random_item_number = dataset_length
            print('\nDS {0} will have random_item_number greater than 10 ({1}) and random_item_number will be set to 10'.format(dataset_number+1, c))
        a = b
        b = c
        dataset_number += 1


def dataset_length_100_negative1_pandas():
    dataset_number = 1
    dataset_length = 100
    number_of_copies = 12
    random_item_number = 1
    a = 1
    b = 1
    c = 2
    alist = list(range(1,dataset_length+1))
    
    # Original dataset
    filename = './dataset_length_' + str(dataset_length) + '_negative1/dataset_1_pandas.csv'
    info_file = open('./dataset_length_' + str(dataset_length) + '_negative1/ds_info_pandas.txt', 'w')
    f = open(filename, 'w')

    f.write('x,y\n')
    f.write('0,0\n')
    for j in range(2,dataset_length+1):
        f.write("1,1\n")
    f.close()
    dataset_number += 1


    # Changed datasets
    for i in range(2,number_of_copies+1):

        filename = './dataset_length_' + str(dataset_length) + '_negative1/dataset_' + str(dataset_number) + '_pandas.csv'
        f = open(filename, 'w')  
        random_items = random.sample(alist, random_item_number)
        info_file.write('DS: {0}, random_item_number: {1}\nRandom_items: {2}\n'.format(dataset_number, random_item_number, sorted(random_items)))

        f.write('x,y\n')
        if (j not in random_items): values = '0,0\n' 
        else: values = '0,-1\n'
        f.write(values)

        for j in range(2,dataset_length+1):
            if (j not in random_items): values = '1,1\n' 
            else: values = '1,-1\n'
            f.write(values)
        f.close()

        c = a + b
        if c <= dataset_length:
            random_item_number = c 
        else: 
            random_item_number = dataset_length
            print('\nDS {0} will have random_item_number greater than 10 ({1}) and random_item_number will be set to 10'.format(dataset_number+1, c))
        a = b
        b = c
        dataset_number += 1

def dataset_length_100_negative1_readline():
    dataset_number = 1
    dataset_length = 100
    number_of_copies = 12
    random_item_number = 1
    a = 1
    b = 1
    c = 2
    alist = list(range(1,dataset_length+1))
    
    # Original dataset
    filename = './dataset_length_' + str(dataset_length) + '_negative1/dataset_1.csv'
    info_file = open('./dataset_length_' + str(dataset_length) + '_negative1/ds_info.txt', 'w')
    f = open(filename, 'w')

    f.write('0,0\n')
    for j in range(2,dataset_length+1):
        f.write("1,1\n")
    f.close()
    dataset_number += 1


    # Changed datasets
    for i in range(2,number_of_copies+1):
        filename = './dataset_length_' + str(dataset_length) + '_negative1/dataset_' + str(dataset_number) + '.csv'
        f = open(filename, 'w')  
        random_items = random.sample(alist, random_item_number)
        info_file.write('DS: {0}, random_item_number: {1}\nRandom_items: {2}\n'.format(dataset_number, random_item_number, sorted(random_items)))

        if (j not in random_items): values = '0,0\n' 
        else: values = '0,-1\n'
        f.write(values)

        for j in range(2,dataset_length+1):
            if (j not in random_items): values = '1,1\n' 
            else: values = '1,-1\n'
            f.write(values)
        f.close()

        c = a + b
        if c <= dataset_length:
            random_item_number = c 
        else: 
            random_item_number = dataset_length
            print('\nDS {0} will have random_item_number greater than 10 ({1}) and random_item_number will be set to 10'.format(dataset_number+1, c))
        a = b
        b = c
        dataset_number += 1


def dataset_length_10000_add1_pandas():
    dataset_number = 1
    dataset_length = 10000
    number_of_copies = 21
    random_item_number = 1
    a = 1
    b = 1
    c = 2
    alist = list(range(1,dataset_length+1))
    
    # Original dataset
    filename = './dataset_length_' + str(dataset_length) + '_add1/dataset_1_pandas.csv'
    info_file = open('./dataset_length_' + str(dataset_length) + '_add1/ds_info_pandas.txt', 'w')
    f = open(filename, 'w')

    # Original dataset
    f.write('x,y\n')
    f.write('0,0\n')
    for j in range(2,dataset_length+1):
        f.write("1,1\n")
    f.close()
    dataset_number += 1


    # Changed datasets
    for i in range(2,number_of_copies+1):
        filename = './dataset_length_' + str(dataset_length) + '_add1/dataset_' + str(dataset_number) + '_pandas.csv'
        f = open(filename, 'w')  
        random_items = random.sample(alist, random_item_number)
        info_file.write('DS: {0}, random_item_number: {1}\nRandom_items: {2}\n'.format(dataset_number, random_item_number, sorted(random_items)))

        f.write('x,y\n')
        if (j not in random_items): values = '0,0\n' 
        else: values = '0,1\n'
        f.write(values)


        for j in range(2,dataset_length+1):
            if (j not in random_items): values = '1,1\n' 
            else: values = '1,2\n'
            f.write(values)
        f.close()

        c = a + b
        if c <= dataset_length:
            random_item_number = c 
        else: 
            random_item_number = dataset_length
            print('\nDS {0} will have random_item_number greater than 10 ({1}) and random_item_number will be set to 10'.format(dataset_number+1, c))
        a = b
        b = c
        dataset_number += 1

def dataset_length_10000_add1_readline():
    dataset_number = 1
    dataset_length = 10000
    number_of_copies = 21
    random_item_number = 1
    a = 1
    b = 1
    c = 2
    alist = list(range(1,dataset_length+1))
    
    # Original dataset
    filename = './dataset_length_' + str(dataset_length) + '_add1/dataset_1.csv'
    info_file = open('./dataset_length_' + str(dataset_length) + '_add1/ds_info.txt', 'w')
    f = open(filename, 'w')

    f.write('0,0\n')
    for j in range(2,dataset_length+1):
        f.write("1,1\n")
    f.close()
    dataset_number += 1


    # Changed datasets
    for i in range(2,number_of_copies+1):
        filename = './dataset_length_' + str(dataset_length) + '_add1/dataset_' + str(dataset_number) + '.csv'
        f = open(filename, 'w')  
        random_items = random.sample(alist, random_item_number)
        info_file.write('DS: {0}, random_item_number: {1}\nRandom_items: {2}\n'.format(dataset_number, random_item_number, sorted(random_items)))

        if (j not in random_items): values = '0,0\n' 
        else: values = '0,1\n'
        f.write(values)
        for j in range(2,dataset_length+1):
            if (j not in random_items): values = '1,1\n' 
            else: values = '1,2\n'
            f.write(values)
        f.close()

        # Calculate random_item_number
        c = a + b
        if c <= dataset_length:
            random_item_number = c 
        else: 
            random_item_number = dataset_length
            print('\nDS {0} will have random_item_number greater than 10 ({1}) and random_item_number will be set to 10'.format(dataset_number+1, c))
        a = b
        b = c
        dataset_number += 1


def dataset_length_10000_negative1_pandas():
    dataset_number = 1
    dataset_length = 10000
    number_of_copies = 21
    random_item_number = 1
    a = 1
    b = 1
    c = 2
    alist = list(range(1,dataset_length+1))
    
    # Original dataset
    filename = './dataset_length_' + str(dataset_length) + '_negative1/dataset_1_pandas.csv'
    info_file = open('./dataset_length_' + str(dataset_length) + '_negative1/ds_info_pandas.txt', 'w')
    f = open(filename, 'w')

    f.write('x,y\n')
    f.write('0,0\n')
    for j in range(2,dataset_length+1):
        f.write("1,1\n")
    f.close()
    dataset_number += 1


    # Changed datasets
    for i in range(2,number_of_copies+1):
        filename = './dataset_length_' + str(dataset_length) + '_negative1/dataset_' + str(dataset_number) + '_pandas.csv'
        f = open(filename, 'w')  
        random_items = random.sample(alist, random_item_number)
        info_file.write('DS: {0}, random_item_number: {1}\nRandom_items: {2}\n'.format(dataset_number, random_item_number, sorted(random_items)))

        f.write('x,y\n')
        if (j not in random_items): values = '0,0\n' 
        else: values = '0,-1\n'
        f.write(values)

        for j in range(2,dataset_length+1):
            if (j not in random_items): values = '1,1\n' 
            else: values = '1,-1\n'
            f.write(values)
        f.close()

        c = a + b
        if c <= dataset_length:
            random_item_number = c 
        else: 
            random_item_number = dataset_length
            print('\nDS {0} will have random_item_number greater than 10 ({1}) and random_item_number will be set to 10'.format(dataset_number+1, c))
        a = b
        b = c
        dataset_number += 1

def dataset_length_10000_negative1_readline():
    dataset_number = 1
    dataset_length = 10000
    number_of_copies = 21
    random_item_number = 1
    a = 1
    b = 1
    c = 2
    alist = list(range(1,dataset_length+1))
    
    # Original dataset
    filename = './dataset_length_' + str(dataset_length) + '_negative1/dataset_1.csv'
    info_file = open('./dataset_length_' + str(dataset_length) + '_negative1/ds_info.txt', 'w')
    f = open(filename, 'w')

    f.write('0,0\n')
    for j in range(2,dataset_length+1):
        f.write("1,1\n")
    f.close()
    dataset_number += 1

    # Changed datasets
    for i in range(2,number_of_copies+1):
        filename = './dataset_length_' + str(dataset_length) + '_negative1/dataset_' + str(dataset_number) + '.csv'
        f = open(filename, 'w')  
        random_items = random.sample(alist, random_item_number)
        info_file.write('DS: {0}, random_item_number: {1}\nRandom_items: {2}\n'.format(dataset_number, random_item_number, sorted(random_items)))

        if (j not in random_items): values = '0,0\n' 
        else: values = '0,-1\n'
        f.write(values)

        for j in range(2,dataset_length+1):
            if (j not in random_items): values = '1,1\n' 
            else: values = '1,-1\n'
            f.write(values)
        f.close()

        c = a + b
        if c <= dataset_length:
            random_item_number = c 
        else: 
            random_item_number = dataset_length
            print('\nDS {0} will have random_item_number greater than 10 ({1}) and random_item_number will be set to 10'.format(dataset_number+1, c))
        a = b
        b = c
        dataset_number += 1




##############################################################

# dataset_length_100_add1_pandas()
# dataset_length_100_add1_readline()
# dataset_length_100_negative1_pandas()
# dataset_length_100_negative1_readline()

# dataset_length_10000_add1_pandas()
# dataset_length_10000_add1_readline()
# dataset_length_10000_negative1_pandas()
# dataset_length_10000_negative1_readline()


# dataset_length_10_add1_readline()
# dataset_length_10_add1_pandas()
# dataset_length_10_negative1_pandas()
# dataset_length_10_negative1_readline()
# dataset_length_100_pandas()
# dataset_length_100_readline()
# create_dataset()
# only_one_value_pandas()
# only_one_value()
# only_one_value()
# dataset_length_increase_pandas()
dataset_length_increase()