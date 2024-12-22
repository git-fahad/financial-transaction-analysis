import seaborn as sns
import matplotlib.pyplot as plt

data =sns.load_dataset("tips")
print(data.head())

sns.scatterplot(data=data, x="total_bill", y="tip", hue="time", style="sex")
plt.title("Scatter Plot of Tips vs Total Bill")
plt.show()