import matplotlib.pyplot as plt

# Initialize lists to hold the extracted data
time_steps = []
x_positions = []
y_positions = []
vx_values = []
vy_values = []
ax_values = []
ay_values = []
dh_dx_values = []
dh_dy_values = []
magnitude_velocity_values = []
h1x_values = []
h2x_values = []
h3x_values = []
h4x_values = []
h1y_values = []
h2y_values = []
h3y_values = []
h4y_values = []


counterof0 = 0
counterdif0 = 0

# Parsing the log data
file_path = "/Users/noamfavier/Desktop/um_project_golf/output.txt"
with open(file_path, "r") as file:
    lines = file.readlines()
    time_step = 0
    for line in lines:
        line = line.strip()
        if line.startswith("x:"):
            parts = line.split(", ")
            x = float(parts[0].split(": ")[1])
            y = float(parts[1].split(": ")[1])
            x_positions.append(x)
            y_positions.append(y)
        elif line.startswith("vx:"):
            parts = line.split(", ")
            vx = float(parts[0].split(": ")[1])
            vy = float(parts[1].split(": ")[1])
            vx_values.append(vx)
            vy_values.append(vy)
        elif line.startswith("magnitude:"):
            magnitude_velocity = float(line.split(": ")[1])
            magnitude_velocity_values.append(magnitude_velocity)
        elif line.startswith("dh_dx:") and "(after threshold)" not in line:
            parts = line.split(", ")
            dh_dx = float(parts[0].split(": ")[1])
            dh_dy = float(parts[1].split(": ")[1])
            dh_dx_values.append(dh_dx)
            dh_dy_values.append(dh_dy)
        elif line.startswith("ax:"):
            parts = line.split(", ")
            ax = float(parts[0].split(": ")[1])
            ay = float(parts[1].split(": ")[1])
            ax_values.append(ax)
            ay_values.append(ay)
            time_steps.append(time_step)
            time_step += 1
        elif line == "dh_dx and dh_dy are zero":
            counterof0 += 1
        elif line == "dh_dx and dh_dy are not zero":
            counterdif0 += 1


print("dh_dx and dh_dy are zero: ", counterof0)
print("dh_dx and dh_dy are not zero: ", counterdif0)

# Plotting the data
fig, axs = plt.subplots(5, 1, figsize=(12, 20), sharex=True)

maxV, minV = [], []
for i in range(len(x_positions)):
    maxV.append(256)
    minV.append(-256)

axs[0].plot(time_steps, x_positions, label='Trajectory', color='blue')
axs[0].plot(time_steps, y_positions, label='Trajectory', color='red')
axs[0].plot(time_steps, maxV, label='max position', color='green')
axs[0].plot(time_steps, minV, label='max position', color='green')
axs[0].set_ylabel('Position')
axs[0].legend()
axs[0].grid(True)

# Plot vx and vy over time
axs[1].plot(time_steps, vx_values, label='vx', color='blue')
axs[1].plot(time_steps, vy_values, label='vy', color='red')
axs[1].set_ylabel('Velocity')
axs[1].legend()
axs[1].grid(True)

# Plot ax and ay over time
axs[2].plot(time_steps, ax_values, label='ax', color='blue')
axs[2].plot(time_steps, ay_values, label='ay', color='red')
axs[2].set_ylabel('Acceleration')
axs[2].legend()
axs[2].grid(True)

# Plot dh_dx and dh_dy over time
axs[3].plot(time_steps, dh_dx_values, label='dh_dx', color='blue')
axs[3].plot(time_steps, dh_dy_values, label='dh_dy', color='red')
axs[3].set_ylabel('Terrain Gradient')
axs[3].legend()
axs[3].grid(True)

# Plot magnitude of velocity over time
axs[4].plot(time_steps, magnitude_velocity_values, label='Magnitude of Velocity', color='green')
axs[4].set_xlabel('Time Step')
axs[4].set_ylabel('Magnitude of Velocity')
axs[4].legend()
axs[4].grid(True)

plt.tight_layout()
plt.show()
