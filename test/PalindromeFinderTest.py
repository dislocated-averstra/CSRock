import unittest
from src.PalindromeFinder import check_if_palindrome


class MyTestCase(unittest.TestCase):
    def test_palindrome_string(self):
        """Test with strings that are palindromes"""
        self.assertTrue(check_if_palindrome("racecar"))
        self.assertTrue(check_if_palindrome("madam"))
        self.assertTrue(check_if_palindrome("level"))
        self.assertTrue(check_if_palindrome("noon"))

    def test_non_palindrome_string(self):
        """Test with strings that are not palindromes"""
        self.assertFalse(check_if_palindrome("hello"))
        self.assertFalse(check_if_palindrome("python"))
        self.assertFalse(check_if_palindrome("world"))

    def test_single_character_string(self):
        """Test with a string that is one character in length"""
        self.assertTrue(check_if_palindrome("a"))
        self.assertTrue(check_if_palindrome("7"))

    def test_empty_string(self):
        """Test with an empty string"""
        self.assertTrue(check_if_palindrome(""))

    def test_incorrect_type(self):
        """Test with incorrect types"""
        with self.assertRaises(TypeError):
            check_if_palindrome(123)
        with self.assertRaises(TypeError):
            check_if_palindrome(["r", "a", "c", "e", "c", "a", "r"])
        with self.assertRaises(TypeError):
            check_if_palindrome({"key": "value"})

    def test_none_input(self):
        """Test with None input"""
        with self.assertRaises(TypeError):
            check_if_palindrome(None)

if __name__ == '__main__':
    unittest.main()
