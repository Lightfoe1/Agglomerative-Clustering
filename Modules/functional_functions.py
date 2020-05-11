'''
The functions here do the clustering process and displaying data
'''
import random
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d # pylint: disable=unused-import
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
    # Check if input is valid
    if(not isinstance(display_data[0], Cluster)
       and not isinstance(display_data, Cluster)
       and not isinstance(display_data, ThreeDimensionalPoint)):
        raise TypeError("Only a point or a cluster can be displayed!(display_image)")
    # If the data is raw data, treat it as a cluster and plot it
    if isinstance(display_data, Cluster):
        display_data.display_cluster(color, 1)
    # If the input is a cluster array, plot it
    elif isinstance(display_data[0], Cluster):
        for item in display_data:
            item.display_cluster(color, 1)
    # If the data is a point, plot it
    elif isinstance(display_data, ThreeDimensionalPoint):
        display_data.print_point(color, 1)
    # Display image
    plt.show()

def print_clusters(cluster_array_function):
    '''
    Prints clusters
    cluster_array_function -- the array which stores the clusters that will be printed
    '''
    if (not isinstance(cluster_array_function, list)
            or not isinstance(cluster_array_function[0], Cluster)):
        raise TypeError("Invalid Input!(print_clusters)")
    if len(cluster_array_function) <= 0:
        raise ValueError(
            "Cluster cannot be printed because there are none!(print_clusters)")
    for cluster in cluster_array_function:
        cluster.print_cluster()

def create_double_clusters(data_array_function, cluster_array_function, max_clustering_distance):
    '''
    Creates clusters with size two
    data_array_function     -- The raw data that will be clustered
    cluster_array_function  -- The clusters will be stored here
    max_clustering_distance -- The maximum distance between two points that will be clustered
    '''
    # Check if the inputs are valid
    if (not isinstance(data_array_function, list)
            or not isinstance(cluster_array_function, list)):
        print("No data or only one point(create_double_clusters)")
        raise TypeError("Incorrect type of input!(create_double_clusters)")
    if len(data_array_function) <= 1:
        raise ValueError(
            "At least two points are needed in order to create a cluster!(create_double_clusters)")

    index_array = []
    for counter_one in range(len(data_array_function)):
        # If counter_one is already in a cluster, continue
        if counter_one in index_array:
            continue
        # Initialize the minimum distance to compare
        min_distance = max_clustering_distance
        # first_point
        point_one = data_array_function[counter_one]
        for counter_two in range(counter_one + 1, len(data_array_function)):
            # If t is already in a cluster, continue
            if counter_two in index_array:
                continue
            # second_point
            point_two = data_array_function[counter_two]
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
            point_two = data_array_function[index_second_point]
            temporary_cluster = Cluster()
            temporary_cluster.append(point_one)
            temporary_cluster.append(point_two)
            cluster_array_function.append(temporary_cluster)
            # Save the indexes of both points in order to delete them once everything is finished
            index_array.append(counter_one)
            index_array.append(index_second_point)
    # Delete indexes from raw data if there are indexes to be deleted
    if index_array:
        delete_indexes(data_array_function, index_array)

def add_to_clusters(data_array_function, cluster_array_function, max_adding_distance):
    '''
    Adds the leftover points to clusters
    data_array_function    -- The leftover data
    cluster_array_function -- The clusters to where points will be added
    max_adding_distance    -- The maximum distance for adding points to clusters
    '''
    # Check if the inputs are valid
    if (not isinstance(data_array_function, Cluster)
            or not isinstance(cluster_array_function, list)
            or not isinstance(max_adding_distance, int)):
        raise TypeError("Input type wrong!(add_to_clusters)")

    if len(data_array_function) == 0:
        raise ValueError("Input value wrong!(add_to_clusters)")

    index_array = []
    # Take an unclustered member
    for i in range(len(data_array_function)):
        # first_point
        point_one = data_array_function[i]
        # Take a cluster
        for cluster in cluster_array_function:
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
        delete_indexes(data_array_function, index_array)

def merge_clusters(cluster_array_function, max_merging_distance):
    '''
    Merges clusters until they can't be merged anymore
    cluster_array_function -- The clusters that will be merged
    max_merging_distance   -- The maximum distance in which the clusters will be merged
    '''


    # Check the inputs
    if (not isinstance(cluster_array_function, list)
            or not isinstance(max_merging_distance, int)):
        raise TypeError(
            "Incorrect type of input!(merge_clusters)")
    if len(cluster_array_function) < 2:
        raise ValueError(
            "No data to be merged!(merge_clusters)")
    # This code will run until there are no changes made to the cluster array
    while True:
        cluster_array_function_temporary = []
        index_array = []
        # Take cluster1
        for counter_one in range(len(cluster_array_function)):
            #Take first cluster
            cluster_one = cluster_array_function[counter_one]
            # Take first_point
            for first_point in cluster_one:
                # Start from next index to avoid comparing with itself Take cluster2
                for counter_two in range(counter_one + 1, len(cluster_array_function)):
                    cluster_two = cluster_array_function[counter_two]
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
                            cluster_array_function_temporary.append(temporary_cluster)
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
            delete_indexes(cluster_array_function, index_array)
            cluster_array_function.extend(cluster_array_function_temporary)
        else:
            break

def clear_small_clusters(data_array_function, cluster_array_function, min_cluster_size):
    '''
    Clears out small clusters
    data_array_function    -- The cleared clusters will be added back to the raw data
    cluster_array_function -- The clusters which will be checked
    min_cluster_size       -- The minimum size for clusters
    '''
    # Check the inputs
    if (not isinstance(cluster_array_function, list)
            or not isinstance(cluster_array_function[0], Cluster)
            or not isinstance(data_array_function, Cluster)
            or not isinstance(min_cluster_size, int)):
        raise TypeError("Incorrect input!(clear_small_clusters)")
    if len(cluster_array_function) <= 0:
        raise ValueError("No data to be deleted!(clear_small_clusters)")

    index_array = []
    for counter_1 in range(len(cluster_array_function)):
        # If the cluster is small add the points back to the raw data
        if len(cluster_array_function[counter_1]) <= min_cluster_size:
            index_array.append(counter_1)
            for point in cluster_array_function[counter_1]:
                # Add back to raw data because we don't want any data loss
                data_array_function.append(point)

    # Delete indexes from cluster_array
    if index_array:
        delete_indexes(cluster_array_function, index_array)
    return 0
