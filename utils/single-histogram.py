import matplotlib.pyplot as plt
import numpy


file = open('count_stuff_results/stack_traces_v2_300.csv')
nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
# max_line = len(nonempty_lines)
file.close()

# for item in ['car','diabetes','energy','house','medical']:

items = ['car','diabetes','energy','house','medical']
Items = ['Car','Diabetes','Energy','House','Medical']
count = 0
type = 'pop'

for line in nonempty_lines:
    if any(item in line for item in items):
        list000 = line.split(',')
        list000.pop(0)
        list000 = sorted(list000)
        # print(str(list000[:10]))

        integer_map = map(int, list000)
        integer_list = list(integer_map)
        myset = set(list000)
        sorted_unique_list = sorted(list(set(list000)))
        print('\n' + str(len(myset)) + ' values') #+' => '+str(sorted(myset)))


        #####################
        # confidence intervals
        lower =  numpy.percentile(integer_list, 5)
        upper =  numpy.percentile(integer_list, 95)
        
        print(f"{items[count]}:")
        print(f"90% CI:     <{int(lower)},{int(upper)}>")
        print(f"Full range: <{sorted_unique_list[0]},{sorted_unique_list[-1]}>")
        #####################

        ## OLD VERSION
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
        plt.rcParams.update({'font.size': 24})
        plt.title(f"'{Items[count]}' dataset: {type} histogram")
        plt.rcParams.update({'font.size': 18})
        plt.xlabel(f"{type} value")
        plt.ylabel('Frequency')

        # Testing: get histogram
        histogram, a, b = ax.hist(list000, alpha=0.8, bins=len(myset)-1, color='deepskyblue')
        print(histogram)
        csv = open('5histogram.csv', 'a')
        for x in numpy.nditer(histogram):
            csv.write(f"{x},")
        csv.write('\n')
        csv.close()
        # numpy.savetxt('myfile.csv', a, delimiter=',')


        ax.hist(list000, alpha=0.8, bins=len(myset)-1, color='deepskyblue')
        ymin, ymax = ax.get_ylim() 
        # print('ymax:', ymax)
        
        # CI zone
        str_lower, str_upper = str(int(lower)), str(int(upper))
        ax.fill_betweenx([0,ymax],[str_lower, str_lower], [str_upper, str_upper] ,
                        facecolor ='orange', alpha = 0.2)
        

        ax.hist(list000, alpha=0.8, bins=len(myset)-1, color='deepskyblue') # Repeat 'hist' to put important columns front
        plt.xticks(rotation=60)
        plt.show()
        # plt.savefig('image'+str(random.randint(1,100000))+'.png')
        plt.close()

        count += 1
        if (count == 5): 
            count = 0
            type = 'push'
