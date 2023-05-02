import matplotlib.pyplot as plt
import numpy as np

# Define customer requirements and design features
customer_reqs = ['Accuracy', 'Speed', 'Efficiency', 'Reliability', 'Safety', 'Ease of Use']
design_features = ['Barcode Scanning', 'RFID', 'Voice Picking', 'AGVs']

# Define relationship matrix
relationship_matrix = np.array([
    [5, 4, 4, 3],
    [4, 5, 3, 2],
    [3, 2, 5, 4],
    [4, 3, 4, 5],
    [5, 4, 3, 3],
    [3, 5, 4, 4]
])

# Define importance ratings
importance_ratings = np.array([5, 4, 4, 5, 4, 3])

# Calculate design ratings
design_ratings = np.dot(relationship_matrix.T, importance_ratings)

# Calculate weighted ratings
weighted_ratings = relationship_matrix * importance_ratings[:, None]
weighted_ratings = np.dot(weighted_ratings.T, importance_ratings)

# Create House of Quality chart
fig, ax = plt.subplots(figsize=(8, 6))

ax.set_title('House of Quality Chart for Smart Warehouse Picking Technologies')
ax.set_xticks(np.arange(len(design_features)))
ax.set_xticklabels(design_features)

ax.set_yticks(np.arange(len(customer_reqs)))
ax.set_yticklabels(customer_reqs)

for i in range(len(customer_reqs)):
    for j in range(len(design_features)):
        ax.text(j, i, relationship_matrix[i, j], ha='center', va='center')

ax.imshow(weighted_ratings, cmap='Reds')

plt.colorbar(ax.imshow(weighted_ratings, cmap='Reds'))

plt.show()
