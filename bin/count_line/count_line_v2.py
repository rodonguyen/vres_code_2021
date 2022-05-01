file = open("trace/vpython_ds1.txt", "r")
nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
line_count = len(nonempty_lines)
file.close()
print(line_count)