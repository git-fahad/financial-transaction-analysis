import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('financial_transactions.csv')

print(df.head())
print(df.isnull().sum())
print(df.dtypes)
print(df.shape[1])

print("Unique transaction types:", df['Type'].nunique())
print(df.groupby('Type').size())

