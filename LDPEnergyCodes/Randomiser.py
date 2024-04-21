import numpy as np
import math


# Unary encoding
def unary_perturbation(encoded_ans, sensitivity, epsilon=5.0):
    return [unary_perturb_bit(b, sensitivity, epsilon) for b in encoded_ans]


# Unary Encoding
def unary_perturb_bit(bit, sensitivity, epsilon=5.0):
    """Compute randomised responsed value of every given bits (encoded energy levels) based on unary encoding.
    :param bit: Every bit of encoded energy levels
    :param epsilon: privacy budget
    :return bit: randomised bits based on the p, q probabilities
    """
    p = pow(math.e, epsilon / sensitivity) / (1 + pow(math.e, epsilon / sensitivity))
    q = 1 - p

    s = np.random.random()
    if bit == 1:
        if s <= p:
            return 1
        else:
            return 0
    elif bit == 0:
        if s <= q:
            return 1
        else:
            return 0


# Optimised unary encoding
# p = 1/2 and q= 1/(1+e pow epsilon)

def optimised_unary_perturbation(encoded_ans, sensitivity, epsilon=5.0):
    return [optimised_unary_perturb_bit(b, sensitivity, epsilon) for b in encoded_ans]


def optimised_unary_perturb_bit(bit, sensitivity, epsilon=5.0):
    """Compute randomised response value of every given bits (encoded energy levels) based on optimised unary encoding. OUE
    introduces a utility enhancement to Unary Encoding by perturbing 0s and 1s differently.
    :param sensitivity: sensitivity of the approach. For our case it is 2*no. of appliances:
    :param bit: Every bit of encoded energy levels
    :param epsilon: privacy budget
    :return bit: randomised bits based on the p, q probabilities
    """
    p = 0.5
    q = 1 / (1 + pow(math.e, 2 * epsilon / sensitivity))

    s = np.random.random()
    if bit == 1:
        if s <= p:
            return 1
        else:
            return 0
    elif bit == 0:
        if s <= q:
            return 1
        else:
            return 0


# Optimises the Optimised Unary Randomised response using the privacy budget coefficient (alpha)

# p = 1/1+alpha and q= 1/(1+alpha *  e pow epsilon/sensitivity/2)--> So if sensitivity is 2 (scenario1): q= 1/(1+alpha *  e pow epsilon)
# If sensitivity is 2n (scenario 2), q= 1/(1+alpha *  e pow epsilon/n)
def optimised_unary_with_coefficient_perturbation(encoded_ans, sensitivity, epsilon=5.0, alpha=1):
    return [optimised_unary_with_coefficient_perturb_bit(b, epsilon, sensitivity, alpha) for b in encoded_ans]


def optimised_unary_with_coefficient_perturb_bit(bit, sensitivity, epsilon=5.0, alpha=1):
    """Compute randomised responsed value of every given bits (encoded energy levels) based on optimised unary encoding.
     The p,q values are adjusted based on privacy budget coefficient (alpha)
       :param bit: Every bit of encoded energy levels
       :param epsilon: privacy budget
       :param sensitivity: the sensitivity of the LDP approach
       :param alpha: privacy budget coefficient
       :return bit: randomised bits based on the p, q probabilities
       """
    p = 1 / (1 + alpha)
    q = 1 / (1 + alpha * pow(math.e, epsilon / (sensitivity / 2)))

    s = np.random.random()
    if bit == 1:
        if s <= p:
            return 1
        else:
            return 0
    elif bit == 0:
        if s <= q:
            return 1
        else:
            return 0


# Code from Local Differential Privacy for Federated Learning paper: need to verify that whether the code I have
# written and below are same
def flip(p):
    return 1 if np.random.random() < p else 0


def randomize(binary_array, epsilon=4.0, sensitivity=40, alpha=10):
    multiplied = []
    flip1 = 0
    flip2 = 0

    prob1_1 = alpha / (1 + alpha)
    prob1_2 = 1 / (1 + math.pow(alpha, 3))
    prob2 = (alpha * math.exp(epsilon / sensitivity)) / (alpha * math.exp(epsilon / sensitivity) + 1)
    prob2_1 = prob2
    prob2_2 = prob2

    it = 0
    for i in range(len(binary_array)):
        if (it % 2 == 0):
            if binary_array[i] == 1:
                flip1 = flip(prob1_1)
                if flip1 == 1:
                    multiplied.append(1)
                else:
                    multiplied.append(0)
            else:
                flip2 = flip(prob2_1)
                if flip2 == 1:
                    multiplied.append(0)
                else:
                    multiplied.append(1)
        else:
            if binary_array[i] == 1:
                flip1 = flip(prob1_2)
                if flip1 == 1:
                    multiplied.append(1)
                else:
                    multiplied.append(0)
            else:
                flip2 = flip(prob2_2)
                if flip2 == 1:
                    multiplied.append(0)
                else:
                    multiplied.append(1)
        it = it + 1

    return multiplied
