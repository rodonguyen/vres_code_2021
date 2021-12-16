# Using readlines()
file1 = open('vpython_ds1.txt', 'r')
lines1 = file1.readlines()
 
file2 = open('vpython_ds2.txt', 'r')
lines1 = file2.readlines()

# Compare length and strim


count = 0
# Strips the newline character
for line in lines1:
    count += 1
    _ , value1 = line.split("->",1)


    # writing to file
    # file1 = open('myfile.txt', 'w')
    # file1.writelines(value1 + ' | ' + value2)
    # file1.close()

    if count > 100:
        break