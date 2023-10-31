import unittest
from exersise1 import palindrome


class TestforPalindrome(unittest.TestCase):
    
    def test_is_palindrome(self):
        string="nivin"
        self.assertTrue(palindrome(string))


    def test_is_not_palindrome(self):
        string="egg"
        self.assertFalse(palindrome(string))

    def test_empty(self):
        string=""
        self.assertTrue(palindrome(string))
        



   












     











if __name__ == '__main__':
    unittest.main()