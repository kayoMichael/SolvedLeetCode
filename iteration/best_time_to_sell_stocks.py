import unittest
from typing import List

"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.

Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

"""


# Peak Valley Algorthm. Find a Valley which is lowest point in the local area of the prices and then find
# a peak that is relative to the lowest point. The difference would be the greatest difference to maximize
# profit up to that point.

def max_profit(prices: List[int]) -> int:
    maximum_profit = 0
    i = 0
    while i < len(prices) - 1:
        while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
            i += 1
        valley = prices[i]

        while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
            i += 1
        peak = prices[i]

        maximum_profit += peak - valley

    return maximum_profit


# Difference Algorithm. A much more simplified version where finding the difference if the next price
# is higher than the current would lead to equivalent results in finding the difference between the peak and the valley

def max_profit_v2(prices: List[int]) -> int:
    maximum = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            maximum += prices[i] - prices[i - 1]
    return maximum


class TestValid(unittest.TestCase):
    def test_max_profit(self):
        self.assertEqual(max_profit([7, 1, 5, 3, 6, 4]), 7)
        self.assertEqual(max_profit([1, 2, 3, 4, 5]), 4)
        self.assertEqual(max_profit([7, 6, 4, 3, 1]), 0)

    def test_max_profit_v2(self):
        self.assertEqual(max_profit_v2([7, 1, 5, 3, 6, 4]), 7)
        self.assertEqual(max_profit_v2([1, 2, 3, 4, 5]), 4)
        self.assertEqual(max_profit_v2([7, 6, 4, 3, 1]), 0)
