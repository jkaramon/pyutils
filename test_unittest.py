import numpy as np
import unittest
from rounder import round_by_error, round_numpy_arr, first_meaningful_digit, get_exp, ceil_by_first_digit
import numpy.testing as npt

class Test_RoundNumpyArr(unittest.TestCase):
    
    def test_round_to_two_decimals(self):
        arr = np.array([1.12345, 2.67891, 3.14159, 4.445])
        result = round_numpy_arr(arr, 2)
        expected = np.array([1.12, 2.68, 3.14, 4.45])
        npt.assert_array_equal(result, expected)
    
    def test_round_to_zero_decimals(self):
        arr = np.array([1.5, 2.5, 3.5])
        result = round_numpy_arr(arr, 0)
        expected = np.array([2.0, 2.0, 4.0])
        
    def test_first_meaningful_digit(self):
        self.assertEqual(first_meaningful_digit(0), 0)
        self.assertEqual(first_meaningful_digit(12345), 1)
        self.assertEqual(first_meaningful_digit(0.12345), 1)
        self.assertEqual(first_meaningful_digit(0.00012345), 1)
        self.assertEqual(first_meaningful_digit(123.), 1)
        self.assertEqual(first_meaningful_digit(0.000987), 9)
    
    def test_get_exp(self):
        self.assertEqual(get_exp(0), 0)
        self.assertEqual(get_exp(12345), 4)
        self.assertEqual(get_exp(0.12345), -1)
        self.assertEqual(get_exp(0.00012345), -4)
        self.assertEqual(get_exp(123.), 2)
        
   
    
    def test_ceil_by_first_digit(self):
        self.assertEqual(ceil_by_first_digit(0), 0)
        self.assertEqual(ceil_by_first_digit(0.12345), 0.13)
        self.assertEqual(ceil_by_first_digit(0.00012345), 0.00013)
        self.assertEqual(ceil_by_first_digit(0.03245), 0.04)
    

    def test_round_by_error(self):
        self.assertEqual(round_by_error(1.76534, 0.0012), 1.7653)
        self.assertEqual(round_by_error(1.76534, 0.002), 1.765)
    
    def test_all(self):
        error = ceil_by_first_digit(0.0012546)
        self.assertEqual(error, 0.0013)
        self.assertEqual(round_by_error(1.76534, error), 1.7653)
        
    
if __name__ == '__main__':
    unittest.main()