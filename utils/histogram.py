import matplotlib.pyplot as plt
import numpy
import random


file = open('count_stuff_results/stack_traces_v2_01.csv')
nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
# max_line = len(nonempty_lines)
file.close()

for line in nonempty_lines:
    for item in ['car']:
        if item in line:
            list000 = line.split(',')
            list000.pop(0)
            list000.pop(-1)
            list000 = sorted(list000)

            integer_map = map(int, list000)
            integer_list = list(integer_map)
            myset = set(list000)
            print('\n'+str(len(myset))+'=>'+str(sorted(myset)))


            #####################
            # confidence intervals
            lower =  numpy.percentile(integer_list, 5)
            upper =  numpy.percentile(integer_list, 95)
            
            print(f"\n90 confidence interval {lower} and {upper}")
            #####################

            # height, bins, patches = plt.hist(list000, alpha=0.8, bins=len(myset)-1)
            # plt.fill_betweenx([0, height.max()], lower, upper, color='g', alpha=0.2)

            plt.hist(list000, alpha=0.8, bins=len(myset)-1)
            plt.xticks(rotation=60)
            plt.show()
            # plt.savefig('image'+str(random.randint(1,100000))+'.png')
