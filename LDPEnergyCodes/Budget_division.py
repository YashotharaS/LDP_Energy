import random
import Randomiser as rr
import Helper as hp
from sklearn.metrics import mean_squared_error
import numpy as np

total_epsilon_spent = 0


def uniform_budget(window_size, epsilon=5.0):
    """LDP budget uniform method: straightforward approach is to uniformly assign LDP budget 𝜖 to all 𝑤 timestamps in
    the sliding windows. Fixed budget for each timestamp in the window 𝜖/𝑤. This method will assign equal budget for
    every timestamp in the window
    :param window_size: Size of the sliding window
    :param epsilon: privacy budget
    :return epsilon: uniform privacy budget
    """
    epsilon = epsilon / window_size
    return epsilon


def sampling_budget(sampling_timestamp, timestamp, epsilon=5.0):
    """LDP Sampling method: user invests the entire budget 𝜖 on a single (sampling) timestamp within the window, while
    saving budget for the next 𝑤 − 1 timestamps via approximation.
     This method will assign whole 𝜖 privacy budget for sampled timestamp (sampling_timestamp) which can be
     selected randomly and 0 privacy budget to other timestamps in the window
    :param sampling_timestamp: The timestamp which is selected randomly to be the sampling timestamp
    :param epsilon: privacy budget
    :param timestamp: current timestamp
    :return epsilon: privacy budget for the current timestamp
    """
    if timestamp == sampling_timestamp:
        epsilon = epsilon
    else:
        epsilon = 0
    return epsilon


# Adaptive Budget division: LDP- Local budget distribution.
def local_budget_distribution(window_size, binary_array, previously_spent_epsilons, previously_spent_et2, rt_last,
                              sensitivity, epsilon=5.0):
    """LDP budget distribtion method: Compares the dissimilarity 𝑑𝑖𝑠 in True statistics binary_array with the potential
    publication error 𝑒𝑟𝑟 at each time to adaptively choose between publication and approximation.
     This method will calculate the error and distance based on the derived epsilon values and publish or approximate the
     current data. If it publishes, the current perturbed data will be added to the Rt list; else previous published data
     will be added
    :param window_size: the size of the window
    :param binary_array: true data of the current timestamp
    :param previously_spent_epsilons: All the previously spent epsilons (et1 and et2) though it is published or not.
    Because et1 is already spent eventhough it is not published. So need to track of all the epsilons
    :param rt: list of released statistics
    :param rt_last: lastly released data
    :param epsilon: total privacy budget for a window
    :return Rt: updated list of released statistics
    :return Rt_last: update lastly released data
    """

    global total_epsilon_spent

    # Sub Mechanism Mt,1:Set dissimilarity budget
    et1 = epsilon / (2 * window_size)
    total_epsilon_spent = total_epsilon_spent + et1

    # Calculate dissimilarity measure dis
    randomised_array = rr.optimised_unary_perturbation(binary_array, sensitivity, epsilon=et1)
    if len(rt_last) == 0:
        rt_last = randomised_array

    dis = hp.calculate_distance(randomised_array, rt_last)
    # # Calculate Dt,1 and ct,1: If we change these codes to server side we need to estimate current values.
    # Currently, we think that it is happening in client end
    # Dt1 = calculate_Dt1(et1)
    # ct1 = calculate_ct1(Dt1, et1)

    # Sub Mechanism Mt,2:
    # Calculate remaining publication budget
    erm = epsilon / 2 - sum(
        previously_spent_et2)  # need to handle sliding window size (Mi,2 calculates the remaining budget)
    # ϵrm for the active window [i−w + 1, i]) in the main.py. Based on that the values have to transfer here

    # Calculate potential publication budget
    et2 = erm / 2
    # Calculate randomised array using the et2 to calculate the error
    randomised_array_et2 = rr.optimised_unary_perturbation(binary_array, sensitivity, epsilon=et2)
    # Calculate potential publication error
    err = hp.calculate_error(randomised_array_et2, binary_array)

    # Publication or approximation strategy
    if dis > err:
        # Publication strategy
        rt = randomised_array_et2
        total_epsilon_spent = total_epsilon_spent + et2
        previously_spent_epsilons.append(total_epsilon_spent)
        previously_spent_et2.append(et2)
    else:
        # Approximation strategy
        rt = rt_last
        et2 = 0
        total_epsilon_spent = total_epsilon_spent + et2
        previously_spent_epsilons.append(total_epsilon_spent)
        previously_spent_et2.append(et2)

    # Return released statistics and lastly released data
    return rt, previously_spent_et2


# Local Budget Absorption
def local_budget_absorption(window_size, binary_array, previously_spent_epsilons, published_epsilons_et2, rt_last,
                            current_timestamp, nullify, sensitivity, epsilon=5.0):
    """LDP budget absorption method: In LBA, the publication budget is uniformly allocated budget at all timestamps
    then the unused budget is absorbed in the timestamps where publication is chosen.
     This method will calculate the error and distance based on the derived epsilon values and publish or approximate
     the current data. If it decides to publish, it will absorb the unused budget from the previous timestamps.
     Then the current perturbed data will be added to the Rt list; else previous published data will be added
    :param window_size: the size of the window
    :param binary_array: true data of the current timestamp
    :param previously_spent_epsilons: all the previously spent epsilons (et1 and et2) though it is published or not.
    Because et1 is already spent even though it is not published. So need to track of all the epsilons
    :param published_epsilons_et2: only to track the published epsilons for the calculations. So, when we go to approximation
    strategy, we add 0 instead of et1. Through that we can track published timestamps easily.
    :param rt: list of released statistics
    :param rt_last: lastly released data
    :param epsilon: total privacy budget for a window
    :return Rt: updated list of released statistics
    :return Rt_last: update lastly released data
    """
    global total_epsilon_spent
    if len(rt_last) == 0:
        rt_last = [0] * len(binary_array)

    # Sub Mechanism Mt,1:Set dissimilarity budget
    et1 = epsilon / (2 * window_size)
    total_epsilon_spent = total_epsilon_spent + et1

    if len(previously_spent_epsilons) != 0:
        # Calculate dissimilarity measure dis
        randomised_array = rr.optimised_unary_perturbation(binary_array, sensitivity, epsilon=et1)
        dis = hp.calculate_distance(randomised_array, rt_last)
        # # Calculate Dt,1 and ct,1: If we change these codes to server side we need to estimate current values.
        # Currently, we think that it is happening in client end
        # Dt1 = calculate_Dt1(et1)
        # ct1 = calculate_ct1(Dt1, et1)

        # Sub Mechanism Mt,2
        # Calculate timestamps to be nullified

        # Find last publication index from the previously_spent_epsilons array
        last_publication_index = np.max(np.nonzero(published_epsilons_et2))
        # Find the last publication epsilon
        last_publication_epsilon = published_epsilons_et2[last_publication_index]
        to_null = (last_publication_epsilon / (epsilon / (2 * window_size))) - 1

        # Check whether the current timestamp falls under the to_nullify timestamps.
        current_timestamp = current_timestamp + 1

        if current_timestamp - (last_publication_index + 1) <= to_null:
            nullify.append(1)
            rt = rt_last
            et2 = 0
            total_epsilon_spent = total_epsilon_spent + et2
            previously_spent_epsilons.append(total_epsilon_spent)
            published_epsilons_et2.append(et2)

        else:
            # Calculate timestamps that can be absorbed
            t_absorb = current_timestamp - (last_publication_index + 1 + to_null)
            if nullify[current_timestamp - 2] == 1:
                # As previous timestamp is nullified, there is nothing to absorb. So its only budget is assigned
                et2 = epsilon / (2 * window_size)
            else:
                # Set potential publication budget
                et2 = epsilon / (2 * window_size) * min(t_absorb, window_size)

                # Assigning its own privacy budget for Sub Mechanism Mt,2
                et2 = et2 + epsilon / (2 * window_size)
            nullify.append(0)
            # Calculate randomised array using the et2 to calculate the error
            randomised_array_et2 = rr.optimised_unary_perturbation(binary_array, sensitivity, epsilon=et2)
            # Calculate potential publication error
            err = hp.calculate_error(randomised_array_et2, binary_array)

            # Perturbation Strategy
            if dis > err:
                # Publication strategy
                rt = randomised_array_et2
                total_epsilon_spent = total_epsilon_spent + et2
                previously_spent_epsilons.append(total_epsilon_spent)
                published_epsilons_et2.append(et2)

            else:
                # Approximation Strategy
                rt = rt_last
                et2 = 0
                total_epsilon_spent = total_epsilon_spent + et2
                previously_spent_epsilons.append(total_epsilon_spent)
                published_epsilons_et2.append(et2)

    else:  # a way to improve the first allocation part as we don't calculate the dissimilarity in first calculation
        nullify.append(0)
        et2 = epsilon / (2 * window_size)
        # Calculate randomised array using the et2 to calculate the error
        randomised_array_et2 = rr.optimised_unary_perturbation(binary_array, sensitivity, epsilon=et2)
        rt = randomised_array_et2
        total_epsilon_spent = total_epsilon_spent + et2
        previously_spent_epsilons.append(total_epsilon_spent)
        published_epsilons_et2.append(et2)

    # Return released statistics and lastly released data
    return rt, published_epsilons_et2, nullify
