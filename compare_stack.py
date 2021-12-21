# Using readlines()
file1 = open("trace/stack_ds1.txt", "r")
file2 = open("trace/stack_ds2.txt", "r")
# lines1 = file1.readlines()
# lines2 = file2.readlines()
file1.close()
file2.close()

dataset = 1
method = 'panda'
# Compare length and strim
nonempty_lines1 = [line.strip("\n") for line in file1 if line != "\n"]
nonempty_lines2 = [line.strip("\n") for line in file2 if line != "\n"]
max_line_1 = len(nonempty_lines1)
max_line_2 = len(nonempty_lines2)
max_line = len(nonempty_lines2) if (nonempty_lines1 >= nonempty_lines2) \
                                else len(nonempty_lines1)
# print(nonempty_lines1[0:10])


counter1 = {'push': 0, 'pop': 0, 'ext_pop': 0, 'stackadjshrink': 0, 'stackadjgrow': 0}
counter2 = {'push': 0, 'pop': 0, 'ext_pop': 0, 'stackadjshrink': 0, 'stackadjgrow': 0}

for i in range(max_line_1):
    _ , value1 = nonempty_lines1[i].split("->",1)
    counter1[value1] += 1
for i in range(max_line_2):
    _ , value2 = nonempty_lines2[i].split("->",1)
    counter2[value2] += 1

print(counter1)
print(counter2)


f = open("comparision.txt", "a")
f.write("Now the file has more content!")
f.close()