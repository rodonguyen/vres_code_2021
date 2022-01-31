import datetime
import os


# # Using readlines()
# def count_stack_1(dataset, method, file1):
#     nonempty_lines1 = [line.strip("\n") for line in file1 if line != "\n"]
#     max_line_1 = len(nonempty_lines1)
#     file1.close()
    
#     counter1 = {'push': 0, 'pop': 0, 'ext_pop': 0, 'stackadjshrink': 0, 'stackadjgrow': 0}
#     start , _ = nonempty_lines1[0].split("->",1)
#     for i in range(max_line_1):
#         end , value1 = nonempty_lines1[i].split("->",1)
#         counter1[value1] += 1
#     exe_time = (int(end) - int(start))/1000000
#     print(counter1)
#     print('Execution time:', exe_time, 's')

#     f = open("results.txt", "a")
#     f.write("Method: " + method + "\n")
#     f.write("Dataset: " + str(dataset) + "\n")
#     f.write('Execution time: ' + str(exe_time) + ' s\n')
#     f.write(str(counter1) + '\n\n')
#     f.close()

# def count_stack_2(dataset, method, file1):
#     nonempty_lines = [line.strip("\n") for line in file1 if line != "\n"]
#     max_line = len(nonempty_lines)
#     file1.close()
#     # print(nonempty_lines1[0:10])

#     _, counter = nonempty_lines[-1].split(' ', 1)
#     start , _ = nonempty_lines[0].split("->",1)
#     for i in reversed(range(max_line)):
#         if '->' in nonempty_lines[i]:
#             print(nonempty_lines[i])
#             end, _ = nonempty_lines[i].split("->",1)
#             break
#     exe_time = (int(end) - int(start))/1000000
#     print(counter)
#     print('Execution time:', exe_time, 's')

#     f = open("results.txt", "a")
#     f.write("Method: " + method + "\n")
#     f.write("Dataset: " + str(dataset) + "\n")
#     f.write('Execution time: ' + str(exe_time) + ' s\n')
#     f.write(counter + '\n\n')
#     f.close()

#     pop, push, sgrow, sshrink = counter.split(' | ')
#     _, pop = pop.split(' ')
#     _, push = push.split(' ')
#     _, sgrow = sgrow.split(' ')
#     _, sshrink = sshrink.split(' ')
#     csv = open('results.csv', 'a')
#     csv.write('{0},{1},{2},{3},{4},{5},{6}\n'.format(method, str(dataset), str(exe_time), \
#                 pop, push, sgrow, sshrink ))

# # Count the stacks of toy code (printing the datasets)
# def run_all_1():
#     # Edit the path before running
#     paths = ['strace_readline/trace/vpython_ds', \
#             'strace_pandas/trace/vpython_ds']
#     for path in paths:
#         for i in range(1,18+1):
#             dataset = i
#             temp_path = path + '%02d.txt' % dataset
#             file = open(temp_path, "r")
#             count_new_stack(dataset, temp_path, file)
    
# def run_individual():
#     one_path = 'strace_numpy/trace/vpython_ds00.txt'
#     count_new_stack(0, one_path , open(one_path, 'r'))





# Count the linear regression stacks
def identify_vpython():
    # Edit the path before running
    destination = './count_stuff_results/stack_traces.csv'
    paths = ['linear_regression_pandas/trace/', 
    'linear_regression_readline/trace/', 
    'linear_regression_additional/trace/'] 
    paths = ['linear_regression_additional/trace/']

    for path in sorted(paths):
        for dir in sorted(os.listdir(path)):
            print('\ndir: ' + dir)
            temp_path = path + dir 
            for vpython_name in sorted(os.listdir(temp_path)):
                count_stack_3(temp_path + '/' + vpython_name, destination)

    csv = open(destination, 'a')
    csv.write('filepath, file no., execution time, start time, end time, pop, push, sgrow, sshrink\n')


def count_stack_3(filename, destination):
    print(filename)
    file = open(filename)
    nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
    max_line = len(nonempty_lines)
    file.close()

    start = nonempty_lines[0].split("->",1)[0]
    for i in reversed(range(max_line)):
        if '->' in nonempty_lines[i]:
            # print(nonempty_lines[i])
            end = nonempty_lines[i].split("->",1)[0]
            break
    for i in reversed(range(max_line)):
        if '>>>' in nonempty_lines[i]:
            counter = nonempty_lines[i].split(' ', 1)[1]
            break

    exe_time = (int(end) - int(start))/1000000
    start_time = datetime.datetime.fromtimestamp(int(start[:-6])).strftime('%H:%M:%S')
    end_time = datetime.datetime.fromtimestamp(int(end[:-6])).strftime('%H:%M:%S')

    # Record stack trace in results.csv
    pop, push, sgrow, sshrink = counter.split(' | ')
    _, pop = pop.split(' ')
    _, push = push.split(' ')
    _, sgrow = sgrow.split(' ')
    _, sshrink = sshrink.split(' ')
    csv = open(destination, 'a')
    csv.write('{0},{1},{2},{3},{4},{5},{6},{7},{8}\n'.format(
                filename, filename[-9:-4], str(exe_time),
                start_time, end_time,
                pop, push, sgrow, sshrink ))


# top -bd 0.5 -o +%MEM | grep "load average" -A 9 > memory_usage.log
def get_cpu_memory_usage():
    file = open('memory_cpu_usage.log')
    nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
    # max_line = len(nonempty_lines)
    file.close()

    csv = open('./count_stuff_results/cpu_usage.csv', 'a')
    csv.write('timestamp,%cpu_user,%cpu_system\n')
    for line in nonempty_lines:
        if 'top -' in line:
            line = line.split()
            timestamp = line[2]
        if 'Cpu(s):' in line:
            line = line.split()
            user, system = line[1], line[3]
            print(timestamp, user, system)
            csv.write('{0},{1},{2}\n'.format(timestamp,user,system))



# get_cpu_memory_usage()
identify_vpython()