import Preprocessing_and_encoding as preprocess
import Budget_division as bd
import numpy as np
import random
import Helper as hp
import Synthesiser as sy
import matplotlib.pyplot as plt
import seaborn as sns
from collections import OrderedDict
import collections

no_of_users = 1000
# Input: granularity levels with ranges(d-levels)
appliance_list = ['A1', 'A2']
n = len(appliance_list) # Number of appliances
no_of_users = 10
no_of_days = 2
no_of_appliances = 2
sensitivity = 2*n

user_appliance_energy_dict_days = {}

domain = ['l10', 'l9', 'l8', 'l7', 'l6', 'l5', 'l4', 'l3', 'l2', 'l1' ]
range_levels = {
  "l1": "0-250",
  "l2": "250-500",
  "l3": "500-750",
  "l4": "750-1000",
  "l5": "1000-1250",
  "l6": "1250-1500",
  "l7": "1500-1750",
  "l8": "1750-2000",
  "l9": "2000-2500",
  "l10": "2500"
}

#Tuning parameters
epsilon = 5 # 0 < ε ≤ 10
alpha = 10 # 4-10
window_size = 2
user_appliance_list = {}
user_actual_value = {}
user_perturbed_data_list = {}
user_true_level_list = {}
user_perturbed_level_list = {}
appliance_level_list = {}
appliance_level_count = {}
appliance_level_average = {}
appliance_level_max = {}
appliance_perturbed_level_count = {}
appliance_perturbed_level_average = {}
appliance_perturbed_level_max = {}

#Synthetic data creation
user_appliance_energy_dict_days = sy.uniform_distribution_synthesising(appliance_list, no_of_users, no_of_days, no_of_appliances)

#LBD
# Calculating the perturbed values for every user seperately
for k in range(no_of_users):
      # Appliance_energy dictionary per day for 30 days. In appliance_energy_dict_days, key specifies the day
    # (day 1, 2, 3...), and value represents the dictionary of  appliances with their energy consumption for the day.
    window_appliance_data = []
    window_binary_array_data = []
    appliance_energy_dict_days = user_appliance_energy_dict_days['U' + str(k+1)]

    #Encode the energy data into energy levels (granularity levels)
    for key, value in appliance_energy_dict_days.items():
        true_energy_levels_dict = preprocess.create_appliance_energy_encoding(appliance_energy_dict_days[key], range_levels)
        # Declare, l = (d*n); // d- number of granular levels, n- number of appliances
        # Generate a long binary string B with the length of l by merging the binary arrays
        binary_array = []
        for i in range(len(true_energy_levels_dict)):
            binary_array.append(list(true_energy_levels_dict.values())[i])
        binary_array = np.array(binary_array).flatten()

        window_appliance_data.append(true_energy_levels_dict.values())
        window_binary_array_data.append(binary_array)

    perturbed_data_window_lbd = []
    perturbed_data_window_lba = []
    #LBD parameters
    previously_spent_epsilons = []
    previously_released = []
    published_epsilons_et2 = []
    #LBA parameters
    nullify = []
    window_iterate = 0
    actual_data = []
    current_timestamp = 0
    previously_spent_et2_lba = []
    # Adding the encoded data in a sliding window format for our calculation
    for window in hp.sliding_window(window_binary_array_data, window_size):
        current_window = window
        window_iterate = window_iterate + 1
        if window_iterate == 1:
            current_window = current_window
        else:
            a = current_window[window_size-1]
            current_window = []
            current_window.append(a.tolist())
            # previously_spent_et2.pop(0)
            # nullify.pop(0)

        actual_data.append(current_window)
        perturbed_data_window_uniform = []
        perturbed_data_window_sampling = []


        # Adaptive Budget division
        # Generate a random number to determine which sampling timestamp to select for use in the LDP sampling method.
        sampling_timestamp = random.randint(window_iterate, (window_iterate+window_size)-1)
        perturbed_data_sampling = []

        for i in range(len(current_window)):
            # LDP Budget Absorption method
            perturbed_data_lba, previously_spent_et2_lba, nullify = bd.local_budget_absorption(window_size, current_window[i],
                                                                                    previously_spent_epsilons,
                                                                                    previously_spent_et2_lba,
                                                                                    previously_released, current_timestamp, nullify, sensitivity, epsilon)

            perturbed_data_window_lba.append(perturbed_data_lba)
            previously_released = perturbed_data_lba
            current_timestamp = current_timestamp + 1

    user_perturbed_data_list['U' + str(k+1) ] = perturbed_data_window_lba
    user_actual_value['U' + str(k+1)] = window_binary_array_data

    #Appliances true energy levels
    a = hp.true_data_appliance_level(user_actual_value['U' + str(k+1) ][0], len(domain), n)
    user_true_level_list['U' + str(k+1)] = a

    #Appliances perturbed energy levels
    b = hp.perturbed_data_appliance_level(user_perturbed_data_list['U' + str(k+1) ][0], len(domain), n)
    user_perturbed_level_list['U' + str(k+1)] = b

#For true value aggregation and level mapping
for i in range (n):
    all_user_appliance_true_values = []
    for j in range (no_of_users):
        appliance_data = user_true_level_list['U' + str(j+1)]['A' + str(i+1)]
        all_user_appliance_true_values.append(appliance_data)
    levels =  hp.frequency_estimation_true_value(all_user_appliance_true_values, domain)
    counter = collections.Counter(levels)
    appliance_level_list['A' + str(i + 1)] = levels
    appliance_level_count['A' + str(i + 1)] = counter

    # Calculating average energy consumption: True value
    appliance_average, max_value = hp.average_calculation(counter, range_levels, domain)
    appliance_level_average['A' + str(i + 1)] = appliance_average
    appliance_level_max['A' + str(i + 1)] = max_value

# Plotting the histogram: true values
sns.histplot(data = appliance_level_list['A1'], kde=True)
plt.show()

#For perturbed value aggregation
for i in range (n):
    all_user_appliance_perturbed_values = []
    for j in range (no_of_users):
        appliance_data = user_perturbed_level_list['U' + str(j+1)]['A' + str(i+1) ]
        all_user_appliance_perturbed_values.append(appliance_data)
    # Estimation and aggregation
    estimated_answers = hp.estimation_from_perturbed_value(all_user_appliance_perturbed_values, The)
    levels_with_count = dict(zip(domain, estimated_answers))
    res = OrderedDict(reversed(list(levels_with_count.items())))
    appliance_perturbed_level_count['A' + str(i + 1)] = res

    # Plotting the histogram: perturbed values
    sns.barplot(x=list(res.keys()), y=list(res.values()))
    plt.show()

    # # Calculating average energy consumption: Perturbed value
    # appliance_average, max_value = hp.average_calculation(res, range_levels, domain)
    # appliance_perturbed_level_average['A' + str(i + 1)] = appliance_average
    # appliance_perturbed_level_max['A' + str(i + 1)] = max_value


#Calculating MSE
# for i in range (n):
#     RMSE = hp.calculate_error(list(appliance_perturbed_level_max.values())[i][1], list(appliance_level_max.values())[i][1])
#
# print('RMSE')
