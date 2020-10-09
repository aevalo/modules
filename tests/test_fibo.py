import unittest

from fibo.fib2 import fib2


class TestFibo(unittest.TestCase):
    def test_fib2(self):
        self.assertEqual(fib2(10), [0, 1, 1, 2, 3, 5, 8])


if __name__ == '__main__':
    unittest.main()
