import numpy as np
import pandas as pd
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math

df = pd.read_csv("./csv/mbt_s4.csv", sep=",")

df_p_1 = df.sort_values(by=["exp"], ascending=True)

num_bins = int(math.sqrt(df_p_1["time"].size))
x = df_p_1["time"]
n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.5)

plt.show()