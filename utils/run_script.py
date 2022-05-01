from count_v1 import *
from convert_v1_to_v2 import *


##################################
#         THINGS TO RUN          #
##################################

'''------------ linear_regression_real ------------'''
try:
    extract_trace_in_path('linear_regression_real/trace_car_only/', 
                            'function_start', 'function_end')
    extract_trace_in_path('linear_regression_real/trace_diabetes_only/', 
                            'function_start', 'function_end')
    extract_trace_in_path('linear_regression_real/trace_energy_only/', 
                            'function_start', 'function_end')
    extract_trace_in_path('linear_regression_real/trace_house_only/', 
                            'function_start', 'function_end')
    extract_trace_in_path('linear_regression_real/trace_medical_only/', 
                            'function_start', 'function_end')
except:
    print('linear_regression_real trace directories are not found.')


'''------------ simple_one ------------'''
try:
    extract_trace_in_path('simple_one/trace_print_nothing/',    'function_start', 'function_end')
    extract_trace_in_path('simple_one/trace_print_nothing/',    'function_start', 'function_end')
except:
    print('simple_one trace directories are not found.')


convert_v1_to_v2()