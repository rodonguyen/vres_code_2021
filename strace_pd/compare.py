# Using readlines()
file1 = open("trace/vpython_ds1.txt", "r")
file2 = open("trace/vpython_ds2.txt", "r")
# lines1 = file1.readlines()
# lines2 = file2.readlines()

# Compare length and strim
nonempty_lines1 = [line.strip("\n") for line in file1 if line != "\n"]
nonempty_lines2 = [line.strip("\n") for line in file2 if line != "\n"]
max_line = len(nonempty_lines2) if (nonempty_lines1 >= nonempty_lines2) \
                                else len(nonempty_lines1)
print(nonempty_lines1[0:10])


# Strips the newline character
lines1 = file1.readlines()
lines2 = file2.readlines()

for i in range(max_line):
    _ , value1 = nonempty_lines1[i].split("->",1)
    _ , value2 = nonempty_lines2[i].split("->",1)
    print( value1 + ' | ' + value2 + "")

    if value1 != value2:
        print('Difference detected!')
        print('Stop at line ' + str(i))
        break
    if i > 1000000:
        print('Stop at line ' + str(i))


file1.close()
file2.close()