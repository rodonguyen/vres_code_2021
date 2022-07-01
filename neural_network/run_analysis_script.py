import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, './utils')

from count_v1 import *
from convert_v1_to_v2 import *
from plot_histogram import *

########################################################
################# Change these variables ###############
########################################################

paths = (
    'neural_network/trace_car'
)
v1_file = './count_result/stack_trace_xxx.csv'
v2_file = './count_result/stack_trace_xxx_v2.json'
histogram_filename_head = 'histogram_xxx_'


########################################################
##################    The magic part   #################
########################################################

extract_trace_v1(traces_dirs=paths, v1_file_output=v1_file,
                 with_tag_functions=True, 
                 function_start='function_start', 
                 function_end='function_end')

convert_v1_to_v2(v1_file_input=v1_file, 
                 v2_file_output=v2_file)

plot_histogram_1by1(v2_file, histogram_filename_head)
