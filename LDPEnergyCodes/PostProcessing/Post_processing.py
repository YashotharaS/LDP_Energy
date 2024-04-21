import json
import numpy as np

# Opening JSON file
f = open(
    '/home/z5288879/Documents/GitHubRepo/LDP_TopK/A-LDP-approach-for-top-k-appliances/Results/normalisation/u100.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list

all_appliance = []
for j in range(20):
    appliance_pvalue = []  # appliances
    for i in range(30):  # window size
        appliance_pvalue.append(data['D' + str(i + 1)]['A' + str(j + 1)]['one_pval'])
    avg = np.average(appliance_pvalue)
    all_appliance.append(avg)
print(all_appliance)

all_appliance = []
for j in range(20):
    appliance_pvalue = []  # appliances
    for i in range(30):  # window size
        appliance_pvalue.append(data['D' + str(i + 1)]['A' + str(j + 1)]['paired_pval'])
    avg = np.average(appliance_pvalue)
    all_appliance.append(avg)
print(all_appliance)

all_appliance = []
for j in range(20):
    appliance_pvalue = []  # appliances
    for i in range(30):  # window size
        appliance_pvalue.append(data['D' + str(i + 1)]['A' + str(j + 1)]['MW_pval'])
    avg = np.average(appliance_pvalue)
    all_appliance.append(avg)
print(all_appliance)

# Closing file
f.close()
