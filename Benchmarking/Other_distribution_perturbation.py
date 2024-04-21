import numpy as np
from scipy.linalg import lapack
from scipy.stats import gamma
import concurrent.futures


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


def add_gamma_noise(original_data):
    """
        Add gamma noise to a single float value or a list of floats.
        :param original_data: Values to add noise to.
        :return user_perturbed_lap_dict: The noised value(s) for each appliance of each user
        """

    # Define privacy parameters
    epsilon = 1.0
    delta = 1e-5
    # Parameters for the gamma distribution (shape and scale)
    shape_parameter = 2.0  # You can adjust this value
    scale_parameter = 10.0  # You can adjust this value

    user_perturbed_gamma_dict = {}
    j = 1
    for user, appliances in original_data.items():
        appliance_dict = {}
        i = 1
        for appliance, values in appliances.items():
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

            # # Apply post-processing to restrict values to be non-negative
            # noisy_averages = np.maximum(noisy_averages, 0)

            appliance_dict['A' + str(i)] = averages
            i = i + 1
        user_perturbed_gamma_dict['U' + str(j)] = appliance_dict
        j = j + 1

    return user_perturbed_gamma_dict




def add_gaussian_noise(original_data):
    """
        Add Gaussian noise to a single float value or a list of floats.
        :param original_data: Values to add noise to.
        :return user_perturbed_lap_dict: The noised value(s) for each appliance of each user
        """

    # Define privacy parameters
    epsilon = 1.0
    delta = 1e-5

    user_perturbed_gaussaian_dict = {}
    j = 1
    for user, appliances in original_data.items():
        appliance_dict = {}
        i = 1
        for appliance, values in appliances.items():
            # Add Laplacian noise to each user's data
            n_features = values.shape[0]
            sensitivity = 1.0  # sensitivity of the average calculation sensitivity = (b - a)
            # Calculate the scale parameter (standard deviation) for the Gaussian noise
            scale = sensitivity / epsilon

            # Sample a random Gaussian variable.
            gaussian_noise = np.random.normal(0, scale=scale, size=(1, n_features))

            # Add the noise to the input value.
            noisy_data = values + gaussian_noise

            # Calculate the average energy consumption across users
            averages = np.mean(noisy_data, axis=0)

            # # Apply post-processing to restrict values to be non-negative
            # noisy_averages = np.maximum(noisy_averages, 0)

            appliance_dict['A' + str(i)] = averages
            i = i + 1
        user_perturbed_gaussaian_dict['U' + str(j)] = appliance_dict
        j = j + 1

    return user_perturbed_gaussaian_dict


def add_exponential_noise(original_data):
    """
        Add exponential noise to a single float value or a list of floats.
        :param original_data: Values to add noise to.
        :return user_perturbed_lap_dict: The noised value(s) for each appliance of each user
        """

    # Define privacy parameters
    epsilon = 1.0
    delta = 1e-5
    user_perturbed_exponential_dict = {}
    j = 1
    for user, appliances in original_data.items():
        appliance_dict = {}
        i = 1
        for appliance, values in appliances.items():
            # Add Laplacian noise to each user's data
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

            # # Apply post-processing to restrict values to be non-negative
            # noisy_averages = np.maximum(noisy_averages, 0)

            appliance_dict['A' + str(i)] = averages
            i = i + 1
        user_perturbed_exponential_dict['U' + str(j)] = appliance_dict
        j = j + 1

    return user_perturbed_exponential_dict


