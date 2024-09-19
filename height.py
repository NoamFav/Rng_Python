import re

import matplotlib.pyplot as plt
import numpy as np

# Parse the positions from the file
positions = []
with open("/Users/noamfavier/Desktop/um_project_golf/output2.txt") as file:
    for line in file:
        if line.startswith("Position:"):
            print("Line:", line)  # Print the line for debugging
            # Using regular expressions to extract the scientific notation numbers
            parts = re.findall(r"[-+]?\d*\.\d+E[+-]?\d+|\d+\.\d+", line)
            print("Extracted parts:", parts)  # Print extracted parts for debugging
            if len(parts) == 3:
                x = float(parts[0])
                y = float(parts[1])
                z = float(parts[2])
                positions.append((x, y, z))

    print("Positions:", positions)  # Print positions for debugging

    # Convert positions to a NumPy array
    if positions:
        positions = np.array(positions)

        # Ensure the array is 2-dimensional
        if positions.ndim == 1:
            positions = positions.reshape(-1, 3)

        # Create a 3D plot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(positions[:, 0], positions[:, 2], positions[:, 1], label='Path')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('3D Path of the Ball')
        ax.legend()

        plt.show()
    else:
        print("No positions were parsed from the file.")