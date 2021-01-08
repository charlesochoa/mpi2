import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./csv/mlt_s4.csv", sep=",")

df_p_1 = df[(df.packet_size == 4)]
df_p_1 = df_p_1.sort_values(by=["bounce"], ascending=True)
df_p_10 = df[(df.packet_size == 40)]
df_p_10 = df_p_10.sort_values(by=["bounce"], ascending=True)
df_p_100 = df[(df.packet_size == 400)]
df_p_100 = df_p_100.sort_values(by=["bounce"], ascending=True)
df_p_1000 = df[(df.packet_size == 4000)]
df_p_1000 = df_p_1000.sort_values(by=["bounce"], ascending=True)
df_p_1000 = df[(df.packet_size == 40000)]
df_p_1000 = df_p_1000.sort_values(by=["bounce"], ascending=True)
df_p_1000 = df[(df.packet_size == 400000)]
df_p_1000 = df_p_1000.sort_values(by=["bounce"], ascending=True)

# fig, ax = plt.subplots()
# lines = df_p_1[(df_p_1.src == 0)][["bounce", "time"]].plot.line(x="bounce", linestyle="-",  ax=ax)
# lines = df_p_1[(df_p_1.src == 2)][["bounce", "time"]].plot.line(x="bounce", linestyle="-",  ax=ax)
# lines = df_p_1[(df_p_1.src == 4)][["bounce", "time"]].plot.line(x="bounce", linestyle="-",  ax=ax)
# lines = df_p_1[(df_p_1.src == 6)][["bounce", "time"]].plot.line(x="bounce", linestyle="-",  ax=ax)
# plt.title("0.0004MB Packet Size")
# plt.xlabel("Bounce")
# plt.ylabel("Time")
# plt.gca().legend(('Source process: 0', 'Source process: 2', 'Source process: 4', 'Source process: 6'))
# plt.show(block=True)

# fig, ax = plt.subplots()
# lines = df_p_10[(df_p_10.src == 0)][["bounce", "time"]].plot.line(x="bounce", linestyle="-",  ax=ax)
# lines = df_p_10[(df_p_10.src == 2)][["bounce", "time"]].plot.line(x="bounce", linestyle="-",  ax=ax)
# lines = df_p_10[(df_p_10.src == 4)][["bounce", "time"]].plot.line(x="bounce", linestyle="-",  ax=ax)
# lines = df_p_10[(df_p_10.src == 6)][["bounce", "time"]].plot.line(x="bounce", linestyle="-",  ax=ax)
# plt.title("0.004MB Packet Size")
# plt.xlabel("Bounce")
# plt.ylabel("Time")
# plt.gca().legend(('Source process: 0', 'Source process: 2', 'Source process: 4', 'Source process: 6'))
# plt.show(block=True)

# fig, ax = plt.subplots()
# lines = df_p_100[(df_p_100.src == 0)][["bounce", "time"]].plot.line(x="bounce", linestyle="-",  ax=ax)
# lines = df_p_100[(df_p_100.src == 2)][["bounce", "time"]].plot.line(x="bounce", linestyle="-",  ax=ax)
# lines = df_p_100[(df_p_100.src == 4)][["bounce", "time"]].plot.line(x="bounce", linestyle="-",  ax=ax)
# lines = df_p_100[(df_p_100.src == 6)][["bounce", "time"]].plot.line(x="bounce", linestyle="-",  ax=ax)
# plt.title("0.4MB Packet Size")
# plt.xlabel("Bounce")
# plt.ylabel("Time")
# plt.gca().legend(('Source process: 0', 'Source process: 2', 'Source process: 4', 'Source process: 6'))
# plt.show(block=True)

fig, ax = plt.subplots()
lines = df_p_1000[(df_p_1000.src == 0)][["bounce", "time"]].plot.line(x="bounce", linestyle="-",  ax=ax)
lines = df_p_1000[(df_p_1000.src == 2)][["bounce", "time"]].plot.line(x="bounce", linestyle="-",  ax=ax)
lines = df_p_1000[(df_p_1000.src == 4)][["bounce", "time"]].plot.line(x="bounce", linestyle="-",  ax=ax)
lines = df_p_1000[(df_p_1000.src == 6)][["bounce", "time"]].plot.line(x="bounce", linestyle="-",  ax=ax)
plt.title("4MB Packet Size")
plt.xlabel("Bounce")
plt.ylabel("Time")
plt.gca().legend(('Source process: 0', 'Source process: 2', 'Source process: 4', 'Source process: 6'))
plt.show(block=True)