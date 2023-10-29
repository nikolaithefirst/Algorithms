import unittest
import sorting_algorithms
import numpy as np


class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(sorting_algorithms.linear_sort([1, 2, 3, 4, 5], 5), 4)

    def test_case_2(self):
        self.assertEqual(sorting_algorithms.linear_sort([3, 25, 6, 576, 4], 0), "Not found")

    def test_case_3(self):
        self.assertEqual(sorting_algorithms.linear_sort([3, 25, 6, 576, 4, 8, 56, 5984, 0, 11], 56), 6)

    def test_case_4(self):
        self.assertEqual(sorting_algorithms.sentinel_linear_search([3, 25, 6, 576, 4, 8, 56, 5984, 0, 11], 10, 56), 6)

    def test_case_5(self):
        self.assertEqual(sorting_algorithms.sentinel_linear_search([3, 25, 6, 576, 4, 8, 56, 5984, 0, 11], 10, 22),
                         "Not found")

    def test_case_6(self):
        self.assertEqual(sorting_algorithms.sentinel_linear_search([3, 22, 6, 25, 4, 8, 56, 25, 0, 11], 10, 25),
                         3)

    def test_case_7(self):
        self.assertEqual(sorting_algorithms.binary_search(np.arange(0, 1000, 1, dtype=int), 1001, 125), 125)

    def test_case_8(self):
        self.assertEqual(sorting_algorithms.binary_search(np.arange(0, 1000, 1, dtype=int), 1001, 825), 825)

    def test_case_9(self):
        self.assertEqual(sorting_algorithms.binary_search(np.arange(0, 1001, 1, dtype=int), 1001, 1002), "Not found")

    def test_case_10(self):
        self.assertEqual(sorting_algorithms.binary_search(np.arange(1, 1001, 1, dtype=int), 1000, 0), "Not found")


if __name__ == '__main__':
    unittest.main()
