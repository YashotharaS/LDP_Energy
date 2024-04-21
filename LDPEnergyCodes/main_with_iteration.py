import Preprocessing_and_encoding as preprocess
import Budget_division as bd
import numpy as np
import random
import Helper as hp
import time
import matplotlib.pyplot as plt
import seaborn as sns
from collections import OrderedDict
import collections
from LDP_Energy_code.Post_processing.Post_processing import Postprocessing_application_level as pal
from LDP_Energy_code.Post_processing import Statistical_analysis as sa
import DataLoading.Data_loading as dl

user_list = []
no_of_users = 1000
no_of_days = 30
n_appliances = 15
elapsed_time_array = []

# Input: granularity levels with ranges(d-levels)
domain = ['l10', 'l9', 'l8', 'l7', 'l6', 'l5', 'l4', 'l3', 'l2', 'l1']
# domain = ['l5', 'l4', 'l3', 'l2', 'l1']
# domain = ['l7', 'l6','l5', 'l4', 'l3', 'l2', 'l1']
# domain = ['l15', 'l14', 'l13', 'l12', 'l11','l10', 'l9', 'l8', 'l7', 'l6', 'l5', 'l4', 'l3', 'l2', 'l1' ]

range_levels = {
    "l1": "0-10",
    "l2": "10-20",
    "l3": "20-40",
    "l4": "40-60",
    "l5": "60-80",
    "l6": "80-100",
    "l7": "100-150",
    "l8": "150-200",
    "l9": "200-300",
    "l10": "300"
}
# range_levels = {
#     "l1": "0-50",
#     "l2": "50-100",
#     "l3": "100-200",
#     "l4": "200-300",
#     "l5": "300"
# }
# range_levels = {
#     "l1": "0-50",
#     "l2": "50-100",
#     "l3": "100-150",
#     "l4": "150-200",
#     "l5": "200-250",
#     "l6": "250-300",
#     "l7": "300",
# }
# range_levels = {
#   "l1": "0-10",
#   "l2": "10-30",
#   "l3": "30-50",
#   "l4": "50-80",
#   "l5": "80-100",
#   "l6": "100-200",
#   "l7": "200-300",
#   "l8": "300-400",
#   "l9": "400-500",
#   "l10":"500-600",
#   "l11":"600-700",
#   "l12":"700-800",
#   "l13":"800-900",
#   "l14":"900-1000",
#   "l15":"1000"
#
# }

appliance_energy_list = []
appliance_energy_dict = {}
# Tuning parameters
epsilon = 10  # 0 < ε ≤ 10
window_size = 3  # 1 ≤ w ≤ 7
window_appliance_data = []
window_binary_array_data = []
user_appliance_list = {}
user_actual_value = {}
user_perturbed_data_list = {}
user_true_level_list = {}
appliance_level_list = {}
appliance_level_count = {}
appliance_perturbed_level_count = {}
appliance_perturbed_level_average = {}
appliance_perturbed_level_max = {}

# Data loading
appliance_list = dl.data_loading()
user_appliance_list = dl.data_loading_method_two_user_wise(appliance_list)

n = 15  # Number of appliances
sensitivity = 2 * n

# Create user list
for i in range(no_of_users):
    user_list.append('U' + str(i + 1))

perturbed_in_iteration = []
for iter in range(10):
    user_perturbed_level_list = {}
    # Calculating the perturbed values for every user separately
    for k in range(len(user_list)):
        appliance_energy_list = user_appliance_list['U' + str(k + 1)]
        window_appliance_data = []
        window_binary_array_data = []

        # Appliance_energy dictionary per day for seven days. In appliance_energy_dict_days, key specifies the day
        # (day 1, 2, 3...), and value represents the dictionary of  appliances with their energy consumption for the day.
        appliance_energy_dict_days = {}
        for j in range(no_of_days):  # for 30 days
            var_name = 'appliance_energy_dict_{}'.format(j)
            globals()[var_name] = {}
            for i in range(n):
                globals()[var_name]["A" + str(i + 1)] = appliance_energy_list['A' + str(i + 1)][j]
            appliance_energy_dict_days["day" + str(j + 1)] = globals()[var_name]

        # Encode the energy data into energy levels (granularity levels)
        for key, value in appliance_energy_dict_days.items():
            start_time = time.time()
            true_energy_levels_dict = preprocess.create_appliance_energy_encoding(appliance_energy_dict_days[key],
                                                                                  range_levels)
            # Declare, l = (d*n); // d- number of granular levels, n- number of appliances
            # Generate a long binary string B with the length of l by merging the binary arrays of each appliance
            binary_array = []
            for i in range(len(true_energy_levels_dict)):
                binary_array.append(list(true_energy_levels_dict.values())[i])
            binary_array = np.array(binary_array).flatten()

            window_appliance_data.append(true_energy_levels_dict.values())
            window_binary_array_data.append(binary_array)

        perturbed_data_window_lbd = []
        perturbed_data_window_lba = []
        perturbed_data_window_uniform = []
        perturbed_data_window_sampling = []
        # LBD parameters
        previously_spent_epsilons = []
        previously_released = []
        published_epsilons_et2 = []
        # LBA parameters
        nullify = []
        window_iterate = 0
        actual_data = []
        current_timestamp = 0
        previously_spent_et2_lba = []
        perturbed_data_sampling = []
        sampling_start_timestamp = 1
        # Adding the encoded data in a sliding window format for our calculation
        for window in hp.sliding_window(window_binary_array_data, window_size):
            current_window = window
            window_iterate = window_iterate + 1
            if window_iterate == 1:
                current_window = current_window
            else:
                sampling_start_timestamp = sampling_start_timestamp + 1
                a = current_window[window_size - 1]
                current_window = [a.tolist()]
                # previously_spent_et2.pop(0) # This variable is related to LBD method only. So for other methods, need to
                # comment.
                # nullify.pop(0)  # This variable is related to LBA method only. So, need to comment for other methods.

            actual_data.append(current_window)

            # Adaptive Budget division
            # Generate a random number to determine which sampling timestamp to select for use in the LDP sampling method.
            sampling_timestamp = random.randint(sampling_start_timestamp, sampling_start_timestamp + window_size - 1)

            for i in range(len(current_window)):
                # # LDP Budget uniform method
                # uniform_epsilon = bd.uniform_budget(window_size)
                #
                # # Scenario2: Combined array with unary encoding
                # perturbed_data_uniform = rr.optimised_unary_perturbation(current_window[i], sensitivity,
                #                                                          epsilon=uniform_epsilon)
                # perturbed_data_window_uniform.append(perturbed_data_uniform)

                # LDP Sampling Method
                # sampling_epsilon = bd.sampling_budget(sampling_timestamp, current_timestamp + 1, epsilon)
                # if sampling_epsilon == 0:
                #     perturbed_data_sampling = perturbed_data_sampling
                # else:
                #     # Scenario2: Combined array with unary encoding
                #     perturbed_data_sampling = rr.optimised_unary_perturbation(current_window[i], sensitivity,
                #                                                               epsilon=sampling_epsilon)
                # if window_iterate == 1:
                #     perturbed_data_window_sampling = [perturbed_data_sampling] * window_size
                # else:
                #     perturbed_data_window_sampling.append(perturbed_data_sampling)

                # LDP Budget Distribution method
                sensitivity = 2 * n
                # perturbed_data_lbd, previously_spent_et2 = bd.local_budget_distribution(window_size, current_window[i],
                #                                                                         previously_spent_epsilons,
                #                                                                         published_epsilons_et2,
                #                                                                         previously_released, sensitivity,
                #                                                                         epsilon)
                # perturbed_data_window_lbd.append(perturbed_data_lbd)
                # previously_released = perturbed_data_lbd

                # LDP Budget Absorption method
                perturbed_data_lba, previously_spent_et2_lba, nullify = bd.local_budget_absorption(window_size,
                                                                                                   current_window[i],
                                                                                                   previously_spent_epsilons,
                                                                                                   previously_spent_et2_lba,
                                                                                                   previously_released,
                                                                                                   current_timestamp,
                                                                                                   nullify, sensitivity,
                                                                                                   epsilon)

                perturbed_data_window_lba.append(perturbed_data_lba)
                previously_released = perturbed_data_lba
                current_timestamp = current_timestamp + 1

        user_perturbed_data_list['U' + str(k + 1)] = perturbed_data_window_lba
        user_actual_value['U' + str(k + 1)] = window_binary_array_data

        # Time complexity
        end_time = time.time()
        elapsed_time = end_time - start_time
        # print('Elapsed_time', elapsed_time)
        elapsed_time_array.append(elapsed_time)

        day_data = {}
        # Appliances true energy levels
        for i in range(no_of_days):
            a = hp.true_data_appliance_level(user_actual_value['U' + str(k + 1)][i], len(domain), n)
            day_data["day" + str(i + 1)] = a
        user_true_level_list['U' + str(k + 1)] = day_data

        day_perturbed_data = {}
        # Appliances perturbed energy levels
        for i in range(no_of_days):
            b = hp.perturbed_data_appliance_level(user_perturbed_data_list['U' + str(k + 1)][i], len(domain), n)
            day_perturbed_data["day" + str(i + 1)] = b
        user_perturbed_level_list['U' + str(k + 1)] = day_perturbed_data
    perturbed_in_iteration.append(user_perturbed_level_list)

final_output_iteration = []
for iter in range(10):
    # Further aggregation and final output experiments
    final_output = {}
    final_true_data_each_day = {}
    final_perturbed_data_each_day = {}

    # For true value aggregation and level mapping
    for w in range(no_of_days):
        appliance_level_average = {}
        appliance_level_max = {}
        appliance_perturbed_level_average = {}
        appliance_perturbed_level_max = {}
        for i in range(n):
            all_user_appliance_true_values = []
            for j in range(no_of_users):
                appliance_data = user_true_level_list['U' + str(j + 1)]['day' + str(w + 1)]['A' + str(i + 1)]
                all_user_appliance_true_values.append(appliance_data)
            levels = hp.frequency_estimation_true_value(all_user_appliance_true_values, domain)
            counter = collections.Counter(levels)
            # appliance_level_list['A' + str(i + 1)] = levels
            appliance_level_count['A' + str(i + 1)] = counter
            appliance_level_count = {k: dict(v) for k, v in appliance_level_count.items()}
            # Calculating average energy consumption: True value
            appliance_average, max_value = hp.average_calculation(counter, range_levels, domain)
            appliance_level_average['A' + str(i + 1)] = appliance_average
            appliance_level_max['A' + str(i + 1)] = max_value

        # Following code is for finding how many users belong to each level
        appliance_level_count_full = {}
        for j in range(len(appliance_level_count)):
            level_dic = {}
            diff = list(set(domain).symmetric_difference(set(list(list(appliance_level_count.values())[j].keys()))))
            for k in range(len(list(list(appliance_level_count.values())[j].keys()))):
                level_dic[int(list(list(appliance_level_count.values())[j].keys())[k].replace('l', ''))] \
                    = list(list(appliance_level_count.values())[j].values())[k]
            for i in range(len(diff)):
                level_dic[int(diff[i].replace('l', ''))] = 0
            level_dic = OrderedDict(sorted(level_dic.items()))

            appliance_level_count_full['A' + str(j + 1)] = level_dic

        # Add level counts and levels average into a dictionary for every day: True data
        final_true_data_each_day.setdefault('day' + str(w + 1), {}).setdefault('appliance_level_count_full', []).append(
            appliance_level_count_full)
        final_true_data_each_day.setdefault('day' + str(w + 1), {}).setdefault('appliance_level_average', []).append(
            appliance_level_average)

        # For perturbed value aggregation
        for i in range(n):
            all_user_appliance_perturbed_values = []
            for j in range(no_of_users):
                appliance_data = perturbed_in_iteration[iter]['U' + str(j + 1)]['day' + str(w + 1)]['A' + str(i + 1)]
                all_user_appliance_perturbed_values.append(appliance_data)
            # Estimation and aggregation
            estimated_answers = hp.estimation_from_perturbed_value(all_user_appliance_perturbed_values, epsilon)
            levels_with_count = dict(zip(domain, estimated_answers))
            res = OrderedDict(reversed(list(levels_with_count.items())))
            res_new = {}
            for j in range(len(list(res.keys()))):
                res_new[j + 1] = list(res.values())[j]
            appliance_perturbed_level_count['A' + str(i + 1)] = res_new

            # Calculating average energy consumption: Perturbed value
            appliance_average_p, max_value_p = hp.average_calculation_perturbed_processed(levels_with_count,
                                                                                          range_levels, domain)
            appliance_perturbed_level_average['A' + str(i + 1)] = appliance_average_p
            appliance_perturbed_level_max['A' + str(i + 1)] = max_value_p

        # Add level counts and levels average into a dictionary for every day: Perturbed data
        final_perturbed_data_each_day.setdefault('day' + str(w + 1), {}).setdefault('appliance_level_average',
                                                                                    []).append(
            appliance_perturbed_level_average)

        output_appliance = {}
        # Statistical analysis I: mean/variance analysis
        for k in range(n):

            # True data
            overall_values = {}
            a = appliance_level_count_full['A' + str(k + 1)]
            temp_actual = list(a.keys())
            count_actual = list(a.values())
            final_actual_data = []

            for i in range(len(temp_actual)):
                for j in range(count_actual[i]):
                    final_actual_data.append(temp_actual[i])

            b = appliance_perturbed_level_count['A' + str(k + 1)]
            temp = list(b.keys())
            counte = list(b.values())
            final_perturbed_data = []

            for i in range(len(temp)):
                for j in range(counte[i]):
                    final_perturbed_data.append(temp[i])

            mean_actual = sum(final_actual_data) / len(final_actual_data)
            variance_actual = sum((i - mean_actual) ** 2 for i in final_actual_data) / len(final_actual_data)

            mean = sum(final_perturbed_data) / len(final_perturbed_data)
            variance = sum((i - mean) ** 2 for i in final_perturbed_data) / len(final_perturbed_data)

            kw_stat, kw_pval = sa.kruskal_wallis_test(count_actual, counte)
            overall_values['kw_pval'] = kw_pval

            output_appliance['A' + str(k + 1)] = overall_values

        final_output['D' + str(w + 1)] = output_appliance
    final_output_iteration.append(final_output)

avg_pvalue_lba_iter = []
for iter in range(5):
    avg_pvalue_lba = []
    for i in range(n):
        sum_val = 0
        for k in range(no_of_days):
            sum_val = sum_val + final_output_iteration[iter]['D' + str(k + 1)]['A' + str(i + 1)]['kw_pval']
        avg = sum_val / no_of_days
        avg_pvalue_lba.append(avg)
    avg_pvalue_lba_iter.append(avg_pvalue_lba)

avg_iter_lba = np.mean(avg_pvalue_lba_iter, axis=0)
print(avg_iter_lba)

# Statistical analysis II: for overall day data
output_appliance_all_day = {}

# Experiment 1: Top k appliances
# Calculating top k appliances in an aggregated domain: perturbed and true
top_k_appliances_true = pal.get_top_k_appliances(final_true_data_each_day, 10)
top_k_appliances_perturbed = pal.get_top_k_appliances(final_perturbed_data_each_day, 10)

# Plotting the top-k appliances: true values
# create a bar plot
sns.set_style("darkgrid")
sns.set_palette("husl")
ax = sns.barplot(x=list(top_k_appliances_true.keys()), y=list(top_k_appliances_true.values()))
# Increase font size
ax.set_xticklabels(ax.get_xticklabels(), fontsize=15)  # Set font size for x-axis labels
ax.set_yticklabels(ax.get_yticklabels(), fontsize=15)  # Set font size for y-axis labels

# add labels and titles
# plt.title("Top-k appliances from true data")
plt.xlabel("Appliances", fontsize=15)
plt.ylabel("Average energy consumption of appliances", fontsize=15)
plt.savefig('True_e10.pdf')
plt.show()

# Plotting the top-k appliances: perturbed values
# create a bar plot
sns.set_style("darkgrid")
sns.set_palette("husl")
ax = sns.barplot(x=list(top_k_appliances_perturbed.keys()), y=list(top_k_appliances_perturbed.values()))
# Increase font size
ax.set_xticklabels(ax.get_xticklabels(), fontsize=15)  # Set font size for x-axis labels
ax.set_yticklabels(ax.get_yticklabels(), fontsize=15)  # Set font size for y-axis labels

# add labels and titles
# plt.title("Top-k appliances from perturbed data")
plt.xlabel("Appliances", fontsize=15)
plt.ylabel("Average energy consumption of appliances", fontsize=15)
plt.savefig('Perturbed_e10.pdf')
plt.show()

# # Experiment 3: Appliance usage pattern
# appliance_usage_true = pal.appliance_usage_pattern(final_true_data_each_day, 'True data')
# appliance_usage_perturbed = pal.appliance_usage_pattern(final_perturbed_data_each_day, 'Perturbed data')
#
# # Experiment 4: individual appliance impact in total
# appliance_usage_true = pal.individual_appliance_impact_in_total(final_true_data_each_day, 'True_data_impact')
# appliance_usage_perturbed = pal.individual_appliance_impact_in_total(final_perturbed_data_each_day,
#                                                                      'Perturbed_data_impact')
