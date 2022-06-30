from count_v1 import *
from convert_v1_to_v2 import *
from plot_histogram import *

##################################
#         THINGS TO RUN          #
##################################

# '''------------ linear_regression_real ------------'''
# paths = (
#     'linear_regression_real/trace_car_only/',
#     'linear_regression_real/trace_diabetes_only/',
#     'linear_regression_real/trace_energy_only/',
#     'linear_regression_real/trace_house_only/',
#     'linear_regression_real/trace_medical_only/'
# )
# try:
#     extract_trace_in_paths_with_function_start_end(
#         paths, 'function_start', 'function_end')
# except:
#     print('Error. MAYBE linear_regression_real trace directories are not found.')


convert_v1_to_v2(
    v1_file='./count_result/stack_trace_laptop_first100.csv',
    v2_file='./count_result/stack_trace_laptop_first100_v2.json')

'''------------ simple_one ------------'''
# paths = (
#     'simple_one/trace_print_nothing/',
#     'simple_one/trace_pandas_play',
#     'simple_one/trace_importing1_many',
#     'simple_one/trace_importing2_pd',
#     'simple_one/trace_importing3_pd_and_load',
#     'simple_one/trace_importing4_manypd',
#     'simple_one/trace_importing5_manysklearn',
#     )
# try:
#     extract_trace_in_paths(paths, 'simple_one')
# except:
#     print('Errors in locating simple_one trace directories')


# convert_v1_to_v2({'pop':5, 'push':6}, 'simple_one',
#         ['importing1_many', 'importing2_pd', 'importing3_pd_and_load',
#         'importing4_manypd', 'importing5_manysklearn',
#         'print_nothing', 'pandas_play'])

# plot_histogram_1by1()
