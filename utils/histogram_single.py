import matplotlib.pyplot as plt
import numpy


########################## UTILITY FUNCTIONS ############################

def plot(line, type):
    # Get all figures of one item 
    list000 = line.split(',')
    dataset_name = list000.pop(0) # remove the item name
    list000 = sorted(list000)
    # print(str(list000[:10]))

    # Get the number of unique values
    integer_map = map(int, list000)
    integer_list = list(integer_map)
    myset = set(list000)
    sorted_unique_list = sorted(list(set(list000)))
    print('\n' + str(len(myset)) + ' values') #+' => '+str(sorted(myset)))
    print(sorted_unique_list)

    # Calculate confidence intervals
    lower =  numpy.percentile(integer_list, 5)
    upper =  numpy.percentile(integer_list, 95)
    
    print(f"{dataset_name}:")
    print(f"90% CI:     <{int(lower)},{int(upper)}>")
    print(f"Full range: <{sorted_unique_list[0]},{sorted_unique_list[-1]}>")

    # Plot 
    # Configure chart
    fig, ax = plt.subplots()
    plt.rcParams.update({'font.size': 24})
    plt.title(f"'{dataset_name}' dataset: {type} histogram")
    plt.rcParams.update({'font.size': 18})
    plt.xlabel(f"{type} value")
    plt.ylabel('Frequency')

    # Plot the histogram 1st time and 
    # Save histogram of each item for later use
    histogram, a, b = ax.hist(list000, alpha=0.8, bins=len(myset)-1, color='deepskyblue')
    print(histogram)
    csv = open('count_stuff_results/histogram-push-and-pop.csv', 'a')
    csv.write(items[count]+'\n')
    csv.write(','.join(sorted_unique_list))
    csv.write('\n')
    for x in numpy.nditer(histogram):
        csv.write(f"{x},")
    csv.write('\n')
    csv.close()
    # numpy.savetxt('myfile.csv', a, delimiter=',')

    # Plot fade Confidence Interval 
    ax.hist(list000, alpha=0.8, bins=len(myset)-1, color='deepskyblue')
    ymin, ymax = ax.get_ylim() 
    # CI zone
    str_lower, str_upper = str(int(lower)), str(int(upper))
    ax.fill_betweenx([0,ymax],[str_lower, str_lower], [str_upper, str_upper] ,
                    facecolor ='orange', alpha = 0.2)

    
    # Plot the histogram 2nd time to overlay the CI layer 
    ax.hist(list000, alpha=0.8, bins=len(myset)-1, color='deepskyblue') # Repeat 'hist' to put important columns front
    plt.xticks(rotation=60)
    plt.show()
    # plt.savefig('image'+str(random.randint(1,100000))+'.png')
    plt.close()


###############################################################


file = open('count_stuff_results/stack_traces_in_each_part_v2.csv')
nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
# max_line = len(nonempty_lines)
file.close()

# for item in ['car','diabetes','energy','house','medical']:

items = ['car','diabetes','energy','house','medical']
Items = ['Car','Diabetes','Energy','House','Medical']
count = 0
type = 'pop'


for i,line in enumerate(nonempty_lines):
    if 'pop' in line:
        try:
            for k in range(1,6):
                plot(nonempty_lines[i+k],'pop')
        except:
            print(f"Other dataset is not found. Stop at k = {k}.")
    if 'push' in line:
        try:
            for k in range(1,6):
                plot(nonempty_lines[i+k],'push')
        except:
            print(f"Other dataset is not found. Stop at k = {k}.")




# for line in nonempty_lines:
#     if any(item in line for item in items):
#         # Get all figures of one item 
#         list000 = line.split(',')
#         list000.pop(0) # remove the item name
#         list000 = sorted(list000)
#         # print(str(list000[:10]))

#         # Get the number of unique values
#         integer_map = map(int, list000)
#         integer_list = list(integer_map)
#         myset = set(list000)
#         sorted_unique_list = sorted(list(set(list000)))
#         print('\n' + str(len(myset)) + ' values') #+' => '+str(sorted(myset)))
#         print(sorted_unique_list)

#         # Calculate confidence intervals
#         lower =  numpy.percentile(integer_list, 5)
#         upper =  numpy.percentile(integer_list, 95)
        
#         print(f"{items[count]}:")
#         print(f"90% CI:     <{int(lower)},{int(upper)}>")
#         print(f"Full range: <{sorted_unique_list[0]},{sorted_unique_list[-1]}>")

#         # Plot 
#         # Configure chart
#         fig, ax = plt.subplots()
#         plt.rcParams.update({'font.size': 24})
#         plt.title(f"'{Items[count]}' dataset: {type} histogram")
#         plt.rcParams.update({'font.size': 18})
#         plt.xlabel(f"{type} value")
#         plt.ylabel('Frequency')

#         # Plot the histogram 1st time and 
#         # Save histogram of each item for later use
#         histogram, a, b = ax.hist(list000, alpha=0.8, bins=len(myset)-1, color='deepskyblue')
#         print(histogram)
#         csv = open('count_stuff_results/histogram-push-and-pop.csv', 'a')
#         csv.write(items[count]+'\n')
#         csv.write(','.join(sorted_unique_list))
#         csv.write('\n')
#         for x in numpy.nditer(histogram):
#             csv.write(f"{x},")
#         csv.write('\n')
#         csv.close()
#         # numpy.savetxt('myfile.csv', a, delimiter=',')

#         # Plot fade Confidence Interval 
#         ax.hist(list000, alpha=0.8, bins=len(myset)-1, color='deepskyblue')
#         ymin, ymax = ax.get_ylim() 
#         # CI zone
#         str_lower, str_upper = str(int(lower)), str(int(upper))
#         ax.fill_betweenx([0,ymax],[str_lower, str_lower], [str_upper, str_upper] ,
#                         facecolor ='orange', alpha = 0.2)

        
#         # Plot the histogram 2nd time to overlay the CI layer 
#         ax.hist(list000, alpha=0.8, bins=len(myset)-1, color='deepskyblue') # Repeat 'hist' to put important columns front
#         plt.xticks(rotation=60)
#         plt.show()
#         # plt.savefig('image'+str(random.randint(1,100000))+'.png')
#         plt.close()

#         count += 1
#         if (count == 5): 
#             count = 0
#             type = 'push'
