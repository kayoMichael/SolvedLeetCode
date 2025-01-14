"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.



Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]



Constraints:

    1 <= temperatures.length <= 105
    30 <= temperatures[i] <= 100


"""

import unittest
from typing import List


def daily_temperatures(temperatures: List[int]) -> List[int]:
    stack = []
    length = len(temperatures)
    output = [0] * length
    for i in range(length):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            days = i - stack[-1]
            output[stack[-1]] = days
            stack.pop()
        stack.append(i)

    return output


class TestDailyTemperatures(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]), [1, 1, 4, 2, 1, 1, 0, 0])
        self.assertEqual(daily_temperatures([30, 40, 50, 60]), [1, 1, 1, 0])
        self.assertEqual(daily_temperatures([30, 60, 90]), [1, 1, 0])

    def test_empty(self):
        self.assertEqual(daily_temperatures([]), [])

    def test_single_element(self):
        self.assertEqual(daily_temperatures([30]), [0])


if __name__ == '__main__':
    unittest.main()
