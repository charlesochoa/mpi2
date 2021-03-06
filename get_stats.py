import pandas as pd
import matplotlib.pyplot as plt

def get_index(n):
    res = []
    for i in range(0, int(n / 2)):
        res.append(i)
        res.append(i)
    print(n, len(res))
    return res

df = pd.read_csv("./csv/blt_s4.csv", sep=",")

df_p_1 = df[(df.packet_size == 4)]
df_p_1["index"] = get_index(df_p_1.index.size)

df_p_10 = df[(df.packet_size == 40)]
df_p_10["index"] = get_index(df_p_10.index.size)

df_p_100 = df[(df.packet_size == 400)]
df_p_100["index"] = get_index(df_p_100.index.size)

df_p_1000 = df[(df.packet_size == 4000)]
df_p_1000["index"] = get_index(df_p_1000.index.size)

df_p_10000 = df[(df.packet_size == 40000)]
df_p_10000["index"] = get_index(df_p_10000.index.size)

fig, ax = plt.subplots()
lines = df_p_1[(df_p_1.version == "MPI_Bcast")][["index", "time"]].plot.line(x="index", linestyle="-",  ax=ax)
lines = df_p_1[(df_p_1.version == "my_broadcast")][["index", "time"]].plot.line(x="index", linestyle="-",  ax=ax)
plt.title("0.0004MB Packet Size")
plt.ylabel("Time")
plt.xlabel("Test")
plt.gca().legend(('Version: MPI_Bcast', 'Version: my_broadcast'))
plt.show(block=True)

fig, ax = plt.subplots()
lines = df_p_10[(df_p_10.version == "MPI_Bcast")][["index", "time"]].plot.line(x="index", linestyle="-",  ax=ax)
lines = df_p_10[(df_p_10.version == "my_broadcast")][["index", "time"]].plot.line(x="index", linestyle="-",  ax=ax)
plt.title("0.004MB Packet Size")
plt.ylabel("Time")
plt.xlabel("Test")
plt.gca().legend(('Version: MPI_Bcast', 'Version: my_broadcast'))
plt.show(block=True)

fig, ax = plt.subplots()
lines = df_p_100[(df_p_100.version == "MPI_Bcast")][["index", "time"]].plot.line(x="index", linestyle="-",  ax=ax)
lines = df_p_100[(df_p_100.version == "my_broadcast")][["index", "time"]].plot.line(x="index", linestyle="-",  ax=ax)
plt.title("0.4MB Packet Size")
plt.ylabel("Time")
plt.xlabel("Test")
plt.gca().legend(('Version: MPI_Bcast', 'Version: my_broadcast'))
plt.show(block=True)

fig, ax = plt.subplots()
lines = df_p_1000[(df_p_1000.version == "MPI_Bcast")][["index", "time"]].plot.line(x="index", linestyle="-",  ax=ax)
lines = df_p_1000[(df_p_1000.version == "my_broadcast")][["index", "time"]].plot.line(x="index", linestyle="-",  ax=ax)
plt.title("4MB Packet Size")
plt.ylabel("Time")
plt.xlabel("Test")
plt.gca().legend(('Version: MPI_Bcast', 'Version: my_broadcast'))
plt.show(block=True)

fig, ax = plt.subplots()
lines = df_p_10000[(df_p_10000.version == "MPI_Bcast")][["index", "time"]].plot.line(x="index", linestyle="-",  ax=ax)
lines = df_p_10000[(df_p_10000.version == "my_broadcast")][["index", "time"]].plot.line(x="index", linestyle="-",  ax=ax)
plt.title("40MB Packet Size")
plt.ylabel("Time")
plt.xlabel("Test")
plt.gca().legend(('Version: MPI_Bcast', 'Version: my_broadcast'))
plt.show(block=True)


# df = pd.read_csv("./csv/mbt_s4.csv", sep=",")

# df_p_1 = df[(df.packet_size == 4)]
# df_p_1 = df_p_1.sort_values(by=["exp"], ascending=True)
# df_p_10 = df[(df.packet_size == 40)]
# df_p_10 = df_p_10.sort_values(by=["exp"], ascending=True)
# df_p_100 = df[(df.packet_size == 400)]
# df_p_100 = df_p_100.sort_values(by=["exp"], ascending=True)
# df_p_1000 = df[(df.packet_size == 4000)]
# df_p_1000 = df_p_1000.sort_values(by=["exp"], ascending=True)
# df_p_10000 = df[(df.packet_size == 40000)]
# df_p_10000 = df_p_10000.sort_values(by=["exp"], ascending=True)
# df_p_100000 = df[(df.packet_size == 400000)]
# df_p_100000 = df_p_100000.sort_values(by=["exp"], ascending=True)

# fig, ax = plt.subplots()
# lines = df_p_1[(df_p_1.src == 0)][["exp", "time"]].plot.line(x="exp", linestyle="-",  ax=ax)
# lines = df_p_1[(df_p_1.src == 2)][["exp", "time"]].plot.line(x="exp", linestyle="-",  ax=ax)
# lines = df_p_1[(df_p_1.src == 4)][["exp", "time"]].plot.line(x="exp", linestyle="-",  ax=ax)
# lines = df_p_1[(df_p_1.src == 6)][["exp", "time"]].plot.line(x="exp", linestyle="-",  ax=ax)
# plt.title("0.0004MB Packet Size")
# plt.xlabel("Test")
# plt.ylabel("Time")
# plt.gca().legend(('Source process: 0', 'Source process: 2', 'Source process: 4', 'Source process: 6'))
# plt.show(block=True)

# fig, ax = plt.subplots()
# lines = df_p_10[(df_p_10.src == 0)][["exp", "time"]].plot.line(x="exp", linestyle="-",  ax=ax)
# lines = df_p_10[(df_p_10.src == 2)][["exp", "time"]].plot.line(x="exp", linestyle="-",  ax=ax)
# lines = df_p_10[(df_p_10.src == 4)][["exp", "time"]].plot.line(x="exp", linestyle="-",  ax=ax)
# lines = df_p_10[(df_p_10.src == 6)][["exp", "time"]].plot.line(x="exp", linestyle="-",  ax=ax)
# plt.title("0.004MB Packet Size")
# plt.xlabel("Test")
# plt.ylabel("Time")
# plt.gca().legend(('Source process: 0', 'Source process: 2', 'Source process: 4', 'Source process: 6'))
# plt.show(block=True)

# fig, ax = plt.subplots()
# lines = df_p_100[(df_p_100.src == 0)][["exp", "time"]].plot.line(x="exp", linestyle="-",  ax=ax)
# lines = df_p_100[(df_p_100.src == 2)][["exp", "time"]].plot.line(x="exp", linestyle="-",  ax=ax)
# lines = df_p_100[(df_p_100.src == 4)][["exp", "time"]].plot.line(x="exp", linestyle="-",  ax=ax)
# lines = df_p_100[(df_p_100.src == 6)][["exp", "time"]].plot.line(x="exp", linestyle="-",  ax=ax)
# plt.title("0.4MB Packet Size")
# plt.xlabel("Test")
# plt.ylabel("Time")
# plt.gca().legend(('Source process: 0', 'Source process: 2', 'Source process: 4', 'Source process: 6'))
# plt.show(block=True)

# fig, ax = plt.subplots()
# lines = df_p_1000[(df_p_1000.src == 0)][["exp", "time"]].plot.line(x="exp", linestyle="-",  ax=ax)
# lines = df_p_1000[(df_p_1000.src == 2)][["exp", "time"]].plot.line(x="exp", linestyle="-",  ax=ax)
# lines = df_p_1000[(df_p_1000.src == 4)][["exp", "time"]].plot.line(x="exp", linestyle="-",  ax=ax)
# lines = df_p_1000[(df_p_1000.src == 6)][["exp", "time"]].plot.line(x="exp", linestyle="-",  ax=ax)
# plt.title("4MB Packet Size")
# plt.xlabel("Test")
# plt.ylabel("Time")
# plt.gca().legend(('Source process: 0', 'Source process: 2', 'Source process: 4', 'Source process: 6'))
# plt.show(block=True)

# fig, ax = plt.subplots()
# lines = df_p_10000[(df_p_10000.src == 0)][["exp", "time"]].plot.line(x="exp", linestyle="-",  ax=ax)
# lines = df_p_10000[(df_p_10000.src == 2)][["exp", "time"]].plot.line(x="exp", linestyle="-",  ax=ax)
# lines = df_p_10000[(df_p_10000.src == 4)][["exp", "time"]].plot.line(x="exp", linestyle="-",  ax=ax)
# lines = df_p_10000[(df_p_10000.src == 6)][["exp", "time"]].plot.line(x="exp", linestyle="-",  ax=ax)
# plt.title("40MB Packet Size")
# plt.xlabel("Test")
# plt.ylabel("Time")
# plt.gca().legend(('Source process: 0', 'Source process: 2', 'Source process: 4', 'Source process: 6'))
# plt.show(block=True)

# fig, ax = plt.subplots()
# lines = df_p_100000[(df_p_100000.src == 0)][["exp", "time"]].plot.line(x="exp", linestyle="-",  ax=ax)
# lines = df_p_100000[(df_p_100000.src == 2)][["exp", "time"]].plot.line(x="exp", linestyle="-",  ax=ax)
# lines = df_p_100000[(df_p_100000.src == 4)][["exp", "time"]].plot.line(x="exp", linestyle="-",  ax=ax)
# lines = df_p_100000[(df_p_100000.src == 6)][["exp", "time"]].plot.line(x="exp", linestyle="-",  ax=ax)
# plt.title("400MB Packet Size")
# plt.xlabel("Test")
# plt.ylabel("Time")
# plt.gca().legend(('Source process: 0', 'Source process: 2', 'Source process: 4', 'Source process: 6'))
# plt.show(block=True)

# df_p_1 = df[(df.packet_size == 4)]
# df_p_1 = df_p_1.sort_values(by=["bounce"], ascending=True)
# df_p_10 = df[(df.packet_size == 40)]
# df_p_10 = df_p_10.sort_values(by=["bounce"], ascending=True)
# df_p_100 = df[(df.packet_size == 400)]
# df_p_100 = df_p_100.sort_values(by=["bounce"], ascending=True)
# df_p_1000 = df[(df.packet_size == 4000)]
# df_p_1000 = df_p_1000.sort_values(by=["bounce"], ascending=True)
# df_p_10000 = df[(df.packet_size == 40000)]
# df_p_10000 = df_p_10000.sort_values(by=["bounce"], ascending=True)
# df_p_100000 = df[(df.packet_size == 400000)]
# df_p_100000 = df_p_100000.sort_values(by=["bounce"], ascending=True)

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

# fig, ax = plt.subplots()
# lines = df_p_1000[(df_p_1000.src == 0)][["bounce", "time"]].plot.line(x="bounce", linestyle="-",  ax=ax)
# lines = df_p_1000[(df_p_1000.src == 2)][["bounce", "time"]].plot.line(x="bounce", linestyle="-",  ax=ax)
# lines = df_p_1000[(df_p_1000.src == 4)][["bounce", "time"]].plot.line(x="bounce", linestyle="-",  ax=ax)
# lines = df_p_1000[(df_p_1000.src == 6)][["bounce", "time"]].plot.line(x="bounce", linestyle="-",  ax=ax)
# plt.title("4MB Packet Size")
# plt.xlabel("Bounce")
# plt.ylabel("Time")
# plt.gca().legend(('Source process: 0', 'Source process: 2', 'Source process: 4', 'Source process: 6'))
# plt.show(block=True)

# fig, ax = plt.subplots()
# lines = df_p_10000[(df_p_10000.src == 0)][["bounce", "time"]].plot.line(x="bounce", linestyle="-",  ax=ax)
# lines = df_p_10000[(df_p_10000.src == 2)][["bounce", "time"]].plot.line(x="bounce", linestyle="-",  ax=ax)
# lines = df_p_10000[(df_p_10000.src == 4)][["bounce", "time"]].plot.line(x="bounce", linestyle="-",  ax=ax)
# lines = df_p_10000[(df_p_10000.src == 6)][["bounce", "time"]].plot.line(x="bounce", linestyle="-",  ax=ax)
# plt.title("40MB Packet Size")
# plt.xlabel("Bounce")
# plt.ylabel("Time")
# plt.gca().legend(('Source process: 0', 'Source process: 2', 'Source process: 4', 'Source process: 6'))
# plt.show(block=True)

# fig, ax = plt.subplots()
# lines = df_p_100000[(df_p_100000.src == 0)][["bounce", "time"]].plot.line(x="bounce", linestyle="-",  ax=ax)
# lines = df_p_100000[(df_p_100000.src == 2)][["bounce", "time"]].plot.line(x="bounce", linestyle="-",  ax=ax)
# lines = df_p_100000[(df_p_100000.src == 4)][["bounce", "time"]].plot.line(x="bounce", linestyle="-",  ax=ax)
# lines = df_p_100000[(df_p_100000.src == 6)][["bounce", "time"]].plot.line(x="bounce", linestyle="-",  ax=ax)
# plt.title("400MB Packet Size")
# plt.xlabel("Bounce")
# plt.ylabel("Time")
# plt.gca().legend(('Source process: 0', 'Source process: 2', 'Source process: 4', 'Source process: 6'))
# plt.show(block=True)

