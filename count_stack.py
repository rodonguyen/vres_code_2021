# Using readlines()

def count_old_stack(dataset, method, file1):
    nonempty_lines1 = [line.strip("\n") for line in file1 if line != "\n"]
    max_line_1 = len(nonempty_lines1)
    file1.close()
    
    counter1 = {'push': 0, 'pop': 0, 'ext_pop': 0, 'stackadjshrink': 0, 'stackadjgrow': 0}
    start , _ = nonempty_lines1[0].split("->",1)
    for i in range(max_line_1):
        end , value1 = nonempty_lines1[i].split("->",1)
        counter1[value1] += 1
    exe_time = (int(end) - int(start))/1000000
    print(counter1)
    print('Execution time:', exe_time)

    f = open("results.txt", "a")
    f.write("Method: " + method + "\n")
    f.write("Dataset: " + str(dataset) + "\n")
    f.write('Execution time: ' + str(exe_time) + '\n')
    f.write(str(counter1) + '\n\n')
    f.close()

def count_new_stack(dataset, method, file1):
    nonempty_lines = [line.strip("\n") for line in file1 if line != "\n"]
    max_line = len(nonempty_lines)
    file1.close()
    # print(nonempty_lines1[0:10])

    _, counter = nonempty_lines[-1].split(' ', 1)
    start , _ = nonempty_lines[0].split("->",1)
    for i in reversed(range(max_line)):
        if '->' in nonempty_lines[i]:
            print(nonempty_lines[i])
            end, _ = nonempty_lines[i].split("->",1)
            break
    exe_time = (int(end) - int(start))/1000000
    print(counter)
    print('Execution time:', exe_time)

    f = open("results.txt", "a")
    f.write("Method: " + method + "\n")
    f.write("Dataset: " + str(dataset) + "\n")
    f.write('Execution time: ' + str(exe_time) + '\n')
    f.write(counter + '\n\n')
    f.close()

# for i in range(1,15+1):
#     dataset = i
#     path = 'strace_pandas/trace/'
#     file = open(path + 'stack_ds' + str(dataset) + '.txt', "r")
#     count_old_stack(dataset, path, file)


path = 'strace_pandas/'
file = open(path + 'stack.txt', "r")
count_old_stack(15, path, file)