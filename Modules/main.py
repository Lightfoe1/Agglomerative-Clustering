'''
- Neccessary imports for clustering
- An example of creating data, clustering it and displaying this data
'''
from functional_functions import (randomize_3d_points, display_image, print_clusters,
                                  create_double_clusters, add_to_clusters, merge_clusters,
                                  clear_small_clusters)

# Initialize global variable
cluster_array = []

# Randomize data
data_array = randomize_3d_points(100, 256)

# Print and display raw data
if data_array:
    print("--------------------------------------------------")
    print("Raw Data:")
    data_array.print_cluster()
    print("First Image: Raw data")
    display_image(data_array, 'black')

# Create clusters with size 2
create_double_clusters(data_array, cluster_array, 15)

# If there are any leftover data, add them to the clusters
if data_array:
    add_to_clusters(data_array, cluster_array, 15)

# Merge the clusters if there are more than 1
if len(cluster_array) > 1:
    merge_clusters(cluster_array, 15)

# Clear small clusters if there are any
if cluster_array:
    clear_small_clusters(data_array, cluster_array, 5)

# Print and display cluster if they exist
if cluster_array:
    print("--------------------------------------------------")
    print("Clustered Data:")
    print_clusters(cluster_array)
    print("Second Image(s): Clustered data")
    display_image(cluster_array, 'blue')

# Print and display leftover data if there is any
if data_array:
    print("--------------------------------------------------")
    print("Leftover Data:")
    data_array.print_cluster()
    print("Third Image: Leftover data")
    display_image(data_array, 'black')
