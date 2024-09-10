import unittest
import random
from tools import generate_random_list, generate_reverse_list
from q1 import Weirdo


class MyTestCase(unittest.TestCase):
    def test_random(self):
        results = []

        for i in range(1000000):
            n = random.randint(2, 50)
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

    def test_reverse(self):
        results = []

        for i in range(1000000):
            n = random.randint(2, 50)
            arr = generate_reverse_list(size=n)
            expected = 2 * n
            actual = Weirdo(arr)
            rslt = expected >= actual
            if not rslt:
                print(arr)
                print(n)
                print(expected)
                print(actual)
            else:
                print(expected, " >= ", actual, "where n =", n)
            results.append(rslt)

        self.assertTrue(False not in results)

    def test_ordered(self):
        results = []

        for i in range(1000000):
            n = random.randint(2, 50)
            arr = generate_reverse_list(size=n)
            arr.reverse()
            expected = 1
            actual = Weirdo(arr)
            rslt = expected == actual
            if not rslt:
                print(arr)
                print(n)
                print(expected)
                print(actual)
            else:
                print(expected, " >= ", actual, "where n =", n)
            results.append(rslt)

        self.assertTrue(False not in results)

if __name__ == '__main__':
    unittest.main()
