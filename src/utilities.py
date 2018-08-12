import json
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt


def read_json(file_name):
	'''
	Wrapper function to read json file into python dictionary

	:param file_name: (str) path to json file
	:return: (dict) python dictionary containint json file
	'''

	with open(file_name) as f:
		py_dict = json.load(f)

	return py_dict

def save_json(py_dict, file_name):
	'''
	Wrapper function to save 

	:param py_dict: (dict) python dictionary to be saved
	:param file_name: (str) path to json file
	'''

	with open(file_name, 'w') as outfile:
		json.dump(py_dict, outfile)


def plot_distribution(values, bins=250):
    '''
    Prints the distribution of a continous variable
    
    :param values: array-like object containing values to be plotted
    :bins: (int) number of bins in the plot
    '''
    
    sns.set(color_codes=True)
    print("avg_value: {}\nmax_value: {}\nmin_value: {}".format(np.mean(values), 
                                                               np.max(values),
                                                               np.min(values)))
    
    sns.distplot(scores, bins=bins)
    plt.show()


def plot_distributions(values_dict, bins=250):
    '''
    Prints the distribution of a continous variable
    
    _param values_dict: (dict) dictionary of array-like object containing values to be plotted
    :param bins: (int) number of bins in the plot
    '''

    sns.set(color_codes=True)
    for key_i in values_dict:
        value_i = values_dict[key_i]
        print(key_i)
        print("avg_value: {}\nmax_value: {}\nmin_value: {}\n".format(np.mean(value_i), 
                                                               np.max(value_i),
                                                               np.min(value_i)))
        sns.distplot(value_i,bins=bins)

    plt.legend(list(values_dict.keys()))
    plt.show()