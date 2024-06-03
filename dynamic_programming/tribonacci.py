import unittest

"""
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.



Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:

Input: n = 25
Output: 1389537

"""


def tribonacci_bottom_up(n: int) -> int:
    nth = [0] * (n + 1)

    if n == 0:
        return n
    elif n <= 2:
        return 1

    nth[0] = 0
    nth[1] = 1
    nth[2] = 1

    for i in range(3, len(nth)):
        nth[i] = nth[i - 3] + nth[i - 2] + nth[i - 1]

    return nth[-1]


def tribonacci_top_down(n: int) -> int:
    memo = {}

    def traverse(i):
        if i == 0:
            return 0
        if i <= 2:
            return 1
        if i not in memo:
            memo[i] = traverse(i - 3) + traverse(i - 2) + traverse(i - 1)
        return memo[i]

    return traverse(n)


# Time Complexity: O(N)
# Space Complexity: O(N)

class TestTribonacci(unittest.TestCase):
    def test_tribonacci(self):
        self.assertEqual(tribonacci_top_down(4), 4)
        self.assertEqual(tribonacci_top_down(25), 1389537)
        self.assertEqual(tribonacci_bottom_up(4), 4)
        self.assertEqual(tribonacci_bottom_up(25), 1389537)
