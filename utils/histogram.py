import matplotlib.pyplot as plt
import numpy


file = open('count_stuff_results/stack_traces_v2_300.csv')
nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
# max_line = len(nonempty_lines)
file.close()

# for item in ['car','diabetes','energy','house','medical']:

items = ['car','diabetes','energy','house','medical']
count = 0
for line in nonempty_lines:
    if any(item in line for item in items):
        list000 = line.split(',')
        list000.pop(0)
        list000 = sorted(list000)
        print(str(list000[:10]))

        integer_map = map(int, list000)
        integer_list = list(integer_map)
        myset = set(list000)
        sorted_unique_list = sorted(list(set(list000)))
        # print('\n'+str(len(myset))+' => '+str(sorted(myset)))


        #####################
        # confidence intervals
        lower =  numpy.percentile(integer_list, 5)
        upper =  numpy.percentile(integer_list, 95)
        
        print(f"\n{items[count]}:\n90% confidence interval is between {lower} and {upper}")
        print(f"Full range is from {sorted_unique_list[0]} to {sorted_unique_list[-1]}")
        #####################


        # plt.title('%s dataset: pop count' % (items[count]))
        # plt.xlabel('value')
        # plt.ylabel('count')

        # print(plt.hist(list000, alpha=0.8, bins=len(myset)-1))
        # ymin, ymax = plt.gca().get_ylim() 
        # print(ymax)
        # plt.xticks(rotation=60)
        # plt.show()
        # plt.close()



        ##################################
        fig, ax = plt.subplots()
        plt.title('%s dataset: pop count' % (items[count]))
        plt.xlabel('value')
        plt.ylabel('count')

        ax.hist(list000, alpha=0.8, bins=len(myset)-1, color='deepskyblue')
        ymin, ymax = ax.get_ylim() 
        print('ymax:', ymax)
        
        # CI zone
        str_lower, str_upper = str(int(lower)), str(int(upper))
        print(str_lower)
        ax.fill_betweenx([0,ymax],[str_lower, str_lower], [str_upper, str_upper] ,
                        facecolor ='orange', alpha = 0.2)
        

        ax.hist(list000, alpha=0.8, bins=len(myset)-1, color='deepskyblue') # Repeat 'hist' to put important columns front
        plt.xticks(rotation=60)
        plt.show()
        # plt.savefig('image'+str(random.randint(1,100000))+'.png')
        plt.close()

        count += 1