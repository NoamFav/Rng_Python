import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Generate tesseract vertices
def tesseract_vertices():
    return np.array([[x, y, z, w] for x in (-1, 1) for y in (-1, 1) for z in (-1, 1) for w in (-1, 1)])

# Generate edges between vertices
def tesseract_edges(vertices):
    edges = []
    for i, v1 in enumerate(vertices):
        for j, v2 in enumerate(vertices):
            if sum(np.abs(v1 - v2)) == 2:  # Select vertices that are connected by an edge
                edges.append([i, j])
    return np.array(edges)

# Rotation in 4D space
def rotate_4d(vertices, angle, axis1, axis2):
    rotation_matrix = np.eye(4)
    rotation_matrix[axis1, axis1] = np.cos(angle)
    rotation_matrix[axis1, axis2] = -np.sin(angle)
    rotation_matrix[axis2, axis1] = np.sin(angle)
    rotation_matrix[axis2, axis2] = np.cos(angle)
    return np.dot(vertices, rotation_matrix)

# Initialize figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])

vertices = tesseract_vertices()
edges = tesseract_edges(vertices)

# Plotting function
def update(frame):
    ax.cla()  # Clear the plot
    ax.set_xlim([-3, 3])
    ax.set_ylim([-3, 3])
    ax.set_zlim([-3, 3])

    # Rotate the tesseract
    rotated_vertices = rotate_4d(vertices, np.radians(frame), 0, 1)
    rotated_vertices = rotate_4d(rotated_vertices, np.radians(frame), 2, 3)

    # Project 4D vertices onto 3D
    projected_vertices = rotated_vertices[:, :3]

    # Draw edges
    for edge in edges:
        points = projected_vertices[edge]
        ax.plot(points[:, 0], points[:, 1], points[:, 2], 'b')
    return fig,

# Create animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 1), blit=False, interval=50)

# Display animation
plt.show()
