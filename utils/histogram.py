import matplotlib.pyplot as plt
import numpy


file = open('count_stuff_results/stack_trace_v2.csv')
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

            height, bins, patches = plt.hist(list000, alpha=0.8, bins=15)
            # plt.fill_betweenx([0, height.max()], lower, upper, color='g', alpha=0.2)

            # fig = plt.figure()
            # ax1 = fig.
            plt.xticks(rotation=60)
            # plt.hist(list000)
            plt.show()
