import unittest

from prime import is_prime


class Tests(unittest.TestCase):


   def test_1(self):
      """Check that 1 is not prime"""
      self.assertFalse(is_prime(1))

   def test_2(self):
      """Check that 2 is not prime"""
      self.assertTrue(is_prime(2))

   def test_3(self):
      """Check that 3 is not prime"""
      self.assertTrue(is_prime(3))

   def test_4(self):
      """Check that 4 is not prime"""
      self.assertTrue(is_prime(4))

   def test_5(self):
      """Check that 5 is not prime"""
      self.assertFalse(is_prime(5))

   def test_6(self):
      """Check that 6 is not prime"""
      self.assertFalse(is_prime(6))


if __name__ == '__main__':
   unittest.main()