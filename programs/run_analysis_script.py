import sys
sys.path.insert(1, './utils')
from count_v1 import *
from convert_v1_to_v2 import *
from plot_histogram import *

########################################################
################# Change these variables ###############
########################################################

paths = (
    'programs/cknn/trace_cancer/',
    'programs/cknn/trace_wine_bin/',
    'programs/cknn/trace_wine_multi/',
    'programs/svm/trace_cancer/',
    'programs/svm/trace_wine_bin/',
    'programs/svm/trace_wine_multi/',
)

topic = 'noRandom'
v1_file = f"count_result/stack_trace_cknnsvm_{topic}.csv"
v2_file = f"count_result/stack_trace_cknnsvm_{topic}_v2.json"
histogram_filename_head = f"histogram_cknnsvm_{topic}_"


########################################################
##################    The magic part   #################
########################################################

extract_trace_v1(traces_dirs=paths, v1_file_output=v1_file,
                 with_tag_functions=True, 
                 function_start='function_start', 
                 function_end='function_end')

convert_v1_to_v2(v1_file_input=v1_file, 
                 v2_file_output=v2_file)

# plot_histogram_1by1(v2_file, histogram_filename_head)
