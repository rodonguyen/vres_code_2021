import datetime
import os

# Count the linear regression stacks
def identify_vpython(paths):
    destination = './count_stuff_results/stack_traces.csv'

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
def get_cpu_memory_usage(usage_logfiles = ['./cpu_usage.log']):
    for usage_logfile in usage_logfiles:
        file = open(usage_logfile)
        nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
        # max_line = len(nonempty_lines)
        file.close()

        csv = open('./count_stuff_results/cpu_usage.csv', 'a')
        csv.write('timestamp,%cpu_user,%cpu_system\n')
        for i, line in enumerate(nonempty_lines):
            if 'top -' in line:
                print(line)
                line = line.split()
                timestamp = line[2]
                try: 
                    if 'python3.9' in nonempty_lines[i+1]:
                        line = nonempty_lines[i+1].split()
                        cpu, memory = line[8], line[9]
                        print(timestamp, cpu, memory)
                        csv.write('{0},{1},{2}\n'.format(timestamp,cpu,memory))
                    else: 
                        csv.write('{0},{1},{2}\n'.format(timestamp,'0','0'))
                except:
                    print('Reach end of file.\n')
        csv.write('\n\n\n')
        




##################################
#         THINGS TO RUN          #
##################################
# usage_logfiles = ['./cpu_usage_pandas_05.log','./cpu_usage_pandas_06.log',
#                 './cpu_usage_readline_01.log', './cpu_usage_readline_02.log']
# get_cpu_memory_usage(usage_logfiles)


# paths = ['linear_regression_pandas/trace/', 
# 'linear_regression_readline/trace/', 
# 'linear_regression_additional/trace/'] 
paths = ['temporary_folder_to_count_stack/trace/']
identify_vpython(paths)