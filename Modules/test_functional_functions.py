''' Unit tests for funcional_functions module '''
import unittest
from class_definitions import (ThreeDimensionalPoint, Cluster)
from functional_functions import (randomize_3d_points, display_image, print_clusters,
                                  create_double_clusters, add_to_clusters, merge_clusters,
                                  clear_small_clusters)

class TestRandomPoints(unittest.TestCase):
    ''' Test errors for randomize_3d_points function '''    
    def test_inputs(self):
        ''' Check if type errors are raised correctly '''
        # 1. Test response to wrong type
        # 1.1  arg1 of correct type, arg2 of wrong type
        self.assertRaises(TypeError, randomize_3d_points, 5, 'a')
        # 1.2 arg1 of wrong type, arg2 of correct type
        self.assertRaises(TypeError, randomize_3d_points, 'b', 15)
        # 2. Check if the function works
        result = randomize_3d_points(10, 10)
        for item in result:
            self.assertIsInstance(item, ThreeDimensionalPoint)

class TestImageDisplay(unittest.TestCase):
    ''' Test errors for display_image function'''
    def test_inputs(self):
        ''' Check if type errors and value errors are raised correctly '''
        # 1. Test response to wrong type
        point = ThreeDimensionalPoint(1, 2, 3)
        cluster_array = []
        cluster_one = Cluster()
        cluster_one.append(point)
        cluster_one.append(point)
        cluster_two = Cluster()
        cluster_two.append(point)
        cluster_two.append(point)
        cluster_array.append(cluster_one)
        cluster_array.append(cluster_two)
        # 0. Test for correct types
        # 0.1 Test for a cluster
        self.assertIsNone(display_image(cluster_one, 'blue'))
        # 0.2 Test for a list of clusters 
        self.assertIsNone(display_image(cluster_array, 'blue'))
        # 1.1  arg1 of correct type, arg2 of wrong type
        self.assertRaises(TypeError, display_image, cluster_one, 5)
        # 1.2 arg1 of wrong type, arg2 of correct type
        self.assertRaises(TypeError, display_image, 5, 'blue')
        # 2. arg1 must be a cluster, a list of clusters or a point
        # 2.1 Test empty cluster
        cluster = Cluster()
        self.assertRaises(ValueError, display_image, cluster, 'blue')
        # 2.2 Test empty list
        data = []
        self.assertRaises(ValueError, display_image, data, 'blue')
        # 2.3 Test random list
        data = [1, 2, 3, 4, 5]
        self.assertRaises(TypeError, display_image, data, 'blue')
        # 2.4 Test corrupt cluster
        cluster = Cluster()
        cluster.append(1)
        self.assertRaises(TypeError, display_image, cluster, 'blue')

class TestPrintClusters(unittest.TestCase):
    ''' Test errors for print_clusters function '''
    def test_inputs(self):
        ''' Check if type errors and value errors are raised correctly '''
        # 1. Check response to wrong type
        self.assertRaises(TypeError, print_clusters, 15)
        # 2. Check response to an empty list
        data = []
        self.assertRaises(ValueError, print_clusters, data)
        # 3. Check response to a cluster
        data = Cluster()
        point = ThreeDimensionalPoint(1, 2, 3)
        data.append(point)
        data.append(point)
        self.assertRaises(TypeError, print_clusters, data)
        # 4. Check response to a random list
        data = [0, 1, 2, 3, 4, 5]
        self.assertRaises(TypeError, print_clusters, data)
        # 5. Check response to valid input
        point = ThreeDimensionalPoint(1, 2, 3)
        cluster_array = []
        cluster_one = Cluster()
        cluster_one.append(point)
        cluster_one.append(point)
        cluster_two = Cluster()
        cluster_two.append(point)
        cluster_two.append(point)
        cluster_array.append(cluster_one)
        cluster_array.append(cluster_two)
        self.assertIsNone(print_clusters(cluster_array))
        # 6. data contains corrupt cluster
        point = ThreeDimensionalPoint(1, 2, 3)
        cluster_array = []
        cluster_one = Cluster()
        cluster_one.append(point)
        cluster_one.append(point)
        cluster_two = Cluster()
        cluster_two.append(point)
        cluster_two.append(point)
        corrupt_cluster = Cluster()
        corrupt_cluster.append(1)
        cluster_array.append(cluster_one)
        cluster_array.append(cluster_two)
        cluster_array.append(corrupt_cluster)
        self.assertRaises(TypeError, print_clusters, cluster_array)

class TestDoubleClusterMaker(unittest.TestCase):
    ''' Test errors for create_double_clusters function '''
    def test_inputs(self):
        ''' Check if type errors and value errors are raised correctly '''

        # Create a correct arg2
        cluster_array = []
        # Create a correct arg1
        data = Cluster()
        point = ThreeDimensionalPoint(1, 2, 3)
        for _ in range(50):
            data.append(point)
        # Create a correct arg3
        distance = 15

        # 1. Check if type errors is raised if arguments are of wrong type
        # 1.1 arg1 of wrong, arg2 and arg3 of correct type
        self.assertRaises(TypeError, create_double_clusters, 'a', cluster_array, distance)
        # 1.2 arg2 of wrong type, arg1 and arg3 of correct type
        self.assertRaises(TypeError, create_double_clusters, data, 15, distance)
        # 1.3 arg3 of wrong type, arg1 and arg2 of correct type
        self.assertRaises(TypeError, create_double_clusters, data, cluster_array, 'b')

        # 2. Check for special circumstances
        # 2.1 arg1 empty cluster
        empty_cluster = Cluster()
        self.assertRaises(ValueError, create_double_clusters, empty_cluster,
                          cluster_array, distance)
        # 2.2 arg2 list with some elements
        arg2_list = [1, 2, 3]
        self.assertRaises(ValueError, create_double_clusters, data, arg2_list, distance)
        # 2.3 corrupt data array
        data_array = Cluster()
        data_array.append(1)
        data_array.append(3)
        self.assertRaises(TypeError, create_double_clusters, data_array, cluster_array, distance)
        
        # 3. Check response to valid input
        create_double_clusters(data, cluster_array, 100)
        for item in cluster_array:
            self.assertIsInstance(item, Cluster)

class TestAddToClusters(unittest.TestCase):
    ''' Test errors for add_to_clusters function '''
    def test_inputs(self):
        ''' Check if type errors and value errors are raised correctly '''
        # Create a correct arg1
        data = Cluster()
        point = ThreeDimensionalPoint(1, 2, 3)
        data.append(point)
        data.append(point)
        # Create a correct arg2
        cluster_array = []
        cluster_one = Cluster()
        cluster_one.append(point)
        cluster_one.append(point)
        cluster_two = Cluster()
        cluster_two.append(point)
        cluster_two.append(point)
        cluster_array.append(cluster_one)
        cluster_array.append(cluster_two)
        # Create a correct arg3
        distance = 15

        # 1. Check if type errors is raised if arguments are of wrong type
        # 1.1 arg1 of wrong, arg2 and arg3 of correct type
        self.assertRaises(TypeError, add_to_clusters, 'a', cluster_array, distance)
        # 1.2 arg2 of wrong type, arg1 and arg3 of correct type
        self.assertRaises(TypeError, add_to_clusters, data, 15, distance)
        # 1.3 arg3 of wrong type, arg1 and arg2 of correct type
        self.assertRaises(TypeError, add_to_clusters, data, cluster_array, 'b')

        # 2. Check for special circumstances
        # 2.1 arg1 empty cluster
        empty_cluster = Cluster()
        self.assertRaises(ValueError, add_to_clusters, empty_cluster, cluster_array, distance)
        # 2.2 arg2 empty list
        empty_list = []
        self.assertRaises(ValueError, add_to_clusters, data, empty_list, distance)
        # 2.3 arg2 list with some elements
        arg2_list = [1, 2, 3]
        self.assertRaises(TypeError, add_to_clusters, data, arg2_list, distance)
        # 2.4 arg1 list with some elements
        arg1_list = [1, 2, 3]
        self.assertRaises(TypeError, add_to_clusters, arg1_list, cluster_array, distance)
        # 2.5 data array contains non point member
        wrong_data_array = Cluster()
        wrong_data_array.append(1)
        self.assertRaises(TypeError, add_to_clusters, wrong_data_array, cluster_array, distance)
        # 2.6 cluster array contains corrupt cluster
        corrupt_cluster = Cluster()
        corrupt_cluster.append(1)
        wrong_cluster_array = []
        wrong_cluster_array.append(corrupt_cluster)
        self.assertRaises(TypeError, add_to_clusters, data, wrong_cluster_array, distance)
        
        # 3. Check for valid inputs
        add_to_clusters(data, cluster_array, 50)
        for item in cluster_array:
            self.assertIsInstance(item, Cluster)

class TestClusterMerger(unittest.TestCase):
    ''' Test errors for merge_clusters function '''
    def test_inputs(self):
        ''' Check if type errors and value errors are raised correctly '''
        # Create correct arg1
        cluster_array = []
        point = ThreeDimensionalPoint(1, 2, 3)
        cluster_one = Cluster()
        cluster_one.append(point)
        cluster_one.append(point)
        cluster_two = Cluster()
        cluster_two.append(point)
        cluster_two.append(point)
        cluster_array.append(cluster_one)
        cluster_array.append(cluster_two)
        # Create correct arg2
        distance = 15

        # 1. Check if type errors is raised if arguments are of wrong type
        # 1.1 arg1 of wrong, arg2 of correct type
        self.assertRaises(TypeError, merge_clusters, cluster_array, 'a')
        # 1.2 arg2 of wrong type, arg1 of correct type
        self.assertRaises(TypeError, merge_clusters, 'b', distance)

        # 2. Check for special circumstances
        # 2.1 arg1 empty list
        empty_list = []
        self.assertRaises(ValueError, merge_clusters, empty_list, distance)
        # 2.2 Cluster array contains non cluster item
        wrong_cluster_array = [1, 2]
        self.assertRaises(TypeError, merge_clusters, wrong_cluster_array, distance)
        # 2.3 Cluster array contains corrupt cluster
        wrong_cluster = Cluster()
        wrong_cluster.append(1)
        wrong_cluster_array = []
        wrong_cluster_array.append(wrong_cluster)
        wrong_cluster_array.append(wrong_cluster)
        self.assertRaises(TypeError, merge_clusters, wrong_cluster_array, distance)

        # 3. Check response to correct input
        merge_clusters(cluster_array, distance)
        for item in cluster_array:
            self.assertIsInstance(item, Cluster)

class TestClearClusters(unittest.TestCase):
    ''' Test errors for clear_small_clusters function '''
    def test_inputs(self):
        ''' Check if type errors and value errors are raised correctly '''
        point = ThreeDimensionalPoint(1, 2, 3)
        # Create a correct arg1
        data = Cluster()
        data.append(point)
        data.append(point)
        # Create a correct arg2
        cluster_array = []
        cluster_one = Cluster()
        cluster_one.append(point)
        cluster_one.append(point)
        cluster_two = Cluster()
        cluster_two.append(point)
        cluster_two.append(point)
        cluster_array.append(cluster_one)
        cluster_array.append(cluster_two)
        # Create a correct arg3
        size = 5

        # 1. Check if type errors is raised if arguments are of wrong type
        # 1.1 arg1 of wrong, arg2 and arg3 of correct type
        self.assertRaises(TypeError, clear_small_clusters, 'a', cluster_array, size)
        # 1.2 arg2 of wrong type, arg1 and arg3 of correct type
        self.assertRaises(TypeError, clear_small_clusters, data, 15, size)
        # 1.3 arg3 of wrong type, arg1 and arg2 of correct type
        self.assertRaises(TypeError, clear_small_clusters, data, cluster_array, 'b')

        # 2. Check for special circumstances
        # 2.1 arg2 empty list
        empty_list = []
        self.assertRaises(ValueError, clear_small_clusters, data, empty_list, size)
        # 2.2 data array cluster but contains non point member
        wrong_data = Cluster()
        wrong_data.append(1)
        self.assertRaises(TypeError, clear_small_clusters, wrong_data, cluster_array, size)
        # 2.3 Cluster array contains non cluster item
        wrong_cluster_array = [1,2]
        self.assertRaises(TypeError, clear_small_clusters, data, wrong_cluster_array, size)
        # 2.4 Cluster array contains a cluster with non point items
        wrong_cluster_array = []
        wrong_cluster_array.append(wrong_data)
        self.assertRaises(TypeError, clear_small_clusters, data, wrong_cluster_array, size)

        # 3. Check response to correct input
        clear_small_clusters(data, cluster_array, 5)
        for item in data:
            self.assertIsInstance(item, ThreeDimensionalPoint)
