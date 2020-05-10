'''
Create random points in 3d space ,cluster them and display them
Content:
1: Initializations And Class Definitions
2: Utility Functions
3: Functional Functions
4: Implementation
'''
import math
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# 1 :Initializations And Class Definitions

# Array where the raw data will be stored
data_array = []
# Array where the clusters will be stored
cluster_array = []


class ThreeDimensionalPoint:
    '''
    The class which is used to store 3d coordinates
    '''
    # Instance attributes

    def __init__(self, x_coordinate, y_coordinate, z_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.z_coordinate = z_coordinate
    # Print the coordinates of the point

    def print_point(self):
        ''' Prints the object'''
        print("X :", self.x_coordinate, "y:",
              self.y_coordinate, "z:", self.z_coordinate)


# 2: Utility Functions

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
    object_array = []
    for _ in range(data_size):
        temporary_x = random.randint(0, dimensions)
        temporary_y = random.randint(0, dimensions)
        temporary_z = random.randint(0, dimensions)
        temporary_object = ThreeDimensionalPoint(
            temporary_x, temporary_y, temporary_z)
        object_array.append(temporary_object)
    return object_array


def calculate_distance(point_one, point_two):
    '''
    Distance calculating function.
    point_one -- the first point
    point_two -- the second point
    Returns distance between the first and second point
    '''
    # Check if the two points are objects of type ThreeDimensionalPoint
    if (not isinstance(point_one, ThreeDimensionalPoint)
            or not isinstance(point_two, ThreeDimensionalPoint)):
        raise TypeError(
            "The input must be two objects of type ThreeDimensionalPoint!(calculate_distance)")
    # Calculate the distance
    distance_x = ((point_one.x_coordinate - point_two.x_coordinate)**2)
    distance_y = ((point_one.y_coordinate - point_two.y_coordinate)**2)
    distance_z = ((point_one.z_coordinate - point_two.z_coordinate)**2)
    distance = math.sqrt(distance_x + distance_y + distance_z)
    return distance


def delete_indexes(deletion_array, index_array):
    '''
    Deletes indexes from array
    deletion_array -- the array where the indexes will be deleted from
    index_array    -- the indexes which will be deleted from the array
    '''

    # Check if input is valid
    if not isinstance(index_array, list) or not isinstance(deletion_array, list):
        raise TypeError(
            "index_array and deletion_array must be of type list!(delete_indexes)")
    if len(index_array) <= 0 or len(deletion_array) <= 0:
        raise ValueError(
            "index_array and data_array must have 1 or more elements!(delete_indexes)")
    # Delete the indexes starting from the end to prevent data corruption
    index_array.sort()
    reverse_counter = -1
    while reverse_counter >= (0 - len(index_array)):
        index = index_array[reverse_counter]
        deletion_array.pop(index)
        reverse_counter -= 1


def print_clusters(cluster_array_function):
    '''
    Prints clusters
    cluster_array_function -- the array which stores the clusters that will be printed
    '''
    if len(cluster_array_function) <= 0:
        raise ValueError(
            "Cluster cannot be printed because there are none!(print_clusters)")
    if (not isinstance(cluster_array_function, list)
            or not isinstance(cluster_array_function[0], list)
            or not isinstance(cluster_array_function[0][0], ThreeDimensionalPoint)):
        raise TypeError(
            "cluster_array_function must be a list of lists with elements of type ThreeDimensionalPoint!(print_clusters)")
    for i in range(len(cluster_array_function)):
        print("cluster", i, ":")
        for k in range(len(cluster_array_function[i])):
            cluster_array_function[i][k].print_point()


def create_xyz_array(data_array_function, key):
    '''
    Makes x y or z array
    data_array_function -- the array of points from which the coordinates will be extracted
    key                 -- Give 0 for x array, 1 for y array and 2 for z array
    '''
    if (not isinstance(data_array_function, list)
            or not isinstance(key, int)
            or not isinstance(data_array_function[0], ThreeDimensionalPoint)):
        raise TypeError(
            "data_array_function must be a list with elements of type ThreeDimensionalPoint, key must be an integer!(create_xyz_array)")
    if len(data_array_function) <= 0 or key >= 3 or key < 0:
        raise ValueError(
            "data_array_function must have 1 or more elements and key must be 0,1 or 2!(create_xyz_array)")
    xyz_array = []
    # Python does not have switch cases so I used if else instead
    if key == 0:
        for i in range(len(data_array_function)):
            xyz_array.append(data_array_function[i].x_coordinate)
    elif key == 1:
        for i in range(len(data_array_function)):
            xyz_array.append(data_array_function[i].y_coordinate)
    elif key == 2:
        for i in range(len(data_array_function)):
            xyz_array.append(data_array_function[i].z_coordinate)
    return xyz_array


# 3: Functional Functions

def display_image(data_array_function, size, color, depth_shade):
    '''
    Displays the data given
    data_array_function -- the data that is wished to be displayed
    size                -- 1 for normal sized points on image
    color               -- color of the points on image(blue,black,red,yellow...)
    depth_shade         -- True for normal image
    '''
    # Check if input is a list and is not empty
    if not isinstance(data_array_function, list):
        raise TypeError("Input must be a list!(display_image)")
    if len(data_array_function) <= 0:
        raise ValueError(
            "Input must be a list with at least one member!(display_image)")
    # If the input is a cluster array
    if isinstance(data_array_function[0], list):
        for item in data_array_function:
            # Make x, y and z arrays to be used in plotting
            x_array = create_xyz_array(item, 0)
            y_array = create_xyz_array(item, 1)
            z_array = create_xyz_array(item, 2)
            # Create figure and plot it
            fig = plt.figure()
            axes = fig.add_subplot(111, projection='3d')
            axes.scatter(x_array, y_array, z_array, s=size,
                         c=color, depthshade=depth_shade)
    # The data is raw data
    else:
        # Make x, y and z arrays to be used in plotting
        x_array = create_xyz_array(data_array_function, 0)
        y_array = create_xyz_array(data_array_function, 1)
        z_array = create_xyz_array(data_array_function, 2)
        # Create figure and plot it
        figure = plt.figure()
        axes = figure.add_subplot(111, projection='3d')
        axes.scatter(x_array, y_array, z_array, s=size,
                     c=color, depthshade=depth_shade)
    # Display the figures
    plt.show()


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
        # If i is already in a cluster, continue
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
            temporary_cluster = [point_one, point_two]
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
    if (not isinstance(data_array_function, list)
            or not isinstance(cluster_array_function, list)
            or not isinstance(max_adding_distance, int)):
        raise TypeError("Input type wrong!(add_to_clusters)")

    if len(cluster_array_function) == 0 or len(data_array_function) == 0:
        raise ValueError("Input value wrong!(add_to_clusters)")

    index_array = []
    # Take an unclustered member
    for i in range(len(data_array_function)):
        # first_point
        point_one = data_array_function[i]
        counter_one = 0
        # Take a cluster
        for counter_one in range(len(cluster_array_function)):
            # Take every member of the cluster
            for point_two in cluster_array_function[counter_one]:
                # Calculate distance between first_point and second_point
                distance = calculate_distance(point_one, point_two)
                # If distance is acceptable; 1: append point to cluster
                # 2: add index to the deletion list
                if distance <= max_adding_distance:
                    cluster_array_function[counter_one].append(point_one)
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
            "Incorrect type of input!(merge_clusterscalculate_distance)")
    if len(cluster_array_function) <= 0:
        raise ValueError(
            "No data to be merged!(merge_clusterscalculate_distance)")
    # This code will run untill there are no changes made to the cluster array
    process_count = math.log(len(cluster_array_function), 2)
    process_count = int(process_count)
    for _ in range(process_count + 1):
        length = len(cluster_array_function)
        index_array = []
        # Take cluster1
        for cluster_one in range(length):
            # If cluster_one is already used you shouldn't us it a second time
            if cluster_one in index_array:
                continue
            # Take first_point
            for first_point in cluster_array_function[cluster_one]:
                # Start from next index to avoid comparing with itself Take cluster2
                for cluster_two in range(cluster_one + 1, length):
                    # If cluster_two is already used you shouldn't use it again
                    if cluster_two in index_array:
                        continue
                    # Take second_point
                    for second_point in cluster_array_function[cluster_two]:
                        # Calculate the distance
                        distance = calculate_distance(
                            first_point, second_point)
                        # If distance is ok merge two clusters and add them to the array
                        if distance <= max_merging_distance:
                            cluster_array_function.append(
                                cluster_array_function[cluster_one]
                                + cluster_array_function[cluster_two])
                            index_array.append(cluster_one)
                            index_array.append(cluster_two)
                            break
                    else:
                        continue
                    break
                else:
                    continue
                break
        if index_array:
            delete_indexes(cluster_array_function, index_array)
        else:
            break
    return cluster_array


def clear_small_clusters(data_array_function, cluster_array_function, min_cluster_size):
    '''
    Clears out small clusters
    data_array_function    -- The cleared clusters will be added back to the raw data
    cluster_array_function -- The clusters which will be checked
    min_cluster_size       -- The minimum size for clusters
    '''
    # Check the inputs
    if (not isinstance(cluster_array_function, list)
            or not isinstance(data_array_function, list)
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
                # Add back to raw data(we don't want any data loss)
                data_array_function.append(point)
    # Delete indexes from cluster_array
    if index_array:
        delete_indexes(cluster_array_function, index_array)
    return 0

# 4: Implementation


# Randomize data
data_array = randomize_3d_points(100, 36)
# Display and print raw data before any process is done
display_image(data_array, 1, 'black', True)
print("raw data:")
for counter in range(len(data_array)):
    print(counter, ". point:")
    data_array[counter].print_point()
# Make clusters with 1 2
create_double_clusters(data_array, cluster_array, 15)
# Add unclustered data to the clusters if there are any
if data_array:
    add_to_clusters(data_array, cluster_array, 15)
# Merge the clusters until there is no more changes
cluster_array = merge_clusters(cluster_array, 150)
print_clusters(cluster_array)
# Clear clusters that have a 1 smaller than specified
clear_small_clusters(data_array, cluster_array, 2)
# print the clusters
print("unclustered data:")
for counter in range(len(data_array)):
    data_array[counter].print_point()
# Display clusters
display_image(cluster_array, 1, 'blue', True)
# Display raw data that is left behind
if data_array:
    display_image(data_array, 1, 'black', True)
