import unittest
from a1 import Extract_Median
from a1 import answer
from tools import generate_random_list

import random

class MyTestCase(unittest.TestCase):
    def test_Extract_Median_on_random_lists(self):

        results = []

        for i in range(10000000):
            n = random.randint(0, 100)
            arr = generate_random_list(size=n, lb=-300, ub=300)
            expected = answer(arr)
            actual = Extract_Median(arr)
            rslt = expected == actual
            if not rslt:
                print(arr)
                print(expected)
                print(actual)
            results.append(rslt)

        self.assertTrue(False not in results)

if __name__ == '__main__':
    unittest.main()
