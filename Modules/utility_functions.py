'''
The functions here are small parts of code which is needed for the functional functions
'''
import math
from class_definitions import (ThreeDimensionalPoint)

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
