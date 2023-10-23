import unittest
import sorting_algorithms


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


if __name__ == '__main__':
    unittest.main()
