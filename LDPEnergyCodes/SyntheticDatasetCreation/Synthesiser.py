import numpy as np
from scipy.stats import truncnorm
from scipy.stats import skewnorm

appliance_energy_dict_days = {}
applaince_energy_list = {}
user_appliance_energy_dict_days = {}


# Normal distribution
def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)


def normal_distribution_synthesising(appliance_list, no_of_users, no_of_days, no_of_appliances):
    # normal distribution with 1000 points (users) within given range for an appliance
    for i in range(no_of_days):  # 30 days
        applaince_energy_list = {}
        for j in range(no_of_appliances):  # 20 appliances
            X = get_truncated_normal(mean=1500, sd=1500, low=1, upp=3000)
            appliance1 = X.rvs(no_of_users)
            applaince_energy_list["A" + str(j + 1)] = appliance1
        appliance_energy_dict_days["day" + str(i + 1)] = applaince_energy_list

    # Change to {U1:{day1:{A1:value, A2:value}} format
    for k in range(no_of_users):
        day = {}
        for i in range(len(appliance_energy_dict_days)):
            appliance = {}
            for j in range(len(appliance_list)):
                a = appliance_energy_dict_days['day' + str(i + 1)]['A' + str(j + 1)][k]
                appliance['A' + str(j + 1)] = a
            day['day' + str(i + 1)] = appliance
        user_appliance_energy_dict_days['U' + str(k + 1)] = day

    return user_appliance_energy_dict_days


def uniform_distribution_synthesising(appliance_list, no_of_users, no_of_days, no_of_appliances):
    # uniform distribution with 1000 points (users) within given range for an appliance
    for i in range(no_of_days):  # 30 days
        applaince_energy_list = {}
        for j in range(no_of_appliances):  # 20 appliances
            appliance1 = np.random.uniform(1, 3000, no_of_users)
            applaince_energy_list["A" + str(j + 1)] = appliance1
        appliance_energy_dict_days["day" + str(i + 1)] = applaince_energy_list

    # Change to {U1:{day1:{A1:value, A2:value}} format
    for k in range(no_of_users):
        day = {}
        for i in range(len(appliance_energy_dict_days)):
            appliance = {}
            for j in range(len(appliance_list)):
                a = appliance_energy_dict_days['day' + str(i + 1)]['A' + str(j + 1)][k]
                appliance['A' + str(j + 1)] = a
            day['day' + str(i + 1)] = appliance
        user_appliance_energy_dict_days['U' + str(k + 1)] = day

    return user_appliance_energy_dict_days


def skewed_distribution_synthesising(appliance_list, no_of_users, no_of_days, no_of_appliances, skew, loc, scale):
    # uniform distribution with 1000 points (users) within given range for an appliance
    a, b = 1, 3000
    for i in range(no_of_days):  # 30 days
        applaince_energy_list = {}
        for j in range(no_of_appliances):  # 20 appliances
            # Generate random numbers from a skewed normal distribution
            appliance1 = skewnorm.rvs(skew, loc=loc, scale=scale, size=no_of_users)
            # Scale the numbers to the desired range
            appliance1 = appliance1 / np.max(np.abs(appliance1))
            appliance1 = appliance1 * (b - a) + a
            appliance1[appliance1 < 0] = 1
            applaince_energy_list["A" + str(j + 1)] = appliance1
        appliance_energy_dict_days["day" + str(i + 1)] = applaince_energy_list

    # Change to {U1:{day1:{A1:value, A2:value}} format
    for k in range(no_of_users):
        day = {}
        for i in range(len(appliance_energy_dict_days)):
            appliance = {}
            for j in range(len(appliance_list)):
                a = appliance_energy_dict_days['day' + str(i + 1)]['A' + str(j + 1)][k]
                appliance['A' + str(j + 1)] = a
            day['day' + str(i + 1)] = appliance
        user_appliance_energy_dict_days['U' + str(k + 1)] = day

    return user_appliance_energy_dict_days

# sns.histplot(data = appliance_energy_dict_days['day1']['A1'])
# plt.show()
