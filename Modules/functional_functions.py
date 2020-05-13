'''
The functions here do the clustering process and displaying data
'''
import random
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
from class_definitions import (ThreeDimensionalPoint, Cluster)
from utility_functions import (calculate_distance, delete_indexes)
# 3: Functional Functions

def randomize_3d_points(dimensions, data_size):
    '''
    Randomizes points
    dimensions    -- the desired dimensions that the points will have
    data_sze      -- the desired number of points
    Returns an array of points
    '''
    if not isinstance(dimensions, int) or not isinstance(data_size, int):
        raise TypeError(
            "The dimension and number of datas must be integers!(random_3d_points)")
    object_array = Cluster()
    for _ in range(data_size):
        temporary_x = random.randint(0, dimensions)
        temporary_y = random.randint(0, dimensions)
        temporary_z = random.randint(0, dimensions)
        temporary_object = ThreeDimensionalPoint(
            temporary_x, temporary_y, temporary_z)
        object_array.append(temporary_object)
    return object_array

def display_image(display_data, color):
    '''
    Displays the data given
    display_data -- the data that is wished to be displayed
    color               -- color of the points on image(blue,black,red,yellow...)
    depth_shade         -- True for normal image
    '''
    # Check display data
    if isinstance(display_data, list) and len(display_data) == 0:
        raise ValueError("No data to be displayed!(display_image)")
    if not isinstance(display_data, Cluster):
        for item in display_data:
            if not isinstance(item, Cluster):
                raise TypeError("Corrupt cluster!(display_image)")
    else:
        for item in display_data:
            if not isinstance(item, ThreeDimensionalPoint):
                raise TypeError("Corrupt cluster!(display_image)")
    # Check color
    if not isinstance(color, str):
        raise TypeError(" Color must be a string!(display_image)")

    # If the data is raw data, treat it as a cluster and plot it
    if isinstance(display_data, Cluster):
        display_data.display_cluster(color, 1)
    # If the input is a cluster array, plot it
    elif isinstance(display_data[0], Cluster):
        for item in display_data:
            item.display_cluster(color, 1)
    # Display image
    plt.show()

def print_clusters(print_data):
    '''
    Prints clusters
    print_data -- the array which stores the clusters that will be printed
    '''
    if not isinstance(print_data, list):
        raise TypeError("print_data must be a list!(print_clusters)")
    if len(print_data) == 0:
        raise ValueError(
            "Print data is empty!(print_clusters)")
    for cluster in print_data:
        if not isinstance(cluster, Cluster):
            raise TypeError("print_data must only contain clusters!(print_clusters)")
        for point in cluster:
            if not isinstance(point, ThreeDimensionalPoint):
                raise TypeError("Corrupt cluster!(print_clusters)")

    for cluster in print_data:
        cluster.print_cluster()

def create_double_clusters(data_array, cluster_array, max_clustering_distance):
    '''
    Creates clusters with size two
    data_array     -- The raw data that will be clustered
    cluster_array  -- The clusters will be stored here
    max_clustering_distance -- The maximum distance between two points that will be clustered
    '''
    # Check data_array
    if isinstance(data_array, Cluster):
        if len(data_array) <= 1:
            raise ValueError(
                "There are less than 2 points!(create_double_clusters)")
        for point in data_array:
            if not isinstance(point, ThreeDimensionalPoint):
                raise TypeError("data_array must only contain points!(create_double_clusters)")
    else:
        raise TypeError("data_array must be a cluster!(create_double_clusters)")
    # Check cluster array
    if isinstance(cluster_array, list):
        if len(cluster_array) >= 1:
            raise ValueError("Cluster array must be empty!(create_double_clusters)")
    else:
        raise TypeError("Cluster array must be a list!(create_double_clusters)")
    # Check max_clustering_distance
    if not isinstance(max_clustering_distance, int):
        raise TypeError("max_clustering distance must be int(create_double_clusters)")


    index_array = []
    for counter_one in range(len(data_array)):
        # If counter_one is already in a cluster, continue
        if counter_one in index_array:
            continue
        # Initialize the minimum distance to compare
        min_distance = max_clustering_distance
        # first_point
        point_one = data_array[counter_one]
        for counter_two in range(counter_one + 1, len(data_array)):
            # If t is already in a cluster, continue
            if counter_two in index_array:
                continue
            # second_point
            point_two = data_array[counter_two]
            # Calculate distance between first_point and second_point
            distance = calculate_distance(point_one, point_two)
            # Check to see if it is the shortest possible distance
            if distance < min_distance:
                # If it is save t in order to use later on, and update the shortest distance
                index_second_point = counter_two
                min_distance = distance
        # If minimum distance is within the accepted range
        if min_distance < max_clustering_distance:
            # 1:Take second point. 2: make first_point and second_point into a cluster.
            # 3: add this cluster to the cluster array
            point_two = data_array[index_second_point]
            temporary_cluster = Cluster()
            temporary_cluster.append(point_one)
            temporary_cluster.append(point_two)
            cluster_array.append(temporary_cluster)
            # Save the indexes of both points in order to delete them once everything is finished
            index_array.append(counter_one)
            index_array.append(index_second_point)
    # Delete indexes from raw data if there are indexes to be deleted
    if index_array:
        data_array = delete_indexes(data_array, index_array)

def add_to_clusters(data_array, cluster_array, max_adding_distance):
    '''
    Adds the leftover points to clusters
    data_array    -- The leftover data
    cluster_array -- The clusters to where points will be added
    max_adding_distance    -- The maximum distance for adding points to clusters
    '''
    # Tests:
    # Check data array
    if isinstance(data_array, Cluster):
        if len(data_array) == 0:
            raise ValueError("Data array empty!(add_to_clusters)")
        for item in data_array:
            if not isinstance(item, ThreeDimensionalPoint):
                raise TypeError("Data array must contain only points!(add_to_clusters)")
    else:
        raise TypeError("Data array is not a cluster!(add_to_clusters)")
    # Check cluster array
    if isinstance(cluster_array, list):
        if len(cluster_array) == 0:
            raise ValueError("Cluster array is empty!(add_to_clusters)")
        for cluster in cluster_array:
            if not isinstance(cluster, Cluster):
                raise TypeError("Cluster array must contain only clusters!(add_to_clusters)")
            for point in cluster:
                if not isinstance(point, ThreeDimensionalPoint):
                    raise TypeError("Clusters must contain only points!(add_to_clusters)")
    else:
        raise TypeError("Cluster array is not a list!(add_to_clusters)")
    # Check max adding distance
    if not isinstance(max_adding_distance, int):
        raise TypeError("max_adding_distance is not int!(add_to_clusters)")

    # Actual function:
    index_array = []
    # Take an unclustered member
    for i in range(len(data_array)):
        # first_point
        point_one = data_array[i]
        # Take a cluster
        for cluster in cluster_array:
            # Take every member of the cluster
            for point_two in cluster:
                # Calculate distance between first_point and second_point
                distance = calculate_distance(point_one, point_two)
                # If distance is acceptable; 1: append point to cluster
                # 2: add index to the deletion list
                if distance <= max_adding_distance:
                    cluster.append(point_one)
                    index_array.append(i)
                    break
            # To break out of nested loops we use if else structure
            else:
                continue
            break
    # Delete the used points from raw data
    if index_array:
        data_array = delete_indexes(data_array, index_array)

def merge_clusters(cluster_array, max_merging_distance):
    '''
    Merges clusters until they can't be merged anymore
    cluster_array -- The clusters that will be merged
    max_merging_distance   -- The maximum distance in which the clusters will be merged
    '''


    # Check cluster_array
    if isinstance(cluster_array, list):
        if len(cluster_array) <= 1:
            raise ValueError("Cluster array is empty or has 1 item!(merge_clusters)")
        for cluster in cluster_array:
            if not isinstance(cluster, Cluster):
                raise TypeError("Cluster array must contain clusters!(merge_clusters)")
            for point in cluster:
                if not isinstance(point, ThreeDimensionalPoint):
                    raise TypeError("Corrupt cluster!(merge_clusters)")
    else:
        raise TypeError("cluster_array must be a list!(merge_clusters)")
    # Check max_merging_distance
    if not isinstance(max_merging_distance, int):
        raise TypeError("max_merging_distance must be int!(merge_clusters)")

    # This code will run until there are no changes made to the cluster array
    while True:
        cluster_array_temporary = []
        index_array = []
        # Take cluster1
        for counter_one in range(len(cluster_array)):
            #Take first cluster
            cluster_one = cluster_array[counter_one]
            # Take first_point
            for first_point in cluster_one:
                # Start from next index to avoid comparing with itself Take cluster2
                for counter_two in range(counter_one + 1, len(cluster_array)):
                    cluster_two = cluster_array[counter_two]
                    # Take second_point
                    for second_point in cluster_two:
                        # Calculate the distance
                        distance = calculate_distance(
                            first_point, second_point)
                        # If distance is ok merge two clusters and add them to the array
                        if distance <= max_merging_distance:
                            temporary_cluster = Cluster()
                            temporary_cluster.extend(cluster_one)
                            temporary_cluster.extend(cluster_two)
                            cluster_array_temporary.append(temporary_cluster)
                            index_array.append(counter_one)
                            index_array.append(counter_two)
                            break
                    else:
                        continue
                    break
                else:
                    continue
                break
            else:
                continue
            break
        if index_array:
            cluster_array = delete_indexes(cluster_array, index_array)
            cluster_array.extend(cluster_array_temporary)
        else:
            break

def clear_small_clusters(data_array, cluster_array, min_cluster_size):
    '''
    Clears out small clusters
    data_array    -- The cleared clusters will be added back to the raw data
    cluster_array -- The clusters which will be checked
    min_cluster_size       -- The minimum size for clusters
    '''
    # Check data array
    if isinstance(data_array, Cluster):
        if len(data_array) >= 1:
            for item in data_array:
                if not isinstance(item, ThreeDimensionalPoint):
                    raise TypeError("Data array must contain only points!(add_to_clusters)")
    else:
        raise TypeError("Data array is not a cluster!(add_to_clusters)")
    # Check cluster array
    if isinstance(cluster_array, list):
        if len(cluster_array) == 0:
            raise ValueError("Cluster array is empty!(add_to_clusters)")
        for cluster in cluster_array:
            if not isinstance(cluster, Cluster):
                raise TypeError("Cluster array must contain only clusters!(add_to_clusters)")
            for point in cluster:
                if not isinstance(point, ThreeDimensionalPoint):
                    raise TypeError("Clusters must contain only points!(add_to_clusters)")
    else:
        raise TypeError("Cluster array is not a list!(add_to_clusters)")
    # Check min_cluster_size
    if not isinstance(min_cluster_size, int):
        raise TypeError("min_cluster_size must be int!(clear_small_clusters)")


    index_array = []
    for counter_1 in range(len(cluster_array)):
        # If the cluster is small add the points back to the raw data
        if len(cluster_array[counter_1]) <= min_cluster_size:
            index_array.append(counter_1)
            for point in cluster_array[counter_1]:
                # Add back to raw data because we don't want any data loss
                data_array.append(point)

    # Delete indexes from cluster_array
    if index_array:
        cluster_array = delete_indexes(cluster_array, index_array)
