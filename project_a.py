from datetime import datetime
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = np.genfromtxt('financial_transactions.csv', delimiter=',', dtype=object, encoding='utf-8', skip_header=1)
data = np.char.decode(data.astype(bytes), 'utf-8')
print("Rows and columns have separate ranges")
print(data[:2,:2])

print("Total number of rows and columns:", data.shape, f'Rows= {data.shape[0]}', f'Columns= {data.shape[1]}')
print(f"Total values = {data.size}")
print("\nFor only rows use a single range [0:5], This will print all the columns:\n")
print(data[0:5])

## Transformations

# Calculating the total amount by transfer type

transfer_type = data[:, 3]
amounts = data[:,4].astype(float)

print(transfer_type.shape)
print(amounts.shape)

sum_of_withdrawal = 0
sum_of_Transfer = 0

for i in range(len(transfer_type)):
	if transfer_type[i] == 'Withdrawal':
		sum_of_withdrawal += amounts[i]
	else:
		sum_of_Transfer +=amounts[i]

print(f'Sum of Withdrawal: {sum_of_withdrawal}')
print(f'sum_of_Transfer: {sum_of_Transfer}')
print("\n")

# Extracting only the Transaction IDs (first column) from the dataset and store them in a separate array.

transaction_ids = data[:,0]
print(transaction_ids)

# Find the unique transaction types (fourth column) in the dataset.

print(np.unique(data[:,3]))

# Calculate the total amount spent or withdrawn (sixth column) across all transactions.

print(f'The total amount spent is: {np.sum(data[:,6].astype(float))}')

# Remove any rows with missing values and count how many rows were removed.
