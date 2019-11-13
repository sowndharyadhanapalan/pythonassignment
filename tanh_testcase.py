"""module to test calculator"""
import unittest
import tanh_calculation


class Testtan(unittest.TestCase):
    """A class for all test cases"""
    def test_tanh(self):
        """test case for tanh(4)"""
        self.assertEqual(tanh_calculation.calculate_tanh(4), 0.9993292997390669)

    def test_tanh1(self):
        """test case for tanh(0)"""
        self.assertEqual(tanh_calculation.calculate_tanh(0), 0.0)

    def test_tanh2(self):
        """test case for tanh(500)"""
        self.assertEqual(tanh_calculation.calculate_tanh(500), 1.0)

    def test_tanh3(self):
        """test case for tanh(-14)"""
        self.assertEqual(tanh_calculation.calculate_tanh(-14), -0.9999999999986172)


if __name__ == "__main__":
    unittest.main()

