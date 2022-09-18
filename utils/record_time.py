import time
import sys

if len(sys.argv) == 1:
    content = str(time.time()) + '\n'
elif sys.argv[1] == 'empty':
    content = '\n'


f = open('count_result/time_mark.csv', 'a')
f.write(content)
f.close()