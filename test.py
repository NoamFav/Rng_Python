import numpy as np
import matplotlib.pyplot as plt


def add_noise_to_velocity(velocity, direction_noise_degrees, magnitude_noise_percentage):
    angle = np.arctan2(velocity[1], velocity[0])
    magnitude = np.linalg.norm(velocity)
    magnitude_noise_percentage = magnitude_noise_percentage / 100

    # Convert direction noise from degrees to radians
    direction_noise_radians = np.radians(direction_noise_degrees)

    # Directional noise: adding Gaussian noise to the angle
    noisy_angle = angle + np.random.normal(0, direction_noise_radians)

    # Magnitude noise: adding Gaussian noise to the magnitude
    magnitude_noise = magnitude_noise_percentage * magnitude
    noisy_magnitude = magnitude + np.random.normal(0, magnitude_noise)

    # Convert polar back to Cartesian coordinates
    noisy_velocity_x = noisy_magnitude * np.cos(noisy_angle)
    noisy_velocity_y = noisy_magnitude * np.sin(noisy_angle)

    return np.array([noisy_velocity_x, noisy_velocity_y])


def add_noise_to_initial_position(position, noise_level):
    noisy_x = position[0] + np.random.normal(0, noise_level)
    noisy_y = position[1] + np.random.normal(0, noise_level)
    return np.array([noisy_x, noisy_y])


def plot_vectors(base_velocities, noise_positions, noisy_velocities, init_position, subplot_index):
    ax = plt.subplot(5, 5, subplot_index + 1)
    for pos, vel in zip(noise_positions, noisy_velocities):
        ax.quiver(pos[0], pos[1], vel[0], vel[1], color='b', scale=1, scale_units='xy', angles='xy')
    ax.quiver(init_position[0], init_position[1], base_velocities[0], base_velocities[1], color='r', scale=1,
               scale_units='xy', angles='xy', label='Original Velocity')
    ax.set_xlim(-15, 15)
    ax.set_ylim(-15, 15)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(True)
    if subplot_index == 0:
        ax.legend(loc='upper left', fontsize='small', title='Legend')

for j in range(1):
    plt.figure(figsize=(18, 18))
    noise_level_direction = 0  # Noise level in degrees
    noise_level_magnitude = 0  # Noise level in percentage
    position_noise_level = .2  # Noise level for initial position
    for i in range(25):
        # Generate new initial position and base velocity for each scenario
        initial_position = np.random.rand(2) * 10 - 5  # Random initial position within [-5, 5] for both x and y
        base_velocity = np.random.rand(2) * 10 + 1  # Random velocity vector ensuring magnitude is at least 2

        # Generate noisy velocities and positions for each scenario
        noisy_positions = []
        noisy_velocity = []
        for _ in range(100):
            noisy_vector = add_noise_to_velocity(base_velocity, noise_level_direction, noise_level_magnitude)
            noisy_position = add_noise_to_initial_position(initial_position, position_noise_level)
            noisy_positions.append(noisy_position)
            noisy_velocity.append(noisy_vector)

        # Plotting the result for the current scenario
        plot_vectors(base_velocity, noisy_positions, noisy_velocity, initial_position, i)

    plt.tight_layout()
    plt.savefig(f"noisy_vector_{j}.png", dpi=300)
    print(f"Saved figure {j}")

