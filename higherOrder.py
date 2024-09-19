import numpy as np
import matplotlib.pyplot as plt

def rk4_system(dydt, y0, t):
    """
    Runge-Kutta 4th order solver for systems of ODEs.
    dydt: System of ODEs.
    y0: Initial conditions.
    t: Time array.
    """
    n = len(t)
    y = np.zeros((n, len(y0)))
    y[0] = y0
    for i in range(0, n - 1):
        h = t[i + 1] - t[i]
        k1 = h * dydt(y[i], t[i])
        k2 = h * dydt(y[i] + 0.5 * k1, t[i] + 0.5 * h)
        k3 = h * dydt(y[i] + 0.5 * k2, t[i] + 0.5 * h)
        k4 = h * dydt(y[i] + k3, t[i] + h)
        y[i + 1] = y[i] + (k1 + 2*k2 + 2*k3 + k4) / 6
    return y

# Define the system of ODEs
def system(y, t):
    dydt = [y[1], y[2], y[3], y[4], y[0]]
    return np.array(dydt)

# Initial conditions
y0 = [0, 0, 0, 0, 1]  # This choice simplifies to a specific analytical solution
t = np.linspace(0, 20, 100)  # Time interval

# Solve the system
y = rk4_system(system, y0, t)

# Plot the solution
plt.plot(t, y[:, 0], label='y(t)')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Numerical Solution of the 5th-order ODE')
plt.legend()
plt.grid(True)
plt.show()
