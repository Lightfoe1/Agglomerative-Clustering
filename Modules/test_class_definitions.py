''' Test cases for class_definitions module'''
import unittest
from class_definitions import ThreeDimensionalPoint, Cluster

class TestThreeDimensionalPoint(unittest.TestCase):
    ''' Test errors for the methods of class ThreeDimensionalPoint '''
    def test_init(self):
        ''' Test errors for __init__ method'''
        # Create a correct arg1
        arg1 = 1
        # Create a correct arg2
        arg2 = 2
        # Create a correct arg3
        arg3 = 3
        # 1. Test response to wrong type
        # 1.1 arg1 of wrong type, arg2 and arg3 of correct type
        self.assertRaises(TypeError, ThreeDimensionalPoint, 'a', arg2, arg3)
        # 1.2 arg2 of wrong type, arg1 and arg3 of correct type
        self.assertRaises(TypeError, ThreeDimensionalPoint, arg1, 'b', arg3)
        # 1.2 arg3 of wrong type, arg1 and arg2 of correct type
        self.assertRaises(TypeError, ThreeDimensionalPoint, arg1, arg2, 'c')

    def test_display_point(self):
        ''' Test errors for print_point method '''
        # Create an object
        point_test = ThreeDimensionalPoint(0, 1, 2)
        # Create a correct arg1
        color = 'black'
        # Create a correct arg2
        delay = 1

        # 1. Test response to wrong type
        # 1.1  arg1 of correct type, arg2 of wrong type
        self.assertRaises(TypeError, point_test.display_point, color, 'a')
        # 1.2 arg1 of wrong type, arg2 of correct type
        self.assertRaises(TypeError, point_test.display_point, 5, delay)

        # 2. Test for special circumstances
        # 2.1 delay not 0 or 1
        delay = 15
        self.assertRaises(ValueError, point_test.display_point, color, delay)

        # 3. Check response to correct input
        self.assertIsNone(point_test.display_point('blue', 0))


class TestCluster(unittest.TestCase):
    ''' Test errors for the methods of class ThreeDimensionalPoint '''
    def test_display_cluster(self):
        ''' Test errors for display_cluster method '''
        # Create a cluster
        cluster_test = Cluster()
        point = ThreeDimensionalPoint(1, 2, 3)
        cluster_test.append(point)
        # Create a correct arg1
        color = 'black'
        # Create a correct arg2
        delay = 1

        # 1. Test response to wrong type
        # 1.1  arg1 of correct type, arg2 of wrong type
        self.assertRaises(TypeError, cluster_test.display_cluster, color, 'a')
        # 1.2 arg1 of wrong type, arg2 of correct type
        self.assertRaises(TypeError, cluster_test.display_cluster, 5, delay)

        # 2. Test for special circumstances
        # 2.1 delay not 0 or 1
        delay = 15
        self.assertRaises(ValueError, cluster_test.display_cluster, color, delay)
        
        # 3. Test delay 0
        delay = 0
        self.assertIsNone(cluster_test.display_cluster(color, delay))

    def test_create_array(self):
        ''' Test errors for create_xyz_array '''
        # Create a cluster
        cluster = Cluster()
        point = ThreeDimensionalPoint(1, 2, 3)
        for _ in range(15):
            cluster.append(point)
        # Create an empty cluster
        empty_cluster = Cluster()
        # Create wrong cluster
        wrong_cluster = Cluster()
        wrong_cluster.append(1)

        # Create a correct key
        key = 1
        # Create a wrong valued key
        wrong_key = 15
        # Create a wrong type of key
        string_key = 'a'

        # 1. Test for different clusters
        # 1.1 Test response to correct cluster
        self.assertIsNotNone(cluster.create_xyz_array, key)
        # 1.2. Test for wrong cluster
        self.assertRaises(TypeError, wrong_cluster.create_xyz_array, key)
        # 1.3 Test response to empty cluster
        self.assertRaises(ValueError, empty_cluster.create_xyz_array, key)

        # 2. Test for different keys
        # 2.1 Test response to wrong valued key
        self.assertRaises(ValueError, cluster.create_xyz_array, wrong_key)
        # 2.2 Test response to wrong type of key
        self.assertRaises(TypeError, cluster.create_xyz_array, string_key)
