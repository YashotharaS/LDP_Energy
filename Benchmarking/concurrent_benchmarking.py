import numpy as np
from scipy.linalg import lapack
from scipy.stats import gamma
import concurrent.futures
import time


def add_laplacian_noise(values, epsilon):
    """
    Add laplace noise to a single float value or a list of floats.
    :param original_data: Values to add noise to.
    :return user_perturbed_lap_dict: The noised value(s) for each appliance of each user
    """

    # Define privacy parameters
    epsilon = 1.0
    delta = 1e-5

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

    return noisy_averages


def add_gamma_noise(values, epsilon):
    """
    Add gamma noise to a single float value or a list of floats.
    :param original_data: Values to add noise to.
    :return user_perturbed_lap_dict: The noised value(s) for each appliance of each user
    """

    # Define privacy parameters
    epsilon = 1.0
    delta = 1e-5

    # Add Laplacian noise to each user's data
    n_features = values.shape[0]
    sensitivity = 1.0  # sensitivity of the average calculation sensitivity = (b - a)
    # Calculate the scale parameter (standard deviation) for the Gamma noise
    scale = sensitivity / epsilon

    # alpha = epsilon / 2.0
    # beta = epsilon / 2.0
    shape = 2

    # Sample a random value from the Gamma distribution.
    gamma_sample = gamma.rvs(shape, scale, size=(1, n_features))

    # Add the noise to the input value.
    noisy_data = values + gamma_sample

    # Calculate the average energy consumption across users
    averages = np.mean(noisy_data, axis=0)

    return averages


def add_gaussian_noise(values, epsilon):
    n_features = values.shape[0]
    sensitivity = 1.0  # sensitivity of the average calculation sensitivity = (b - a)
    # Calculate the scale parameter (standard deviation) for the Gaussian noise
    scale = sensitivity / epsilon

    # Sample a random Gaussian variable.
    gaussian_noise = np.random.normal(0, scale=scale, size=(1, n_features))

    # Add the noise to the input values.
    noisy_data = values + gaussian_noise

    # Calculate the average energy consumption for this appliance
    average = np.mean(noisy_data, axis=0)

    return average


def add_exponential_noise(values, epsilon):
    """
        Add exponential noise to a single float value or a list of floats.
        :param values:
        :return user_perturbed_lap_dict: The noised value(s) for each appliance of each user
        """

    # Define privacy parameters
    epsilon = 1.0
    delta = 1e-5

    n_features = values.shape[0]
    sensitivity = 1.0  # sensitivity of the average calculation sensitivity = (b - a)
    # Calculate the scale parameter (standard deviation) for the Gaussian noise
    scale = epsilon / sensitivity

    # Sample a random Gaussian variable.
    exponential_noise = np.random.exponential(scale=scale, size=(1, n_features))

    # Add the noise to the input value.
    noisy_data = values + exponential_noise

    # Calculate the average energy consumption across users
    averages = np.mean(noisy_data, axis=0)

    return averages


def add_noise_to_user(user, appliances, epsilon):
    noisy_appliances = {}
    start_time_bench = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {appliance: executor.submit(add_exponential_noise, values, epsilon) for appliance, values in
                   appliances.items()}
    for appliance, future in futures.items():
        noisy_appliances[appliance] = future.result()
    end_time_bench = time.time()
    elapsed_time_bench = end_time_bench - start_time_bench
    return user, noisy_appliances, elapsed_time_bench


def add_noise_to_users(original_data):
    epsilon = 1.0
    user_perturbed_dict = {}
    overall_elapsed_time_bench = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {user: executor.submit(add_noise_to_user, user, appliances, epsilon) for user, appliances in
                   original_data.items()}

    for user, future in futures.items():
        user_perturbed_dict[user] = future.result()[1]

    overall_elapsed_time_bench.append(future.result()[2])
    avg_elapsed_time_bench = sum(overall_elapsed_time_bench) / len(overall_elapsed_time_bench)
    print("Average elapsed time for LDP: ", avg_elapsed_time_bench)

    return user_perturbed_dict
