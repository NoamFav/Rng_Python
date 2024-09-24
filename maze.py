import matplotlib.pyplot as plt
import numpy as np
import random
import matplotlib

# Maze dimensions
HEIGHT = 40
WIDTH = 40

# Initialize the maze grid
maze = np.zeros((HEIGHT, WIDTH), dtype=int)

# Define directions: UP, DOWN, LEFT, RIGHT
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]


# Randomized Prim's Algorithm
def prim_maze():
    walls = []
    start_x, start_y = random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)
    maze[start_y, start_x] = 1
    walls.extend([(start_x + dx, start_y + dy) for dx, dy in directions if
                  0 <= start_x + dx < WIDTH and 0 <= start_y + dy < HEIGHT])

    while walls:
        wall = random.choice(walls)
        neighbors = [(wall[0] + dx, wall[1] + dy) for dx, dy in directions if
                     0 <= wall[0] + dx < WIDTH and 0 <= wall[1] + dy < HEIGHT]
        passage_neighbors = [(x, y) for x, y in neighbors if maze[y, x] == 1]

        if len(passage_neighbors) in [1, 0]:
            maze[wall[1], wall[0]] = 1
            walls.extend(neighbors)

        walls.remove(wall)


# Recursive Backtracking Algorithm
def recursive_backtracking_maze(x, y):
    maze[y, x] = 1
    directions_shuffled = random.sample(directions, len(directions))
    for dx, dy in directions_shuffled:
        nx, ny = x + dx, y + dy
        if 0 <= nx < WIDTH and 0 <= ny < HEIGHT and maze[ny, nx] == 0:
            recursive_backtracking_maze(nx, ny)


# Sidewinder Algorithm
def sidewinder_maze():
    for y in range(HEIGHT):
        run = []
        for x in range(WIDTH):
            maze[y, x] = 1
            run.append((x, y))
            if x == WIDTH - 1 or (y > 0 and random.randint(0, 1) == 0):
                cell = random.choice(run)
                if cell[0] + 1 < WIDTH:
                    maze[cell[1], cell[0] + 1] = 1
                run = []
            else:
                if y + 1 < HEIGHT:
                    maze[y + 1, x] = 0


# Generate mazes
prim_maze()
recursive_backtracking_maze(0, 0)
sidewinder_maze()

# Plot the maze
plt.figure(figsize=(10, 10))

# Plot the maze for each algorithm
plt.subplot(131)
plt.imshow(maze, cmap='binary')
plt.title("Randomized Prim's Algorithm")

plt.subplot(132)
plt.imshow(maze, cmap='binary')
plt.title("Recursive Backtracking Algorithm")

plt.subplot(133)
plt.imshow(maze, cmap='binary')
plt.title("Sidewinder Algorithm")

plt.tight_layout()
plt.show()
