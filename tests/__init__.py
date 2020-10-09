import unittest

from sample.simple import add_one
from fibo.fib2 import fib2


class TestSimple(unittest.TestCase):
    def test_add_one(self):
        self.assertEqual(add_one(5), 6)
    
    def test_fib2(self):
        self.assertEqual(fib2(10), [1, 1, 2, 3, 5, 8])

if __name__ == '__main__':
    unittest.main()
