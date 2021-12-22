# Using readlines()


def f(dataset, method, file1):
    # Compare length and strim
    nonempty_lines1 = [line.strip("\n") for line in file1 if line != "\n"]
    max_line_1 = len(nonempty_lines1)
    file1.close()
    # print(nonempty_lines1[0:10])


    counter1 = {'push': 0, 'pop': 0, 'ext_pop': 0, 'stackadjshrink': 0, 'stackadjgrow': 0}

    for i in range(max_line_1):
        _ , value1 = nonempty_lines1[i].split("->",1)
        counter1[value1] += 1

    print(counter1)


    f = open("comparision.txt", "a")
    f.write("Method: " + method + "\n")
    f.write("Dataset: " + str(dataset) + "\n")
    f.write(str(counter1) + '\n\n')
    f.close()

for i in range(6,9):
    dataset = i
    method = 'readline'
    file1 = open("strace_"+ method + "/trace/stack_ds" + str(dataset) + ".txt", "r")
    f(dataset, method, file1)