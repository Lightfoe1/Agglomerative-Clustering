''' Unit tests for module utility_functions '''
import unittest
from utility_functions import calculate_distance, delete_indexes
from class_definitions import ThreeDimensionalPoint

class TestDistance(unittest.TestCase):
    '''Test return value and test type error '''

    # Check if calculation is done correctly
    def test_distance(self):
        ''' Check if calculation is done correctly '''
        # Check to see if the distance is calculated correctly 1, 1, 1 to 1, 1, 2 should be 1
        self.assertAlmostEqual(calculate_distance(ThreeDimensionalPoint(1, 1, 1),
                                                  ThreeDimensionalPoint(1, 1, 2)), 1)
        # Check if the distance from a point to itself is 0
        self.assertAlmostEqual(calculate_distance(ThreeDimensionalPoint(1, 2, 3),
                                                  ThreeDimensionalPoint(1, 2, 3)), 0)
        # Check if the distance is calculated correctly(Should be: 6.928203230275509)
        self.assertAlmostEqual(calculate_distance(ThreeDimensionalPoint(-1, -2, -3),
                                                  ThreeDimensionalPoint(-5, -6, -7)), 6.928203230275509)

    def test_inputs(self):
        ''' Check if type errors are raised correctly '''
        # 1. Test response to wrong type
        # 1.1  arg1 of correct type, arg2 of wrong type
        self.assertRaises(TypeError, calculate_distance, ThreeDimensionalPoint(-5, -6, -7), 5)
        # 1.2 arg1 of wrong type, arg2 of correct type
        self.assertRaises(TypeError, calculate_distance, 5, ThreeDimensionalPoint(-5, -6, -7))


class TestDeleteIndexes(unittest.TestCase):
    ''' Test type errors and value errors '''
    # Check to see if type errors and value errors are raised correctly
    def test_inputs(self):
        ''' Test for errors with wrong type and empty list '''
        # 1. Test response to wrong type
        # 1.1 arg1 of correct type, arg2 of wrong type
        self.assertRaises(TypeError, delete_indexes, [1, 2, 3, 4, 5], 5)
        # 1.2 arg1 of wrong type, arg2 of correct type
        self.assertRaises(TypeError, delete_indexes, 5, [1, 2, 3, 4, 5])

        # 2. Test response to empty list
        # 2.1 arg1 of correct type, arg2 empty list
        self.assertRaises(ValueError, delete_indexes, [0, 1, 2], [])
        # 2.2 arg1 empty list, arg2 of correct type
        self.assertRaises(ValueError, delete_indexes, [], [0, 1, 2])

        # 3. Test if code is correctly working
        data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        deletion = [0, 3, 6, 9]
        correct_result = [1, 2, 4, 5, 7, 8]
        self.assertEqual(delete_indexes(data, deletion), correct_result)