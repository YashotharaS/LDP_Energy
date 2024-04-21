import pandas as pd


def energy_per_day_calculation(df):
    """The data can be measured in different time intervals. But, generally data is shared with service providers once in a day.
    This method computes the energy consumption per day
    :param df: Dataframe that contains all data
    :return consumption_per_day: energy consumption of appliances per day
    """
    df['timestamp'] = pd.to_datetime(df['timestamp'])  # convert column to datetime object
    df.set_index('timestamp', inplace=True)  # set column 'date' to index

    consumption_per_day = round(df.resample('D').sum() / 1000, 2)  # note!! (Sum) # D =>> for day sample
    return consumption_per_day


def energy_per_day_calculation_v2(df, interval_frequency):
    """The data can be measured in different time intervals. But, generally data is shared with service providers once in a day.
    This method computes the energy consumption per day
    :param interval_frequency: freqency of sharing data
    :param df: Dataframe that contains all data
    :return consumption_per_day: energy consumption of appliances per day
    """
    df['timestamp'] = pd.to_datetime(df['timestamp'])  # convert column to datetime object
    df.set_index('timestamp', inplace=True)  # set column 'date' to index

    consumption_per_day = round(df.resample(interval_frequency).sum() / 1000, 2)  # note!! need to decide the same
    # D: day, T-minutes, S- seconds, M- month
    return consumption_per_day


# Encode the energy data into levels
def create_appliance_energy_encoding(appliance_energy_dict, granularity_levels):
    """Map and encode the numerical values of the energy consumption into encoded bits (o's and 1's)
    :param appliance_energy_dict: Dictionary of appliances and consumed energy (in numeric)
    :param granularity_levels: Energy levels in defined granularity which specify the range of the energy level
    :return mapped_energy_levels_dict: Appliances with mapped energy levels
    """
    mapped_energy_levels = []
    mapped_energy_levels_dict = {}
    for i in range(len(appliance_energy_dict)):
        for j in range(len(granularity_levels)):
            if (list(appliance_energy_dict.values())[i] >= int(
                    list(granularity_levels.values())[j].split('-')[0]) and len(
                list(granularity_levels.values())[j].split('-')) == 1):
                buckets = [0] * len(granularity_levels)
                buckets[len(granularity_levels) - j - 1] = 1
                mapped_energy_levels.append(buckets)
            elif (list(appliance_energy_dict.values())[i] >= int(list(granularity_levels.values())[j].split('-')[0]) and
                  list(appliance_energy_dict.values())[i] < int(list(granularity_levels.values())[j].split('-')[1])):
                buckets = [0] * len(granularity_levels)
                buckets[len(granularity_levels) - j - 1] = 1
                mapped_energy_levels.append(buckets)
        mapped_energy_levels_dict["A" + str(i + 1)] = mapped_energy_levels[i]
    return mapped_energy_levels_dict
