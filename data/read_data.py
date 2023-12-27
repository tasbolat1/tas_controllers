import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 


column_names = ["x_target", "y_target", "z_target", "q0_target", "q1_target", "q2_target", "q3_target",
                "x", "y", "z", "q0", "q1", "q2", "q3",
                 "t", "theta"]
df = pd.read_csv("data_circular_2.txt", names=column_names)
df.t = df.t-df.t[0]
df.t = 1e-9*df.t

print(df.head())

fig, ax = plt.subplots()
ax.plot(df.x, df.y)
ax.plot(df.x_target, df.y_target)

plt.show()


fig, ax = plt.subplots(nrows=3, figsize=(16,9))


ax[0].plot(df.t, df.x, color='r', label='x')
ax[0].plot(df.t, df.x_target, color='r', linestyle='--')
ax[1].plot(df.t, df.y, color='g',)
ax[1].plot(df.t, df.y_target, color='g', linestyle='--')
ax[2].plot(df.t, df.y, color='g')
ax[2].plot(df.t, df.y_target, color='g', linestyle='--')

plt.show()