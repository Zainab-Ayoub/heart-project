import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 3.2, 1000)
position_in_beat = np.mod(t, 0.8)

flow = np.where(position_in_beat < 0.3, 400 * np.sin(np.pi * position_in_beat / 0.3), 0)

plt.plot(t, flow)
plt.xlabel('time (seconds)')
plt.ylabel('blood flow from heart (mL/s)')
plt.show()