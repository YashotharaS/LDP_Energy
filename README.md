# Local Differential Privacy for Smart Meter Data Sharing with Energy Disaggregation


## The Datasets
IDEAL dataset. Refere to the paper for more details.
Can be obtained from https://datashare.ed.ac.uk/handle/10283/3647
We augmented dataset with synthetic data to evaluate the performance of the proposed approach with more users as LDP approach needs many users.

Synthetic datasets: Please refer code in the 'DataLoading/Syntetic_datasets' folder to generate synthetic datasets. We used different distributions of synthetic data such normal, skewed, and uniform distributions.

## Usage
After downloading the datasets, you can run the code in the 'LDP_Energy_code' folder to evaluate the performance of the proposed approach. The code have adaptive budget division methods also in Budget_division.py file.

## Citation
If you use this code, please cite the following paper:
```Shanmugarasa, Yashothara, et al. "Local Differential Privacy for Smart Meter Data Sharing." arXiv preprint arXiv:2311.04544 (2023).```