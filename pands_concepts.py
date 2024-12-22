# Pandas is a powerful Python library for data manipulation and analysis.
import numpy as np
#series

import pandas as pd
print("-------")
s = pd.Series(['One','two','three'], index=[1,2,3])
print(s)
print("-------")
# Data Frame
print("-------")
df = pd.DataFrame({'Name': ['Fahad','Zaid'], 'Age': [28, 28]})
print(df)
print("-------")
df_1 = pd.read_csv('dataset.csv')
print(df_1)
print("-------")
df.to_csv('outputtocsv.csv', index=True)
print("-------")
df = pd.read_csv('outputtocsv.csv')
print(df)
print("-------")

print(df['Name'])
print("-------")
print(df.loc[1])

print("-------")

print(df.iloc[1])
print("-------")
print("Group by")
new = (df['Age'] > 29)
# Adding a column
df['Salary'] = [50000, 60000]

# Filling missing values
#  df['Salary'].fillna(0, inplace=True)

print(df.groupby('Name').sum())

df2 = pd.DataFrame({'Job' : ['Date Engineer', 'TAM'], 'Age': [28,28]})
print(df2)
print("             ")
print(pd.merge(df, df2, on = 'Age'))

print("xxxxxxxxxxx")
print("           ")
df['Age'] = df['Age'].apply(lambda x: x+1)
print(df)
print("           ")
print("xxxxxxxxxxx")
print("           ")

data = pd.DataFrame(
    {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Employee_id': ['224', '221', '436'],
        'Location': ['Delhi', 'Mogadishu', 'Hong Kong']
    }
)
print(data)
print("           ")

print(data['Employee_id'])
print(data.iloc[0:2])
filtered_df = df[df['Age'] > 22]
print(filtered_df)

# Handling missing data
print("           ")
missing_df = pd.DataFrame(
    {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [19, 22, np.nan],
        'Location': ['Delhi', 'Mogadishu', 'Hong Kong']
    }
)

print(missing_df)
missing_df['Age'].fillna(missing_df['Age'].mean(), inplace=True)
print(missing_df)