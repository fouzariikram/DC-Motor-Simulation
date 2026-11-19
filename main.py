
import numpy as np
import matplotlib.pyplot as plt

# DC Motor Parameters
K = 0.1       # Motor gain
tau = 0.5     # Time constant (seconds)

# Simulation time
t = np.linspace(0, 5, 500)

# Unit step input
u = 1

# Motor speed response
speed = K * u * (1 - np.exp(-t / tau))

# Plot the response
plt.figure(figsize=(8, 5))
plt.plot(t, speed, label="Motor Speed")

plt.xlabel("Time (seconds)")
plt.ylabel("Angular Speed (rad/s)")
plt.title("DC Motor Step Response")

plt.grid(True)
plt.legend()
plt.show()
