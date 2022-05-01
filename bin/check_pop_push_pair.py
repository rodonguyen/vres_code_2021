import matplotlib.pyplot as plt
import numpy


file = open('count_stuff_results/stack_traces_v2_200_copy.csv')
nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
# max_line = len(nonempty_lines)
file.close()

# for item in ['car','diabetes','energy','house','medical']:

items = ['car','diabetes','energy','house','medical']
# items = ['car']
count = 0
car = {}
pop = 1

for item in items:
    # Get 2 lines of pop and push values
    print(f"\n=== item: {item} ===")
    for line in nonempty_lines:
        if item in line and pop == 0:
            list1 = line.split(',')
            list1.pop(0)
            print(f"sample list1: {list1[0:5]}")
            pop = 9999
            # list1 = sorted(list1)
        if item in line and pop == 1:
            list0 = line.split(',')
            list0.pop(0)
            print(f"sample list0: {list0[0:5]}")
            # list0 = sorted(list0)
            pop -= 1

    # Compare and check the theory
    for i,key in enumerate(list0):
        if key in car.keys():
            if car[key] != list1[i]: print(f"eeeer, different value at i = {i}")
        else:
            car[key] = list1[i]

    pop = 1
