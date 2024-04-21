import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans
import plotly.graph_objects as go
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns


# Experiment 1: Top k appliance finding and having a graph
def get_top_k_appliances(data, k):
    # sort the list in descending order
    # sorted_lst = sorted(lst.values(), reverse=True)
    # Calculate the total energy consumption for each appliance
    total_energy = {}
    for day, appliance_data in data.items():
        for appliance, energy_consumptions in appliance_data['appliance_level_average'][0].items():
            if isinstance(energy_consumptions, float):
                energy_consumptions = [energy_consumptions]
            if appliance not in total_energy:
                total_energy[appliance] = 0
            total_energy[appliance] += sum(energy_consumptions)

    sorted_d = dict(sorted(total_energy.items(), key=lambda item: item[1], reverse=True)[:k])
    # get the top-k items
    # top_k_items = sorted_d[:k]

    return sorted_d


# Experiment 2: Segmenting consumers based on energy usage patterns
def segment_customers(data, n_clusters, title):
    # Convert data to matrix format
    matrix = []
    users = []
    for user in data.keys():
        users.append(user)
        user_data = []
        for appliance in data[user].keys():
            user_data.extend(data[user][appliance])
        matrix.append(user_data)
    matrix = np.array(matrix)

    # Cluster the users
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(matrix)

    # Get the cluster labels and centroids
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_

    # Create the bubble plot
    fig = go.Figure()

    for i in range(len(matrix)):
        # Get the label and color for the user
        label = labels[i]
        color = 'blue' if label == 0 else 'red'

        # Add the bubble for the user
        fig.add_trace(go.Scatter(x=[matrix[i, 0]], y=[matrix[i, 1]], mode='markers',
                                 marker=dict(size=15, color=color), name=users[i]))

    # Add the centroid bubbles
    fig.add_trace(go.Scatter(x=centroids[:, 0], y=centroids[:, 1], mode='markers',
                             marker=dict(size=30, color='black', line=dict(width=2)), name='Centroids'))

    # Set the plot layout
    fig.update_layout(title='User Clustering',
                      xaxis_title='days',
                      yaxis_title='Energy Consumptions for Appliances: ' + title,
                      template='plotly')

    # Show the plot
    fig.show()


# Experiment 3: Appliance usage pattern analysis over a time
def appliance_usage_pattern(data, title):
    # Flatten the data to create a Pandas dataframe
    df = pd.DataFrame(data={'day': [], 'appliance': [], 'energy_consumption': []})

    for day, appliance_data in data.items():
        for appliance, energy_consumptions in appliance_data['appliance_level_average'][0].items():
            df = df.append({'day': day, 'appliance': appliance, 'energy_consumption': energy_consumptions},
                           ignore_index=True)

    # Create the plot
    sns.set_style("darkgrid")
    sns.set_palette("husl")
    plt.figure(figsize=(8, 6))
    sns.lineplot(data=df, x='day', y='energy_consumption', hue='appliance',
                 linewidth=2, style='appliance', markers=True, dashes=False)
    plt.title('Energy Consumption by Appliance: ' + title)
    plt.xlabel('Day')
    plt.ylabel('Energy Consumption (kWh)')
    # plt.savefig('Perturbed_e10.pdf')
    plt.show()


def individual_appliance_impact_in_total(data, title):
    # Calculate the total energy consumption for each appliance
    total_energy = {}
    for day, appliance_data in data.items():
        for appliance, energy_consumptions in appliance_data['appliance_level_average'][0].items():
            if isinstance(energy_consumptions, float):
                energy_consumptions = [energy_consumptions]
            if appliance not in total_energy:
                total_energy[appliance] = 0
            total_energy[appliance] += sum(energy_consumptions)

    # Create the plot

    # Set the style and palette
    sns.set_style("darkgrid")
    # Set the color palette
    colors = sns.color_palette("husl", n_colors=15)

    # Adjust the saturation and lightness values
    desaturated_colors = sns.color_palette([(h, s * 0.85, l * 0.85) for h, s, l in colors])

    plt.figure(figsize=(8, 8))
    pie = plt.pie(x=list(total_energy.values()), labels=list(total_energy.keys()), colors=desaturated_colors, autopct='%1.1f%%')
    # Increase font size of values
    for text in pie[1]:
        text.set_fontsize(15)
    for text in pie[2]:
        text.set_fontsize(15)
        # plt.title('Energy Consumption by Appliance: ' + title)
    plt.savefig(title + '.pdf')
    # Show the plot
    plt.show()


#
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.cluster import KMeans
#
# # Input data
# data = {
#     'User1': {
#         'A1': [125.0, 125.0],
#         'A2': [125.0, 125.0],
#         'A3': [1625.0, 2500.0],
#         'A4': [2500.0, 2500.0],
#         'A5': [375.0, 125.0],
#         'A6': [1375.0, 2500.0],
#         'A7': [2250.0, 2250.0],
#         'A8': [375.0, 875.0],
#         'A9': [125.0, 625.0],
#         'A10': [125.0, 375.0]
#     },
#     'User2': {
#         'A1': [125.0, 125.0],
#         'A2': [125.0, 125.0],
#         'A3': [1625.0, 2500.0],
#         'A4': [2500.0, 2500.0],
#         'A5': [375.0, 125.0],
#         'A6': [1375.0, 2500.0],
#         'A7': [2250.0, 2250.0],
#         'A8': [375.0, 875.0],
#         'A9': [125.0, 625.0],
#         'A10': [125.0, 375.0]
#     }
# }
#
# # Convert data to matrix format
# matrix = []
# users = []
# for user in data.keys():
#     users.append(user)
#     user_data = []
#     for appliance in data[user].keys():
#         user_data.extend(data[user][appliance])
#     matrix.append(user_data)
# matrix = np.array(matrix)
#
# # Cluster the users
# kmeans = KMeans(n_clusters=2, random_state=0).fit(matrix)
#
# # Get the cluster labels and centroids
# labels = kmeans.labels_
# centroids = kmeans.cluster_centers_
# import plotly.graph_objects as go
#
# # Create the bubble plot
# fig = go.Figure()
#
# for i in range(len(matrix)):
#     # Get the label and color for the user
#     label = labels[i]
#     color = 'blue' if label == 0 else 'red'
#
#     # Add the bubble for the user
#     fig.add_trace(go.Scatter(x=[matrix[i, 0]], y=[matrix[i, 1]], mode='markers',
#                              marker=dict(size=15, color=color), name=users[i]))
#
# # Add the centroid bubbles
# fig.add_trace(go.Scatter(x=centroids[:, 0], y=centroids[:, 1], mode='markers',
#                          marker=dict(size=30, color='black', line=dict(width=2)), name='Centroids'))
#
# # Set the plot layout
# fig.update_layout(title='User Clustering',
#                   xaxis_title='Energy Consumption for Appliance A1',
#                   yaxis_title='Energy Consumption for Appliance A2',
#                   template='plotly')
#
# # Show the plot
# fig.show()



