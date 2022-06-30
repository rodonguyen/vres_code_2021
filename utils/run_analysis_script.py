from count_v1 import *
from convert_v1_to_v2 import *
from plot_histogram import *

########################################################
################# Change these variables ###############
paths = (
    'linear_regression_real/trace_car_only/',
    'linear_regression_real/trace_diabetes_only/',
    'linear_regression_real/trace_energy_only/',
    'linear_regression_real/trace_house_only/',
    'linear_regression_real/trace_medical_only/'
)
v1_file = './count_result/stack_trace_laptop_first100.csv'
v2_file = './count_result/stack_trace_laptop_first100_v2.json'
histogram_filename_head = 'histogram_xxx_'


########################################################
##################    The magic part   #################
extract_trace_v1(paths, v1_file,
                 True, 'function_start', 'function_end')

convert_v1_to_v2(v1_file=v1_file, v2_file=v2_file)

plot_histogram_1by1(v2_file, histogram_filename_head)
