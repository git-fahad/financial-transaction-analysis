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

# Calculating the





