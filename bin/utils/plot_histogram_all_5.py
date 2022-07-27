import matplotlib.pyplot as plt
import numpy
# from scipy.interpolate import make_interp_spline, BSpline

mybiglist = []

integer_list_for_CI = [
    4,18,24,35,49,34,36,26,19,16,18,5,6,3,5,2 
]
lower =  numpy.percentile(integer_list_for_CI, 5)
upper =  numpy.percentile(integer_list_for_CI, 95)
lower = sum(integer_list_for_CI)*0.05 # => From 3rd collumn
upper =  sum(integer_list_for_CI)*0.95  # => To 12th column inclusive 
lower = 2.76
upper = 12.8
print(lower, upper, sum(integer_list_for_CI))

with open('5histogram.csv') as f:
    for i in range(6):
        mylist = f.readline().replace('\n','').split(',')

        integer_map = map(int, mylist)
        mybiglist.append(list(integer_map))

        # print(mybiglist)

# average = numpy.array([3.6,12.6,24.2,33.8,43.6,35.6,40.2,32.2,22.8,16.8,11.6,7.2,6.8,4.6,2.6,2.6])
# average = numpy.array([5,	12,	22,	34	,38	,40,36,	31,	23,	18,	12	,8	,6	,5	,3	,2])
# spl = make_interp_spline(mybiglist[0], average, k=2)
# spline = make_interp_spline(mybiglist[0], average, k=3)
# xnew = numpy.linspace(min(mybiglist[0]), max(mybiglist[0]), 300)
# average = spl(xnew)


plt.rcParams.update({'font.size': 24})
plt.title(f"5 real-world datasets: pop histogram")
plt.rcParams.update({'font.size': 18})
plt.xlabel(f"Representing value")
plt.ylabel('Frequency')

width = 0.15
ax = plt.subplot(111)
ax.fill_betweenx([0,max(integer_list_for_CI)],[lower, lower], [upper, upper] ,
                        facecolor ='orange', alpha = 0.15)
                        
# ax.bar(mybiglist[0],mybiglist[1], width, color='red')
ax.bar(mybiglist[0],mybiglist[1], width, color='gold')
ax.bar(numpy.array(mybiglist[0]) +width,mybiglist[2], width, color='orange')
ax.bar(numpy.array(mybiglist[0]) +width*2,mybiglist[3], width, color='limegreen')
ax.bar(numpy.array(mybiglist[0]) +width*3,mybiglist[4], width, color='deepskyblue')
ax.bar(numpy.array(mybiglist[0]) +width*4,mybiglist[5], width, color='darkviolet')

# ax.bar(mybiglist[0],mybiglist[1], width)
# ax.bar(numpy.array(mybiglist[0]) +width,mybiglist[2], width)
# ax.bar(numpy.array(mybiglist[0]) +width*2,mybiglist[3], width)
# ax.bar(numpy.array(mybiglist[0]) +width*3,mybiglist[4], width)
# ax.bar(numpy.array(mybiglist[0]) +width*4,mybiglist[5], width)
# ax.plot(xnew, average, color = 'blue' )


colors = {'car':'gold', 'diabetes':'orange', 'energy':'limegreen', 
            'house':'deepskyblue', 'medical':'darkviolet', }         
# set 2
# colors = {'car':'red', 'diabetes':'orange', 'energy':'limegreen', 
#             'house':'deepskyblue', 'medical':'darkviolet', }         

labels = list(colors.keys())
handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
plt.legend(handles, labels)

plt.show()


# file = open('count_stuff_results/stack_traces_v2_300.csv')
# nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
# # max_line = len(nonempty_lines)
# file.close()

# # for item in ['car','diabetes','energy','house','medical']:

# items = ['car','diabetes','energy','house','medical']
# Items = ['Car','Diabetes','Energy','House','Medical']
# count = 0
# type = 'pop'

# for line in nonempty_lines:
#     if any(item in line for item in items):
#         list000 = line.split(',')
#         list000.pop(0)
#         list000 = sorted(list000)
#         # print(str(list000[:10]))

#         integer_map = map(int, list000)
#         integer_list = list(integer_map)
#         myset = set(list000)
#         sorted_unique_list = sorted(list(set(list000)))
#         print('\n' + str(len(myset)) + ' values') #+' => '+str(sorted(myset)))


#         #####################
#         # confidence intervals
#         lower =  numpy.percentile(integer_list, 5)
#         upper =  numpy.percentile(integer_list, 95)
        
#         print(f"{items[count]}:")
#         print(f"90% CI:     <{int(lower)},{int(upper)}>")
#         print(f"Full range: <{sorted_unique_list[0]},{sorted_unique_list[-1]}>")
#         #####################

#         ## OLD VERSION
#         # plt.title('%s dataset: pop count' % (items[count]))
#         # plt.xlabel('value')
#         # plt.ylabel('count')

#         # print(plt.hist(list000, alpha=0.8, bins=len(myset)-1))
#         # ymin, ymax = plt.gca().get_ylim() 
#         # print(ymax)
#         # plt.xticks(rotation=60)
#         # plt.show()
#         # plt.close()
#         ##################################
#         fig, ax = plt.subplots()
#         plt.rcParams.update({'font.size': 24})
#         plt.title(f"'{Items[count]}' dataset: {type} histogram")
#         plt.rcParams.update({'font.size': 18})
#         plt.xlabel(f"{type} value")
#         plt.ylabel('Frequency')

#         # Testing: get histogram
#         histogram, a, b = ax.hist(list000, alpha=0.8, bins=30, color='deepskyblue')
#         print(histogram)
#         csv = open('5histogram.csv', 'a')
#         for x in numpy.nditer(histogram):
#             csv.write(f"{x},")
#         csv.write('\n')
#         csv.close()
#         # numpy.savetxt('myfile.csv', a, delimiter=',')


#         ax.hist(list000, alpha=0.8, bins=len(myset)-1, color='deepskyblue')
#         ymin, ymax = ax.get_ylim() 
#         # print('ymax:', ymax)
        
#         # CI zone
#         str_lower, str_upper = str(int(lower)), str(int(upper))
#         ax.fill_betweenx([0,ymax],[str_lower, str_lower], [str_upper, str_upper] ,
#                         facecolor ='orange', alpha = 0.2)
        

#         ax.hist(list000, alpha=0.8, bins=len(myset)-1, color='deepskyblue') # Repeat 'hist' to put important columns front
#         plt.xticks(rotation=60)
#         plt.show()
#         # plt.savefig('image'+str(random.randint(1,100000))+'.png')
#         plt.close()

#         count += 1
#         if (count == 5): 
#             count = 0
#             type = 'push'