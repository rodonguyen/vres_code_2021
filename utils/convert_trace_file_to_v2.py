def write_to_csv(table_name):

    # DESTINATION
    v2_trace_file = open('./count_stuff_results/stack_traces_300_v2.csv', 'a')
    
    # write to csv
    v2_trace_file.write(table_name+'\n')
    v2_trace_file.write('car')
    for j in car:
        v2_trace_file.write(','+j)
    v2_trace_file.write('\n')

    v2_trace_file.write('diabetes')
    for j in diabetes:
        v2_trace_file.write(','+j)
    v2_trace_file.write('\n')

    v2_trace_file.write('energy')
    for j in energy:
        v2_trace_file.write(','+j)
    v2_trace_file.write('\n')

    v2_trace_file.write('house')
    for j in house:
        v2_trace_file.write(','+j)
    v2_trace_file.write('\n')

    v2_trace_file.write('medical')
    for j in medical:
        v2_trace_file.write(','+j)
    v2_trace_file.write('\n\n\n')

    v2_trace_file.close()



# STARTING FILE
v1_trace_file = open('./count_stuff_results/stack_traces_300.csv')

nonempty_lines = [line.strip("\n") for line in v1_trace_file if line != "\n"]
# max_line = len(nonempty_lines)
v1_trace_file.close()

my_dict = {'execution time':2,'pop':5,'push':6}
for item in my_dict.keys():
    car = []
    diabetes = []
    energy = []
    house = []
    medical = []
    for i, line in enumerate(nonempty_lines):
        if 'car' in line:
            print('car: ',line)
            line = line.split(',')
            car.append(line[my_dict[item]])
        if 'diabetes' in line:
            print('diabetes: ',line)
            line = line.split(',')
            diabetes.append(line[my_dict[item]])
        if 'energy' in line:
            print('energy: ',line)
            line = line.split(',')
            energy.append(line[my_dict[item]])
        if 'house' in line:
            print('house: ',line)
            line = line.split(',')
            house.append(line[my_dict[item]])
        if 'medical' in line:
            print('medical: ',line)
            line = line.split(',')
            medical.append(line[my_dict[item]])

    write_to_csv(item)