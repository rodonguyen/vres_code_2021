import time

f = open('count_result/time_mark.csv', 'a')
f.write(str(time.time()) + '\n')
f.close()