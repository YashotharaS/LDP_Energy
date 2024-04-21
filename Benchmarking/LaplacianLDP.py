import numpy as np
from scipy.linalg import lapack

# # Prepare the data
# original_data = {
#     'U1': {
#         'A1': [10, 20, 30, 40],
#         'A2': [5, 10, 15, 20],
#         'A3': [5, 10, 22, 44]
#     },
#     'U2': {
#         'A1': [15, 25, 45, 55],
#         'A2': [7, 14, 21, 28]
#     }
# }

# Generate example energy consumption data
data = np.array([
    [125.0, 125.0, 1625.0, 2500.0, 375.0, 1375.0, 2250.0, 375.0, 125.0, 125.0]
])


def add_laplacian_noise(original_data):
    """
    Add laplace noise to a single float value or a list of floats.
    :param original_data: Values to add noise to.
    :return user_perturbed_lap_dict: The noised value(s) for each appliance of each user
    """

    # Define privacy parameters
    epsilon = 1.0
    delta = 1e-5
    user_perturbed_lap_dict = {}
    j = 1
    for user, appliances in original_data.items():
        appliance_dict = {}
        i = 1
        for appliance, values in appliances.items():
            # Add Laplacian noise to each user's data
            n_features = values.shape[0]
            sensitivity = 1.0  # sensitivity of the average calculation sensitivity = (b - a)
            scale = sensitivity / epsilon
            noise = np.random.laplace(scale=scale, size=(1, n_features))
            noisy_data = values + noise

            # Calculate the average energy consumption across users
            averages = np.mean(noisy_data, axis=0)

            # Add additional noise for privacy amplification
            amplification_factor = np.sqrt(2 * np.log(1.25 / delta)) / epsilon
            amplified_noise = np.random.normal(scale=amplification_factor, size=n_features)
            noisy_averages = averages + amplified_noise

            # # Apply post-processing to restrict values to be non-negative
            # noisy_averages = np.maximum(noisy_averages, 0)

            appliance_dict['A' + str(i)] = noisy_averages
            i = i + 1
        user_perturbed_lap_dict['U' + str(j)] = appliance_dict
        j = j + 1

    return user_perturbed_lap_dict


def appliance_wise_average_energy_consumption(user_perturbed_lap_dict, n_users, n_appliances):
    # Create a list to store all the values from all appliances and users

    average_dict = {}
    average_days = {}
    average_days_appliances= {}
    # Iterate over the users, appliances, and values
    for j in range(n_appliances):
        all_values = []
        for k in range(n_users):
            all_values.append(user_perturbed_lap_dict['U' + str(k+1)]['A' + str(j+1)])
        for d in range(30):
            average_days['day' + str(d+1)] = np.mean([x[d] for x in all_values])
        average_days_appliances['A' + str(j+1)] = average_days
    # Calculate the average of all the values
        average = np.mean(all_values)
        average_dict['A' + str(j+1)] = average
    return average_dict, average_days_appliances
