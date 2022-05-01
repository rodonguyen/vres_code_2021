def write_to_csv(table_name, car, diabetes, energy, house, medical):

    # DESTINATION
    v2_file = open('./count_result/stack_trace_multiple_parts_v2.csv', 'a')
    
    # write to csv
    v2_file.write(table_name+'\n')
    v2_file.write('car')
    for j in car:
        v2_file.write(','+j)
    v2_file.write('\n')

    v2_file.write('diabetes')
    for j in diabetes:
        v2_file.write(','+j)
    v2_file.write('\n')

    v2_file.write('energy')
    for j in energy:
        v2_file.write(','+j)
    v2_file.write('\n')

    v2_file.write('house')
    for j in house:
        v2_file.write(','+j)
    v2_file.write('\n')

    v2_file.write('medical')
    for j in medical:
        v2_file.write(','+j)
    v2_file.write('\n\n\n')

    v2_file.close()



def convert_v1_to_v2():

    v1_file = open('./count_result/stack_trace_multiple_parts.csv')
    nonempty_lines = [line.strip("\n") for line in v1_file if line != "\n"]
    # max_line = len(nonempty_lines)
    v1_file.close()

    # Because memory operation number BEFORE A area is idempotent, that's 
    # the only area we check.
    # Hence, my_dict = {'pop':2, 'push':3} but not {'pop':[2,4,6,8], 'push':[3,5,7,9]}}
    my_dict = {'pop':2, 'push':3}
    for item in my_dict.keys():
        car = []
        diabetes = []
        energy = []
        house = []
        medical = []
        for line in nonempty_lines:
            if 'car' in line:
                print('car: ',line)
                line = line.split(',')
                car.append(line[my_dict[item]])
            elif 'diabetes' in line:
                print('diabetes: ',line)
                line = line.split(',')
                diabetes.append(line[my_dict[item]])
            elif 'energy' in line:
                print('energy: ',line)
                line = line.split(',')
                energy.append(line[my_dict[item]])
            elif 'house' in line:
                print('house: ',line)
                line = line.split(',')
                house.append(line[my_dict[item]])
            elif 'medical' in line:
                print('medical: ',line)
                line = line.split(',')
                medical.append(line[my_dict[item]])

        write_to_csv(item, car, diabetes, energy, house, medical)