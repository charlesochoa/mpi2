import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./csv/mbt_s4.csv", sep=",")

df_p_1 = df[(df.packet_size == 40000)]
df_p_1 = df_p_1.sort_values(by=["exp"], ascending=True)

boxplot = df_p_1.boxplot(column=['time'])
plt.show()