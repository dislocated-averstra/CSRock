import unittest
from src import ShellSort

unsorted_numbers = [30, 2, 100, 54, 3, 96, 47, 35, 42, 60, 71, 85, 12 , 15, 35]
sorted_numbers = [100, 96, 85, 71, 60, 54, 47, 42, 35, 35, 30, 15, 12, 3, 2]

class MyTestCase(unittest.TestCase):
    # sort a list
    def test_shell_sort_list(self):
        self.assertEqual(sorted_numbers, ShellSort.sort(unsorted_numbers), "The list did not sort correctly")

    def test_shell_sort_none(self):
        self.assertEqual([], ShellSort.sort(None), "None did not return an empty list")

    def test_shell_sort_empty_list(self):
        self.assertEqual([], ShellSort.sort([]), "Shell sort did not return an empty list when sorting an empty list")

    def test_shell_sort_single_item(self):
        self.assertEqual([1], ShellSort.sort([1]), "Shell sort did not return correctly for a single item list")

    def test_shell_sort_bad_input(self):
        with self.assertRaises(TypeError):
            ShellSort.sort("a")

if __name__ == '__main__':
    unittest.main()
