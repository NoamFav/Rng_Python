import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import noise


# Function to generate simplex noise terrain
def generate_terrain(width, height, scale, octaves, persistence, lacunarity, seed):
    terrain = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            terrain[i][j] = noise.snoise3(i / scale, j / scale, seed, octaves=octaves, persistence=persistence,
                                          lacunarity=lacunarity)
    return terrain


# Apply constraints to the terrain
def apply_constraints(terrain):
    # Rescale terrain to range [0, 1]
    terrain = (terrain - np.min(terrain)) / (np.max(terrain) - np.min(terrain))

    # Apply rules for hills, flat areas, water, and bunkers
    terrain = terrain * 100  # Ensure maximum height is 100m
    terrain = np.where(terrain < 10, 10, terrain)  # Minimum height is 10m for flat areas
    terrain = np.where(terrain > 90, 90, terrain)  # Maximum height is 90m for hills
    # Add water bodies and rivers

    # Add bunkers

    return terrain


# Generate island shape
def generate_island_shape(width, height, center_x, center_y, island_radius):
    island = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            distance_to_center = np.sqrt((i - center_x) ** 2 + (j - center_y) ** 2)
            if distance_to_center < island_radius:
                island[i][j] = 1
    return island


# Generate terrain
width = 100
height = 100
scale = 20
octaves = 6
persistence = 0.5
lacunarity = 2.0
seed = np.random.randint(0, 100)
terrain = generate_terrain(width, height, scale, octaves, persistence, lacunarity, seed)

# Apply constraints
terrain = apply_constraints(terrain)

# Generate island shape
center_x = width // 2
center_y = height // 2
island_radius = min(width, height) // 3
island_shape = generate_island_shape(width, height, center_x, center_y, island_radius)

# Apply island shape
terrain = terrain * island_shape

# Visualize 3D terrain
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(0, width - 1, width)
y = np.linspace(0, height - 1, height)
X, Y = np.meshgrid(x, y)

ax.plot_surface(X, Y, terrain, cmap='terrain')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Height')
ax.set_title('3D Terrain with Simplex Noise')

plt.show()
