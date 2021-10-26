import numpy as np


def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers')

    matrix = np.array([
        list[:3],
        list[3:6],
        list[6:]
    ])

    calc_mean = matrix.mean()
    calc_variance = matrix.var()
    calc_std_deviation = matrix.std()
    calc_max = matrix.max()
    calc_min = matrix.min()
    calc_sum = matrix.sum()

    axis1_mean = [matrix[:, :1].mean(), matrix[:, 1:2].mean(), matrix[:, 2:].mean()]
    axis2_mean = [matrix[:1, :].mean(), matrix[1:2, :].mean(), matrix[2:, :].mean()]
    axis1_variance = [matrix[:, :1].var(), matrix[:, 1:2].var(), matrix[:, 2:].var()]
    axis2_variance = [matrix[:1, :].var(), matrix[1:2, :].var(), matrix[2:, :].var()]
    axis1_std_deviation = [matrix[:, :1].std(), matrix[:, 1:2].std(), matrix[:, 2:].std()]
    axis2_std_deviation = [matrix[:1, :].std(), matrix[1:2, :].std(), matrix[2:, :].std()]
    axis1_max = [matrix[:, :1].max(), matrix[:, 1:2].max(), matrix[:, 2:].max()]
    axis2_max = [matrix[:1, :].max(), matrix[1:2, :].max(), matrix[2:, :].max()]
    axis1_min = [matrix[:, :1].min(), matrix[:, 1:2].min(), matrix[:, 2:].min()]
    axis2_min = [matrix[:1, :].min(), matrix[1:2, :].min(), matrix[2:, :].min()]
    axis1_sum = [matrix[:, :1].sum(), matrix[:, 1:2].sum(), matrix[:, 2:].sum()]
    axis2_sum = [matrix[:1, :].sum(), matrix[1:2, :].sum(), matrix[2:, :].sum()]

    calculations = {
        'mean': [axis1_mean, axis2_mean, calc_mean],
        'variance': [axis1_variance, axis2_variance, calc_variance],
        'standard deviation': [axis1_std_deviation, axis2_std_deviation, calc_std_deviation],
        'max': [axis1_max, axis2_max, calc_max],
        'min': [axis1_min, axis2_min, calc_min],
        'sum': [axis1_sum, axis2_sum, calc_sum]
    }


    return calculations

try:
    list_number = calculate([0, 1, 2, 3, 4, 5, 6, 7,8])
    print(list_number)
except ValueError as error:
    print('Error', error)
