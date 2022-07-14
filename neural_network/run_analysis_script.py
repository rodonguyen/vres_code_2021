import sys
sys.path.insert(1, './utils')

from count_v1 import *
from convert_v1_to_v2 import *
from plot_histogram import *

########################################################
################# Change these variables ###############
########################################################

# Trace directories created in our bash script
paths = (
    'neural_network/trace_car/',
    'neural_network/trace_diabetes/',
    'neural_network/trace_energy/',
    'neural_network/trace_house/',
    'neural_network/trace_medical/',

    # 'neural_network/trace_car_withRandom/',
    # 'neural_network/trace_diabetes_withRandom/',
    # 'neural_network/trace_energy_withRandom/',
    # 'neural_network/trace_house_withRandom/',
    # 'neural_network/trace_medical_withRandom/',
)

# Define filenames to store results
topic = 'withRandom_40_forLoop_8'
v1_file = f"count_result/stack_trace_nn_{topic}.csv"
v2_file = f"count_result/stack_trace_nn_{topic}_v2.json"
histogram_filename_head = f"histogram_nn_{topic}_"

# v1_file = 'count_result/stack_trace_nn_withRandom.csv'
# v2_file = 'count_result/stack_trace_nn_withRandom_v2.json'
# histogram_filename_head = 'histogram_nn_withRandom_'


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



