import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors

def statistical_outlier_removal(data, k=8, std_dev_multiplier=2.0):
    # Convert DataFrame to numpy array
    points = data[['x', 'y', 'z']].values
    
    # Fit the nearest neighbors model
    nbrs = NearestNeighbors(n_neighbors=k).fit(points)
    distances, _ = nbrs.kneighbors(points)
    
    # Compute mean and standard deviation of distances
    mean_distances = distances.mean(axis=1)
    global_mean = mean_distances.mean()
    global_std_dev = mean_distances.std()
    
    # Determine the threshold
    threshold = global_mean + std_dev_multiplier * global_std_dev
    
    # Identify inliers
    inliers = mean_distances < threshold
    
    # Return filtered data
    return data[inliers]

# Load the dataset
file_path = 'synthetic_lidar_data.csv'
data = pd.read_csv(file_path)

# Apply Statistical Outlier Removal
filtered_data = statistical_outlier_removal(data)

# Save the filtered data to a new CSV file
output_file_path = 'filtered_lidar_data.csv'
filtered_data.to_csv(output_file_path, index=False)

print("Filtering completed and saved to", output_file_path)
