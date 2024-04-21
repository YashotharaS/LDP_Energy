import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from LDP_Energy_code.Post_processing import Statistical_analysis as sa
import DataLoading.Data_loading as dl
import Benchmarking.LaplacianLDP as lap
import Benchmarking.concurrent_benchmarking as cb


user_list = []
no_of_users = 1000
no_of_days = 30
n_appliances = 15
same_ranks = []

for k in range(2):

    # Data loading
    appliance_list = dl.data_loading()
    user_appliance_list = dl.data_loading_method_two_user_wise(appliance_list)

    # Benchmarking: LDP-Laplacian (single noise adding everytime)
    user_appliance_laplacian_list = {}
    user_average_list = {}
    overall_elapsed_time_bench = []
    overall_p_value_bench = []
    for l in range(10):
        # start_time_bench = time.time()
        user_appliance_laplacian_list = cb.add_noise_to_users(user_appliance_list)
        # user_appliance_laplacian_list = other.add_gaussian_noise(user_appliance_list)
        user_perturbed_average_list, user_perturbed_average_days_list = lap.appliance_wise_average_energy_consumption(
            user_appliance_laplacian_list, no_of_users, n_appliances)
        # print('user_perturbed_average_list: ', user_perturbed_average_list)
        # Time complexity
        # end_time_bench = time.time()
        # elapsed_time_bench = end_time_bench - start_time_bench
        # overall_elapsed_time_bench.append(elapsed_time_bench)
        # True_data: appliance-wise average energy consumption
        user_true_average_list, user_true_average_days_list = lap.appliance_wise_average_energy_consumption(
            user_appliance_list, no_of_users, n_appliances)
        # Benchmarking: accuracy calculation: krusakal-wallis test
        stat, lap_p_values = sa.kruskal_wallis_test(np.array(list(user_true_average_list.values())),
                                                    np.array(list(user_perturbed_average_list.values())))

        overall_p_value_bench.append(lap_p_values)

    # avg_elapsed_time_bench = sum(overall_elapsed_time_bench) / len(overall_elapsed_time_bench)
    avg_p_value_bench = sum(overall_p_value_bench) / len(overall_p_value_bench)

    # print("Average elapsed time for LDP-Laplacian: ", avg_elapsed_time_bench)
    print("Average p-value for LDP-Laplacian: ", avg_p_value_bench)

    # Further aggregation and final output experiments
    final_output = {}
    final_true_data_each_day = {}
    final_perturbed_data_each_day = {}

    converted_lap_data = {}

    for d in range(n_appliances):
        converted_lap_data['A' + str(d + 1)] = user_perturbed_average_list['A' + str(d + 1)] * no_of_days
    sorted_d = dict(sorted(converted_lap_data.items(), key=lambda item: item[1], reverse=True)[:10])
    print('sorted_d: ', sorted_d)


    # Experiment 1: Top k appliances
    # Calculating top k appliances in an aggregated domain: perturbed and true
    top_k_appliances_true = {'A7': 6104.635000000003, 'A6': 4065.755, 'A2': 2994.1099999999997, 'A3': 2068.25, 'A4': 1895.17, 'A1': 1477.2800000000002, 'A11': 915.365, 'A9': 711.8350000000002, 'A8': 657.1249999999999, 'A13': 604.5799999999999}
    print('top_k_appliances_true: ', top_k_appliances_true)

    # Changing true and laplace values to list
    true_values = list(top_k_appliances_true.keys())
    print('true_values: ', true_values)
    laplace_values = list(sorted_d.keys())
    print('laplace_values: ', laplace_values)

    # Check if the values are same in true and laplace in the same order
    # Initialize a count for the same values
    same_count = 0

    # Check how many values are the same in the same position
    for i in range(len(true_values)):
        if true_values[i] == laplace_values[i]:
            same_count += 1

    # print(f"{same_count} values are the same in the same position.")

    same_ranks.append(same_count)

print('same_ranks: ', same_ranks)
print('Average same ranks: ', sum(same_ranks)/len(same_ranks))


# Plotting the top-k appliances: perturbed values: Laplacian
# create a bar plot
sns.set_style("darkgrid")
sns.set_palette("husl")
sns.barplot(x=list(sorted_d.keys()), y=list(sorted_d.values()))
# add labels and titles
plt.title("Top-k appliances from perturbed data by Laplacian noise")
plt.xlabel("Appliances")
plt.ylabel("Average energy consumption of appliances")
plt.savefig('Perturbed_lap.pdf')
# plt.show()

