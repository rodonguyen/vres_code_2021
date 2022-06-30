import json

def convert_v1_to_v2(
        v1_file,
        v2_file,
        dataset_names=['car', 'diabetes',
                       'energy', 'house',
                       'medical']):
    '''
    Convert v1 stack trace file to v2.
    Counts of an operation type are collected and put in 1 lines.

    Parameters
        v1_file (string): Path to v1 stack trace file
        v2_file (string): v2 stack trace file location with .json tail
        dataset_names (list): Lists of dataset name(s) to extract. Default: ['car', 'diabetes', 'energy', 'house', 'medical']
    '''

    v1_file = open(v1_file)
    nonempty_lines = [line.strip("\n") for line in v1_file if line != "\n"]
    v1_file.close()

    # Because memory operation number BEFORE A area is idempotent, that's the only area we check.
    # Hence, my_dict = {'pop':2, 'push':3} but not {'pop':[2,4,6,8], 'push':[3,5,7,9]}}
    operations_dict = {'pop': 2, 'push': 3}

    # Initiate an empty dictionary with all dataset names as keys
    empty_counts = dict()
    for dataset_name in dataset_names:
        empty_counts[dataset_name] = list()

    for operation in operations_dict.keys():
        position = operations_dict[operation]
        counts = dict(empty_counts)

        for line in nonempty_lines:
            for dataset_name in dataset_names:
                if dataset_name in line:
                    line = line.split(',')

                    a_count = [line[position]]
                    counts[dataset_name] = counts[dataset_name] + a_count
                    break
        operations_dict[operation] = counts

    with open(v2_file, 'w') as f:
        f.write(json.dumps(operations_dict))


##############################################################
#                          Code cemetery
##############################################################