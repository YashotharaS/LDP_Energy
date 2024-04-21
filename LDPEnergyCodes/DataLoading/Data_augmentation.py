# This file contains the code for data augmentation of IDEAL dataset to increase the number of users using
# Variational Autoencoder (VAE) and statistical methods. This is used to create differet synthetic data for our
# experiments. The code is divided into two methods: a Variational Autoencoder (VAE) to generate synthetic time
# series data in PyTorch and  statistical methods to generate synthetic data for energy consumption dataset. The code
# is written in Python using PyTorch and NumPy libraries.



# Method 1: a Variational Autoencoder (VAE) to generate synthetic time series data in PyTorch
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from torchvision.utils import save_image
import numpy as np
from scipy.stats import truncnorm
import matplotlib.pyplot as plt
import itertools


def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)


def appliance_wise_augmentation(appliance_energy_list):
    A1 = list(itertools.chain(
        appliance_energy_list[0], appliance_energy_list[4], appliance_energy_list[10], appliance_energy_list[16],
        appliance_energy_list[21], appliance_energy_list[23], appliance_energy_list[28], appliance_energy_list[36],
        appliance_energy_list[39], appliance_energy_list[43], appliance_energy_list[46], appliance_energy_list[47],
        appliance_energy_list[50], appliance_energy_list[51], appliance_energy_list[55], appliance_energy_list[59],
        appliance_energy_list[63], appliance_energy_list[67], appliance_energy_list[68], appliance_energy_list[69],
        appliance_energy_list[70], appliance_energy_list[71], appliance_energy_list[76], appliance_energy_list[77],
        appliance_energy_list[79], appliance_energy_list[82], appliance_energy_list[83], appliance_energy_list[86],
        appliance_energy_list[90], appliance_energy_list[95], appliance_energy_list[98], appliance_energy_list[100],
        appliance_energy_list[103], appliance_energy_list[105], appliance_energy_list[109], appliance_energy_list[111],
        appliance_energy_list[118], appliance_energy_list[124], appliance_energy_list[125], appliance_energy_list[126],
        appliance_energy_list[129], appliance_energy_list[132], appliance_energy_list[136], appliance_energy_list[139],
        appliance_energy_list[143], appliance_energy_list[148], appliance_energy_list[150], appliance_energy_list[153],
        appliance_energy_list[155], appliance_energy_list[158], appliance_energy_list[161], appliance_energy_list[164],
        appliance_energy_list[167], appliance_energy_list[170], appliance_energy_list[173], appliance_energy_list[175],
        appliance_energy_list[180], appliance_energy_list[183], appliance_energy_list[184], appliance_energy_list[187],
        appliance_energy_list[190], appliance_energy_list[194], appliance_energy_list[196], appliance_energy_list[200],
        appliance_energy_list[203], appliance_energy_list[204], appliance_energy_list[206], appliance_energy_list[210]
    ))
    A2 = list(itertools.chain(
        appliance_energy_list[1], appliance_energy_list[5], appliance_energy_list[11], appliance_energy_list[18],
        appliance_energy_list[24], appliance_energy_list[29], appliance_energy_list[33], appliance_energy_list[42],
        appliance_energy_list[44], appliance_energy_list[60], appliance_energy_list[64], appliance_energy_list[78],
        appliance_energy_list[84], appliance_energy_list[94], appliance_energy_list[99], appliance_energy_list[104],
        appliance_energy_list[110], appliance_energy_list[114], appliance_energy_list[120], appliance_energy_list[131],
        appliance_energy_list[138], appliance_energy_list[149], appliance_energy_list[163], appliance_energy_list[169],
        appliance_energy_list[179], appliance_energy_list[195], appliance_energy_list[211], appliance_energy_list[214]

    ))
    A3 = list(itertools.chain(
        appliance_energy_list[6], appliance_energy_list[14], appliance_energy_list[19], appliance_energy_list[30],
        appliance_energy_list[34], appliance_energy_list[48], appliance_energy_list[58], appliance_energy_list[61],
        appliance_energy_list[72], appliance_energy_list[80], appliance_energy_list[87], appliance_energy_list[96],
        appliance_energy_list[106], appliance_energy_list[112], appliance_energy_list[115], appliance_energy_list[121],
        appliance_energy_list[127], appliance_energy_list[133], appliance_energy_list[145], appliance_energy_list[151],
        appliance_energy_list[157], appliance_energy_list[165], appliance_energy_list[176], appliance_energy_list[185],
        appliance_energy_list[191], appliance_energy_list[197], appliance_energy_list[207], appliance_energy_list[215]

    ))
    A4 = list(itertools.chain(
        appliance_energy_list[2], appliance_energy_list[7], appliance_energy_list[15], appliance_energy_list[20],
        appliance_energy_list[25], appliance_energy_list[31], appliance_energy_list[40], appliance_energy_list[52],
        appliance_energy_list[73], appliance_energy_list[88], appliance_energy_list[97], appliance_energy_list[116],
        appliance_energy_list[128], appliance_energy_list[146], appliance_energy_list[152], appliance_energy_list[171],
        appliance_energy_list[186], appliance_energy_list[198], appliance_energy_list[208], appliance_energy_list[216]

    ))

    A5 = list(itertools.chain(
        appliance_energy_list[37],
        appliance_energy_list[92],
        appliance_energy_list[134]
    ))

    A6 = list(itertools.chain(appliance_energy_list[8], appliance_energy_list[26], appliance_energy_list[35],
                              appliance_energy_list[41], appliance_energy_list[45], appliance_energy_list[53],
                              appliance_energy_list[56], appliance_energy_list[65], appliance_energy_list[74],
                              appliance_energy_list[93], appliance_energy_list[101], appliance_energy_list[107],
                              appliance_energy_list[113], appliance_energy_list[117], appliance_energy_list[122],
                              appliance_energy_list[135], appliance_energy_list[140], appliance_energy_list[159],
                              appliance_energy_list[172], appliance_energy_list[177], appliance_energy_list[182],
                              appliance_energy_list[188], appliance_energy_list[192], appliance_energy_list[199],
                              appliance_energy_list[202], appliance_energy_list[209], appliance_energy_list[212],
                              appliance_energy_list[217]))

    A7 = list(itertools.chain(appliance_energy_list[3], appliance_energy_list[9], appliance_energy_list[17],
                              appliance_energy_list[27], appliance_energy_list[32], appliance_energy_list[38],
                              appliance_energy_list[49], appliance_energy_list[54], appliance_energy_list[57],
                              appliance_energy_list[62], appliance_energy_list[66], appliance_energy_list[75],
                              appliance_energy_list[81], appliance_energy_list[89], appliance_energy_list[102],
                              appliance_energy_list[108], appliance_energy_list[119], appliance_energy_list[123],
                              appliance_energy_list[130], appliance_energy_list[137], appliance_energy_list[141],
                              appliance_energy_list[147], appliance_energy_list[154], appliance_energy_list[160],
                              appliance_energy_list[166], appliance_energy_list[174], appliance_energy_list[178],
                              appliance_energy_list[189], appliance_energy_list[193], appliance_energy_list[201],
                              appliance_energy_list[205], appliance_energy_list[213], appliance_energy_list[218]))

    A8 = list(itertools.chain(appliance_energy_list[13], appliance_energy_list[22], appliance_energy_list[91],
                              appliance_energy_list[144], appliance_energy_list[168], appliance_energy_list[181]))

    A9 = list(itertools.chain(appliance_energy_list[12], appliance_energy_list[85], appliance_energy_list[142],
                              appliance_energy_list[156], appliance_energy_list[162]))

    A10 = list(itertools.chain(appliance_energy_list[16], appliance_energy_list[194]))

    A11 = list(itertools.chain(appliance_energy_list[139], appliance_energy_list[158], appliance_energy_list[167],
                               appliance_energy_list[183], appliance_energy_list[190]))

    A12 = list(itertools.chain(appliance_energy_list[70]))

    A13 = list(itertools.chain(appliance_energy_list[39], appliance_energy_list[47], appliance_energy_list[51],
                               appliance_energy_list[71], appliance_energy_list[79], appliance_energy_list[86],
                               appliance_energy_list[95], appliance_energy_list[100], appliance_energy_list[105],
                               appliance_energy_list[111], appliance_energy_list[124], appliance_energy_list[126],
                               appliance_energy_list[132], appliance_energy_list[143], appliance_energy_list[150],
                               appliance_energy_list[164], appliance_energy_list[170], appliance_energy_list[175],
                               appliance_energy_list[180], appliance_energy_list[184], appliance_energy_list[196],
                               appliance_energy_list[206]))

    A14 = list(itertools.chain(appliance_energy_list[187]))

    A15 = list(itertools.chain(appliance_energy_list[67], appliance_energy_list[76], appliance_energy_list[82],
                               appliance_energy_list[155], appliance_energy_list[203]))

    appliances = [A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15]

    # Normal distribution
    import numpy as np
    from scipy.stats import truncnorm

    for i in range(len(appliances)):
        needed = 30000 - len(appliances[i])
        X = get_truncated_normal(mean=np.average(appliances[i]), sd=np.var(appliances[i]), low=min(appliances[i]),
                                 upp=max(appliances[i]))
        appliance1 = X.rvs(needed)
        appliances[i] = appliances[i] + list(appliance1)
    return appliances


# Method 1:This code generates new data with a similar mean and variance as the original data by sampling from a
# normal distribution with the calculated mean and variance. It also generates new data with a similar difference
# between adjacent points by sampling from a normal distribution with the calculated mean and standard deviation of
# the differences. Finally, it integrates the differences to get the synthetic data. This approach can be extended to
# more complex time series data by estimating the underlying distribution of the data using more advanced statistical
# models.

def user_wise_mean_variance_augmentation(original_data):
    # Calculate mean and variance for each combination

    result = {}

    for user, appliances in original_data.items():
        user_dict = {}
        for appliance, values in appliances.items():
            mean = np.mean(values)
            variance = np.var(values)
            appliance_dict = {'mean': mean, 'variance': variance}
            user_dict[appliance] = appliance_dict
        result[user] = user_dict

    # Generate synthetic data for 1000 users
    augmented_data = {}
    u = 0
    # Define the bounds for truncation (no negative values)
    a = 0  # Lower bound
    b = 25000  # Upper bound (large positive value)
    for i in range(len(original_data.items())):
        for j in range(25):
            user = f"U{u + 40}"
            user_appliance_data = {}
            k = 1
            for appliance, value in result['U' + str(i + 1)].items():
                mean = value['mean']
                variance = value['variance']
                # A small positive value (1e-9) is added to the variance to ensure it is non-zero.
                variance = max(variance, 1e-9)
                # synthetic_values = np.random.normal(mean, np.sqrt(variance), size=30) # I fixed the no. of days
                # Generate random numbers from a truncated normal distribution
                synthetic_values = truncnorm.rvs((a - mean) / np.sqrt(variance), (b - mean) / np.sqrt(variance),
                                                 loc=mean, scale=np.sqrt(variance), size=30)
                # considered as 30 here
                user_appliance_data[appliance] = synthetic_values
                k = k + 1
            augmented_data[user] = user_appliance_data
            u = u + 1

    # Create a new DataFrame with the augmented data
    columns = ['user', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15']
    df = pd.DataFrame(columns=columns)

    for user, appliances in augmented_data.items():
        row_data = {'user': user}
        for appliance, values in appliances.items():
            row_data[appliance] = values
        df = df.append(row_data, ignore_index=True)

    return df, augmented_data


# Define the VAE architecture
class VAE(nn.Module):
    def __init__(self, input_dim, latent_dim):
        super(VAE, self).__init__()

        # Encoder layers
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 256),
            nn.ReLU(),
            nn.Linear(256, latent_dim * 2)  # Outputting mean and log variance
        )

        # Decoder layers
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 256),
            nn.ReLU(),
            nn.Linear(256, input_dim)
        )

    def reparameterize(self, mu, log_var):
        std = torch.exp(0.5 * log_var)
        eps = torch.randn_like(std)
        return mu + eps * std

    def forward(self, x):
        # Encoder pass
        z_mean_log_var = self.encoder(x)
        mu, log_var = torch.split(z_mean_log_var, split_size_or_sections=z_mean_log_var.size(1) // 2, dim=1)
        z = self.reparameterize(mu, log_var)

        # Decoder pass
        x_hat = self.decoder(z)

        return x_hat, mu, log_var


# Define a custom dataset
class EnergyConsumptionDataset(Dataset):
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        user, appliance, energy_consumption = self.data[index]
        return torch.tensor(energy_consumption, dtype=torch.float32)

    def __len__(self):
        return len(self.data)


def VAE_augmentation(original_data):
    # Convert the original data into a list of tuples (user, appliance, energy_consumption)
    data = []
    for user, user_data in original_data.items():
        for appliance, energy_consumption in user_data.items():
            energy_consumption = energy_consumption.tolist()
            data.append((user, appliance, energy_consumption))

    # Hyperparameters
    input_dim = 30  # Dimensionality of the input (energy consumption) (As it contains 30 elements in a raw)
    latent_dim = 2  # Dimensionality of the latent space
    batch_size = 4  # Batch size for training

    # Prepare the dataset and dataloader
    dataset = EnergyConsumptionDataset(data)
    data_loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

    # Instantiate the VAE
    vae = VAE(input_dim, latent_dim)

    # Set the optimizer
    optimizer = optim.Adam(vae.parameters(), lr=0.001)

    # Training loop
    num_epochs = 10
    for epoch in range(num_epochs):
        for batch in data_loader:
            optimizer.zero_grad()

            # Forward pass
            x = batch  # Input data
            x_hat, mu, log_var = vae(x)

            # Compute reconstruction loss
            recon_loss = nn.MSELoss()(x_hat, x)

            # Compute KL divergence loss
            kl_divergence_loss = 0.5 * torch.sum(torch.exp(log_var) + mu ** 2 - 1 - log_var)

            # Total loss
            loss = recon_loss + kl_divergence_loss

            # Backpropagation and optimization
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        # Generate augmented data
        augmented_data = []
        for _ in range(1000):
            # Sample from the latent space
            z = torch.randn(1, latent_dim)

            # Decode the latent vector to generate new data
            generated_data = vae.decoder(z)

            augmented_data.append(generated_data)
