import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

# Initialize lists to store the data
time_stamps = []
magnitude_velocity = []
dh_dx_values = []
dh_dz_values = []
ax_values = []
az_values = []
vx_values = []
vz_values = []
kinetic_friction_values = []
static_friction_values = []

# Read the log file and extract data
with open('/Users/noamfavier/Desktop/um_project_golf/output.txt', 'r') as file:
    for line in file:
        if 'Time:' in line:
            time_stamps.append(float(line.split(': ')[1].strip()))
        elif 'Magnitude velocity:' in line:
            magnitude_velocity.append(float(line.split(': ')[1].strip()))
        elif 'dh_dxValue:' in line:
            dh_dx_values.append(float(line.split(': ')[1].strip()))
        elif 'dh_dzValue:' in line:
            dh_dz_values.append(float(line.split(': ')[1].strip()))
        elif 'ax:' in line:
            ax_values.append(float(line.split(': ')[1].strip()))
        elif 'az:' in line:
            az_values.append(float(line.split(': ')[1].strip()))
        elif 'vx:' in line:
            vx_values.append(float(line.split(': ')[1].strip()))
        elif 'vz:' in line:
            vz_values.append(float(line.split(': ')[1].strip()))
        elif 'Kinetic Friction:' in line:
            kinetic_friction_values.append(float(line.split(': ')[1].strip()))
        elif 'Static Friction:' in line:
            static_friction_values.append(float(line.split(': ')[1].strip()))

# Ensure all lists have the same length by truncating to the shortest length
min_length = min(len(time_stamps), len(vx_values), len(vz_values), len(ax_values), len(az_values), len(magnitude_velocity), len(dh_dx_values), len(dh_dz_values), len(kinetic_friction_values), len(static_friction_values))
time_stamps = time_stamps[:min_length]
vx_values = vx_values[:min_length]
vz_values = vz_values[:min_length]
ax_values = ax_values[:min_length]
az_values = az_values[:min_length]
magnitude_velocity = magnitude_velocity[:min_length]
dh_dx_values = dh_dx_values[:min_length]
dh_dz_values = dh_dz_values[:min_length]
kinetic_friction_values = kinetic_friction_values[:min_length]
static_friction_values = static_friction_values[:min_length]

# Plot the values
fig, axs = plt.subplots(6, 1, figsize=(12, 18))

axs[0].plot(time_stamps, magnitude_velocity, label='Magnitude Velocity')
axs[0].set_xlabel('Time')
axs[0].set_ylabel('Magnitude Velocity')
axs[0].legend()

axs[1].plot(time_stamps, dh_dx_values, label='dh/dx')
axs[1].plot(time_stamps, dh_dz_values, label='dh/dz')
axs[1].set_xlabel('Time')
axs[1].set_ylabel('Slope')
axs[1].legend()

axs[2].plot(time_stamps, ax_values, label='ax')
axs[2].plot(time_stamps, az_values, label='az')
axs[2].set_xlabel('Time')
axs[2].set_ylabel('Acceleration')
axs[2].legend()

axs[3].plot(time_stamps, vx_values, label='vx')
axs[3].plot(time_stamps, vz_values, label='vz')
axs[3].set_xlabel('Time')
axs[3].set_ylabel('Velocity')
axs[3].legend()

axs[4].plot(time_stamps, kinetic_friction_values, label='Kinetic Friction')
axs[4].plot(time_stamps, static_friction_values, label='Static Friction')
axs[4].set_xlabel('Time')
axs[4].set_ylabel('Friction')
axs[4].legend()

plt.tight_layout()
plt.show()
