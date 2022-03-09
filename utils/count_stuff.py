import datetime
import os

def extract_trace_in_path(path, function_start_name, function_end_name):
    destination1 = './count_stuff_results/stack_traces.csv'
    csv = open(destination1, 'a')
    csv.write('filepath, file no., execution time, start time, end time, pop, push, sgrow, sshrink\n')
    csv.close()

    destination2 = './count_stuff_results/stack_traces_in_each_part.csv'
    csv = open(destination2, 'a')
    csv.write('filepath, file no., pop_before_A, push_before_A, sgrow_before_A, sshrink_before_A,' + 
                'pop_in_A, push_in_A, sgrow_in_A, sshrink_in_A,' + 
                'pop_after_A, push_after_A, sgrow_after_A, sshrink_after_A\n')
    csv.close()

    for vpython_name in sorted(os.listdir(path)):
        full_vpython_path = path + vpython_name
        print(full_vpython_path)

        # Record all trace
        # count_stack(full_vpython_path, destination1)

        # Record in an area
        count_stack_in_each_part(full_vpython_path, destination2,
                                    function_start_name, function_end_name)
        

def count_stack_in_each_part(vpython_path, output_file, function_start_name, function_end_name):
    file = open(vpython_path)
    nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
    max_line = len(nonempty_lines)
    file.close()

    # Get memory_op before and after
    for i in reversed(range(max_line)):
        if function_start_name in nonempty_lines[i]:
            if '>>> ' in nonempty_lines[i-1]:
                memory_op_before_function_start = nonempty_lines[i-1].split(' ', 1)[1]
            else: 
                print('memory_op is not found in previous line.')
            break
    
    for i in reversed(range(max_line)):
        if function_end_name in nonempty_lines[i]:
            if '>>> ' in nonempty_lines[i+1]:
                memory_op_after_function_end = nonempty_lines[i+1].split(' ', 1)[1]
            else: 
                print('memory_op is not found in line after.')
            break

    for i in reversed(range(max_line)):
        if '>>>' in nonempty_lines[i]:
            memory_op_last = nonempty_lines[i].split(' ', 1)[1]
            break
    
    # Memory op before A (pop1, ...)
    pop, push, sgrow, sshrink = memory_op_before_function_start.split(' | ')
    _, pop1 = pop.split(' ')
    _, push1 = push.split(' ')
    _, sgrow1 = sgrow.split(' ')
    _, sshrink1 = sshrink.split(' ')

    pop, push, sgrow, sshrink = memory_op_after_function_end.split(' | ')
    _, pop2 = pop.split(' ')
    _, push2 = push.split(' ')
    _, sgrow2 = sgrow.split(' ')
    _, sshrink2 = sshrink.split(' ')

    pop, push, sgrow, sshrink = memory_op_last.split(' | ')
    _, pop3 = pop.split(' ')
    _, push3 = push.split(' ')
    _, sgrow3 = sgrow.split(' ')
    _, sshrink3 = sshrink.split(' ')

    # Memory op in A
    pop, push, sgrow, sshrink = int(pop2)-int(pop1), int(push2)-int(push1), int(sgrow2)-int(sgrow1), int(sshrink2)-int(sshrink1)
    # Memory op after A
    pop4, push4, sgrow4, sshrink4 = int(pop3)-int(pop2), int(push3)-int(push2), int(sgrow3)-int(sgrow2), int(sshrink3)-int(sshrink2)

    # Record delta stuff in a line
    csv = open(output_file, 'a')
    csv.write('{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16},{17}\n'.format(
                vpython_path, vpython_path[-7:-4],
                pop1, push1, sgrow1, sshrink1,
                pop, push, sgrow, sshrink,
                pop4, push4, sgrow4, sshrink4,
                pop3, push3, sgrow3, sshrink3))
    csv.close()
    # End


# Count the linear regression stacks
def extract_trace_in_multiple_paths(paths):
    destination = './count_stuff_results/stack_traces.csv'

    for path in sorted(paths):
        for dir in sorted(os.listdir(path)):
            print('\ndir: ' + dir)
            temp_path = path + dir 
            for vpython_name in sorted(os.listdir(temp_path)):
                count_stack(temp_path + '/' + vpython_name, destination)
            csv = open(destination, 'a')
            csv.write('\n')
            csv.close()

    csv = open(destination, 'a')
    csv.write('filepath, file no., execution time, start time, end time, pop, push, sgrow, sshrink\n')
    csv.close()

def count_stack(vpython_path, output_file):
    print(vpython_path)
    file = open(vpython_path)
    nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
    max_line = len(nonempty_lines)
    file.close()

    start_time = nonempty_lines[0].split("->",1)[0]
    for i in reversed(range(max_line)):
        if '->' in nonempty_lines[i]:
            # print(nonempty_lines[i])
            end_time = nonempty_lines[i].split("->",1)[0]
            break
    for i in reversed(range(max_line)):
        if '>>>' in nonempty_lines[i]:
            counter_end = nonempty_lines[i].split(' ', 1)[1]
            break

    exe_time = (int(end_time) - int(start_time))/1000000
    start_time = datetime.datetime.fromtimestamp(int(start_time[:-6])).strftime('%H:%M:%S')
    end_time = datetime.datetime.fromtimestamp(int(end_time[:-6])).strftime('%H:%M:%S')

    # Record stack trace in results.csv
    pop, push, sgrow, sshrink = counter_end.split(' | ')
    _, pop = pop.split(' ')
    _, push = push.split(' ')
    _, sgrow = sgrow.split(' ')
    _, sshrink = sshrink.split(' ')
    csv = open(output_file, 'a')
    csv.write('{0},{1},{2},{3},{4},{5},{6},{7},{8}\n'.format(
                vpython_path, vpython_path[-7:-4], str(exe_time),
                start_time, end_time,
                pop, push, sgrow, sshrink ))
    csv.close()

def get_cpu_usage(usage_logfiles = ['./cpu_usage.log']):
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

# usage_logfiles = ['cpu_usage_readline_04.log', 
#     'cpu_usage_readline_05.log',
#     'cpu_usage_readline_06.log']
# get_cpu_usage(usage_logfiles)


# paths = ['linear_regression_pandas/trace/', 
# 'linear_regression_readline/trace/', 
# 'linear_regression_additional/trace/'] 
# paths = ['temporary_folder_for_stacks/trace/']


## This one extract all vpython in its sub-dir
# paths = ['linear_regression_additional/trace/']
# extract_trace_in_multiple_paths(paths)

extract_trace_in_path('linear_regression_additional/trace_car_only/', 
                        'function_start', 'function_end')