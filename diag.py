import numpy as np

A = np.array([[4, 1], [2, 3]])

eigenvalues, eigenvectors = np.linalg.eig(A)

D = np.diag(eigenvalues)
P_user = np.array([[1, -1], [1, 2]])
P_inverse_user = np.linalg.inv(P_user)

# Compute PDP^-1
PDP_inverse = P_user @ D @ P_inverse_user

print(PDP_inverse)
