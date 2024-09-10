import unittest
import random
from tools import generate_random_list
from q1 import Weirdo


class MyTestCase(unittest.TestCase):
    def test_something(self):
        results = []

        for i in range(10000000):
            n = random.randint(0, 100)
            arr = generate_random_list(size=n, lb=-300, ub=300)
            expected = 2 * n
            actual = Weirdo(arr)
            rslt = expected >= actual
            if not rslt:
                print(arr)
                print(n)
                print(expected)
                print(actual)
            results.append(rslt)

        self.assertTrue(False not in results)  # add assertion here


if __name__ == '__main__':
    unittest.main()
