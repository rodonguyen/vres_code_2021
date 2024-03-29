import sys
sys.path.insert(1, './utils')
from count_v1 import *
from convert_v1_to_v2 import *
from plot_histogram import *

########################################################
################# Change these variables ###############
########################################################

paths = (
    # 'programs/cknn/trace_cancer/',
    # 'programs/cknn/trace_wine_bin/',
    # 'programs/cknn/trace_wine_multi/',
    # 'programs/svm/trace_cancer/',
    # 'programs/svm/trace_wine_bin/',
    # 'programs/svm/trace_wine_multi/',

    # 'programs/linear_regression/trace_car/',
    # 'programs/linear_regression/trace_energy/',
    # 'programs/linear_regression/trace_house/',
    # 'programs/linear_regression/trace_medical/',

    # 'programs/activity/v2_nb/trace_pa/',
    # 'programs/activity/v2_nb/trace_pg/',

    # 'programs/activity/v2_nb/trace_pa_path/',

    # 'programs/activity/v2_nb/trace_pa_integer/',
    # 'programs/activity/v2_nb/trace_pa_X100integer/',

    # 'programs/mushroom/trace/',
    # 'programs/weather/trace/',

    # 'programs/mnist/trace/',
    'programs/gan_mnist/trace/',

)

topic = ''
program = 'ganMNIST'
v1_file = f"count_result/trace_{program}_{topic}.csv"
v2_file = f"count_result/trace_{program}_{topic}_v2.json"
histogram_filename_head = f"histogram_{program}_{topic}_"


########################################################
##################    The magic part   #################
########################################################

extract_trace_v1(   traces_dirs=paths, 
                    v1_file_output=v1_file,
                    with_tag_functions=True,
                    function_start='function_start', 
                    function_end='function_end'
                )

# convert_v1_to_v2(v1_file_input=v1_file, 
#                  v2_file_output=v2_file)

# plot_histogram_1by1(v2_file, histogram_filename_head)
