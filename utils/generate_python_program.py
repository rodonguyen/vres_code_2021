import sys
sys.path.insert(0, './programs')
import program_text

def generate(program_content, row_nums):
    for col_num in col_nums:
        for row_num in row_nums:
            filename = f"{filename_head}_{col_num}col_{row_num:08d}.py"
            dataset_filename = f"{filename_head}_{col_num}col_{row_num}.csv"
            full_path = destination_dir + filename
            f = open(full_path, "w") 
            f.write(program_content % (dataset_filename))
        f.close()

def generate_nn_code(program_content, row_nums):
    for row_num in row_nums:
        filename = f"{filename_head}_{row_num}.py"
        full_path = destination_dir + filename
        f = open(full_path, "w") 
        f.write(program_content % (row_num, row_num))
    f.close()

destination_dir = "programs/mnist/code6layers/"
filename_head = 'mnist' # w_IntegerX100Temp # w_Float2DigitsTemp
# row_nums = [10,20,50,75,100,250,500,750,1000,2500,5000,7500,
#             10_000,25_000,50_000,75_000,100_000,250_000,500_000,750_000,
#             1000_000,1250_000,1500_000,1750_000,2000_000]
# row_nums = [i*(10**power) for power in range(1, 5) 
#                 for i in range(1, 10)] + [100_000]
# row_nums = (1234,2300,15151,22000,43000,48000,74000,82820,94444)
# row_nums = [str(i*(10**power)) for power in range(1, 3) 
#                 for i in range(1, 10)] + [str(i*1000) for i in range(1, 6)]
row_nums = [i*(10**power) for power in range(1, 4) 
                for i in range(1, 10)] + [i*10000 for i in range(1, 7)]
# row_nums_test = [26, 97, 150, 373, 642, 1234, 4880, 7601, 7899, 11890, 26090, 33333, 53011]
col_nums = (0,)





generate_nn_code(program_text.mnist_6layers, row_nums)
# print(row_nums)