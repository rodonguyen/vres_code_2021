from count_v1 import *
from convert_v1_to_v2 import *


##################################
#         THINGS TO RUN          #
##################################

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

convert_v1_to_v2()