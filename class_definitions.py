'''
- Define the two classes 3d point and cluster.
- Define their methods which prints and displays them.
- Define function to make x y or z array to be used while displaying
'''
import matplotlib.pyplot as plt


class ThreeDimensionalPoint:
    '''
    The class which is used to store 3d coordinates
    '''

    def __init__(self, x_coordinate, y_coordinate, z_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.z_coordinate = z_coordinate

    def print_point(self):
        ''' Prints the point'''
        print("X :", self.x_coordinate, "y:",
              self.y_coordinate, "z:", self.z_coordinate)

    def display_point(self, color, display_delay):
        '''
        Displays the point using matplotlib
        color         -- the color of the display
        display_delay -- If the display wants to be delayed until plt.show() enter True,
                         if it is to be immediately displayed enter False
        '''
        # Create figure and plot it
        fig = plt.figure()
        axes = fig.add_subplot(111, projection='3d')
        axes.scatter(self.x_coordinate, self.y_coordinate, self.z_coordinate, s=1,
                     c=color, depthshade=True)
        # If the image is to be immediately displayed
        if display_delay == 0:
            plt.show()

class Cluster(list):
    '''
    This class will behave like an array, but it stores points as members
    '''
    def print_cluster(self):
        ''' Prints the cluster'''
        print("Cluster: ")
        for point in self:
            point.print_point()

    def display_cluster(self, color, display_delay):
        ''' Displays the cluster using matplotlib'''
        # Create figure and plot it
        # Make x, y and z arrays to be used in plotting
        x_array = create_xyz_array(self, 0)
        y_array = create_xyz_array(self, 1)
        z_array = create_xyz_array(self, 2)
        # Create figure and plot it
        fig = plt.figure()
        axes = fig.add_subplot(111, projection='3d')
        axes.scatter(x_array, y_array, z_array, s=1,
                     c=color, depthshade=True)
        if display_delay == 0:
            plt.show()

def create_xyz_array(data_array_function, key):
    '''
    Makes x y or z array to be used in plotting
    data_array_function -- the array of points from which the coordinates will be extracted
    key                 -- Give 0 for x array, 1 for y array and 2 for z array
    '''

    if (not isinstance(key, int)
            or not isinstance(data_array_function, Cluster)):
        raise TypeError(
            "data_array_function or key are of wrong type!(create_xyz_array)")
    if len(data_array_function) <= 0 or key >= 3 or key < 0:
        raise ValueError(
            "data_array_function Null or key is not 0,1 or 2!(create_xyz_array)")

    xyz_array = []
    # Python does not have switch cases so I used if else instead
    if key == 0:
        for point_object in data_array_function:
            xyz_array.append(point_object.x_coordinate)
    elif key == 1:
        for point_object in data_array_function:
            xyz_array.append(point_object.y_coordinate)
    elif key == 2:
        for point_object in data_array_function:
            xyz_array.append(point_object.z_coordinate)
    return xyz_array
