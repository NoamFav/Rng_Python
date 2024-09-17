import matplotlib.pyplot as plt

TS1 = [10, 2, 5, 10, 2, 7]
TS2 = [3, 1, 15, 5, 3, 6]
TS3 = [2, 1, 4, 7, 1, 4]

def euclidean_distance(a, b):
    return sum((x-y)**2 for x, y in zip(a, b)) ** 0.5

def manhattan_distance(a, b):
    return sum(abs(x-y) for x, y in zip(a, b))

def infinite_distance(a, b):
    return max(abs(x-y) for x, y in zip(a, b))

# Plot the time series
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(TS1, label="TS1", marker='o')
plt.plot(TS2, label="TS2", marker='o')
plt.plot(TS3, label="TS3", marker='o')
plt.legend()
plt.title("Time Series TS1, TS2, and TS3")
plt.xlabel("Time step")
plt.ylabel("Value")
plt.grid(True)

# Compute and plot the distances
labels = ['Euclidean', 'Manhattan', 'Infinite']
distances_TS1_TS2 = [euclidean_distance(TS1, TS2), manhattan_distance(TS1, TS2), infinite_distance(TS1, TS2)]
distances_TS1_TS3 = [euclidean_distance(TS1, TS3), manhattan_distance(TS1, TS3), infinite_distance(TS1, TS3)]
distances_TS2_TS3 = [euclidean_distance(TS2, TS3), manhattan_distance(TS2, TS3), infinite_distance(TS2, TS3)]

plt.subplot(1, 2, 2)
x = range(len(labels))
plt.bar(x, distances_TS1_TS2, width=0.2, label="TS1 vs TS2", align='center')
plt.bar([i+0.2 for i in x], distances_TS1_TS3, width=0.2, label="TS1 vs TS3", align='center')
plt.bar([i+0.4 for i in x], distances_TS2_TS3, width=0.2, label="TS2 vs TS3", align='center')

plt.xlabel("Distance Type")
plt.ylabel("Distance Value")
plt.title("Distances among Time Series")
plt.xticks([i+0.2 for i in x], labels)
plt.legend()

plt.tight_layout()
plt.show()
