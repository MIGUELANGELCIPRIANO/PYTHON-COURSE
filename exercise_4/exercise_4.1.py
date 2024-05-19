import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataframe = pd.read_csv("exercise_4\\csv_file.csv")

sns.barplot(x="name", y="power_toughness", data=dataframe)
plt.show()
