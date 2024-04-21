import math
import Randomiser as rr
from sklearn.metrics import mean_squared_error
import numpy as np
from collections import deque


# Assign energy consumptions to users
def create_user_appliance_list(user_list, n, applaince_energy_list, time_interval):
    user_appliance_list = {}
    start = 0
    for j in range(len(user_list)):
        app = []
        for i in range(n):
            app.append(applaince_energy_list[i][start:time_interval])
        user_appliance_list[user_list[j]] = app
        time_interval = time_interval + 7
        start = start + 7
    return user_appliance_list


def sliding_window(sequence, window_size):
    """Output the current window sequence based on the sliding window concept
    :param sequence: sequence of encoded energy data with energy levels
    :param window_size: window size of the sliding window
    :return window: elements with based on the window size
    """
    actual_window_size = min(window_size, len(sequence))
    for i in range(len(sequence) - actual_window_size + 1):
        yield sequence[i:i + actual_window_size]


def calculate_distance(current, last_release):
    """Calculation of distance based on Root Mean Squared Error (RMSE) between current data and lastly published
     perturbed data
        :param current: current data in the sequence after perturbation
        :param last_release: lastly published perturbed data
        :return distance: distance based on RMSE between current and last_last_release
        """
    distance = np.sqrt(np.square(np.subtract(current, last_release)).mean())
    return distance


def calculate_error(original, perturbed):
    """Calculation of error based on Root Mean Squared Error (RMSE) between current data (no perturbation) and
    perturbed data
        :param original: current data in the sequence without perturbation
        :param perturbed: perturbed current data
        :return mse, rmse: error based on MSE and RMSE between original and perturbed
        """
    mse = np.square(np.subtract(original, perturbed)).mean()
    # RMSE
    rmse = np.sqrt(np.square(np.subtract(original, perturbed)).mean())
    return rmse


def true_data_appliance_level(data_per_day, d, n):
    """ Performance evaluation: Decode the true data by extracting the appliance and its corresponding energy level from
            the binary array we generated earlier
        :param n: number of appliances
        :param d: number of energy levels
        :param data_per_day: true data binary array with all appliances for a day
        :return appliances_true_data: Each appliance's true energy data
        """
    appliances_true_data = {}
    x = 0
    y = d
    for i in range(n):
        appliances_true_data['A' + str(i + 1)] = data_per_day[x:y]
        x = x + d
        y = y + d

    return appliances_true_data


def perturbed_data_appliance_level(perturbed_data_per_day, d, n):
    """ Performance evaluation: Decode the perturbed data by extracting the appliance and its corresponding energy level
            from the binary array we generated earlier
        :param perturbed_data_per_day: perturbed data binary array with all appliances for a day
        :param n: number of appliances
        :param d: number of energy levels
        :return appliances_perturbed_data: Each appliance's perturbed energy data
        """
    appliances_perturbed_data = {}
    x = 0
    y = d
    for i in range(n):
        appliances_perturbed_data['A' + str(i + 1)] = perturbed_data_per_day[x:y]
        x = x + d
        y = y + d

    return appliances_perturbed_data


def frequency_estimation_true_value(appliance_true_values, domain):
    """Estimate the actual answers from true_values by aggregating all users data belongs to each energy level
            :param appliance_true_values: true_values of overall appliances
            :param domain: energy levels
            :return levels: actual levels of an appliance
            """
    levels = []
    for i in range(len(appliance_true_values)):
        index = np.where(appliance_true_values[i] == 1)
        level = domain[index[0][0]]
        levels.append(level)

    return levels


def estimation_from_perturbed_value(perturbed_answers, epsilon=5.0 ):
    """Estimate the actual answers from perturbed outputs by again applying p,q probabilities to make it back. It will
        not come to original state. we are estimating only. Then aggrgate the values for all users based on users'
        energy levels
        :param perturbed_answers: perturbed values using LDP
        :param epsilon: privacy budget
        :return estimated_value: estimated value of the perturbed answers
        """
    # expected_value = sum([p * response + (1 - p) * (1 - response) for response in modified_responses]) / len(
    # modified_responses) p = pow(math.e, 2*epsilon/sensitivity) / (1 + pow(math.e, 2*epsilon/sensitivity)) q = 1 - p
    sensitivity = 2  # We considered only one appliance at this time
    p = 0.5
    q = 1 / (1 + pow(math.e, 2 * epsilon / sensitivity))

    sums = np.sum(perturbed_answers, axis=0)
    n = len(perturbed_answers)
    # return sums
    return [int((i - n * q) / (p - q)) for i in sums]


def average_calculation(levels_with_counts, range_levels, domain):
    avg_ranges = []
    for j in range(len(range_levels) - 1):
        avg_range = (int(list(range_levels.values())[j].split('-')[0]) + int(
            list(range_levels.values())[j].split('-')[1])) / 2
        avg_ranges.append(avg_range)
    avg_ranges.append(int(list(range_levels.values())[j + 1].split('-')[0]))
    domain1 = list(reversed(domain))
    levels_with_average = dict(zip(domain1, avg_ranges))

    total = 0
    max_level = 0
    max_value = []

    for i in range(len(levels_with_counts)):
        for j in range(len(levels_with_average)):
            if list(levels_with_counts.keys())[i] == list(levels_with_average.keys())[j]:
                total = total + list(levels_with_average.values())[j] * list(levels_with_counts.values())[i]
        if (list(levels_with_counts.values())[i] >= max_level):
            max_level = list(levels_with_counts.values())[i]
            max_value = list(levels_with_counts.keys())[i], levels_with_average[list(levels_with_counts.keys())[i]]

    return total / sum(list(levels_with_counts.values())), max_value


def average_calculation_perturbed_processed(levels_with_counts, range_levels, domain):
    avg_ranges = []
    for j in range(len(range_levels) - 1):
        avg_range = (int(list(range_levels.values())[j].split('-')[0]) + int(
            list(range_levels.values())[j].split('-')[1])) / 2
        avg_ranges.append(avg_range)
    avg_ranges.append(int(list(range_levels.values())[j + 1].split('-')[0]))
    domain1 = list(reversed(domain))
    levels_with_average = dict(zip(domain1, avg_ranges))

    total = 0
    max_level = 0
    max_value = []
    multification_factors = [1, 0.7, 0.6, 0.5, 0.3, 0.1, 0.05, 0.01, 0.005, 0.001]
    # multification_factors = [1, 0.7, 0.6, 0.55, 0.5, 0.4, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.0025, 0.002, 0.001]

    sorted_data = dict(sorted(levels_with_counts.items(), key=lambda x: x[1], reverse=True))

    for i in range(len(sorted_data)):
        for j in range(len(levels_with_average)):
            if list(sorted_data.keys())[i] == list(levels_with_average.keys())[j]:
                total = total + list(levels_with_average.values())[j] * list(sorted_data.values())[i] * multification_factors[i]
        if list(sorted_data.values())[i] >= max_level:
            max_level = list(sorted_data.values())[i]
            max_value = list(sorted_data.keys())[i], levels_with_average[list(sorted_data.keys())[i]]

    return total / sum(list(sorted_data.values())), max_value
