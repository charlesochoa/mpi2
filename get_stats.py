import pandas as pd
import matplotlib.pyplot as plt

def get_speedup_esc(version, time):
    if ".noavx." in version:
        return TIME_ESC_1_THREAD / time
    else:
        return 0.0

def get_speedup_vec(version, time):
    if ".avx." in version:
        return TIME_VEC_1_THREAD / time
    else:
        return 0.0

df = pd.read_csv("./results.csv", sep=",")

df["speedup_esc"] = df.apply(lambda x: get_speedup_esc(x["version"], x["time(ns)"]), axis=1)
df["speedup_vec"] = df.apply(lambda x: get_speedup_vec(x["version"], x["time(ns)"]), axis=1)

print(df)



# fig, ax = plt.subplots()
# lines = df[["Normalized Performance to Power Ratio", "Target Load"]].plot.line(x="Target Load", linestyle="-",  ax=ax)
# lines = df[["Normalized Average Active Power (W)", "Target Load"]].plot.line(x="Target Load", linestyle="--",  ax=ax, secondary_y=True)
# plt.show(block=True)