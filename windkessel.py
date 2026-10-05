import numpy as np
import matplotlib.pyplot as plt

R = 2.0
C = 1.5

dt = 0.001
t = np.arrange(0, 20, dt)

position_in_beat = np.mod(t, 0.8)
Q = np.where(position_in_beat < 0.3, 400 * np.sin(np.pi * position_in_beat / 0.3, 0))

P = np.zeros(len(t))
P[0] = 80

for i in range(len(t) - 1):
    leak = P[i] / R
    change_per_second = (Q[i] - leak) / C
    P[i+1] = P[i] + change_per_second * dt

plt.plot(t, P)
plt.xlabel('time (seconds)')    
plt.ylabel('blood pressure (mmHg)')    
plt.show()