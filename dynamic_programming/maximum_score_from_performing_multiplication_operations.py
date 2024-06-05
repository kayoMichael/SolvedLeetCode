import unittest
from typing import List

"""
You are given two 0-indexed integer arrays nums and multipliers of size n and m respectively, where n >= m.

You begin with a score of 0. You want to perform exactly m operations. On the ith operation (0-indexed) you will:

    Choose one integer x from either the start or the end of the array nums.
    Add multipliers[i] * x to your score.
        Note that multipliers[0] corresponds to the first operation, multipliers[1] to the second operation, and so on.
    Remove x from nums.

Return the maximum score after performing m operations.

Example 1:

Input: nums = [1,2,3], multipliers = [3,2,1]
Output: 14
Explanation: An optimal solution is as follows:
- Choose from the end, [1,2,3], adding 3 * 3 = 9 to the score.
- Choose from the end, [1,2], adding 2 * 2 = 4 to the score.
- Choose from the end, [1], adding 1 * 1 = 1 to the score.
The total score is 9 + 4 + 1 = 14.

Example 2:

Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
Output: 102
Explanation: An optimal solution is as follows:
- Choose from the start, [-5,-3,-3,-2,7,1], adding -5 * -10 = 50 to the score.
- Choose from the start, [-3,-3,-2,7,1], adding -3 * -5 = 15 to the score.
- Choose from the start, [-3,-2,7,1], adding -3 * 3 = -9 to the score.
- Choose from the end, [-2,7,1], adding 1 * 4 = 4 to the score.
- Choose from the end, [-2,7], adding 7 * 6 = 42 to the score.
The total score is 50 + 15 - 9 + 4 + 42 = 102.
"""


def maximum_score_from_multiplications(nums: List[int], multipliers: List[int]) -> int:
    cache = {}

    def find_max_score(left, mult):
        if mult == len(multipliers):
            return 0
        elif (left, mult) in cache:
            return cache[(left, mult)]

        left_score = nums[left] * multipliers[mult] + find_max_score(left + 1, mult + 1)

        right_score = nums[(len(nums) - 1) - (mult - left)] * multipliers[mult] + find_max_score(left, mult + 1)

        cache[(left, mult)] = max(left_score, right_score)

        return cache[(left, mult)]

    return find_max_score(0, 0)


# Time Complexity: O(N^2) where N is the length of multipliers
# Space Complexity: O(N^2)

class TestMaxScoreFromMultiplication(unittest.TestCase):
    def test_max_multiplication_score(self):
        self.assertEqual(maximum_score_from_multiplications([1, 2, 3], [3, 2, 1]), 14)
        self.assertEqual(maximum_score_from_multiplications([-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6]), 102)
        self.assertEqual(maximum_score_from_multiplications([1], [1]), 1)
