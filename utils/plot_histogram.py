from cmath import e
import matplotlib.pyplot as plt
import numpy
import json


def plot(type, dataset_name, number_list, save_filename):
    # Get all the numbers
    numbers = sorted(number_list)

    # Miscellaneous
    numbers_map = map(int, numbers)
    numbers_list = list(numbers_map)
    numbers_set = set(numbers)
    sorted_unique_list = sorted(list(set(numbers)))
    print('\n' + str(len(numbers_set)) + ' unique values')
    print(sorted_unique_list)

    # Calculate confidence intervals
    lower = numpy.percentile(numbers_list, 5)
    upper = numpy.percentile(numbers_list, 95)

    print(f"{dataset_name}:")
    print(f"90% CI:     <{int(lower)},{int(upper)}>")
    print(f"Full range: <{sorted_unique_list[0]},{sorted_unique_list[-1]}>")

    # === BETTER HISTOGRAM ===
    labels, counts = numpy.unique(
        numbers, return_counts=True)   # Histogram data
    fig = plt.figure(figsize=[11, 12])
    fig.tight_layout()
    fig.subplots_adjust(bottom=0.2)
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title(f"'{dataset_name}' dataset: {type} histogram", fontsize=24)
    ax.set_xlabel(f"{type} value", fontsize=18)
    ax.set_ylabel('Frequency', fontsize=18)
    ax.bar(labels, counts, align='center')
    ax.tick_params(axis='x', labelrotation=60)

    # Add confidence interval layer
    _, ymax = ax.get_ylim()
    str_lower, str_upper = str(int(lower)), str(int(upper))
    ax.fill_betweenx([0, ymax], [str_lower, str_lower], [str_upper, str_upper],
                     facecolor='orange', alpha=0.17)

    # Overlay the bars again
    ax.bar(labels, counts, align='center', color='#0072BD', alpha=1)

    # plt.show()
    fig.savefig('./count_result/'+save_filename+dataset_name+'_'+type+'.png')


def plot_histogram_1by1(v2_file, save_filename='histogram_'):
    '''
    Plot and save histograms to /count_result 

    Parameters
        v2_file (string): v2 stack trace file location with .json tail
        save_filename (string): head of the plot filenames
    '''

    # Opening JSON file
    f = open(v2_file)
    # Returns JSON object as a dictionary
    data = json.load(f)

    for operation in data:
        for dataset_name in data[operation]:
            plot(operation, dataset_name,
                 data[operation][dataset_name], save_filename)
