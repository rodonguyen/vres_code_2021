def write_to_csv(table_name):

    # DESTINATION
    csv = open('./count_stuff_results/stack_traces_v2_300.csv', 'a')
    
    # write to csv
    csv.write(table_name+'\n')
    csv.write('car')
    for j in car:
        csv.write(','+j)
    csv.write('\n')

    csv.write('diabetes')
    for j in diabetes:
        csv.write(','+j)
    csv.write('\n')

    csv.write('energy')
    for j in energy:
        csv.write(','+j)
    csv.write('\n')

    csv.write('house')
    for j in house:
        csv.write(','+j)
    csv.write('\n')

    csv.write('medical')
    for j in medical:
        csv.write(','+j)
    csv.write('\n\n\n')

    csv.close()



# STARTING FILE
file = open('./count_stuff_results/stack_traces.csv')

nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
# max_line = len(nonempty_lines)
file.close()

for item in [5,6,2]:
    car = []
    diabetes = []
    energy = []
    house = []
    medical = []
    for i, line in enumerate(nonempty_lines):
        if 'car' in line:
            print('car: ',line)
            line = line.split(',')
            car.append(line[item])
        if 'diabetes' in line:
            print('diabetes: ',line)
            line = line.split(',')
            diabetes.append(line[item])
        if 'energy' in line:
            print('energy: ',line)
            line = line.split(',')
            energy.append(line[item])
        if 'house' in line:
            print('house: ',line)
            line = line.split(',')
            house.append(line[item])
        if 'medical' in line:
            print('medical: ',line)
            line = line.split(',')
            medical.append(line[item])

    write_to_csv(['','','execution time','','','pop','push'][item])