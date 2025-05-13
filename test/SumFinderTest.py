import unittest
from src import SumFinder


class MyTestCase(unittest.TestCase):
    #A large number to check
    def test_sum_finder_600(self):
        self.assertEqual(180_300, SumFinder.find_sum_of_all_integers_too(600), "The sum is wrong.")

    #Basic case
    def test_sum_finder_10(self):
        self.assertEqual(55, SumFinder.find_sum_of_all_integers_too(10), "The sum is wrong.")

    #Bad input
    def test_sum_finder_not_int(self):
        with self.assertRaises(TypeError):
            SumFinder.find_sum_of_all_integers_too("a")

    #Zero input
    def test_sum_finder_zero(self):
        self.assertEqual(0, SumFinder.find_sum_of_all_integers_too(0), "The sum is wrong.")

    #Null input
    def test_sum_finder_none(self):
        self.assertEqual(0, SumFinder.find_sum_of_all_integers_too(None), "What should the function return.")

    #Missing case, there is a use case I missed

if __name__ == '__main__':
    unittest.main()
