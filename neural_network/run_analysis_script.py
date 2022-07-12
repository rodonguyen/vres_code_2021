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
    # 'neural_network/trace_car_noRandom/',
    # 'neural_network/trace_diabetes_noRandom/',
    # 'neural_network/trace_energy_noRandom/',
    # 'neural_network/trace_house_noRandom/',
    # 'neural_network/trace_medical_noRandom/',
    # 'neural_network/trace_car_withRandom/',
    # 'neural_network/trace_diabetes_withRandom/',
    # 'neural_network/trace_energy_withRandom/',
    # 'neural_network/trace_house_withRandom/',
    'neural_network/trace_medical_withRandom/',
)

# Define filenames to store results
# v1_file = 'count_result/stack_trace_nn_noRandom.csv'
# v2_file = 'count_result/stack_trace_nn_noRandom_v2.json'
# histogram_filename_head = 'histogram_nn_noRandom_'

v1_file = 'count_result/stack_trace_nn_withRandom.csv'
v2_file = 'count_result/stack_trace_nn_withRandom_v2.json'
histogram_filename_head = 'histogram_nn_withRandom_'


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



